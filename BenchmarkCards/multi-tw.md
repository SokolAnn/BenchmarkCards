# Multi-TW

## 📊 Benchmark Details

**Name**: Multi-TW

**Overview**: Multi-TW is the first Traditional Chinese benchmark for evaluating the performance and latency of any-to-any multimodal models. It comprises 900 multiple-choice questions (image & text, audio & text pairs) from authentic proficiency tests.

**Data Type**: multiple-choice questions (image & text, audio & text pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Traditional Chinese

**Similar Benchmarks**:
- TMMLU+
- VisTW-MCQ
- ALM-Bench
- OmniBench

**Resources**:
- [Resource](https://drive.google.com/drive/folders/1IvBOXR1GpMNtst0T3HT6dM59_ASlXdyn)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the capabilities of multimodal large language models in Traditional Chinese with respect to performance and latency.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Multiple Choice Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated from authentic proficiency tests developed with the Steering Committee for the Test of Proficiency-Huayu.

**Size**: 900 multiple-choice questions

**Format**: JSON

**Annotation**: Each item was independently reviewed by a second annotator to verify content consistency and accuracy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact-match accuracy

**Calculation**: Accuracy reflects the percentage of correctly answered multiple-choice questions.

**Interpretation**: Higher accuracy indicates better performance in answering the multimodal questions.

**Validation**: Each item was subjected to quality control checks including completeness, file consistency, and label accuracy verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
