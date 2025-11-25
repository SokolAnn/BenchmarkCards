# RobustMath

## 📊 Benchmark Details

**Name**: RobustMath

**Overview**: RobustMath is a dataset consisting of 300 high-quality adversarial samples for Math Word Problems (MWP), proposed to evaluate the robustness of large language models in their math solving ability.

**Data Type**: adversarial math word problem samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MultiAirth

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To measure the robustness of large language models' math solving ability through adversarial samples.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Math Word Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Generated adversarial samples from existing math word problem datasets GSM8K and MultiAirth.

**Size**: 300 examples

**Format**: N/A

**Annotation**: Manual check to ensure high quality and preservation of mathematical logic.

## 🔬 Methodology

**Methods**:
- Adversarial attack

**Metrics**:
- Attack Success Rate (ASR)
- Clean Accuracy
- Attack Accuracy
- Similarity

**Calculation**: Metrics calculated based on the predictions of victim models before and after the attack, along with semantic similarity evaluations.

**Interpretation**: Higher Attack Success Rate (ASR) indicates more effective adversarial samples, while higher Clean Accuracy represents better performance on original problems.

**Baseline Results**: N/A

**Validation**: Extensive experimentation with existing math benchmarks and manual validation of adversarial samples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
