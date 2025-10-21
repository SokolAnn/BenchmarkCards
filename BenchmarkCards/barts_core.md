# BARTS CORE

## 📊 Benchmark Details

**Name**: BARTS CORE

**Overview**: BARTS CORE is a metric for evaluating generated text that conceptualizes the evaluation as a text generation problem, utilizing pre-trained sequence-to-sequence models to assess fluency, accuracy, and effectiveness of generated content.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/neulab/BARTScore)
- [Resource](http://explainaboard.nlpedia.ai/leaderboard/task-meval/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a flexible and effective evaluation mechanism for generated text across various dimensions like informativeness and factuality.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Generation
- Machine Translation
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Evaluation on multiple datasets covering 16 datasets from tasks such as machine translation and text summarization.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Spearman Correlation
- Kendall's Tau

**Calculation**: Metrics based on the probability of generating a target text from a source input using pre-trained models.

**Interpretation**: Higher scores indicate better quality of generated text.

**Baseline Results**: N/A

**Validation**: Empirical results showing effectiveness against existing metrics.

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
