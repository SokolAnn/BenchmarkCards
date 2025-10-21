# MMAR (Multi-disciplinary Multi-modal Audio Reasoning)

## 📊 Benchmark Details

**Name**: MMAR (Multi-disciplinary Multi-modal Audio Reasoning)

**Overview**: MMAR is a new benchmark designed to evaluate the deep reasoning capabilities of Audio-Language Models (ALMs) across massive multi-disciplinary tasks, comprising 1,000 meticulously curated audio-question-answer triplets. It focuses on real-world audio scenarios, requiring multi-step reasoning beyond surface-level understanding.

**Data Type**: audio-question-answer triplets

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Japanese
- Korean
- French
- Italian
- German

**Resources**:
- [GitHub Repository](https://github.com/ddlBoJack/MMAR)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MMAR is to provide a rigorous benchmark for evaluating audio deep reasoning capabilities in a variety of audio contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Deep Reasoning
- Audio Processing

**Limitations**: N/A

## 💾 Data

**Source**: Collected from real-world internet videos with iterative error corrections.

**Size**: 1,000 examples

**Format**: JSON

**Annotation**: Manual annotation by expert annotators trained in audio processing.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Classification accuracy

**Calculation**: Accuracy is calculated based on the number of correct predictions from the model compared to the ground truth.

**Interpretation**: Higher accuracy indicates better reasoning capabilities of the models in handling multi-step audio reasoning tasks.

**Baseline Results**: The best-performing open-source model Qwen-2.5-Omni achieves an average accuracy below 60%.

**Validation**: Validated through expert review and quality control processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sources are publicly available videos, minimizing privacy concerns.

**Data Licensing**: The dataset will be released under a CC-BY-NC license for non-commercial use.

**Consent Procedures**: Consent procedures are not applicable as the data is collected from public sources.

**Compliance With Regulations**: Not Applicable
