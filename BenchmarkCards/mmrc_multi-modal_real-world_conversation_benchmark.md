# MMRC (Multi-Modal Real-world Conversation benchmark)

## 📊 Benchmark Details

**Name**: MMRC (Multi-Modal Real-world Conversation benchmark)

**Overview**: MMRC is a benchmark for evaluating six core open-ended abilities of Multimodal Large Language Models (MLLMs) in real-world conversations, consisting of 5,120 conversations and 28,720 corresponding manually labeled questions.

**Data Type**: conversational dialogue with text and images

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MT-Bench
- DialogBench
- LongMemEval

**Resources**:
- [GitHub Repository](https://github.com/tiuxuxsh76075/MMRC)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for MLLMs' performance in practical, open-ended conversational settings.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Information Extraction
- Cross-turn Reasoning
- Information Update
- Image Management
- Memory Recall
- Answer Refusal

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from real-world multi-modal conversations through the DialogFlow platform.

**Size**: 5,120 conversations

**Format**: Text and images

**Annotation**: Manually annotated questions and responses

## 🔬 Methodology

**Methods**:
- GPT-based evaluation
- Human evaluation
- Objective precision metrics

**Metrics**:
- Accuracy
- Precision

**Calculation**: Metrics are calculated based on comparisons of model responses against manually annotated ground truth answers.

**Interpretation**: Performance is interpreted based on a scoring scale from 0 to 5 for each evaluated ability, with higher scores indicating better performance.

**Baseline Results**: Performance assessed against 20 mainstream MLLMs

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection was done with informed consent, ensuring participant privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from participants for data usage.

**Compliance With Regulations**: Not Applicable
