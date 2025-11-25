# VaccineRAG

## 📊 Benchmark Details

**Name**: VaccineRAG

**Overview**: VaccineRAG is a novel Chain-of-Thought-based retrieval-augmented generation dataset, designed to evaluate models using data with varying positive/negative sample ratios and enhance models' sample-discrimination capabilities through explicit Chain-of-Thought reasoning.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WebQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the robustness of models against harmful retrieval samples in multimodal retrieval-augmented generation tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed based on the WebQA dataset.

**Size**: 10,000 entries

**Format**: N/A

**Annotation**: Annotated using a state-of-the-art commercial large model followed by manual verification.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Partial-GRPO

**Metrics**:
- Accuracy

**Calculation**: Evaluated based on the triad of question, ground truth, and model-generated answer scored from 0 to 5, normalized to a range of 0 to 100.

**Interpretation**: Higher scores indicate better alignment with human assessments.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
