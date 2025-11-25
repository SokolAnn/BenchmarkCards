# OpenHuEval

## 📊 Benchmark Details

**Name**: OpenHuEval

**Overview**: OpenHuEval is the first benchmark for LLMs focusing on the Hungarian language and specifics, providing comprehensive assessment through eight Hungarian-specific dimensions across five tasks with a total of 3953 questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Hungarian

**Similar Benchmarks**:
- HuLU

**Resources**:
- [GitHub Repository](https://github.com/opendatalab/OpenHuEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of LLMs in handling Hungarian language and its specifics.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Hungarian WildBench
- Hungarian SimpleQA
- Hungarian Proverb Reasoning
- Hungarian Matching Fill-in-the-Blank
- Hungarian Standard Fill-in-the-Blank

**Limitations**: N/A

## 💾 Data

**Source**: Hungarian-specific materials sourced from various realms including forums, Wikipedia, proverbs, and educational resources.

**Size**: 3953 questions

**Format**: JSON

**Annotation**: Manual review by Hungarian language experts and users.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-as-judge

**Metrics**:
- Accuracy
- F1 Score
- Question-level Accuracy
- Blank-level Accuracy

**Calculation**: Metrics are calculated based on comparison of model-generated answers with standard answers.

**Interpretation**: A good performance is indicated by high accuracy scores in tasks designed to evaluate relevant Hungarian-specific knowledge.

**Baseline Results**: N/A

**Validation**: The benchmark was validated by comparing it against existing models and benchmarks, along with expert validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All annotators were informed about data usage and ensured data was void of social bias or ethical concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided informed consent for their data to be used.

**Compliance With Regulations**: Not Applicable
