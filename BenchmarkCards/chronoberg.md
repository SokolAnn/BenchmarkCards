# Chronoberg

## 📊 Benchmark Details

**Name**: Chronoberg

**Overview**: Chronoberg is a temporally structured corpus of English book texts spanning 250 years, curated from Project Gutenberg. It includes a variety of temporal annotations which enable analysis and training of LLMs to better contextualize the evolution of language and capture diachronic variation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- COCA
- COHA
- CCOHA

**Resources**:
- [Resource](https://huggingface.co/datasets/spaul25/Chronoberg)
- [GitHub Repository](https://github.com/paulsubarna/Chronoberg)

## 🎯 Purpose and Intended Users

**Goal**: To support the analysis and training of large language models on diachronic shifts and temporal generalization in language, enabling research on contextualized sentiment and discrimination detection across various time periods.

**Target Audience**:
- ML Researchers
- Linguists
- Data Scientists

**Tasks**:
- Text Classification
- Sentiment Analysis
- Linguistic Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Project Gutenberg

**Size**: 25,061 books yielding 2.7 billion tokens

**Format**: Plain text

**Annotation**: Temporal annotations and sentence-level VAD (Valence-Arousal-Dominance) scores.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Lexical semantic analysis

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the VAD scores annotated throughout the corpus, used to assess sentiment trends and diachronic shifts.

**Interpretation**: Affect scores indicate the emotional valence of words over time, and model performance is interpreted via perplexity on test sets drawn from Chronoberg.

**Validation**: Data validation through cross-referencing publication dates and consistency checks with external bibliographic sources.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: BSD 2-Clause License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
