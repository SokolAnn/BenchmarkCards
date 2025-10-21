# GridToM

## 📊 Benchmark Details

**Name**: GridToM

**Overview**: GridToM is a novel multimodal dataset that incorporates diverse belief-testing tasks alongside perceptual information from multiple perspectives, designed to evaluate the Theory of Mind capabilities of multimodal large language models.

**Data Type**: video-text pairs

**Domains**:
- Artificial Intelligence
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMToM-QA
- ToMi
- MindGames

**Resources**:
- [Resource](https://annaisavailable.github.io/GridToM)

## 🎯 Purpose and Intended Users

**Goal**: The primary goal of this benchmark is to evaluate the Theory of Mind capabilities of multimodal large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- First-Order Belief Assessment
- Second-Order Belief Assessment

**Limitations**: The tasks in this dataset are limited to first-order and second-order belief tasks within the ATOMS framework.

## 💾 Data

**Source**: Generated using the Multigrid library, based on 27 distinct 10x7 maps incorporating visual and linguistic data.

**Size**: 1,296 video-text pairs

**Format**: JSON

**Annotation**: Automatically generated and verified, minimal manual annotation.

## 🔬 Methodology

**Methods**:
- Logistic Regression for probing
- Intervention strategies

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correctly answered belief questions in the dataset.

**Interpretation**: Higher accuracy indicates better performance in understanding and reasoning about beliefs in a multimodal context.

**Baseline Results**: Humans achieved 99.9% accuracy in belief assessments, while models showed lower performance, especially in distinguishing first-order beliefs.

**Validation**: The dataset undergoes rigorous quality control including automated validation and human review to ensure correctness in task design.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
