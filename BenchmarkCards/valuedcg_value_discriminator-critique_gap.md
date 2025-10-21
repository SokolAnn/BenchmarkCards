# ValueDCG (Value Discriminator-Critique Gap)

## 📊 Benchmark Details

**Name**: ValueDCG (Value Discriminator-Critique Gap)

**Overview**: ValueDCG is a comprehensive evaluation metric designed to quantitatively assess the understanding of human values by language models, focusing on both the ability to identify values ('know what') and to explain them ('know why').

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ValueNet
- ETHICS

**Resources**:
- [GitHub Repository](https://github.com/zowiezhang/ValueDCG)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the understanding of human values by large language models in a comprehensive manner that considers both identification and explanation capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Value Understanding Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Datasets include ValueNet and ETHICS, which provide human-annotated labels for different values.

**Size**: N/A

**Format**: N/A

**Annotation**: Human annotation by trained evaluators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ValueDCG

**Calculation**: ValueDCG is calculated by comparing the outputs from language models on 'know what' and 'know why' assessments.

**Interpretation**: A lower ValueDCG score indicates a better understanding of human values.

**Baseline Results**: N/A

**Validation**: Evaluation is based on multiple datasets with human labeling compared against model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
