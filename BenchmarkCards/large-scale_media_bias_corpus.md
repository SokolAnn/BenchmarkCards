# large-scale media bias corpus

## 📊 Benchmark Details

**Name**: large-scale media bias corpus

**Overview**: A large-scale corpus of US online news articles (2010–2021) introduced to study the interaction of social bias and political bias and to evaluate which word embedding algorithms best quantify social bias in text corpora. The corpus covers more than 500,000 articles from 47 English-language US online news outlets and is annotated for political bias using allsides.com media bias ratings.

**Data Type**: text (news articles)

**Domains**:
- Natural Language Processing
- Media/Journalism

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/webis-de/EMNLP-22)
- [Resource](https://commoncrawl.org)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale news corpus annotated for political bias and to evaluate how different word embedding algorithms represent social bias (gender, ethnicity, religion) in news texts using WEAT and word-similarity evaluations.

**Target Audience**:
- Computational researchers
- Natural Language Processing researchers

**Tasks**:
- Bias Evaluation
- Intrinsic Word Similarity Evaluation
- Temporal Analysis

**Limitations**: Distantly supervised labeling by outlet (articles labeled by outlet bias) may not reflect article-level bias; outlet bias may have changed over time; word lists used in WEAT are not complete and may suffer from selection bias; only a limited number of embedding algorithms were evaluated; chosen fine-tuning settings (four epochs) may affect results.

## 💾 Data

**Source**: Collected from Common Crawl and mapped to media bias ratings from allsides.com; articles from 47 English-language US online news outlets (liberal, neutral/center, conservative) covering 2010–2021. Text extracted from WARC files using news-please; publication dates extracted automatically where possible.

**Size**: 520,798 news articles

**Format**: WARC (Common Crawl) raw files extracted to plain text; tokenized with HuggingFace tokenizer (vocabulary of around 39k tokens) for some models

**Annotation**: Distant supervision: articles labeled by outlet political bias using allsides.com ratings (left, lean-left, center, lean-right, right aggregated into liberal/neutral/conservative subsets). Publication dates extracted automatically for most articles (about 80%); no article-level manual political-bias annotation reported.

## 🔬 Methodology

**Methods**:
- Automated metrics (WEAT via WEFE framework)
- Intrinsic word similarity evaluation (Spearman's rho on MEN and WordSim353)
- Temporal evaluation (yearly models and WEAT over time)

**Metrics**:
- Word Embedding Association Test (WEAT effect size, range -2 to 2)
- Spearman's rho (correlation between cosine similarities and human similarity annotations)

**Calculation**: WEAT effect size computed as the mean difference of association between target group vectors and attribute vectors divided by the pooled standard deviation (resulting in values from -2 to 2). Word-similarity evaluation: compute cosine similarity between word vectors for annotated word pairs and report Spearman's rho between these similarities and human annotations (MEN and WordSim353). WEAT calculations performed using the WEFE implementation and word lists from Spliethöver and Wachsmuth (2021).

**Interpretation**: WEAT value 0 represents the least possible bias; positive/negative values indicate direction and magnitude of association. The paper emphasizes that absolute WEAT values may be less meaningful across embedding algorithms and recommends relative comparisons (e.g., differences between models trained on conservative vs. liberal subsets) to assess alignment with psychology literature expectations.

**Baseline Results**: Baseline models include Static (word2vec) and pre-trained BERT. Reported results: Decontextualized embeddings achieved the highest word-similarity scores (Spearman's rho ranging approximately 0.62–0.77). WEAT results (Table 3) show no single algorithm consistently best: Fine-Tuned had the highest conservative-vs-liberal delta for gender; FrecAgn performed closest to expectation for ethnicity; Decontext had the highest delta for religion. Static models often performed worse on word similarity.

**Validation**: Validation via intrinsic word-similarity tests (MEN and WordSim353) to assess embedding quality, comparison of model WEAT results to expectations from psychology literature, and temporal evaluation (training per-year models and measuring WEAT trends).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Transparency**: Uncertain data provenance
- **Governance**: Lack of data transparency, Incomplete usage definition
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The benchmark evaluation includes WEAT analyses for Gender, Ethnicity, and Religion to assess group-specific social bias.

**Potential Harm**: ['Prejudices and discrimination that cause lasting harm', 'Harmful consequences in practical applications and impact on audiences']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
