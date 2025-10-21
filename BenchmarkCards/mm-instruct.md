# MM-Instruct

## 📊 Benchmark Details

**Name**: MM-Instruct

**Overview**: This paper introduces MM-Instruct, a large-scale dataset of diverse and high-quality visual instruction data designed to enhance the instruction-following capabilities of large multimodal models (LMMs).

**Data Type**: instruction-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jihaonew/MM-Instruct)

## 🎯 Purpose and Intended Users

**Goal**: To provide a novel dataset and benchmark specifically designed to enhance and evaluate the instruction-following capabilities of LMMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Large-scale image captioning datasets and data generated through augmenting and summarization via ChatGPT.

**Size**: 234,000 instruction-answer pairs

**Format**: N/A

**Annotation**: Automatically generated content using LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Win rates

**Calculation**: Overall win rates were calculated for performance comparison by prompting GPT-4V to compare outputs from the model.

**Interpretation**: Higher win rates indicate better instruction-following capabilities.

**Baseline Results**: LLaV A-Instruct demonstrated improved win rates compared to LLaV A-1.5 on various tasks.

**Validation**: Manual checks for data quality were implemented on the generated instances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
