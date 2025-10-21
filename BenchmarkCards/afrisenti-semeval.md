# AfriSenti-SemEval

## 📊 Benchmark Details

**Name**: AfriSenti-SemEval

**Overview**: This paper introduces a benchmark for sentiment analysis across 12 African languages using the AfriSenti-SemEval Shared Task 12 dataset, which includes annotated data collected from Twitter for sentiment classification.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Hausa
- Yoruba
- Igbo
- Nigerian Pidgin
- Amharic
- Algerian Arabic
- Moroccan Arabic
- Swahili
- Kinyarwanda
- Twi
- Mozambican Portuguese
- Xitsonga

**Similar Benchmarks**:
- NaijaSenti

**Resources**:
- [Resource](http://bit.ly/40yvilf)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark and evaluate the performance of current state-of-the-art transformer models for sentiment analysis across multiple African languages.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Sentiment Analysis

**Limitations**: More data would improve performance across the board, and the reliance on pre-existing models carries limitations and potential bias.

## 💾 Data

**Source**: Twitter datasets from the AfriSenti-SemEval Shared Task 12.

**Size**: 77,338 examples

**Format**: N/A

**Annotation**: Manually annotated sentiment labels for positive, negative, and neutral sentiments.

## 🔬 Methodology

**Methods**:
- Model-based evaluation

**Metrics**:
- F1 Score
- Precision
- Recall
- Accuracy

**Calculation**: Standard, weighted average classification metrics were used to evaluate model performance.

**Interpretation**: Higher weighted average metrics indicate better model performance on sentiment classification tasks.

**Baseline Results**: XLM-R was used as a baseline model for comparison.

**Validation**: The evaluation utilized held-out validation sets and multiple seeds to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misuse includes mass surveillance and suppression of free speech.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
