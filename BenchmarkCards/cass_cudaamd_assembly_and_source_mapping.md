# CASS (CUDA–AMD ASsembly and Source Mapping)

## 📊 Benchmark Details

**Name**: CASS (CUDA–AMD ASsembly and Source Mapping)

**Overview**: CASS is the first large-scale dataset for GPU code transpilation, containing 70k semantically aligned Nvidia ↔AMD pairs at both the source (CUDA ↔HIP) and assembly levels (SASS ↔RDNA3), covering 16 real-world GPU domains.

**Data Type**: code pairs

**Domains**:
- Computer Vision
- Natural Language Processing
- Scientific Computing
- Machine Learning
- Graphics
- Cryptography

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/GustavoStahl/CASS)
- [Resource](https://huggingface.co/datasets/MBZUAI/cass)

## 🎯 Purpose and Intended Users

**Goal**: To address the lack of cross-architecture GPU translation datasets and to validate the effectiveness of GPU code transpilation models.

**Target Audience**:
- ML Researchers
- Domain Experts
- Compiler Developers

**Tasks**:
- Source-to-Source Translation
- Assembly-to-Assembly Translation

**Limitations**: Current performance is inadequate for production due to limited accuracy in complex or underrepresented domains. The dataset only covers one host/device pair per vendor.

## 💾 Data

**Source**: The dataset is constructed from verified CUDA and HIP code pairs, along with their corresponding assembly representations.

**Size**: 70,000 pairs

**Format**: Aligned source and assembly code

**Annotation**: Manually verified to compile and run successfully

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the percentage of successful translations compared to ground-truth outputs.

**Interpretation**: Higher accuracy indicates better performance in translating GPU code across different architectures.

**Baseline Results**: Achieved 95% accuracy in source translation and 37.5% in assembly translation.

**Validation**: The dataset and models were validated against real-world execution scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All data, models, and evaluation tools are released as open source.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
