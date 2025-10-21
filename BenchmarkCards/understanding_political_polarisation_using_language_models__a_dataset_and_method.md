# Understanding Political Polarisation using Language Models: A dataset and method

## 📊 Benchmark Details

**Name**: Understanding Political Polarisation using Language Models: A dataset and method

**Overview**: The paper introduces a dataset extracted from Wikipedia spanning the past 120 years and a language-model-based method to analyze how polarized a US political candidate is. The dataset is divided into Background, Political, and Other sections and split into four chronological phases. The authors apply classical embedding methods (Word2Vec, Doc2Vec) and transformer-based models (Longformer, RoBERTa, BigBird) to measure polarization, compute nearest neighbors in embedding space, and derive a polarization metric based on neighbor party ratios.

**Data Type**: text (Wikipedia page sections; per-politician documents with section headings as keys and content as values; annotated into Background / Political Career / Other)

**Domains**:
- Natural Language Processing
- Political Science

**Resources**:
- [Resource](https://arxiv.org/abs/2301.00891)

## 🎯 Purpose and Intended Users

**Goal**: To analyze political polarization in the US political system using language models, and to provide a dataset and metrics to help understand how polarizing a candidate is and how polarization has changed over time; to aid voters and inform candidates.

**Target Audience**:
- Research community
- Voters
- Candidates

**Tasks**:
- Text Classification
- Embedding-based Similarity Search
- Interpretability/Attention Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia pages of US politicians (Senators and Congress members) from the 58th to the 117th Congress; data scraped section-wise from each politician's Wikipedia page.

**Size**: Phase 4: 1,631 instances; 1,656 categories merged into 3 categories in the first pass (covering roughly 26 years, 1995-2021). Overall dataset spans the 58th to 117th Congress (past 120 years) but total number of instances across all phases is not explicitly stated.

**Format**: JSON-like dictionaries per politician (section headings as keys and content as values); both raw and annotated versions to be released.

**Annotation**: Manual annotation of Wikipedia page sections into three categories: Background, Political Career, Other. Authors will release both annotated and raw versions.

## 🔬 Methodology

**Methods**:
- Word2Vec (pretrained and trained on collected data)
- Doc2Vec
- K-means clustering
- Binary SVM classification
- RoBERTa
- Longformer (longformer-base-4096, longformer-large-4096)
- BigBird
- Embedding nearest-neighbor search
- Attention analysis / global attention scores

**Metrics**:
- Accuracy
- Polarization ratio (ratio of same-party neighbors among top 20 nearest neighbors)

**Calculation**: Accuracy reported as percent correct classification from K-means and binary SVM experiments on political and background subsets. Polarization ratio computed as ratio of neighbors belonging to a party (e.g., number of Republican neighbors / 20) among the top 20 nearest neighbors in embedding space.

**Interpretation**: Higher classification Accuracy indicates better discrimination of party affiliation from text. For polarization ratio, the authors hypothesize that a non-polarized politician would have a neighbor-party ratio near 0.5 (Democrats/total) when using background data; higher ratios indicate stronger polarization toward a party.

**Baseline Results**: K-means: Doc2Vec Political 59.520, Doc2Vec Background 61.846, Allenai/longformer-large-4096 Political 52.128, Allenai/longformer-large-4096 Background 56.383. Binary SVM: Doc2Vec Political 72.872, Doc2Vec Background 63.564, Allenai/longformer-large-4096 Political 76.862, Allenai/longformer-large-4096 Background 69.681.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors run a Named Entity Recognition model to remove names and organizations from the data; location names are removed only from the political section (kept in background). They also remove numbers and other irrelevant patterns via regular expressions as part of cleaning.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
