# NeckPass

This repository provides the artifacts accompanying the paper **NeckPass**. The repository contains datasets, experimental results, and source code required to reproduce the main findings reported in the paper. The provided artifacts allow researchers to replicate the evaluation results under different experimental scenarios described in the manuscript.

---

# Repository Overview

The repository is organized into three compressed packages:
1. **ExperimentalResults**
   This package contains the processed data sources and trained models used to generate the experimental results reported in the paper. Each experimental scenario includes a runnable script (`run.py`) that reproduces the corresponding evaluation results.

2. **SourceCode**
   This package provides the implementation of the proposed NeckPass framework, including data preprocessing pipelines, feature processing, and model training code. By replacing the dataset with the corresponding scenario dataset and executing the provided scripts, users can reproduce the processing pipeline and experimental outcomes described in the paper.

3. **Datasets**
   This package contains the datasets used in each experimental scenario. To preserve user privacy, the datasets are released in **Mel-cepstral feature representation**, which enables reproducibility while preventing reconstruction of the original audio signals.

---

# ExperimentalResults Package Structure

The directory structure of the **ExperimentalResults** package is shown below:

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
# Reproducibility Instructions

The experiments can be reproduced by following the steps below.

## Step 1 — Install Dependencies
In the first-level directory, the `requirements.txt` file lists all the libraries required for this folder. To install the dependencies, execute the following command (My Python version 3.9.11):
> `pip install -r requirements.txt `


## Step 2 — Reference Experimental Results
The `Result.xlsx` file provides the data presented in each scenario of the paper, serving as a reference outline for readers. 

## Step 3 — Core Library Implementation
The `lib` folder contains implementations of library functions. The remaining folders correspond to the scenario resource files, named to align with the sections in the paper for easy reference. 

## Step 4 — Running Experiments
Every scenario directory typically contains:
- `Dataset_NeckPass` — dataset used for the experiment  
- `Model_Am` — pretrained authentication models (if applicable)  
- `run.py` — script for reproducing the experimental results

For each scenario (paper section), running `run.py` allows you to locally obtain the results, consistent with those provided in `Result.xlsx` and in the paper. The corresponding commands are as follows:
> `python run.py`

**Due to size constraints of the repository, we provide only processed features and trained models that are sufficient to reproduce all reported results. Upon acceptance, we will release a more complete artifact. If you encounter any difficulties, please don't hesitate to reach out for assistance. Thank you sincerely for your interest, time and patience.**
