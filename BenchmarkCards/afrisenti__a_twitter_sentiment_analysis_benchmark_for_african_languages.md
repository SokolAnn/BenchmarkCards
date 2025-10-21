# AfriSenti: A Twitter Sentiment Analysis Benchmark for African Languages

## 📊 Benchmark Details

**Name**: AfriSenti: A Twitter Sentiment Analysis Benchmark for African Languages

**Overview**: AfriSenti, a sentiment analysis benchmark that contains a total of >110,000 tweets in 14 African languages (Amharic, Algerian Arabic, Hausa, Igbo, Kinyarwanda, Moroccan Arabic, Mozambican Portuguese, Nigerian Pidgin, Oromo, Swahili, Tigrinya, Twi, Xitsonga, and Yorùbá) from four language families. The tweets were annotated by native speakers and used in the AfriSenti-SemEval shared task.

**Data Type**: text (tweets / Twitter messages)

**Domains**:
- Natural Language Processing

**Languages**:
- Amharic
- Algerian Arabic
- Hausa
- Igbo
- Kinyarwanda
- Moroccan Arabic
- Mozambican Portuguese
- Nigerian Pidgin
- Oromo
- Swahili
- Tigrinya
- Twi
- Xitsonga
- Yorùbá

**Similar Benchmarks**:
- NaijaSenti
- Ethiopic Twitter Dataset for Amharic (ETD-AM)

**Resources**:
- [Resource](https://afrisenti-semeval.github.io)
- [GitHub Repository](https://github.com/afrisenti-semeval/afrisent-semeval-2023)

## 🎯 Purpose and Intended Users

**Goal**: To enable sentiment analysis research in African languages by creating and releasing the largest Twitter dataset for sentiment analysis in under-represented African languages (110,000+ tweets in 14 languages), and to support the AfriSenti-SemEval shared task.

**Target Audience**:
- Research community interested in sentiment analysis and under-represented languages

**Tasks**:
- Sentiment Analysis
- Text Classification
- Polarity Classification (positive/negative/neutral)

**Limitations**: Offensive tweets were deleted and some conflicting tweets were removed or re-annotated; the data can suffer from label bias and annotator disagreement; data collection relied on keywords and geographic locations leading to imbalanced datasets; limited to 14 languages in this release.

**Out of Scope Uses**:
- The authors explicitly forbid the use of the datasets for commercial purposes unless explicitly approved by the dataset creators.
- The authors explicitly forbid the use of the datasets by state actors unless explicitly approved by the dataset creators.
- Systems trained on the datasets should not be used to make high-stakes decisions for individuals.

## 💾 Data

**Source**: Collected from Twitter using the Twitter Academic API; data collection combined location-based and vocabulary-based heuristics (stopwords, sentiment lexicons, language-specific word lists); includes ten newly annotated datasets and four curated existing datasets (e.g., Yimam et al., Muhammad et al.).

**Size**: 110,000+ tweets (total across 14 languages)

**Format**: N/A

**Annotation**: Tweets annotated by native speakers using the Simple Sentiment Questionnaire annotation guide (Mohammad, 2016); majority voting used to determine final labels (three annotators per tweet except Ethiopian languages annotated by two annotators and curated by a third); cases where all annotators disagreed were discarded. Individual annotator labels are released.

## 🔬 Methodology

**Methods**:
- Model fine-tuning experiments (monolingual fine-tuning of pretrained language models)
- Multilingual training (fine-tune on combined training data)
- Zero-shot cross-lingual transfer evaluation
- Automated metrics for model evaluation

**Metrics**:
- Accuracy
- F1 Score
- Free-marginal multi-rater kappa

**Calculation**: Model evaluation metrics (Accuracy and F1 Score) are reported and averaged over 5 runs. Inter-annotator agreement is measured using the free-marginal multi-rater kappa (Randolph, 2005).

**Interpretation**: Higher Accuracy and F1 Score indicate better model performance; inter-annotator agreement reported via free-marginal multi-rater kappa (values reported per language). No absolute performance thresholds are provided; authors compare models (e.g., AfroXLMR-large achieves the best overall F1 in reported experiments).

**Baseline Results**: Multilingual baseline F1 scores (average over 5 runs) reported in Table 8: AfriBERTa-large 64.7, XLM-R-base 64.3, AfroXLMR-base 68.4, mDeBERTaV3-base 66.1, XLM-T-base 65.9, XLM-R-large 66.9, AfroXLMR-large 71.2. Monolingual baseline results and per-language scores are reported in Table 7.

**Validation**: Train/dev/test splits provided per language (see Table 6); languages with limited training data (Oromo, Tigrinya) are evaluated in zero-shot transfer; inter-annotator agreement reported and individual annotator labels released to support validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Privacy
- Fairness
- Value Alignment
- Societal Impact

**Atlas Risks**:
- **Misuse**: Improper usage
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Value Alignment**: Over- or under-reliance
- **Societal Impact**: Impact on human agency

**Potential Harm**: ['Automatic sentiment analysis can be abused by those with the power to suppress dissent.', 'Systems trained on these datasets are not reliable at individual instance-level and should not be used to make high-stakes decisions for individuals.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Tweets were anonymized by replacing all @mentions with @user and removing all URLs. For some Nigerian language test sets tweets were lower-cased.

**Data Licensing**: The authors explicitly forbid the use of the datasets for commercial purposes or by state actors unless explicitly approved by the dataset creators. No standard license (e.g., CC) is specified in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
