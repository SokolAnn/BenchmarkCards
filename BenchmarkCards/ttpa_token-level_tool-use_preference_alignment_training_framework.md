# TTPA (Token-level Tool-use Preference Alignment Training Framework)

## 📊 Benchmark Details

**Name**: TTPA (Token-level Tool-use Preference Alignment Training Framework)

**Overview**: TTPA is a training paradigm that constructs token-level tool-use preference datasets to align LLMs with fine-grained preferences using an error-oriented scoring mechanism.

**Data Type**: instruction instances and preference pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolBench
- Berkeley Function-Calling Benchmark (BFCL)

**Resources**:
- [GitHub Repository](https://github.com/Anonymous/TTPA)

## 🎯 Purpose and Intended Users

**Goal**: Enhance the tool-use capabilities of large language models (LLMs) by aligning them with fine-grained user preferences.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Tool Usage
- Multi-turn Interaction

**Limitations**: Fine-grained token-level preference sampling may increase computational complexity and training time.

## 💾 Data

**Source**: Generated using LLMs based on the TTPA framework methods.

**Size**: 3,895 instruction instances and 8,550 preference pairs

**Format**: JSON

**Annotation**: Automatically generated with some manual verification.

## 🔬 Methodology

**Methods**:
- Error-oriented scoring mechanism
- Token-level preference sampling
- Reversed dataset construction

**Metrics**:
- Accuracy
- Pass Rate

**Calculation**: Metrics calculated based on the performance of LLMs in selecting appropriate tools and parameters.

**Interpretation**: Higher scores indicate better tool-selection and parameter generation capabilities.

**Baseline Results**: TTPA (Qwen) achieved 86.0% accuracy in the ToolBench benchmark.

**Validation**: Extensive experiments on benchmark datasets demonstrate significant improvements in tool usage.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data privacy measures followed using publicly available datasets.

**Data Licensing**: All tools and datasets used were obtained from existing benchmarks and public resources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
