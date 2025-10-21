# AGMMU (Agricultural Multimodal Understanding Benchmark)

## 📊 Benchmark Details

**Name**: AGMMU (Agricultural Multimodal Understanding Benchmark)

**Overview**: AGMMU is a challenging real-world benchmark for evaluating and advancing vision-language models (VLMs) in the knowledge-intensive domain of agriculture, constructed from authentic dialogues between users and agricultural experts.

**Data Type**: multiple-choice and open-ended questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SimpleQA
- ScienceQA
- MMMU

**Resources**:
- [GitHub Repository](https://github.com/AgMMU/AgMMU)
- [Resource](https://huggingface.co/datasets/AgMMU/AgMMU_v1)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of vision-language models in handling knowledge-intensive agricultural scenarios and improve their performance on related tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Agricultural Experts

**Tasks**:
- Insect Identification
- Plant Identification
- Disease Categorization
- Management Instruction
- Symptom Description

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from 116,231 real-world dialogues between growers and USDA-authorized experts.

**Size**: 116,231 dialogues

**Format**: JSON

**Annotation**: Automated knowledge extraction followed by human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the evaluation of VLMs' performance on provided questions.

**Interpretation**: Higher accuracy and F1 scores indicate better performance in VLM understanding and knowledge integration.

**Validation**: Evaluation of 12 leading VLMs to benchmark their performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All personal identifying information from users and experts was removed during data curation.

**Data Licensing**: CC-BY-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
