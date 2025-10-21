# TCELongBench

## 📊 Benchmark Details

**Name**: TCELongBench

**Overview**: TCELongBench is established to evaluate the proficiency of LLMs in handling temporal dynamics and understanding extensive text through three distinct tasks - reading comprehension, temporal sequencing, and future event forecasting.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2406.02472)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of TCELongBench is to evaluate LLMs' capability of temporal and long text understanding.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Reading Comprehension
- Temporal Sequencing
- Future Event Forecasting

**Limitations**: N/A

## 💾 Data

**Source**: Mideast-TE corpus that has identified Temporal Complex Events from GDELT.

**Size**: 88,821 question answering pairs

**Format**: N/A

**Annotation**: Generated using a generate-then-verify paradigm.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU score

**Calculation**: Metrics are calculated based on model performance on question answering tasks.

**Interpretation**: Higher accuracy and F1 scores indicate better model performance in understanding Temporal Complex Events.

**Baseline Results**: Gpt-4-128k outperforms all other models in tasks.

**Validation**: Human evaluation and multiple rounds of QA verification were conducted.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
