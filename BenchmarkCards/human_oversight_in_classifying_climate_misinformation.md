# Human Oversight in Classifying Climate Misinformation

## 📊 Benchmark Details

**Name**: Human Oversight in Classifying Climate Misinformation

**Overview**: This paper benchmarks the performance of LLMs, both open-source and proprietary, in the classification of false or misleading claims about climate change using expert-annotated datasets.

**Data Type**: paragraphs of text with expert annotations

**Domains**:
- Natural Language Processing
- Climate Science

**Languages**:
- English

**Similar Benchmarks**:
- CARDS (Computer Assisted Recognition of Denial and Skepticism)

**Resources**:
- [GitHub Repository](https://github.com/nwccpp/climatechange)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs for the classification of climate misinformation and to highlight the necessity of human oversight in such governance tasks.

**Target Audience**:
- AI Researchers
- Climate Scientists
- Policymakers

**Tasks**:
- False Claims Classification
- Misinformation Detection

**Limitations**: The dataset is in English and potentially biased towards claims from climate skeptic sources.

## 💾 Data

**Source**: Public expert-annotated dataset of climate misinformation claims and curated social media content.

**Size**: 23,436 training examples, 2,605 validation examples, 2,904 test examples

**Format**: JSONL

**Annotation**: Annotated by climate communication experts

## 🔬 Methodology

**Methods**:
- Zero-shot classification
- Fine-tuning on expert-annotated data

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics were calculated based on the performance of LLMs in classifying claims compared to expert annotations.

**Interpretation**: Higher F1, precision, and recall indicate better accuracy in classifying false or misleading claims.

**Baseline Results**: Fine-tuned GPT-3.5-turbo achieved F1 score of 0.84, outperforming other models.

**Validation**: Results validated against expert annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misuse in the spread of disinformation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
