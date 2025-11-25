# RAAMove

## 📊 Benchmark Details

**Name**: RAAMove

**Overview**: RAAMove is a comprehensive multi-domain corpus dedicated to the annotation of move structures in research article abstracts, facilitating move analysis and automatic move identification, constructed through manual and automated methods.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Engineering

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ljk1228/RAAMove)

## 🎯 Purpose and Intended Users

**Goal**: To assist in the analysis of move structures in research article abstracts and enhance the understanding of writing skills in academic contexts.

**Target Audience**:
- ML Researchers
- Academics
- Language Educators

**Tasks**:
- Move Analysis
- Discourse Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Annotated abstracts from leading journals and conferences in the fields of Artificial Intelligence and Engineering.

**Size**: 33,988 annotated instances

**Format**: JSON

**Annotation**: Manual annotation by expert annotators followed by BERT-based automatic annotation with expert modifications.

## 🔬 Methodology

**Methods**:
- Manual annotation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the model's predictions compared to the gold-standard annotations.

**Interpretation**: Higher scores indicate better performance in accurately identifying the rhetorical moves within abstracts.

**Baseline Results**: BERT: 76.72%, BERT+Context: 77.60%, RAAMove model: 78.53%

**Validation**: Preliminary experiments conducted to verify the model's effectiveness.

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
