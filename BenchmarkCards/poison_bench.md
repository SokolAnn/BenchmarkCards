# POISON BENCH

## 📊 Benchmark Details

**Name**: POISON BENCH

**Overview**: POISON BENCH is a benchmark for evaluating large language models’ susceptibility to data poisoning during preference learning.

**Data Type**: preference data

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/TingchenFu/PoisonBench)

## 🎯 Purpose and Intended Users

**Goal**: To measure the efficacy of data poisoning attacks during preference learning and benchmark the robustness of existing LLM backbones.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners

**Tasks**:
- Preference Learning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Preference datasets HH-RLHF and Ultrafeedback

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Attack Success (AS)
- Stealthiness Score (SS)

**Calculation**: AS is calculated as the frequency of the target entity being mentioned with a trigger present versus without, while SS measures model performance on non-trigger inputs.

**Interpretation**: Higher AS indicates greater success of the attack, while higher SS indicates better normal model performance.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Security

**Atlas Risks**:
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Manipulation of model responses']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
