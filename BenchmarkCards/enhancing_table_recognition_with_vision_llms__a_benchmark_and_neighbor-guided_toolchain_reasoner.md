# Enhancing Table Recognition with Vision LLMs: A Benchmark and Neighbor-Guided Toolchain Reasoner

## 📊 Benchmark Details

**Name**: Enhancing Table Recognition with Vision LLMs: A Benchmark and Neighbor-Guided Toolchain Reasoner

**Overview**: The paper proposes a benchmark to evaluate the recognition capabilities of Vision Large Language Models (VLLMs) in table recognition tasks, highlighting challenges such as low-quality image inputs and introducing a new framework called the Neighbor-Guided Toolchain Reasoner (NGTR).

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- SciTSR
- PubTabNet
- WTW

**Resources**:
- [GitHub Repository](https://github.com/lqzxt/NGTR)

## 🎯 Purpose and Intended Users

**Goal**: To establish a benchmark for evaluating table recognition capabilities of Vision Large Language Models (VLLMs).

**Target Audience**:
- ML Researchers
- Practitioners
- Model Developers

**Tasks**:
- Table Recognition

**Limitations**: Performance may depend on the underlying toolkit and the range of scenarios covered by neighbor candidates.

## 💾 Data

**Source**: Datasets include SciTSR, PubTabNet, and WTW for evaluation of table recognition.

**Size**: 15,000 images for SciTSR, 500,777 images for PubTabNet, 10,970 images for WTW

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Experiments on public datasets

**Metrics**:
- Tree Edit Distance (TEDS)
- Accuracy
- Micro-averaged F1 Score

**Calculation**: Calculating similarity between the predicted and ground-truth tree structures of tables.

**Interpretation**: Higher TEDS values indicate better recognition accuracy.

**Baseline Results**: Comparison against traditional lightweight models.

**Validation**: Extensive experiments on multiple public datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
