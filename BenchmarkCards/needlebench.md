# NeedleBench

## 📊 Benchmark Details

**Name**: NeedleBench

**Overview**: NeedleBench is a comprehensive synthetic framework designed to assess retrieval and reasoning performance in bilingual long-context tasks with adaptive context lengths, categorizing tasks into information-sparse and information-dense scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](https://openreview.net/forum?id=cEvmIKsRw0)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models on their retrieval and reasoning capabilities across varying information densities and context lengths.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Retrieval
- Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated according to the NeedleBench framework.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- Keyword-aware Score

**Calculation**: Score is calculated based on predefined sets of core keywords compared to the model's predictions, averaging across different experimental dimensions and configurations.

**Interpretation**: A higher score indicates better retrieval and reasoning capabilities, while lower scores indicate difficulties in handling long-context information.

**Baseline Results**: N/A

**Validation**: Evaluation is repeated multiple times to enhance result stability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
