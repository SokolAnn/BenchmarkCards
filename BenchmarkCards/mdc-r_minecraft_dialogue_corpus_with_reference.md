# MDC-R (Minecraft Dialogue Corpus with Reference)

## 📊 Benchmark Details

**Name**: MDC-R (Minecraft Dialogue Corpus with Reference)

**Overview**: This work presents a new corpus that combines existing annotations of the Minecraft Dialogue Corpus allowing for the study of clarification questions and their relation to referential ambiguity.

**Data Type**: dialogue interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CoDraw

**Resources**:
- [GitHub Repository](https://github.com/arciduca-project/MDC-R/tree/sdrt)

## 🎯 Purpose and Intended Users

**Goal**: To compare human and LLM behavior in asking clarification questions in the face of ambiguity.

**Target Audience**:
- ML Researchers
- Dialogue System Developers
- Linguists

**Tasks**:
- Clarification Question Generation
- Dialogue Management

**Limitations**: N/A

## 💾 Data

**Source**: Combines annotations from the Minecraft Dialogue Corpus and related discourse annotation efforts.

**Size**: 100 dialogues

**Format**: MMAX

**Annotation**: Aligned annotations for reference and clarification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Correlation with human responses
- Frequency of clarification questions

**Calculation**: Comparison of clarification question frequency and relevance in responses by LLMs and humans.

**Interpretation**: High frequency of LLM-generated clarification questions suggests effective handling of referential ambiguity.

**Baseline Results**: N/A

**Validation**: Comparative analysis with human participants in similar dialogue tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
