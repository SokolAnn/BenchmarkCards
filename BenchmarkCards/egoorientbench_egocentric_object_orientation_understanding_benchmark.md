# EgoOrientBench (Egocentric Object Orientation Understanding Benchmark)

## 📊 Benchmark Details

**Name**: EgoOrientBench (Egocentric Object Orientation Understanding Benchmark)

**Overview**: EgoOrientBench is a benchmark designed to comprehensively evaluate MLLMs’ orientation understanding across three tasks and five image datasets by aligning object orientation comprehension with the user’s egocentric perspective.

**Data Type**: images

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jhCOR/EgoOrientBench)

## 🎯 Purpose and Intended Users

**Goal**: To enhance MLLMs’ understanding of object orientation from the user’s egocentric perspective and evaluate performance through three carefully designed tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Object Orientation Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Five distinct image datasets including ImageNet, D3, DomainNet, PACS, and OmniObject3D.

**Size**: Approximately 6,000 images across various orientations.

**Format**: N/A

**Annotation**: Manually annotated based on an egocentric perspective using a consistent annotation rule.

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Instruction tuning

**Metrics**:
- Accuracy

**Calculation**: Metrics evaluation through three tasks: Choose (classification), Verify (binary classification), and Freeform (descriptive response).

**Interpretation**: Higher accuracy indicates better alignment with human perception of object orientation.

**Baseline Results**: N/A

**Validation**: Evaluated using standard benchmarks for multimodal models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
