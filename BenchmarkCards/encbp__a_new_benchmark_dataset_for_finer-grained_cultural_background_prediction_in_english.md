# EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English

## 📊 Benchmark Details

**Name**: EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English

**Overview**: We collect, annotate, manually validate, and benchmark EnCBP, a finer-grained news-based cultural background prediction dataset in English. EnCBP contains country-level (EnCBP-country) and district/state-level (EnCBP-district) labels and is intended to enable modeling of culture-specific English writing styles and to study the effect of cultural background information on downstream NLP tasks.

**Data Type**: Paragraph-level news text (paragraphs chunked from news articles)

**Domains**:
- Natural Language Processing
- Psycholinguistics

**Languages**:
- English

**Similar Benchmarks**:
- CoNLL-2003
- PAWS-Wiki
- QNLI
- STS-B
- RTE
- SST-5
- SST-2
- Emotion
- Go-Emotions

**Resources**:
- [Resource](https://mediacloud.org/)
- [Resource](https://www.reddit.com/)
- [Resource](https://www.statista.com/statistics/325144/reddit-global-active-user-distribution/)
- [Resource](https://arxiv.org/abs/2203.14498)

## 🎯 Purpose and Intended Users

**Goal**: To construct, manually validate, and benchmark a finer-grained English cultural background prediction dataset (EnCBP) and to evaluate how incorporating cultural background information affects performance on a variety of downstream NLP tasks.

**Target Audience**:
- Researchers in Natural Language Processing
- Model Developers

**Tasks**:
- Text Classification (Cultural Background Prediction)
- Named Entity Recognition
- Paraphrase Identification
- Natural Language Inference
- Semantic Textual Similarity
- Textual Entailment
- Sentiment Analysis
- Emotion Recognition

**Limitations**: Dataset is news-based (news domain) and may not generalize to other domains such as social media; EnCBP-district (state-level) contains higher noise and is more difficult; cultural feature augmentation can harm performance when the evaluation dataset has imbalanced cultural-background distributions (e.g., Go-Emotions); the authors cannot manually examine all articles and note the possibility that the dataset may contain unethical information.

## 💾 Data

**Source**: News articles streamed from Media Cloud API sampled from specific mainstream outlets: US (New York Times, Fox News, Wall Street Journal), UK (BBC), Canada (Big News Network - Canada), Australia (Sydney Morning Herald), India (Times of India); district/state outlets for EnCBP-district: Georgia (Coosa Valley News, WJCL, Macon Daily), New York (Times Union, Gotham Gazette, Newsday), California (NBC Los Angeles, LA Times, San Diego Union Tribune), Texas (Hardin County News, Jasper Newsboy, El Paso Times).

**Size**: EnCBP-country: 5 countries × 2,000 paragraphs = 10,000 paragraphs. EnCBP-district: 4 states × 2,000 paragraphs = 8,000 paragraphs. Each class has 2,000 sampled paragraphs; train/dev/test split is 80%/10%/10%.

**Format**: Paragraph-level preprocessed text with country/district mentions replaced by special tokens ([country], [district]); datasets split into train/dev/test (80%/10%/10%).

**Annotation**: Labels assigned based on the country or US state codes of the news outlets by which paragraphs were posted. Manual validation: randomly sampled instances validated on Amazon Mechanical Turk with three annotators per questionnaire; validators were location-filtered to match the label's country or state; duplicates and overly short documents (<100 words) removed; paragraphs containing high-IDF named entities were filtered out.

## 🔬 Methodology

**Methods**:
- Language Modeling evaluations (masked language model fine-tuning and perplexity measurement)
- Manual validation via crowdsourcing on Amazon Mechanical Turk
- Benchmarking via fine-tuning models (BiLSTM, BERT, RoBERTa)
- Two-stage training (pre-fine-tune on EnCBP then on target task)
- Multi-task learning (joint training with EnCBP as auxiliary task)
- Automated metrics reporting (averages over multiple runs)

**Metrics**:
- F1-macro
- Perplexity
- Accuracy
- Fleiss' kappa (inter-annotator agreement)
- Pearson correlation
- Spearman correlation

**Calculation**: Benchmark F1-macro scores reported as averages across five runs with different random seeds; standard deviations reported. Language model perplexity measured by fine-tuning bert-base-cased with the MLM objective and evaluating on test corpora. Inter-annotator agreement measured by Fleiss' kappa. Downstream-task-specific metrics: Accuracy for QNLI, RTE, and SST-2; Pearson's and Spearman's correlations for STS-B; F1-macro for other tasks.

**Interpretation**: Higher F1-macro indicates better cultural background prediction performance. Lower perplexity indicates better LM adaptation to a cultural domain. Moderate to substantial Fleiss' kappa values support annotation reliability. Improvements in downstream-task metrics indicate beneficial cultural feature augmentation when text domains align; decreases indicate domain mismatch or imbalanced cultural distributions.

**Baseline Results**: Benchmark performance (average F1-macro over five runs, standard deviations in parentheses): BiLSTM: EnCBP-country 50.89 (0.98), EnCBP-district 44.53 (1.39). BERT (bert-base-cased): EnCBP-country 78.13 (0.67), EnCBP-district 72.09 (1.84). RoBERTa (roberta-base): EnCBP-country 82.96 (0.89), EnCBP-district 73.96 (1.01).

**Validation**: Manual validation: 50 instances sampled per class and validated on MTurk. Each questionnaire paired a sampled instance with a random EnCBP paragraph and asked three annotators (location-filtered to the same country/state) to judge which paragraph(s) were from local outlets. Validation accuracy (ACC) and Fleiss' kappa (IAA) reported per class (Table 2). Payment to annotators was $0.14 per instance; annotator participation was anonymized.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on affected communities

**Potential Harm**: ['The paper notes the possibility that the released news-based dataset may contain unethical information despite using mainstream outlets.', 'Imbalanced cultural-background distributions (e.g., in Go-Emotions) can harm model performance and lead to biased evaluation results.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors state the dataset contains no sensitive or private information (labels derived from public news outlets) and that the annotation process was anonymized; mentions of countries/districts were replaced with special tokens to avoid information leakage. MTurk annotators were location-filtered and anonymized.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
