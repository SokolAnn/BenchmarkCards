# S2SBench

## 📊 Benchmark Details

**Name**: S2SBench

**Overview**: S2SBench is a benchmark designed to quantify performance degradation in speech large language models (LLMs) by evaluating model performance under audio and text input conditions. It includes diagnostic datasets focusing on sentence continuation and commonsense reasoning.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/undobug/S2SBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of S2SBench is to systematically evaluate the gap in reasoning and generation performance of speech models compared to text-based models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Sentence Continuation
- Commonsense Reasoning

**Limitations**: This work primarily evaluates the intelligence capability of speech large language models through the speech-to-text (S → T) setting.

## 💾 Data

**Source**: Constructed evaluation datasets focused on sentence continuation and commonsense reasoning.

**Size**: 4,743 questions for commonsense reasoning in sCMMLU; datasets for sentence continuation.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Pairwise evaluation based on perplexity differences

**Metrics**:
- Perplexity
- Accuracy

**Calculation**: Perplexity is calculated for positive and negative samples, indicating model confidence in given samples.

**Interpretation**: Lower perplexity indicates higher model confidence. The model makes a correct judgment when the positive example has lower perplexity than the negative example.

**Baseline Results**: N/A

**Validation**: Evaluation conducted under controlled settings to assess model behavior across text-token and audio-token conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Transparency

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
