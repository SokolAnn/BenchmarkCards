# MMT: A Multilingual and Multi-Topic Indian Social Media Dataset

## 📊 Benchmark Details

**Name**: MMT: A Multilingual and Multi-Topic Indian Social Media Dataset

**Overview**: We introduce a large-scale multilingual and multi-topic dataset (MMT) collected from Twitter (~1.7 million Tweets), encompassing 13 coarse-grained and 63 fine-grained topics in the Indian context. We further annotate a subset of 5,346 tweets from the MMT dataset with various Indian languages and their code-mixed counterparts (MMT-LID). We demonstrate that existing tools fail to capture the linguistic diversity in MMT on two downstream tasks: topic modeling and language identification. The anonymized and annotated dataset will be made available in the public domain.

**Data Type**: text (Twitter tweets; multilingual and code-mixed social media posts)

**Domains**:
- Natural Language Processing
- Social Media Analysis

**Languages**:
- English
- Hindi
- Bengali
- Marathi
- Telugu
- Assamese

**Resources**:
- [GitHub Repository](https://github.com/twintproject/twint)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale multilingual and multi-topic Twitter dataset for the Indian context to support research in multilingual topic modeling, language identification, and related downstream tasks.

**Target Audience**:
- Researchers

**Tasks**:
- Topic Modeling
- Language Identification
- Named Entity Recognition
- Machine Translation

**Limitations**: Dataset collected from Twitter without language-specific constraints; English is over-represented while under-spoken languages such as Assamese are under-represented, presenting challenges for building robust multilingual systems.

## 💾 Data

**Source**: Collected from Twitter using the TWINT tool; MMT-LID is a human-annotated subset of MMT (language annotation by annotators).

**Size**: 1,755,145 tweets (MMT); annotated subset: 5,346 tweets (MMT-LID).

**Format**: N/A

**Annotation**: Manual human annotation by 49 student annotators organized into 13 teams for language tags (MMT-LID). Inter-annotator agreement evaluated via Cohen's Kappa on 325 re-annotated tweets resulting in CK = 0.94.

## 🔬 Methodology

**Methods**:
- Topic modeling experiments using LDA (Latent Dirichlet Allocation)
- Cross-lingual contextual topic modeling using ZeroShotTM (CTM)
- Language identification evaluation using systems: Twitter TLID, Polyglot, FastText, Langdetect, CLD3
- Automated metric-based evaluation (no human evaluation of downstream outputs reported beyond language annotation IAA)

**Metrics**:
- Accuracy
- Weighted F1 Score
- Coherence score
- Cohen's Kappa

**Calculation**: Topic modeling experiments: dataset randomly partitioned into 95% train and 5% inference; LDA and CTM trained on train split and evaluated on inference split reporting Accuracy, Weighted F1, and Coherence. Language identification: systems' predicted language tags compared against human annotator language tags (MMT-LID) reporting Accuracy and Weighted F1. Inter-annotator agreement computed by re-annotating 325 tweets and calculating Cohen's Kappa.

**Interpretation**: CTM (ZeroShotTM) outperforms LDA on reported Accuracy, Weighted F1, and Coherence. Performance on English partitions is substantially better than on non-English partitions. Existing multilingual language identification systems perform well on English but poorly on non-English and code-mixed data. LDA is ineffective on multilingual/non-English partitions; CTM improves results but non-English performance remains lower.

**Baseline Results**: Topic modeling on MMT (13 topics, All): LDA Accuracy 0.424, CTM Accuracy 0.492; W-F1 LDA 0.408, CTM 0.469; Coherence LDA 0.534, CTM 0.629. MMT (63 subtopics, All): LDA Accuracy 0.095, CTM 0.130; W-F1 LDA 0.091, CTM 0.124; Coherence LDA 0.542, CTM 0.636. On MMT-LID (13 topics, All): LDA Accuracy 0.395, CTM 0.488; W-F1 LDA 0.363, CTM 0.434; Coherence LDA 0.447, CTM 0.602. Language identification (MMT-LID, All): Twitter (TW) Accuracy 0.816, Polyglot 0.812, FastText 0.820, Langdetect 0.797, CLD3 0.721; W-F1 TW 0.795, PG 0.777, FT 0.780, LD 0.781, CLD3 0.755. Inter-annotator agreement (Cohen's Kappa) on language annotation: 0.94.

**Validation**: Inter-annotator agreement for language annotation measured via Cohen's Kappa on 325 re-annotated tweets (CK = 0.94). Topic modeling experiments use 95:5 train:inference split; topics and subtopics manually assigned/mapped for evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Transparency**: Uncertain data provenance

**Demographic Analysis**: Table 2 provides topic-wise distribution of top-5 languages, number of unique languages per topic (#L), average tweet length per topic, and IAA per topic.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper states the anonymized and annotated dataset will be made available in the public domain.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
