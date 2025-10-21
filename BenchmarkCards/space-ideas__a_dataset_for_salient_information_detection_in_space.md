# SPACE-IDEAS: A Dataset for Salient Information Detection in Space

## 📊 Benchmark Details

**Name**: SPACE-IDEAS: A Dataset for Salient Information Detection in Space

**Overview**: SPACE-IDEAS is a dataset for salient information detection from innovation ideas related to the Space domain. It's manually annotated using a methodology that ensures high-quality annotations, and includes an extended version annotated using a large generative language model.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/expertailab/SPACE-IDEAS)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset for detecting salient information in the context of innovation ideas in the Space domain.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Sequential Sentence Classification

**Limitations**: N/A

## 💾 Data

**Source**: Ideas submitted to the Open Space Innovation Platform (OSIP).

**Size**: 176 ideas, 1733 sentences

**Format**: N/A

**Annotation**: Manually annotated and also annotated via a generative language model (gpt-3.5-turbo).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Micro F1-score and span-F1.

**Interpretation**: Higher F1 score indicates better classification performance.

**Validation**: Hold out 20% of the SPACE-IDEAS dataset for testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Only includes text from ideas explicitly marked by the authors as non-confidential.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
