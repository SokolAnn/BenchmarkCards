# NICE and STOPS (Short Texts Of Products and Services)

## 📊 Benchmark Details

**Name**: NICE and STOPS (Short Texts Of Products and Services)

**Overview**: We introduce two new real-world short text datasets in the domain of goods and services (NICE and STOPS) to cover additional dataset characteristics in a realistic use-case and examine the performance of a variety of short text classifiers as well as top performing traditional text classifiers. NICE is a classification system for goods and services that divides them into 45 classes and is based on the Nice Classification of the World Intellectual Property Organization. The Short Texts Of Products and Services (STOPS) dataset is based on Amazon product descriptions and Yelp business entries.

**Data Type**: short text (product and service descriptions) - classification pairs

**Domains**:
- Natural Language Processing
- Tax Auditing
- Product/Service Classification

**Similar Benchmarks**:
- R8
- MR
- SearchSnippets
- Twitter
- TREC
- SST-2

**Resources**:
- [GitHub Repository](https://github.com/FKarl/short-text-classification)
- [Resource](https://arxiv.org/abs/2211.16878)
- [Resource](http://www.daviddlewis.com/resources/testcollections/reuters21578/)
- [Resource](https://www.cs.cornell.edu/people/pabo/movie-review-data/)
- [Resource](http://jwebpro.sourceforge.net/data-web-snippets.tar.gz)
- [Resource](https://www.nltk.org/howto/twitter.html#Using-a-Tweet-Corpus)
- [Resource](https://cogcomp.seas.upenn.edu/Data/QA/QC/)
- [Resource](https://nlp.stanford.edu/sentiment/)
- [Resource](http://webdatacommons.org/largescaleproductcorpus/)
- [Resource](https://www.wipo.int/nice/its4nice/ITSupport_and_download_area/20220101/MasterFiles/index.html)
- [GitHub Repository](https://github.com/google-research-datasets/MAVE)
- [Resource](https://www.yelp.com/dataset/download)

## 🎯 Purpose and Intended Users

**Goal**: Compare various modern text classification techniques on short texts, introduce two new real-world datasets in the goods and services domain (NICE and STOPS) to cover additional dataset characteristics, and evaluate whether Transformers achieve state-of-the-art accuracy on short text classification.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners
- Tax Auditors

**Tasks**:
- Text Classification
- Product/Service Classification
- Short Text Classification

**Limitations**: Most experiments were conducted once (except SHINE and InducT-GCN which were run five times). STOPS contains user-generated labels, some of which may not be entirely accurate. Existing benchmark datasets share many characteristics and may not cover all real-world use cases.

## 💾 Data

**Source**: NICE: WIPO Nice Classification data converted and preprocessed. STOPS: derived from MAVE (Amazon product descriptions) and YELP business entries; benchmark datasets used: R8 (Reuters 21578 subset), MR, SearchSnippets, Twitter, TREC, SST-2.

**Size**: NICE-45: 9,593 documents (6,715 train / 2,878 test). NICE-2: 9,593 documents (6,715 train / 2,878 test). STOPS-41: 200,341 documents (140,238 train / 60,103 test). STOPS-2: 200,341 documents (140,238 train / 60,103 test). Benchmark datasets: R8 7,674; MR 10,662; SearchSnippets 12,340; Twitter 10,000; TREC 5,952; SST-2 9,613 (train/test splits provided in Table 1).

**Format**: N/A

**Annotation**: Labels derived from existing sources: NICE uses WIPO Nice Classification labels; STOPS labels derived from MAVE and YELP original labels (multi-label categories were mapped to the most common single label). No additional manual annotation procedure is described.

## 🔬 Methodology

**Methods**:
- Automated metrics (Accuracy)
- Model-based evaluation (comparative experiments using retrieved models from literature and own experiments)
- Hyperparameter optimization (as described in Section 4.4)

**Metrics**:
- Accuracy
- Subset Accuracy (for multi-class cases)

**Calculation**: Accuracy is used to measure classification. For multi-class cases, the subset accuracy is calculated.

**Interpretation**: Higher accuracy indicates better classification performance. The paper interprets consistently higher accuracy of Transformer models as state-of-the-art performance on short text classification and notes NICE-45 as particularly challenging for models, making it a good benchmark for future work.

**Baseline Results**: Baseline and experimental results are reported in Tables 2 and 3. Examples: BERT achieves 72.79% on NICE-45 and 89.4% on STOPS-41 (Table 3). DeBERTa achieves 59.42% on NICE-45 (Table 3). WideMLP achieves 58.99% on NICE-45 (Table 3). Detailed per-model and per-dataset accuracies are provided in Tables 2 and 3 of the paper.

**Validation**: Most experiments were conducted once. SHINE and InducT-GCN were run five times and means and standard deviations are reported due to known high variance in GNN-based models. Train/test splits: datasets were randomly shuffled and split 70% train / 30% test (for NICE and STOPS).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Governance

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Governance**: Lack of testing diversity

**Potential Harm**: The paper notes that STOPS contains user-generated labels that may not be entirely accurate and that over-reliance on limited benchmark datasets can miss important dataset characteristics; these are cited as threats to validity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
