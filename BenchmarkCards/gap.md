# GAP

## 📊 Benchmark Details

**Name**: GAP

**Overview**: A gender-balanced labeled corpus of 8,908 ambiguous pronoun–name pairs sampled to provide diverse coverage of challenges posed by real-world text.

**Data Type**: corpus

**Domains**:
- natural language understanding
- coreference resolution

**Languages**:
- English

**Similar Benchmarks**:
- Winograd schemas
- OntoNotes

**Resources**:
- [Resource](http://goo.gl/language/gap-coreference)

## 🎯 Purpose and Intended Users

**Goal**: To address gender bias in existing coreference corpora and provide a benchmark for evaluating coreference resolution systems on ambiguous gendered pronouns.

**Target Audience**:
- researchers
- developers of NLP systems

**Tasks**:
- coreference resolution
- gender bias analysis

**Limitations**: Only contains ambiguous pronouns from Wikipedia.

**Out of Scope Uses**:
- non-ambiguous pronouns
- data not reflecting gender dynamics

## 💾 Data

**Source**: Wikipedia

**Size**: 8,908 ambiguous pronoun-name pairs

**Format**: labeled corpus

**Annotation**: Human-annotated with multiple labels for coreference resolution.

## 🔬 Methodology

**Methods**:
- coreference resolution analysis
- gender bias detection

**Metrics**:
- F1 score
- Bias

**Calculation**: F1 score calculated overall and by gender; Bias defined as the ratio of feminine to masculine F1 scores.

**Interpretation**: Lower F1 scores and high bias indicate systems favoring masculine pronouns.

**Baseline Results**: Best scoring baseline achieved 66.9% F1.

**Validation**: Inter-annotator agreement was measured using Fleiss' kappa statistics.

## ⚠️ Targeted Risks

**Risk Categories**:
- gender bias
- inequitable representation

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The corpus aims for a balanced 1:1 gender ratio.

**Potential Harm**: Potential reinforcement of gender stereotypes if biases are not addressed.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not applicable as the data is extracted from publicly available Wikipedia articles.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
