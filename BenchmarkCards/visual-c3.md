# Visual-C3

## 📊 Benchmark Details

**Name**: Visual-C3

**Overview**: Visual-C3 is a large-scale human-annotated Visual Chinese Character Checking dataset with faked and misspelled Chinese characters, consisting of 10,072 sentences represented by images and 12,019 wrong characters. It facilitates automatic detection and correction of faked characters in writing assistance.

**Data Type**: sentence-image pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- SIGHAN2013
- SIGHAN2014
- SIGHAN2015

**Resources**:
- [GitHub Repository](https://github.com/THUKElab/Visual-C3)

## 🎯 Purpose and Intended Users

**Goal**: To improve the correctness and quality of input texts through character checking by detecting and correcting faked and misspelled characters.

**Target Audience**:
- NLP Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Character Detection
- Character Correction

**Limitations**: N/A

## 💾 Data

**Source**: Photos of handwritten essays collected from students in a middle school.

**Size**: 1,611 photos containing 10,072 images and 12,019 wrong characters (5,670 misspelled and 6,349 faked characters)

**Format**: Images

**Annotation**: Manual annotation by well-trained annotators

## 🔬 Methodology

**Methods**:
- Character-level Annotation
- Sentence-level Annotation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision and Recall are computed for both detection and correction tasks at character and sentence levels.

**Interpretation**: High Precision and Recall indicate effective detection and correction of faked and misspelled characters.

**Baseline Results**: OCR-based and CLIP-based methods were used as baselines, with varying performance metrics.

**Validation**: Annotation accuracy is verified by double-checking by senior annotators, with a Fleiss’ kappa score of 85.20% indicating almost perfect agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data has been authorized by its providers and desensitized before annotation to ensure privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Written consent obtained from students providing data.

**Compliance With Regulations**: Not Applicable
