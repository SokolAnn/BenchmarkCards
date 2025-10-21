# EVA-SCORE (Extraction-and-Validation Score)

## 📊 Benchmark Details

**Name**: EVA-SCORE (Extraction-and-Validation Score)

**Overview**: EVA-SCORE is a new evaluation metric for assessing the informativeness of abstractive long-form summarization by extracting atomic facts from candidate and reference summaries, identifying overlap, and validating information using LLMs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2407.04969)

## 🎯 Purpose and Intended Users

**Goal**: To provide an objective and quantitative analysis for evaluating the informativeness of long-form summaries.

**Target Audience**:
- ML Researchers
- Evaluation Metric Developers

**Tasks**:
- Summarization Evaluation

**Limitations**: EVA-SCORE is time-consuming to run and primarily focuses only on informativeness.

## 💾 Data

**Source**: Datasets used include CNN DailyMail, PubMed, GovReport, arXiv, and BookSum for testing EVA-SCORE.

**Size**: N/A

**Format**: N/A

**Annotation**: Manual annotation by five expert annotators for the evaluation process.

## 🔬 Methodology

**Methods**:
- Atomic Fact Generation
- Atomic Fact Chain Generation
- Document-level Relation Extraction
- LLM Validation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: EVA-SCORE is defined as the harmonic mean of Precision and Recall.

**Interpretation**: Higher scores indicate better alignment with human judgments.

**Baseline Results**: EVA-SCORE shows the highest correlations with human evaluations compared to traditional metrics like ROUGE and BERTScore.

**Validation**: Validation through multiple annotators to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['N/A']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
