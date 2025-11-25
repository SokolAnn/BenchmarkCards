# WikiSQE: A Large-Scale Dataset for Sentence Quality Estimation in Wikipedia

## 📊 Benchmark Details

**Name**: WikiSQE: A Large-Scale Dataset for Sentence Quality Estimation in Wikipedia

**Overview**: WikiSQE is the first large-scale dataset for sentence quality estimation in Wikipedia. Each sentence is extracted from the entire revision history of English Wikipedia and assigned quality labels based on Wikipedia's inline cleanup templates. The dataset contains about 3.4M sentences with 153 quality labels organized into five categories to enable fine-grained estimation of sentence quality (e.g., citation needs, syntactic/semantic issues, need for additional information, disputed claims).

**Data Type**: text (sentences with quality labels)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Citation Needed
- Weasel words
- Peacock
- Puffery
- WikiReliability
- FEVER
- StereoSet

**Resources**:
- [GitHub Repository](https://github.com/ken-ando/WikiSQE)
- [Resource](https://dumps.wikimedia.org/enwiki/)
- [Resource](https://www.mediawiki.org/wiki/MediaWiki)
- [Resource](https://en.wikipedia.org/wiki/Category:Inline_cleanup_templates)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale, fine-grained dataset to estimate sentence quality in English Wikipedia and to enable evaluation and research on various sentence-level quality aspects.

**Target Audience**:
- Natural Language Processing researchers
- Model developers
- Wikipedia editors

**Tasks**:
- Sentence Quality Estimation
- Text Classification
- Binary Classification (per-label detection)

**Limitations**: The authors did not evaluate detection performance with a realistic distribution at test time (they constructed balanced positive/negative sets for experiments). The dataset is English-only (multilingual not provided). The dataset may contain offensive, biased, or discriminatory sentences and no filtering was performed for such content.

## 💾 Data

**Source**: Sentences extracted from the entire edit/revision history of English Wikipedia (HTML conversion of full revision history produced by MediaWiki as of before 1 March 2019, based on the dataset used in Mitrevski, Piccardi, and West 2020). Quality labels are derived from Wikipedia's inline cleanup templates (initially 344 templates, manually filtered/expanded to 153 labels, including past/deprecated templates matched to current labels).

**Size**: 3,417,955 sentences; source HTML revision history required ~7 TB of files to download

**Format**: N/A

**Annotation**: Labels are derived from Wikipedia inline cleanup templates (153 templates manually selected and mapped). The main dataset labels come from editor-applied inline templates; additional crowdsourced human annotation was conducted for validation experiments (pairwise annotation via Appen for a subset of labels).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (fine-tuning pre-trained language models: DeBERTaV3, BERT, RoBERTa)
- Human evaluation via crowdsourcing (Appen) for subset validation
- Automatic dataset extraction and filtering (sentence splitting with pySBD, filtering rules, deduplication)

**Metrics**:
- F1 Score
- Accuracy
- Perplexity

**Calculation**: For model experiments: training/dev/test splits created per-label/category. Development and test sets each consist of 500 positive and 500 negative examples (1,000 sentences). Remaining data used for training. For large classes (e.g., 'Citation needed') downsampling to 200,000 examples was applied. Models were fine-tuned with classification objective; best model selected by highest F1 on the development set; reported averages over three seeds.

**Interpretation**: Authors report that the model can detect poor-quality sentences with F1 scores of about 70–85% depending on category; higher F1 indicates better detectability of the quality aspect (e.g., Information addition detected well), while categories like Citation, Syntactic/Semantic revision, and Disputed claim are more difficult. Perplexity (computed with GPT-2) reflects category difficulty.

**Baseline Results**: Reported baseline automatic detection F1s: Overall ('All') F1 ~70.4 (DeBERTa), 72.3 (BERT), 71.6 (RoBERTa). 'Common' cluster F1 ~79.5 (DeBERTa), 79.0 (BERT), 80.0 (RoBERTa). Individual label F1s vary widely (examples: 'Citation needed' F1 70.0; 'Who?' F1 88.7; 'Sic' F1 92.9).

**Validation**: Validation via crowdsourced human annotation (Appen) on a subset of 11 labels using pairwise comparisons (10 pairs per label, 10 annotators per pair) and model vs. annotator comparisons. Models averaged performance over three seeds; best model by dev F1 used for test predictions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Offensive content', 'Biased content', 'Discriminatory content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
