# CCQA (Cycle-Consistency in Question Answering)

## 📊 Benchmark Details

**Name**: CCQA (Cycle-Consistency in Question Answering)

**Overview**: CCQA is a novel inference-time reasoning method designed to enhance the reasoning capabilities of small language models (SLMs) by generating questions from candidate solutions and selecting the most consistent response based on similarity to the original question.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- CommonSenseQA
- StrategyQA
- ARC-Challenge
- Multi-Arith
- SV AMP

**Resources**:
- [GitHub Repository](https://github.com/scai-research/ccqa_official)

## 🎯 Purpose and Intended Users

**Goal**: To improve inference-time reasoning in small language models through cycle consistency in question answering.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Commonsense Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Evaluated on reasoning benchmarks like GSM8K, SV AMP, CSQA, StrategyQA, and ARC-Challenge.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on how well CCQA performs on various reasoning tasks compared to state-of-the-art methods.

**Interpretation**: Higher accuracy indicates improved reasoning capability.

**Baseline Results**: CCQA achieved 69.60% accuracy on GSM8K, outperforming USC at 53.83%; and 38.74% accuracy on CommonSenseQA compared to USC's 33.99%.

**Validation**: Validated through extensive experiments across multiple reasoning benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
