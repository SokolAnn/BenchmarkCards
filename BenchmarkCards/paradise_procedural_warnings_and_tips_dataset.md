# PARADISE (Procedural Warnings and Tips Dataset)

## 📊 Benchmark Details

**Name**: PARADISE (Procedural Warnings and Tips Dataset)

**Overview**: PARADISE is an abducive reasoning task using Q&A format on practical procedural text sourced from wikiHow, focusing on warning and tip inference tasks associated with goals.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/GGLAB-KU/paradise)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the implicit planning skills of language models through warning and tip inference tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: wikiHow tutorials, expert-curated dataset

**Size**: 104,000 examples in total

**Format**: JSON

**Annotation**: Expert annotation, with validation to ensure relevance and appropriateness for reasoning tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Standard metrics calculated based on model predictions against provided correct answers.

**Interpretation**: Higher accuracy indicates better performance in reasoning tasks.

**Baseline Results**: Human performance: 94% accuracy; Fine-tuned models show varying accuracies, with DeBERTa achieving the highest.

**Validation**: Extensive testing validated through expert-reviewed annotation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Complies with Creative Commons licensing for wikiHow content.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
