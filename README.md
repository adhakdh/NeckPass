# NeckPass
The files in this repository are for the paper: **NeckPass**

We provide the following three compressed data packages:
1. **ExperimentalResults**: This package contains the data sources for all scenarios presented in the paper. It includes processed data and trained models. For each scenario, simply `python run.py` to obtain the data results shown in the paper.
1. **SourceCode**: This package provides the source code for the technical approach mentioned in the paper. It includes data processing methods and model building code. By replacing the dataset with the corresponding scenario dataset mentioned in the paper and running `python run.py`, you can achieve the data processing results presented in the paper.
1. **Datasets**: This package includes the datasets for each scenario in the paper (in Mel-cepstral form, facilitating user privacy and a quick start), which can be used for training models and validating experimental results.

**Detailed Explanation of the First Data Package:.** *ExperimentalResults*. The directory structure is as follows:

```
requirements.txt
Result.xlsx
lib
├── ast_model.py
├── lib_siam.py
└── tpr.json
B. Overall Performance
├── Dataset_NeckPass
├── Model_Am
├── run.py
└── run_auc_eer.py
C-1) Impacts of Controller Side
├── Dataset_NeckPass
└── run.py
C-2) Impacts of Biometric Long-term Variability
├── Dataset_NeckPass
└── run.py
C-3) Impacts of Genetics
├── Dataset_NeckPass
├── Model_Am
└── run.py
C-4) Impacts of XR Devices
├── Dataset_NeckPass
├── Model_Am
└── run.py
C-5) Impacts of Voting Mechanism
├── Dataset_NeckPass
└── run.py
C-6) Physiological Stress Test
├── Dataset_NeckPass
└── run.py
C-7) Evaluation of Computational Delay
├── Authentication
│   ├── Dataset_NeckPass
│   └── run.py
├── SignalRefinementAndConversion
│   ├── Dataset_NeckPass
│   ├── LibCode.py
│   ├── Preprocessing.py
│   ├── run.py
│   ├── SampleConversion.py
│   └── SignalRefinement.py
└── VRapp
    └── dataset.py
D-2) Impersonation Attack
├── Dataset_NeckPass
└── run.py
D-3) Replay Attack
├── Dataset_NeckPass
└── run.py
D-4) Spoofing Attack
├── Dataset_NeckPass
├── run_device.py
└── run_location.py
```

**Step 1.** In the first-level directory, the `requirements.txt` file lists all the libraries required for this folder. To install the dependencies, execute the following command (My Python version 3.9.11):
> `pip install -r requirements.txt `

**Step 2.** The `Result.xlsx` file provides the data presented in each scenario of the paper, serving as a reference outline for readers. 

**Step 3.** The `lib` folder contains implementations of library functions. The remaining folders correspond to the scenario resource files, named to align with the sections in the paper for easy reference. 

**Step 4.** For each scenario (paper section), the folder contains two item: the original dataset (named `Dataset_NeckPass`), trained authentication models (`Model_Am`) and `run.py`. Running `run.py` allows you to locally obtain the results, consistent with those provided in `Result.xlsx` and in the paper. The corresponding commands are as follows:
> `python run.py`

**Due to size constraints of the repository, we provide only processed features and trained models that are sufficient to reproduce all reported results. Upon acceptance, we will release a more complete artifact. If you encounter any difficulties, please don't hesitate to reach out for assistance. Thank you sincerely for your interest, time and patience.**
