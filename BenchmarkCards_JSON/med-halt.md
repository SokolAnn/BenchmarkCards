# Med-HALT

## 📊 Benchmark Details

**Name**: Med-HALT

**Overview**: Med-HALT is a benchmark and dataset designed to evaluate and mitigate hallucinations in large language models (LLMs) specifically within the medical domain.

**Data Type**: Multinational medical examination dataset

**Domains**:
- Medicine

**Resources**:
- [Resource](medhalt.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and reduce hallucinations in LLMs in the medical domain.

**Target Audience**:
- Researchers
- Medical professionals
- Students

**Tasks**:
- Testing LLMs' performance on hallucination tasks

**Limitations**: N/A

## 💾 Data

**Source**: Derived from medical examinations across various countries, including India, Spain, the U.S., and Taiwan.

**Size**: 18,866 samples for each Reasoning Hallucination Test; 4,916 samples for Memory Hallucination Test.

**Format**: N/A

**Annotation**: Medical examination questions and evaluations of generated outputs.

## 🔬 Methodology

**Methods**:
- Reasoning Hallucination Test (RHT)
- Memory Hallucination Test (MHT)

**Metrics**:
- Accuracy
- Pointwise Score

**Calculation**: Pointwise Score = Sum of (points for correct answers - points for incorrect answers)

**Interpretation**: Higher scores indicate better performance in minimizing hallucinations.

**Validation**: Comparison with leading LLMs including Text Davinci, GPT-3.5, LlaMa-2, MPT, and Falcon.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
