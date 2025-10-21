# Japanese Legal Dataset

## 📊 Benchmark Details

**Name**: Japanese Legal Dataset

**Overview**: We introduce a high-quality, native Japanese legal dataset specifically designed for legal text retrieval, developed manually to preserve essential cultural and linguistic nuances.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- Japanese

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/name)

## 🎯 Purpose and Intended Users

**Goal**: To improve retrieval performance for Japanese legal texts through a specialized dataset and a novel two-phase retrieval pipeline.

**Target Audience**:
- ML Researchers
- Legal Practitioners

**Tasks**:
- Text Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was generated using Gemini 1.5 Pro and includes manually verified legal articles and employment contract documents.

**Size**: 3,259 rows of training data, 73 rows of validation data, 130 rows of test data

**Format**: N/A

**Annotation**: Manual verification and labeling of legal articles was performed to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall
- Mean Reciprocal Rank (MRR)
- Mean Average Precision (MAP)
- Normalized Discounted Cumulative Gain (nDCG)

**Calculation**: Metrics are calculated based on the ranking of retrieved documents against true relevant documents.

**Interpretation**: Higher recall and ranking metrics indicate better retrieval performance.

**Baseline Results**: Competing models include TF-IDF, BM25+, and various neural retrieval models.

**Validation**: The dataset is validated through comparisons with state-of-the-art retrieval methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
