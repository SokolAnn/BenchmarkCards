# HCT-QA (Human-Centric Tables for Question Answering)

## 📊 Benchmark Details

**Name**: HCT-QA (Human-Centric Tables for Question Answering)

**Overview**: HCT-QA is an extensive benchmark for Question Answering on Human-Centric Tables (HCTs), containing 2,188 real-world HCTs with 9,835 QA pairs and 4,679 synthetic HCTs with 67,500 QA pairs, aimed at assessing the capability of Large Language Models in processing and querying such complex tables.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/shahmeer99/HCT-QA-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a novel benchmark for evaluating the performance of Large Language Models in answering questions based on human-centric tables.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: HCTs collected from diverse real-world document sources including government statistics and scientific data.

**Size**: 6,867 HCTs with 77,580 QA pairs

**Format**: CSV, Image

**Annotation**: 33% manually created and 66% automatically generated and manually annotated

## 🔬 Methodology

**Methods**:
- Evaluation of Large Language Models
- Human evaluation

**Metrics**:
- Mean Containment (MC Score)
- Complete Containment (CC Score)

**Calculation**: MC Score is calculated as the average proportion of values from the ground truth found within the model's answer; CC Score equals 1 when MC=1 and 0 otherwise.

**Interpretation**: Higher MC and CC scores signify better model performance in answering questions accurately.

**Validation**: Multiple LLMs were evaluated using the benchmark to assess their performance on HCTs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
