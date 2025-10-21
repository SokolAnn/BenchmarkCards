# Harmful-LGBTQIA

## 📊 Benchmark Details

**Name**: Harmful-LGBTQIA

**Overview**: Introduce a real-world multi-labeled dataset of online conversational content to study and detect harmful Anti-LGBTQIA+ conversational content; construct a multi-label classification dataset with 6 distinct harmful language labels (toxicity, severe toxicity, obscene, threat, insult, identity attack) for binary and multi-label toxic comment classification; release labeled dataset and all code online.

**Data Type**: text (Reddit comments / online conversational comments)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- REDDIT BIAS
- RAL-E (Reddit Abusive Language English)

**Resources**:
- [GitHub Repository](https://github.com/daconjam/Harmful-LGBTQIA)
- [GitHub Repository](https://github.com/umanlp/RedditBias)
- [GitHub Repository](https://github.com/unitaryai/detoxify)
- [Resource](https://outrightinternational.org/)
- [Resource](https://www.pytorchlightning.ai)
- [Resource](https://huggingface.co/docs/transformers/index)
- [Resource](https://www.dictionary.com)

## 🎯 Purpose and Intended Users

**Goal**: 1) Detect several forms of toxicity in comments geared toward LGBTQIA+ individuals (threats, obscenity, insults, identity-based attacks). 2) Conduct exploratory data analysis and a detailed human evaluation to gain insights into the new multi-labeled dataset. 3) Accurately identify and detect harmful conversational content in social media comments.

**Target Audience**:
- AI and NLP practitioners
- Researchers
- Practitioners

**Tasks**:
- Binary Classification
- Multi-label Classification
- Toxic Comment Classification
- Harmful Content Detection

**Limitations**: Class imbalance (e.g., very few 'threat' and 'severe toxicity' samples) causing lower performance on rare labels; dataset contains offensive, profane, and potentially triggering content which may distress LGBTQIA+ individuals; potential bias toward African American English and other dialectal varieties that may lead to censoring or unfair treatment of vulnerable groups.

## 💾 Data

**Source**: Adapted the queerness (LGBTQIA+ , straight) dimension from REDDIT BIAS (Barikeri et al., 2021); collected comments from Reddit (REDDIT BIAS) to create the dataset.

**Size**: 9,930 comments

**Format**: N/A

**Annotation**: Automated labeling using Detoxify (multi-headed BERT) to produce probabilities for six labels and threshold mapping (c>=0.5 => harmful:1) to create binary labels; human annotation via Amazon Mechanical Turk (up to 15 annotators) for a 1,000-sample evaluation; inter-annotator agreement measured with Krippendorff's alpha = 0.81.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (fine-tuning large language models: BERT, RoBERTa, HateBERT)
- Baseline ML evaluation (Logistic Regression, Support Vector Machine)
- Automated labeling via Detoxify
- Human evaluation (Amazon Mechanical Turk)

**Metrics**:
- Precision
- Recall
- F1 Score
- Macro F1 Score
- Weighted F1 Score

**Calculation**: Precision is defined as the percentage of samples classified as positive that are truly positive; recall is defined as the true positive rate; F1 score is the harmonic mean of precision and recall. Label thresholding: label probability threshold l>0.7 used for correlation analysis; class threshold mapping c>=0.5 => class 1 (harmful).

**Interpretation**: Higher precision, recall, and F1 indicate better detection performance. Deep learning models outperform baseline models on macro and weighted F1; BERT achieves the best overall performance across tasks and labels in this study.

**Baseline Results**: Binary classification (Toxicity label) macro and weighted F1: Logistic Regression macro F1=0.76 weighted F1=0.83; SVM macro F1=0.79 weighted F1=0.84. Deep models: BERT macro F1=0.90 weighted F1=0.92; RoBERTa macro F1=0.87 weighted F1=0.91; HateBERT macro F1=0.88 weighted F1=0.91. (Results reported in Tables 4 and 5 of the paper.)

**Validation**: Human evaluation on 1,000 randomly sampled comments via Amazon Mechanical Turk; inter-annotator agreement measured with Krippendorff's alpha = 0.81. Additional EDA: label correlation matrices, feature distribution plots, and word contribution analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Societal Impact
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Societal Impact**: Impact on affected communities
- **Transparency**: Lack of training data transparency, Uncertain data provenance

**Demographic Analysis**: N/A

**Potential Harm**: ['Hate speech directed at LGBTQIA+ individuals', 'Offensive language and insults', 'Threats (including death threats)', 'Identity-based attacks and harassment aimed at LGBTQIA+ individuals']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used is publicly available. Annotator optional demographic information was collected but not saved. Annotators were filtered by HIT approval rate and location as described.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators on Amazon Mechanical Turk were asked eligibility and willingness questions and could stop participation if they might be triggered; demographic questions were optional and not saved.

**Compliance With Regulations**: Not Applicable
