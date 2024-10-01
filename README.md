# ViSoLex-Resources

## Overview
This repository contains code and data for the ViSoLex project, focused on lexical normalization for Vietnamese social media texts. The project includes rule-based approaches, preprocessing steps, and datasets for model training and evaluation.

## Repository Structure

```
Code/
  ├── Preprocessing Data/                # Code for preprocessing raw_data to tempt_data
  └── Learning_From_Rule/                # Code for processing tempt_data to data

data/                                    # Contains data files for ViSoLex
  ├── train.csv                          
  ├── dev.csv                            
  ├── test.csv
  └── unlabeled.csv

raw_data/                                # Contains data files and tempt_data
  ├── Annotation/                        # Contains annotated data
  ├── ASTRA                              # Contains tempt_data in processing
  ├── ViLexNorm                          # Contains labeled data files in processing
  └── downstream_data                    # Contains downstream data files in processing

```
## File Creation Process
This guide explains how to generate the data files (`train.csv`, `dev.csv`, `test.csv`, and `unlabeled.csv`) located in the `data/` folder by using the raw data and code provided in this repository.

### 1. Raw Data Overview
- The `raw_data/` folder contains various data sources such as:
  - `Annotation/`: Manually annotated data.
  - `ASTRA/`: Temporary data files generated during processing.
  - `ViLexNorm/`: Labeled data files.
  - `downstream_data/`: Data for downstream processing tasks.
  
### 2. Preprocessing Step
This step involves converting the `raw_data/` into a temporary format (`ASTRA/`) that is ready for further rule-based processing.

#### Code Location: `Code/Preprocessing Data/`
- **Functionality**: 
  - Prepares raw text by applying basic preprocessing (e.g., tokenization, removing unwanted characters, handling special symbols).
  - Converts raw files to intermediate data (`ASTRA`), which is a cleaner format used for training.
#### Instructions:

### 3. Rule-based Processing Step
Once the `ASTRA/` is prepared, this step applies lexical normalization rules to create the final datasets used for training models.

#### Code Location: `Code/Learning_From_Rule/`
- **Functionality**:
  - Implements normalization rules (based on linguistic patterns or pre-defined dictionaries).
  - Transforms the `ASTRA/` into labeled data suitable for model training (producing `train.csv`, `dev.csv`, `test.csv`, and `unlabeled.csv`).

#### Instructions:
