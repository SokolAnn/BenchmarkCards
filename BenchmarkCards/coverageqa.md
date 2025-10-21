# CoverageQA

## 📊 Benchmark Details

**Name**: CoverageQA

**Overview**: CoverageQA is a benchmark of underspecified questions with multiple equally plausible answers, designed to assess generation diversity in language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2410.09038)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate generation diversity from large language models by measuring their ability to recall valid solutions to underspecified questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Generation

**Limitations**: CoverageQA is sensitive to the model selecting meaningful axes in auto-stratification and correct joint probabilities in heuristic estimation.

## 💾 Data

**Source**: Automatically generated from WikiData, ensuring a diverse and extensive benchmark.

**Size**: 105 questions

**Format**: N/A

**Annotation**: Automatically transformed into natural language questions using GPT-4.

## 🔬 Methodology

**Methods**:
- KL Divergence Measurement
- Recall Measurement

**Metrics**:
- Recall
- KL Divergence

**Calculation**: KL Divergence is calculated between the model's output distribution and a uniform distribution over valid answers.

**Interpretation**: Lower KL Divergence indicates a closer alignment with the desired uniform distribution; higher recall represents better diversity.

**Baseline Results**: On CoverageQA, SimpleStrat achieves a 0.36 reduction in KL Divergence and a 0.05 increase in recall compared to baseline methods.

**Validation**: Evaluated using both proprietary and open-source models on diverse underspecified questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
