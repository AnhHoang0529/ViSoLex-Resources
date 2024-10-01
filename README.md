# ViSoLex-Resources

## Overview
This repository contains code and data for the ViSoLex project, focused on lexical normalization for Vietnamese social media texts. The project includes rule-based approaches, preprocessing steps, and datasets for model training and evaluation.

## Repository Structure

```
Code/
  ├── Preprocessing Data/                # Code for preprocessing raw_data to tempt_data
  └── Learning_From_Rule/                # Code for processing temp_data to data

data/                                    # Contains data files for ViSoLex
  ├── train.csv                          
  ├── dev.csv                            
  ├── test.csv
  └── unlabeled.csv

raw_data/                                # Contains raw data files and Temporary data
  ├── Annotation/                        # Contains annotated data
  ├── temp_data                          # Contains temp_data during processing
  ├── ViLexNorm                          # Contains labeled data files during processing
  └── downstream_data                    # Contains downstream data files during processing

```
## File Creation Process
This guide explains how to generate the data files (`train.csv`, `dev.csv`, `test.csv`, and `unlabeled.csv`) located in the `data/` folder by using the raw data and code provided in this repository.

### 1. Raw Data Overview
- The `raw_data/` folder contains various data sources such as:
  - `Annotation/`: Manually annotated data.
  - `temp_data/`: Temporary data files generated during processing.
  - `ViLexNorm/`: Labeled data files.
  - `downstream_data/`: Data for downstream processing tasks.
  
### 2. Preprocessing Step
This step involves converting the `raw_data/` into a temporary format (`temp_data/`) that is ready for further rule-based processing.

#### Code Location: `Code/Preprocessing Data/`

1. **`preprocessing_labeled_dataset.ipynb`**  
   - **Purpose**: Preprocesses raw labeled data from the `ViLexNorm/raw_data` folder to prepare it for further processing.
   - **Output**: Creates processed labeled data files `temp_data/ViLexNorm.csv`.

2. **`preprocessing_downstream_dataset.ipynb`**  
   - **Purpose**: Preprocesses downstream datasets (from `downstream_data/`) into a temporary format (`temp_data/`), cleaning and standardizing the text.
   - **Output**: Cleaned downstream datasets stored as `temp_data/*.csv`.

3. **`create_dataset_for_astra.ipynb`**  
   - **Purpose**: Combines multiple `temp_data/` sources and processes them to create an unlabeled dataset for use in the ViSoLex task.
   - **Output**: Downstream data file, `temp_data/downstream_data.csv`.

4. **`create_lexnorm_dict.ipynb`**  
   - **Purpose**: Preprocesses labeled data and annotated data to create a normalization dictionary for further rule-based learning.
   - **Output**: A dictionary for lexical normalization `raw_data/ViLexNorm/LexNorm_dict_segment.json`.

5. **`create_annotation_sheet.ipynb`**  
   - **Purpose**: Generates an annotation sheet from processed data, facilitating manual review and updates.

6. **`dictionary_statistic.ipynb`**  
   - **Purpose**: Performs analysis on the dictionary and annotated data, generating insights into the data distribution and usage.

### 3. Rule-based Processing Step
Once the `temp_data/` is prepared, this step applies lexical normalization rules to create the final datasets used for training models.

#### Code Location: `Code/Learning_From_Rule/`

1. **`generate_data.py`**  
   - **Purpose**: Generates processed datasets (`train.csv`, `dev.csv`, `test.csv`, and `unlabeled.csv`) by applying custom string handling, regex, and dictionary-based rules.
   - **Key Functions**:
     - `custom_str(x)`: Converts floats to strings while preserving formatting.
     - `flatten_lst(lst)`: Flattens a list of words.
     - `regrex_rule(sent, sent_lst, rule_list)`: Applies regex-based rules to the text.
     - `dictionary_rule(sent, sent_lst, dictionary)`: Applies dictionary-based normalization.
   - **Output**: Processes the data and stores the outputs (`train.csv`, `dev.csv`, `test.csv`, and `unlabeled.csv`) based on the application of these rules.
2. **`generate_rule_dict.py`**  
   - **Purpose**: Generates rule-based dictionaries used for normalization.
   
3. **`get_elmo_contextual_embeddings.py`**  
   - **Purpose**: Retrieves contextual embeddings using ELMo, which can be used to enrich data representation.

4. **`rules.py`**  
   - **Purpose**: Contains various regex and dictionary-based rules for text normalization.

5. **`requirements.txt`**  
   - **Purpose**: Lists dependencies required to run the above scripts, such as Pandas, Numpy, etc.

#### Instructions:
```

pip install -r requirements.txt
python generate_data.py

```
### 4. Output Files
After running both preprocessing and rule-based normalization steps, the following files will be generated in the `data/` folder:
- `train.csv`: Training dataset with normalized text and labels.
- `dev.csv`: Development/validation dataset.
- `test.csv`: Test dataset for evaluating model performance.
- `unlabeled.csv`: Unlabeled dataset for further tasks such as unsupervised learning or data augmentation.

### 5. Customization
You can modify the rule sets or preprocessing parameters by adjusting the respective files in the `Code/` folder. Make sure to update the input and output paths in the commands accordingly if your directory structure differs.

---
