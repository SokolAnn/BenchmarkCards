# LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code Completion

## 📊 Benchmark Details

**Name**: LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code Completion

**Overview**: This paper conducts the first evaluation study on deprecated API usage in LLM-based code completion involving seven advanced LLMs, 145 API mappings from eight popular Python libraries, and 28,125 completion prompts, revealing the status quo of deprecated API usage in code completions.

**Data Type**: completion prompts

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2406.09834)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the statuses and causes of deprecated API usages in LLM-based code completion and propose lightweight mitigation methods.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Code Completion

**Limitations**: N/A

## 💾 Data

**Source**: Open-source Python repositories, including API mappings and functions from popular libraries (Numpy, Pandas, scikit-learn, SciPy, PyTorch, TensorFlow, and Transformers).

**Size**: 28,125 completion prompts

**Format**: N/A

**Annotation**: The completions were annotated using a systematic approach to classify them as deprecated or replacement completions.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- API Usage Plausibility (AUP)
- Deprecated Usage Rate (DUR)

**Calculation**: AUP measures plausible completions corresponding to deprecated or replacement APIs; DUR calculates the rate of plausible completions that are deprecated API suggestions.

**Interpretation**: AUP and DUR metrics indicate the effectiveness of LLMs in handling deprecated API usages in code completions.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Avoiding reliance on deprecated APIs to maintain code integrity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
