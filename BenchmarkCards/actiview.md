# ActiView

## 📊 Benchmark Details

**Name**: ActiView

**Overview**: ActiView evaluates active perception in Multimodal Large Language Models (MLLMs) through Visual Question Answering (VQA) tasks that require models to perform view shifting and zooming to gather information from images to answer questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- BLINK
- V*
- CNT

**Resources**:
- [GitHub Repository](https://github.com/THUNLP-MT/ActiView)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ActiView is to develop methods for MLLMs to understand multimodal inputs in a more natural and holistic way by evaluating their active perception capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually curated images and question-answer pairs with visual clues.

**Size**: 314 images, 1,625 evaluation instances

**Format**: N/A

**Annotation**: Manual annotation with specific guidelines for question and options related to visual clues.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct answers among the given responses.

**Interpretation**: A higher accuracy indicates better performance in understanding multimodal images and reasoning based on visual information.

**Baseline Results**: Human performance achieved an average accuracy of 84.67%.

**Validation**: Benchmarked against 30 models, including proprietary and open-source.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination, Evasion attack
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
