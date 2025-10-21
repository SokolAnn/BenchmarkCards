# SWE-Dev (Software Development Evaluation Dataset)

## 📊 Benchmark Details

**Name**: SWE-Dev (Software Development Evaluation Dataset)

**Overview**: SWE-Dev is the first large-scale dataset designed to evaluate and train autonomous coding systems on real-world feature development tasks. It consists of 14,000 training and 500 test instances, each uniquely equipped with runnable environments and developer-authored executable unit tests.

**Data Type**: task instances with runnable environments and executable unit tests

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- SWE-Bench
- RepoBench

**Resources**:
- [GitHub Repository](https://github.com/DorothyDUUU/SWE-Dev)

## 🎯 Purpose and Intended Users

**Goal**: To provide a critical platform for evaluating autonomous coding systems on feature-driven development tasks.

**Target Audience**:
- ML Researchers
- Software Developers
- AI Practitioners

**Tasks**:
- Feature Development

**Limitations**: The current focus is on Python and basic training strategies, lacking multilingual support and more advanced paradigms.

## 💾 Data

**Source**: Real-world open-source software repositories from PyPI.

**Size**: 14,500 samples (14,000 training and 500 test)

**Format**: N/A

**Annotation**: Each instance is paired with executable test cases and project requirement descriptions.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning (SFT)
- Reinforcement Learning (RL)
- Multi-Agent System Training

**Metrics**:
- Pass@1
- Pass@3

**Calculation**: Metrics are calculated based on the pass rate of test cases written for each coding task in the dataset.

**Interpretation**: Higher Pass@1 and Pass@3 indicates better model performance in solving coding tasks.

**Baseline Results**: Models like Claude-3.7-Sonnet and GPT-4o achieved notable scores on SWE-Dev but struggled with complex tasks.

**Validation**: Validation is performed via executable unit tests that check the implemented features.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All codebases and data are sourced from publicly available repositories respecting their licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
