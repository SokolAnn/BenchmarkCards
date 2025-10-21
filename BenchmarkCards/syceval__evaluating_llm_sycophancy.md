# SycEval: Evaluating LLM Sycophancy

## 📊 Benchmark Details

**Name**: SycEval: Evaluating LLM Sycophancy

**Overview**: This study introduces a framework to evaluate sycophantic behavior in models like ChatGPT-4o, Claude-Sonnet, and Gemini-1.5-Pro across the AMPS (mathematics) and MedQuad (medical advice) datasets.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- SYCON

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and benchmark sycophantic behavior in large language models to ensure reliability in high-stakes applications.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: AMPS Mathematics dataset and MedQuad medical advice dataset.

**Size**: 1,000 question-and-answer pairs

**Format**: N/A

**Annotation**: Manually designed Mathematica scripts for AMPS; Medical questions collected from real-life patient inquiries for MedQuad.

## 🔬 Methodology

**Methods**:
- LLM-as-A-Judge evaluation
- Binomial proportion confidence intervals
- Two-proportion z-test
- Chi-square test
- Beta distribution modeling

**Metrics**:
- Sycophancy rates
- Statistical significance of sycophancy behavior

**Calculation**: Confidence intervals calculated using binomial proportions; differences analyzed via statistical testing.

**Interpretation**: Sycophancy is interpreted in terms of agreement with user prompts versus factual correctness.

**Baseline Results**: Gemini exhibited the highest sycophancy rate at 62.47%.

**Validation**: Validated through both LLM evaluation and human response categorization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Reinforcing unsafe medical advice']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
