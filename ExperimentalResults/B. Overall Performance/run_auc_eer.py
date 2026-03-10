import os
import sys
import numpy as np
import torch


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
sys.path.append(parent_dir)

from lib_siam import SiameseNetwork




def natural_sort_key(filename):
    return [int(part) if part.isdigit() else part for part in filename.replace('.pt', '').split('_')]

def load_model(model_path, input_dim):
    model = SiameseNetwork(input_dim=input_dim)
    
    state = torch.load(model_path, map_location='cpu')
    model.load_state_dict(state)
    model.eval()
    return model

def get_user_data(user_dir):
    """
    读取某个用户目录下所有 .pt 特征文件（含 mean_feature.pt）。
    你的命名约定：file_name.split('_')[0] == "1" (genuine) or "0" (impostor)
    返回：[(tensor, file_stem, label_str), ...]
    """
    all_data = []
    all_file_names = os.listdir(user_dir)
    if 'mean_feature.pt' in all_file_names:
        all_file_names.remove('mean_feature.pt')

    sorted_file_names = sorted(all_file_names, key=natural_sort_key)
    
    sorted_file_names.append('mean_feature.pt')

    for file_name in sorted_file_names:
        file_path = os.path.join(user_dir, file_name)
        data = torch.load(file_path, map_location='cpu')
        label = file_name.split("_")[0]  
        all_data.append((data, file_name.split(".pt")[0], label))
    return all_data

def pair_scores_max(score_list, num_time=2):
    """
    用滑窗 max(score) 来模拟你原 get_paired 的 “OR 逻辑”
    - 你原来：窗口内只要有一次判为 1，则输出 1
    - 对 score 来说：窗口内只要有一个 score 高，就应该更易通过阈值 => max 合理
    """
    final_scores = []
    for i in range(len(score_list) - num_time + 1):
        window = score_list[i:i + num_time]
        final_scores.append(float(np.max(window)))
    return final_scores

def compute_eer_from_roc(fpr, tpr, thresholds):
    """
    给定 ROC（fpr=FAR, tpr=TPR），计算 EER 和对应阈值（最近点法 + 线性插值增强）。
    """
    fnr = 1.0 - tpr
    diff = fpr - fnr

    
    idx = int(np.nanargmin(np.abs(diff)))
    eer_nearest = 0.5 * (fpr[idx] + fnr[idx])
    thr_nearest = thresholds[idx]

    
    sign_change = np.where(np.sign(diff[:-1]) * np.sign(diff[1:]) < 0)[0]
    if len(sign_change) == 0:
        return float(eer_nearest), float(thr_nearest), None

    j = int(sign_change[0])
    
    x0, x1 = j, j + 1
    y0, y1 = diff[j], diff[j + 1]
    alpha = -y0 / (y1 - y0)  
    fpr_i = fpr[j] + alpha * (fpr[j + 1] - fpr[j])
    fnr_i = fnr[j] + alpha * (fnr[j + 1] - fnr[j])
    thr_i = thresholds[j] + alpha * (thresholds[j + 1] - thresholds[j])
    eer_i = 0.5 * (fpr_i + fnr_i)

    return float(eer_nearest), float(thr_nearest), (float(eer_i), float(thr_i))




if __name__ == "__main__":
    
    Input_path = "Dataset_NeckPass"
    Model_dir = "Model_Am"  
    pos_user_list =  ['User0', 'User10', 'User11', 'User12', 'User14', 'User15', 'User16', 'User17', 'User19', 'User2', 'User20', 'User21', 'User22', 'User23', 'User24', 'User26', 'User28', 'User3', 'User30', 'User31', 'User4', 'User5', 'User7', 'User8'] 
    USE_PAIRING = True
    PAIR_K = 2

    all_genuine_scores = []
    all_impostor_scores = []
    per_user_scores = {}  
    user_list = [u for u in pos_user_list if os.path.isdir(os.path.join(Input_path, u))]
    user_list = sorted(user_list)

    for user in user_list:
        user_dir = os.path.join(Input_path, user)
        all_users_data = get_user_data(user_dir)
        input_dim = all_users_data[0][0].shape[0]
        model_path = os.path.join(Model_dir, f"Am_{user}.pth")
        if not os.path.exists(model_path):
            print(f"[WARN] model not found for user={user}: {model_path}, skip.")
            continue

        model = load_model(model_path, input_dim)
        mean_feature_path = os.path.join(Input_path, user, "mean_feature.pt")
        mean_feature = torch.load(mean_feature_path, map_location='cpu')
        model.anchor = mean_feature
        model.eval()
        genuine_scores = []
        impostor_scores = []

        for data, file_name, label in all_users_data:
            if file_name == "mean_feature":
                continue  
            with torch.no_grad():
                _, _, outputs = model(data)
                score = float(outputs[0].item() if torch.is_tensor(outputs[0]) else outputs[0])
            if label == "1":
                genuine_scores.append(score)
            elif label == "0":
                impostor_scores.append(score)
            else:
                pass

        if USE_PAIRING:
            if len(genuine_scores) >= PAIR_K:
                genuine_scores = pair_scores_max(genuine_scores, PAIR_K)
            else:
                genuine_scores = []
            if len(impostor_scores) >= PAIR_K:
                impostor_scores = pair_scores_max(impostor_scores, PAIR_K)
            else:
                impostor_scores = []
        per_user_scores[user] = (genuine_scores, impostor_scores)
        all_genuine_scores.extend(genuine_scores)
        all_impostor_scores.extend(impostor_scores)

    if len(all_genuine_scores) == 0 or len(all_impostor_scores) == 0:
        raise RuntimeError("No genuine or impostor scores collected. Check labels and file naming.")
    scores = np.array(all_genuine_scores + all_impostor_scores, dtype=float)
    labels = np.array([1] * len(all_genuine_scores) + [0] * len(all_impostor_scores), dtype=int)

    from sklearn.metrics import roc_curve, auc
    fpr, tpr, thresholds = roc_curve(labels, scores, pos_label=1)
    roc_auc = auc(fpr, tpr)

    eer_near, thr_near, eer_interp = compute_eer_from_roc(fpr, tpr, thresholds)
    print("\n===== Overall ROC/EER =====")
    print(f"AUC = {roc_auc:.6f}")
    if eer_interp is not None:
        print(f"EER (interp)  = {eer_interp[0]*100:.3f}% at threshold {eer_interp[1]:.6f}")
    
    try:
        import matplotlib.pyplot as plt
        import numpy as np

        fnr = 1 - tpr
        eer_index = int(np.nanargmin(np.abs(fpr - fnr)))
        eer_fpr = float(fpr[eer_index])
        eer_tpr = float(tpr[eer_index])
        eer_val = float((eer_fpr + (1 - eer_tpr)) / 2)  
        plt.figure()
        plt.plot(fpr, tpr, label="ROC")
        x = np.linspace(0, 1, 200)
        plt.plot(x, 1 - x, "--", label="TPR = 1 - FPR (EER line)")
        plt.scatter([eer_fpr], [eer_tpr], zorder=5, label=f"EER ≈ {eer_val*100:.2f}%")
        plt.plot([eer_fpr, eer_fpr], [0, eer_tpr], "--")
        plt.plot([0, eer_fpr], [eer_tpr, eer_tpr], "--")
        plt.xlabel("FPR (FAR)")
        plt.ylabel("TPR (1 - FRR)")
        plt.title("Overall ROC with EER")
        plt.grid(True)
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.legend(loc="lower right")
        plt.show()
    except Exception as e:
        print(f"\n[WARN] ROC plot not saved: {e}")
