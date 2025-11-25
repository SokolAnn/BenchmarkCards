# RECALL: A Benchmark for LLMs Robustness against External Counterfactual Knowledge

## 📊 Benchmark Details

**Name**: RECALL: A Benchmark for LLMs Robustness against External Counterfactual Knowledge

**Overview**: We create a benchmark for LLMs to evaluate their robustness against counterfactual knowledge from external texts, consisting of two tasks: Question Answering and Text Generation.

**Data Type**: question-answering pairs and text generation samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified and reliable standard for evaluating LLMs’ robustness against external counterfactual information.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Existing datasets including EventKG and UJ-CS/Math/Phy, with counterfactual information added via ChatGPT.

**Size**: 47,000 samples

**Format**: N/A

**Annotation**: Counterfactual information added and tested against original datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Metric-based evaluation

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- Misleading Rate (M-Rate)
- Mistake Reappearance Rate (R-Rate)

**Calculation**: Metrics are calculated based on the performance of models on edited vs. original contexts.

**Interpretation**: High metrics indicate better robustness against counterfactual information.

**Validation**: Evaluation includes multiple language models under varying conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
