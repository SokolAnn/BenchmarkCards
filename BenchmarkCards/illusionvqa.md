# IllusionVQA

## 📊 Benchmark Details

**Name**: IllusionVQA

**Overview**: IllusionVQA is a diverse dataset of challenging optical illusions and hard-to-interpret scenes designed to test the capability of Vision Language Models (VLMs) in two distinct multiple-choice VQA tasks - comprehension and soft localization.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GVIL
- HallusionBench

**Resources**:
- [GitHub Repository](https://github.com/csebuetnlp/IllusionVQA)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously test the ability of Vision Language Models (VLMs) to locate and comprehend challenging optical illusions.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Visual Question Answering

**Limitations**: The number of examples in the IllusionVQA-Comprehension dataset is relatively modest due to the rigorous filtering process applied to the initial candidate set of over 3500 images scraped from the Internet.

## 💾 Data

**Source**: Datasets of optical illusions collected from multiple online repositories, with over 3500 images scraped and filtered for quality.

**Size**: 374 images

**Format**: N/A

**Annotation**: Manually crafted question-answer pairs with multiple choice options.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the percentage of correct answers provided by VLMs and human evaluators.

**Interpretation**: Higher accuracy indicates better comprehension and localization abilities of VLMs compared to human performance.

**Baseline Results**: GPT4V achieves 62.99% accuracy (4-shot) on the comprehension task and 49.7% on the localization task.

**Validation**: Internal filtering checks using GPT4V to ensure the optical illusions meet dataset criteria.

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
