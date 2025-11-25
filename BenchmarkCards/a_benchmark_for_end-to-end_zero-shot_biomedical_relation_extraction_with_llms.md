# A Benchmark for End-to-End Zero-Shot Biomedical Relation Extraction with LLMs

## 📊 Benchmark Details

**Name**: A Benchmark for End-to-End Zero-Shot Biomedical Relation Extraction with LLMs

**Overview**: This paper introduces a benchmark for end-to-end zero-shot biomedical relation extraction (RE) using OpenAI models, exploring their performance across seven datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/bionlproc/ZeroShotRE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and understand the effectiveness of zero-shot methodologies in biomedical relation extraction, comparing results across various datasets.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Relation Extraction

**Limitations**: The performance of models decreases significantly with longer texts that contain multiple relations.

## 💾 Data

**Source**: Seven different biomedical datasets used for relation extraction tasks.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation of performance across multiple datasets using OpenAI LLMs.

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: F1 scores are calculated by assessing matches between predicted and gold relations.

**Interpretation**: Each predicted relation is considered correct if extracted entity mentions match any gold entity mentions.

**Baseline Results**: Performance results compared against fine-tuned and existing methods as detailed in the results section.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
