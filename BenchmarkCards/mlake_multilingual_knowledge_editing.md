# MLaKE (Multilingual Knowledge Editing)

## 📊 Benchmark Details

**Name**: MLaKE (Multilingual Knowledge Editing)

**Overview**: MLaKE is a novel benchmark comprising 5360 single-hop and 4072 multi-hop questions designed to evaluate the adaptability of knowledge editing methods across five languages: English, Chinese, Japanese, French, and German.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Japanese
- French
- German

**Resources**:
- [GitHub Repository](https://github.com/Hi-archers/MLaKE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of knowledge editing methods in multilingual contexts and improve current methodologies for better generalization.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Knowledge Editing

**Limitations**: N/A

## 💾 Data

**Source**: Fact chains collected from Wikipedia and generated using LLMs.

**Size**: 13,632 examples

**Format**: N/A

**Annotation**: Automatically generated and manually verified questions and answers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The accuracy is determined by whether the model-generated sentences contain the correct answer or its aliases.

**Interpretation**: Higher accuracy indicates better performance in knowledge editing across languages.

**Validation**: Evaluation of multilingual generalization and transferability using current knowledge editing methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
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
