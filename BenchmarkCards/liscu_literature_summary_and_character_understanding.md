# LiSCU (Literature Summary and Character Understanding)

## 📊 Benchmark Details

**Name**: LiSCU (Literature Summary and Character Understanding)

**Overview**: LiSCU is a new dataset of literature summaries paired with descriptions of characters that appear in them, designed to facilitate character-centric narrative understanding.

**Data Type**: literary summaries and character descriptions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/fabrahman/char-centric-story)

## 🎯 Purpose and Intended Users

**Goal**: To encourage research in character-centric narrative understanding through the introduction of a new dataset and tasks.

**Target Audience**:
- ML Researchers
- Literary Scholars
- NLP Practitioners

**Tasks**:
- Character Identification
- Character Description Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various online study guides including Shmoop, SparkNotes, CliffsNotes, and LitCharts.

**Size**: 1,708 literature summaries and 9,499 character descriptions

**Format**: N/A

**Annotation**: Descriptions were written by literary experts, typically teachers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BERT-F1

**Calculation**: Metrics are calculated using standard procedures for evaluating NLP tasks.

**Interpretation**: Higher scores indicate better performance in tasks related to character understanding and description generation.

**Baseline Results**: Human performance: 91.8%; Best model (ALBERT-XXL): 83.33%

**Validation**: The dataset was validated through human evaluations and inter-annotator agreements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis indicates more male characters than female characters (66% male).

**Potential Harm**: Potential reinforcement of societal biases present in literature.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
