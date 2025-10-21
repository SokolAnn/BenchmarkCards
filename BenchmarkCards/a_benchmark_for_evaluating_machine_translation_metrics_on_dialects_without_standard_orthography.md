# A Benchmark for Evaluating Machine Translation Metrics on Dialects Without Standard Orthography

## 📊 Benchmark Details

**Name**: A Benchmark for Evaluating Machine Translation Metrics on Dialects Without Standard Orthography

**Overview**: The paper proposes a benchmark for evaluating machine translation metrics specifically on dialects that lack standard orthography by collecting a new dataset of human translations and developing a challenge set that highlights the performance of existing metrics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- German

**Resources**:
- [GitHub Repository](https://github.com/textshuttle/dialect_eval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and develop machine translation metrics that are robust against dialect variations without standardized spelling.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Machine Translation

**Limitations**: The study focuses on two Swiss German dialects and recognizes that it could not generalize to other language varieties due to a lack of available translation systems.

## 💾 Data

**Source**: Dataset of human translations created by native Swiss German speakers based on the English NTREX-128 data.

**Size**: 1,997 sentences

**Format**: N/A

**Annotation**: Human translation by native speakers of the respective Swiss German dialects.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Statistical analysis of metrics

**Metrics**:
- BLEU
- chrF
- COMET

**Calculation**: Metrics are calculated based on comparisons to human judgments and references, analyzing their ability to handle dialectal variations.

**Interpretation**: Metrics are considered robust if they reliably assess the quality of translations that exhibit spelling variability.

**Validation**: The challenge set allows for systematic evaluation of metric performance through controlled testing on dialect variations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Potential Harm**: The benchmark aims to mitigate risks related to the evaluation of non-standardized languages and dialects.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Translators and raters are native dialect speakers, selected to avoid bias.

**Data Licensing**: Not Applicable

**Consent Procedures**: All participants were compensated for their work.

**Compliance With Regulations**: Not Applicable
