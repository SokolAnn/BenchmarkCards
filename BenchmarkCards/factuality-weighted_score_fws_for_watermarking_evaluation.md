# Factuality-Weighted Score (FWS) for Watermarking Evaluation

## 📊 Benchmark Details

**Name**: Factuality-Weighted Score (FWS) for Watermarking Evaluation

**Overview**: We propose a medical-focused evaluation workflow that jointly assesses factual accuracy and coherence using FWS, a composite metric prioritizing factual accuracy in watermarking methods for medical texts.

**Data Type**: text

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/rochanaph/fact-eval-wllm)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable framework for evaluating watermarking methods in medical domains by emphasizing factual integrity in generated texts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Medical Professionals

**Tasks**:
- Text Completion
- Question Answering
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: HealthQA dataset, MeQSum dataset

**Size**: 200 question-answer pairs from HealthQA, various texts from MeQSum

**Format**: JSON

**Annotation**: Annotated using human evaluation and automatic metrics

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- GPT-Judger assessments

**Metrics**:
- Factuality-Weighted Score (FWS)
- ROUGE-2
- F1 Score
- AlignScore

**Calculation**: FWS is calculated by emphasizing factual accuracy over coherence based on a weighted formula.

**Interpretation**: Higher FWS indicates better factual integrity in the generated text.

**Baseline Results**: Current watermarking methods face notable factuality degradation despite high detection capabilities.

**Validation**: Validated through correlation analysis with human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
