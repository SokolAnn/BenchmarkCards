# ICE-FLARE (Integrated Chinese-English Financial Language Assessment and Recognition Evaluation)

## 📊 Benchmark Details

**Name**: ICE-FLARE (Integrated Chinese-English Financial Language Assessment and Recognition Evaluation)

**Overview**: ICE-FLARE is the first comprehensive bilingual evaluation benchmark for financial LLMs, designed to assess the cross-lingual capabilities of language models in the financial sector, featuring diverse metrics and multilingual tasks.

**Data Type**: evaluation benchmark with dataset spanning multiple NLP tasks

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- FinCUGE
- CFBenchmark
- FinanceBench

**Resources**:
- [GitHub Repository](https://github.com/YY0649/ICE-PIXIU)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation benchmark for assessing bilingual financial models' performance across various tasks and contexts.

**Target Audience**:
- ML Researchers
- Financial Analysts
- Model Developers

**Tasks**:
- Text Classification
- Named Entity Recognition
- Question Answering
- Sentiment Analysis
- Event Detection
- Relationship Extraction
- Text Summarization
- Stock Prediction

**Limitations**: Limited to financial NLP tasks and may not generalize well outside of this domain.

## 💾 Data

**Source**: Bilingual financial instruction datasets derived from various open-source financial corpora.

**Size**: 1,185,076 data points including 603,940 fine-tuning instruction data and 95,091 evaluation data

**Format**: N/A

**Annotation**: Expert-annotated prompts and generated instruction datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Fine-tuned language model evaluation

**Metrics**:
- Weighted F1 Score
- Accuracy
- Entity-level F1 Score
- Exact Match Accuracy
- Matthews Correlation Coefficient

**Calculation**: Metrics are computed across various bilingual financial tasks based on model outputs against ground truth answers.

**Interpretation**: Higher scores in metrics indicate better performance in bilingual financial tasks.

**Baseline Results**: ICE-INTERN models outperform many existing state-of-the-art models including GPT-4 in various Chinese financial tasks.

**Validation**: Results are validated through comparison with numerous baseline models and extensive task diversity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Decision bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Analysis of model performance across different Chinese and English demographics in financial contexts.

**Potential Harm**: Potential for misuse in financial contexts if models are deployed without appropriate oversight.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-source licensed as per the project's specifications.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
