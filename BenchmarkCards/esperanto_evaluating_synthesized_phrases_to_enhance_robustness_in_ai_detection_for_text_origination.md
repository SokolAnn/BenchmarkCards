# ESPERANTO (Evaluating Synthesized Phrases to Enhance Robustness in AI Detection for Text Origination)

## 📊 Benchmark Details

**Name**: ESPERANTO (Evaluating Synthesized Phrases to Enhance Robustness in AI Detection for Text Origination)

**Overview**: This paper introduces a dataset of 720k human-authored and LLM-generated texts used to assess the robustness of AI text detection mechanisms and proposes a novel manipulation technique through back-translation to evade existing detection methods.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/navid-aub/Esperanto-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the robustness of AI text detection systems against manipulation techniques such as back-translation.

**Target Audience**:
- ML Researchers
- AI Ethics Researchers
- Detection System Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: A dataset comprising human-authored and LLM-generated texts created through back-translation and various prompts across multiple styles.

**Size**: 720,000 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation on AI text detectors
- Back-translation manipulation

**Metrics**:
- True Positive Rate (TPR)

**Calculation**: Measured TPR before and after applying back-translation manipulation across multiple datasets.

**Interpretation**: Higher TPR indicates better detection capability of AI text detectors, while a reduction in TPR indicates vulnerability.

**Baseline Results**: N/A

**Validation**: Conducted tests using nine different AI detectors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
