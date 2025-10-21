# Laboratory Safety Benchmark (LabSafety Bench)

## 📊 Benchmark Details

**Name**: Laboratory Safety Benchmark (LabSafety Bench)

**Overview**: LabSafety Bench is a comprehensive framework designed to evaluate large language models and vision language models on their ability to identify potential hazards, assess risks, and predict the consequences of unsafe actions in laboratory environments, consisting of multiple-choice questions and realistic laboratory scenarios.

**Data Type**: multiple-choice questions and open-ended questions

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/YujunZhou/LabSafety-Bench)
- [Resource](https://huggingface.co/datasets/yujunzhou/LabSafety_Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reliability of LLMs and VLMs in assessing laboratory safety, thereby enhancing safe practices in laboratory environments.

**Target Audience**:
- ML Researchers
- Safety Personnel
- Laboratory Practitioners

**Tasks**:
- Hazards Identification
- Risk Assessment
- Consequence Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Expert-curated dataset with contributions from domain specialists and AI.

**Size**: 765 multiple-choice questions, 404 realistic laboratory scenarios, 3128 open-ended questions total

**Format**: JSON

**Annotation**: Manual annotation by experts after cross-review for accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on model responses compared to expert-curated answers and ground truth.

**Interpretation**: Models are assessed on their understanding of safety protocols in laboratory settings, with high accuracy indicating sound operational safety knowledge.

**Validation**: Benchmark validated through comparisons with human expert performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Increased risk of hazardous incidents in laboratories due to model inaccuracies.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study includes a human evaluation approved by the Institutional Review Board (IRB) at the University of Notre Dame.
