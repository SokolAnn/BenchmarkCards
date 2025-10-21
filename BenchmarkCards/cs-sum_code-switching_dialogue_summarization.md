# CS-Sum (Code-Switching Dialogue Summarization)

## 📊 Benchmark Details

**Name**: CS-Sum (Code-Switching Dialogue Summarization)

**Overview**: CS-Sum is the first benchmark for code-switching (CS) dialogue summarization across Mandarin-English (EN-ZH), Tamil-English (EN-TA), and Malay-English (EN-MS), consisting of 900-1300 human-annotated dialogues per language pair.

**Data Type**: code-switched dialogue-summary pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Mandarin
- Tamil
- Malay

**Similar Benchmarks**:
- GupShup
- DialogSum
- SAMSum

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the comprehensibility of code-switching by large language models through dialogue summarization.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Dialogue Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Human-annotated CS dialogue-summary pairs created by native speakers and synthetic data from existing English dialogue datasets.

**Size**: 900-1300 dialogue-summary pairs per language pair

**Format**: N/A

**Annotation**: Translated by native speakers from English dialogues to code-switched dialogues.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE
- BERTScore
- SBERT-Cosine
- Jaccard
- METEOR

**Calculation**: Metrics were calculated based on the comparison of generated summaries with reference summaries obtained from the original dialogues.

**Interpretation**: Higher metric scores indicate better alignment with reference summaries.

**Baseline Results**: Evaluated ten LLMs including open-source and proprietary models.

**Validation**: In-depth error analysis and comparative evaluation of model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
