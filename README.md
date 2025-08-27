# NeckPass
The files in this repository are for the paper: **NeckPass: Effortless Authentication for VR/AR Systems via Neck Ballistocardiogram Biometric**

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
8.2_OverallPerformance
├── dataset.py
└── run.py
8.3.1_ImpactsofSingle-sideController
├── dataset.py
└── run.py
8.3.2_ImpactsofIntensePhysicalActivity
├── dataset.py
└── run.py
8.3.3_ImpactsofDynamicBehavior
├── dataset.py
└── run.py
8.3.4_ImpactsofBiometricLong-termVariability
├── dataset.py
└── run.py
8.3.5_ImpactsofVRDevices
├── dataset.py
└── run.py
8.3.6_ImpactsofGenetics
├── dataset.py
└── run.py
8.3.7_ImpactsofVotingMechanism
├── dataset.py
└── run.py
8.3.8_EvaluationofComputationalDelay
├── Authentication
│   ├── dataset.py
│   └── run.py
├── SignalRefinementAndConversion
│   ├── dataset.py
│   ├── LibCode.py
│   ├── Preprocessing.py
│   ├── run.py
│   ├── SampleConversion.py
│   └── SignalRefinement.py
└── VRapp
    └── dataset.py
9.2_ImpersonationAttack
├── dataset.py
└── run.py
9.3_ReplayAttack
├── dataset.py
└── run.py
9.4_SpoofingAttack
├── dataset.py
├── run_device.py
└── run_location.py
```

**Step 1.** In the first-level directory, the `requirements.txt` file lists all the libraries required for this folder. To install the dependencies, execute the following command (My Python version 3.9.11):
> `pip install -r requirements.txt `

**Step 2.** The `Result.xlsx` file provides the data presented in each scenario of the paper, serving as a reference outline for readers. 

**Step 3.** The `lib` folder contains implementations of library functions. The remaining folders correspond to the scenario resource files, named to align with the sections in the paper for easy reference. 

**Step 4.** For each scenario (paper section), the folder contains two files: `dataset.py` and `run.py`. Running these two files allows you to download the original dataset (named `Dataset_NeckPass`) and trained authentication models (`Model_Am`) from the cloud and locally obtain the results, consistent with those provided in `Result.xlsx` and in the paper. The corresponding commands are as follows:
> `python dataset.py`
> `python run.py`

**If you encounter any difficulties, please don't hesitate to reach out for assistance. Thank you sincerely for your interest, time and patience.**