# Andersen and Persuasion Datasets

## 📊 Benchmark Details

**Name**: Andersen and Persuasion Datasets

**Overview**: The paper introduces two new datasets, Andersen and Persuasion, for testing AI's competence in understanding character-location relationships in narratives. The datasets consist of manually annotated character-location pairings in children's stories and a novel.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/batuhan-ozyurt/Location-of-Characters-in-Narratives-Andersen-and-Persuasion-Datasets)

## 🎯 Purpose and Intended Users

**Goal**: To assess the ability of AI models in understanding spatial reasoning within narratives through character-location mapping.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually annotated datasets from children's stories and the novel 'Persuasion'.

**Size**: 249 annotations for Andersen, 264 annotations for Persuasion

**Format**: tab-separated value

**Annotation**: Manual annotation by researchers

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Fuzzy Matching

**Calculation**: Exact matching and fuzzy matching based on the outputs of the LLMs compared to gold location annotations.

**Interpretation**: Performance is evaluated based on the correctness of character location identification in narrative contexts.

**Baseline Results**: Exact Match: Andersen 54.11%, Persuasion 41.46%; Fuzzy Match: Andersen 55.84%, Persuasion 46.34%

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
