# CDEval

## 📊 Benchmark Details

**Name**: CDEval

**Overview**: CDEval is designed to evaluate the cultural dimensions of Large Language Models (LLMs) by covering six key cultural dimensions across seven domains. It provides insights into the cultural orientations of mainstream LLMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- German

**Similar Benchmarks**:
- MMLU
- CValues

**Resources**:
- [Resource](https://huggingface.co/datasets/Rykeryuhang/CDEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for assessing the cultural dimensions within large language models and to enhance their alignment with cultural diversity.

**Target Audience**:
- ML Researchers
- Cultural Analysts
- Ethics Researchers

**Tasks**:
- Cultural Evaluation
- Cross-Cultural Assessment

**Limitations**: The cultural dimensions explored are confined to six, which may limit real-world applications.

## 💾 Data

**Source**: Generated using GPT-4 and verified by humans.

**Size**: 2,953 questions

**Format**: JSON

**Annotation**: Human verification of generated questions

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Cultural Orientation Likelihood

**Calculation**: Cultural orientation likelihood is calculated based on user prompts and model responses.

**Interpretation**: Higher values indicate a stronger alignment towards a specified cultural orientation.

**Validation**: Evaluated across different LLMs to ensure stability and consistency

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
