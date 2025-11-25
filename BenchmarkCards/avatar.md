# AVATAR

## 📊 Benchmark Details

**Name**: AVATAR

**Overview**: AVATAR is a collection of 9,515 programming problems and their solutions written in two popular languages, Java and Python, aimed at supporting program translation tasks.

**Data Type**: programming problems and solutions

**Domains**:
- Software Development

**Languages**:
- Java
- Python

**Resources**:
- [GitHub Repository](https://github.com/wasiahmad/AVATAR)

## 🎯 Purpose and Intended Users

**Goal**: To contribute to the development of translation systems for programming languages by providing a sizeable parallel corpus.

**Target Audience**:
- Software Developers
- Researchers
- ML Researchers

**Tasks**:
- Program Translation
- Function Translation

**Limitations**: The proposed benchmark has a few limitations. AVATAR has a smaller training data size, covers only two programming languages, and focuses primarily on data structures and algorithms.

## 💾 Data

**Source**: Collected from competitive programming sites, online platforms, and open-source repositories.

**Size**: 9,515 programming problems and solutions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation of neural machine translation systems on the dataset
- Functional correctness evaluation using unit tests

**Metrics**:
- BLEU
- Syntax Match (SM)
- Dataflow Match (DM)
- CodeBLEU (CB)
- Execution Accuracy (EA)
- Computational Accuracy (CA)

**Calculation**: Metrics like BLEU compute the overlap between candidate and reference translations.

**Interpretation**: Higher scores on BLEU and other metrics indicate better translation quality.

**Baseline Results**: Evaluation metrics results for various models trained on the corpus.

**Validation**: The dataset is split into training, validation, and test sets in a 75:5:20 ratio.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive information has been minimized by removing natural language comments and docstrings.

**Data Licensing**: Mixed licensing according to sources, e.g., MIT, Apache-2.0, CC BY-NC-SA 4.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
