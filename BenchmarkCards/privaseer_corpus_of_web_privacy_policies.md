# PrivaSeer Corpus of Web Privacy Policies

## 📊 Benchmark Details

**Name**: PrivaSeer Corpus of Web Privacy Policies

**Overview**: We present the PrivaSeer Corpus of 1,005,380 English language website privacy policies collected from the web. We describe a corpus creation pipeline (web crawler, language detection, document classification, duplicate and near-duplicate removal, and content extraction), employ unsupervised topic modelling to investigate corpus contents, analyze relationships between privacy policy domain PageRanks and text features, and use the corpus to pretrain PrivBERT, obtaining state of the art results on data practice classification and question answering tasks.

**Data Type**: text (website privacy policy documents)

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- OPP-115 Corpus
- PrivacyQA

**Resources**:
- [Resource](https://privaseer.ist.psu.edu/)
- [Resource](https://commoncrawl.org/)
- [Resource](https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-22/cc-index.paths.gz)
- [Resource](https://arxiv.org/abs/2004.11131)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale corpus of contemporary website privacy policies (1,005,380 documents) to enable large-scale semi-supervised and unsupervised models to interpret and simplify privacy policies, to support in-domain pretraining of language models (PrivBERT), and to facilitate research on privacy policy analysis and automated extraction of salient details.

**Target Audience**:
- Internet users
- Regulators
- Researchers

**Tasks**:
- Text Classification (data practice classification)
- Question Answering (answer sentence selection)
- Document Classification (privacy policy detection)
- Topic Modeling
- Readability Analysis

**Limitations**: Corpus contains only English language privacy policies (non-English documents were excluded).

## 💾 Data

**Source**: Seed URLs obtained from the Common Crawl May 2019 URL dump; filtered for likely privacy policy URLs (containing 'privacy' or 'data' and 'protection'); crawled with Scrapy; language detection with Langid; content extraction using boilerpipe; document classification using supervised models (random forests and RoBERTa); duplicate and near-duplicate removal using hashing and Simhash; cross-verified with landing page crawls.

**Size**: 1,005,380 documents (privacy policies) from 995,475 unique web domains

**Format**: N/A

**Annotation**: The final corpus documents are not annotated. For document classification, two researchers manually labeled 1,600 randomly selected candidate documents (1,145 privacy policies, 455 non-policies) with consultation from a privacy expert to train classifiers.

## 🔬 Methodology

**Methods**:
- Focused web crawling using Common Crawl seeds and Scrapy
- Language detection using Langid
- Content extraction using boilerpipe
- Document classification using Random Forests and RoBERTa sequence classification
- Duplicate removal using hashing and Simhash
- Topic modeling using Latent Dirichlet Allocation (LDA)
- Readability analysis using Flesch-Kincaid Grade Level
- Pretraining a transformer-based language model (PrivBERT) and fine-tuning on downstream tasks

**Metrics**:
- Precision
- Recall
- F1 Score
- Macro-average F1
- Micro-average F1
- Sentence-level F1 (for answer sentence selection)
- Flesch-Kincaid Grade Level
- PageRank (domain popularity measure)

**Calculation**: Classification metrics: precision, recall, and F1 (macro and micro averages reported for multi-label data practice classification). Sentence-level F1 for question answering: precision and recall calculated by measuring overlap between predicted sentences and gold standard sentences (per Ravichander et al., 2019). Readability measured using the Flesch-Kincaid Grade Level. PageRank values computed from Common Crawl web graphs using the Gauss-Seidel algorithm as described in the paper.

**Interpretation**: Higher Precision, Recall, and F1 indicate better model performance. The paper reports PrivBERT achieves state-of-the-art performance, improving RoBERTa's macro-average F1 by about 4% on the data practice classification task and improving BERT's F1 by about 6% on the answer sentence selection task. A higher Flesch-Kincaid Grade Level indicates greater required education level to understand a policy (mean FKG = 14.87). Higher PageRank indicates more popular domains which tend to have longer policies and cover more topics.

**Baseline Results**: Data practice classification (table values): Polisis macro F1 0.71, RoBERTa macro F1 0.79, PrivBERT macro F1 0.83; micro averages: Polisis 0.78, RoBERTa 0.84, PrivBERT 0.87. Answer sentence selection: BERT Precision 0.442 Recall 0.348 F1 0.39; PrivBERT Precision 0.483 Recall 0.424 F1 0.452.

**Validation**: Document classification: the 1,600 labeled documents were split into 960 training, 240 validation, and 400 test documents; 5-fold cross-validation was used to tune hyperparameters and average test results. OPP-115 fine-tuning split: 3:1:1 for training, validation, and testing. PrivacyQA: 1,350 questions for training and validation and 400 questions for testing (test questions annotated by at least three experts).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Legal Compliance

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Corpus contains policies from over 800 top-level domains (TLDs). Distribution: .com 63%, .org 5%, .net 3%; country-level domains such as .uk, .au, .ca account for 12%, 4%, and 2% respectively. PageRank bins were used to analyze relationships between domain popularity and number of topics, policy length, and readability.

**Potential Harm**: ['Detection of compliance issues']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
