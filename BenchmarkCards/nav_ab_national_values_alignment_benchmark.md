# NaV AB (National Values Alignment Benchmark)

## 📊 Benchmark Details

**Name**: NaV AB (National Values Alignment Benchmark)

**Overview**: NaV AB is a comprehensive benchmark designed to evaluate the alignment of Large Language Models (LLMs) with the values of five major nations: China, the United States, the United Kingdom, France, and Germany.

**Data Type**: value assessment data

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English
- French
- German

**Resources**:
- [Resource](https://huggingface.co/datasets/JadenGGGeee/NaVAB)
- [Resource](https://anonymous.4open.science/r/NVA-Pipeline-57DB)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate and align LLMs with nation-specific values.

**Target Audience**:
- ML Researchers
- Ethicists
- Policymakers

**Tasks**:
- Value Alignment Evaluation

**Limitations**: The dataset is sourced from open media platforms, which may not fully capture a nation’s core values or the diverse perspectives of its people.

## 💾 Data

**Source**: Collected from official media outlets from China, United States, United Kingdom, France, and Germany.

**Size**: approximately 10 million articles

**Format**: JSON

**Annotation**: The value assessment data generation method employs a multi-stage extraction process.

## 🔬 Methodology

**Methods**:
- Multiple-Choice (MC) Evaluation
- Answer-Judgment (AJ) Evaluation

**Metrics**:
- Correct rate

**Calculation**: The correct rate is calculated by comparing the perplexity of generated responses for positive and negative prompts.

**Interpretation**: Higher correct rate indicates better alignment performance.

**Validation**: The benchmark was tested for reliability through multiple trials and cross-validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: The benchmark does not provide specific demographic analysis but evaluates alignment across nations.

**Potential Harm**: The benchmark aims to prevent the propagation of biased content reflective of certain national values.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is publicly accessible and does not contain personal or sensitive information.

**Data Licensing**: All datasets and models used comply with licensing requirements for academic research.

**Consent Procedures**: Participants in the Conflict Reduction process volunteered, as stated in the paper.

**Compliance With Regulations**: This study follows the principles outlined in the ACM Code of Ethics and Professional Conduct.
