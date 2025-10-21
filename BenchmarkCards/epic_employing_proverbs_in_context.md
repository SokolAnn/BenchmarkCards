# ePiC (Employing Proverbs in Context)

## 📊 Benchmark Details

**Name**: ePiC (Employing Proverbs in Context)

**Overview**: ePiC is a high-quality crowdsourced dataset of narratives paired with proverbs, designed to evaluate abstract language understanding and complex analogical reasoning in language models through three main tasks: proverb recommendation and alignment prediction, narrative generation for a proverb, and identification of narratives with similar motifs.

**Data Type**: narrative-proverb pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE

**Resources**:
- [Resource](https://epic-benchmark.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the abstract reasoning and analogical abilities of large language models through the use of proverbs in narrative contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Proverb Recommendation
- Alignment Prediction
- Narrative Generation
- Identifying Similar Narratives

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced via Amazon Mechanical Turk, with manual curation and annotation for alignment spans.

**Size**: 2500 proverb-narrative pairs

**Format**: JSON

**Annotation**: Fine-grained annotation of aligned spans between proverbs and narratives.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Mean Reciprocal Rank (MRR)
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the predictions made for the proverb-narrative tasks and the generated narratives.

**Interpretation**: Metrics indicate the ability of models to understand and generate appropriate narratives related to the proverbs.

**Baseline Results**: RoBERTa achieved the highest accuracy of 28.2% for predicting unseen proverbs.

**Validation**: The dataset was validated through human evaluations and various NLP tasks' results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset shows a significant imbalance in gender distribution among narrative mentions (61% male, 39% female).

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal information was collected from turkers, who were fairly compensated.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset adheres to ethical standards concerning data sourcing and participant rights.
