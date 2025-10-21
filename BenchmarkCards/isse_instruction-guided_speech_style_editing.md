# ISSE (Instruction-guided Speech Style Editing)

## 📊 Benchmark Details

**Name**: ISSE (Instruction-guided Speech Style Editing)

**Overview**: ISSE is a novel dataset for instruction-guided speech style editing, comprising nearly 400 hours of speech and over 100,000 source-target pairs, each aligned with fine-grained textual editing instructions.

**Data Type**: source-target speech pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://ychenn1.github.io/ISSE/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for precise instruction-guided speech style editing.

**Target Audience**:
- ML Researchers
- Speech Technology Developers

**Tasks**:
- Speech Style Editing

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from various speech datasets including Ears and Expresso, focusing on speech style editing.

**Size**: 382 hours

**Format**: N/A

**Annotation**: Annotated with fine-grained editing instructions.

## 🔬 Methodology

**Methods**:
- Model training
- Quality Evaluation
- Instruction Design

**Metrics**:
- Word Error Rate (WER)
- Style Similarity
- Speaker Similarity

**Calculation**: Metrics are calculated based on transcription similarity and speaker verification.

**Interpretation**: Lower WER indicates better content preservation, while higher style and speaker similarity denote successful style editing.

**Baseline Results**: LlasaEdit model trained on ISSE outperforms counterparts on ESD dataset.

**Validation**: The dataset's performance is validated through comparisons of models trained on ISSE and ESD.

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
