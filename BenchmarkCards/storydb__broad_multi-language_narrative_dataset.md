# StoryDB: Broad Multi-language Narrative Dataset

## 📊 Benchmark Details

**Name**: StoryDB: Broad Multi-language Narrative Dataset

**Overview**: StoryDB is a corpus of texts that includes stories in 42 different languages. Every language includes 500+ stories. The dataset serves as a resource for the study of the role of narrative in natural language processing across various languages including low resource ones.

**Data Type**: narrative texts

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Armenian
- Italian
- French
- Russian
- German
- Dutch
- Ukrainian
- Portuguese
- Polish
- Spanish
- Persian
- Finnish
- Hungarian
- Czech
- Japanese

**Resources**:
- [Resource](https://drive.google.com/drive/folders/1RCWk7pyvIpubtsf-f2pIsfqTkvtV80Yv)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large multi-language dataset of narratives to facilitate various aspects of narrative research and improve narrative generation.

**Target Audience**:
- NLP Researchers
- Machine Learning Practitioners
- Story Generation Researchers

**Tasks**:
- Multilabel Classification
- Cross-lingual Learning
- Narrative Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia articles that contain plot summaries in various languages.

**Size**: Over 20,000 stories across 42 languages

**Format**: TSV

**Annotation**: Automatically tagged using categories from Wiki API and manual tagging procedures.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Hamming Score
- Multilabel Accuracy
- AUC-ROC

**Calculation**: Metrics calculated based on performance of transformer-based models on multilabel classification tasks.

**Interpretation**: Higher scores indicate better model performance in predicting narrative tags accurately.

**Baseline Results**: The results from models such as mBERT, mDistilBERT, and XLM-RoBERTa showed varying performance in tag classification.

**Validation**: Evaluation performed on ten largest languages in the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
