# ParaPhraser Plus

## 📊 Benchmark Details

**Name**: ParaPhraser Plus

**Overview**: We collect, rank and evaluate a new publicly available headline paraphrase corpus (ParaPhraser Plus), and then perform text generation experiments with manual evaluation on automatically ranked corpora using the Universal Transformer architecture.

**Data Type**: headline paraphrase pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Russian

**Similar Benchmarks**:
- ParaPhraser
- ParaPlag
- Opusparcus
- PPDB

**Resources**:
- [Resource](http://paraphraser.ru/download/)

## 🎯 Purpose and Intended Users

**Goal**: To collect, automatically rank and evaluate a large publicly available headline paraphrase corpus for Russian (ParaPhraser Plus) and to demonstrate its usefulness for paraphrase generation using transformer models.

**Tasks**:
- Paraphrase Generation
- Paraphrase Detection
- Sentence Similarity
- Text Generation

**Limitations**: The training sets are noisy to a certain extent; the generation model does not reach human parity; inter-annotator agreement for ranking evaluation was only fair (Fleiss Kappa = 0.267, p < 0.05).

## 💾 Data

**Source**: Distilled from a database of news headlines provided by the Russian Internet monitoring service Webground; headlines were clustered by events over a ten year span (starting from 2009) and pairs were formed from combinations within clusters.

**Size**: 56,000,000 pairs of potential paraphrases

**Format**: N/A

**Annotation**: Automatically ranked using a supervised model (fine-tuned RuBERT). Manual annotation for evaluation: a random subsample of 500 pairs annotated by 5 annotators using the Creutz (2018) similarity degrees; original ParaPhraser training set contains 7,227 human-classified pairs into three classes.

## 🔬 Methodology

**Methods**:
- Supervised ranking using fine-tuned RuBERT
- Baseline cosine similarity using Word2Vec embeddings
- Manual annotation of a 500-pair subsample by 5 annotators (ranking evaluation)
- Paraphrase generation using Sequence-to-Sequence Universal Transformer
- Automated evaluation metrics (BLEU, METEOR)
- Human preference evaluation (3 annotators) for generation

**Metrics**:
- BLEU
- METEOR
- F1 Score
- Accuracy
- Pearson correlation coefficient
- Fleiss Kappa
- Human preference (percentage)

**Calculation**: Ranking quality measured by Pearson correlation between model rankings and manual annotations; inter-annotator agreement measured by Fleiss Kappa (5 annotators). Generation quality measured by BLEU and METEOR on test sets for different training sizes; human evaluation counted percentages of preference among Human / Machine / Tie by 3 annotators.

**Interpretation**: Higher training set sizes (top-N ranked samples) correlate with higher BLEU and METEOR scores. Supervised model rankings show stronger correlation with human judgments (Pearson r = 0.734) compared to Word2Vec cosine baseline (Pearson r = 0.535). Generated paraphrases do not reach human parity (Machine + Tie user preference: 47.7% for Opusparcus and 38.4% for ParaPhraser Plus).

**Baseline Results**: Paraphrase detection results (from Table 1): Shallow Neural Networks F1=79.82 Accuracy=76.65; Linguistic Features Classifier F1=81.10 Accuracy=77.39; Machine Translation Based Semantic Similarity F1=78.51 Accuracy=81.41; RuBERT F1=87.73 Accuracy=84.99. Correlation baseline: Word2Vec cosine similarity Pearson r = 0.535; supervised model Pearson r = 0.734. Generation scores (Table 3) example: ParaPhraser Plus BLEU (2m) = 9.81 METEOR (2m) = 38.09; Opusparcus BLEU (2m) = 6.46 METEOR (2m) = 33.19.

**Validation**: Manual validation of ranking via annotation of 500 randomly selected pairs by 5 annotators with Fleiss Kappa = 0.267 (p < 0.05); comparison of model rankings to human judgments using Pearson correlation; generation validated by BLEU/METEOR on test sets and by human preference evaluation with 3 annotators.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
