# HiNER: A Large Hindi Named Entity Recognition Dataset

## 📊 Benchmark Details

**Name**: HiNER: A Large Hindi Named Entity Recognition Dataset

**Overview**: Releases a significantly sized standard-abiding Hindi NER dataset containing 109,146 sentences and 2,220,856 tokens, annotated with 11 tags. The paper describes dataset creation (following CoNLL-2003 guidelines with I-O-B encoding), an annotation tool and baseline NER engine, and evaluates various pre-trained language models on the dataset. The authors release the dataset, code, and models for further research.

**Data Type**: text (sentence-level token annotations; I-O-B encoded Named Entity Recognition labels)

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi

**Similar Benchmarks**:
- FIRE 2014 NER Corpus
- IJCNLP 2008 NER Dataset
- WikiANN

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Collect a large manually annotated NER dataset for Hindi (HiNER) and release it publicly; evaluate the efficacy of various deep learning-based NER approaches on this dataset and compare with other publicly available datasets.

**Target Audience**:
- NLP community

**Tasks**:
- Named Entity Recognition
- Sequence Labeling

**Limitations**: The dataset was annotated by a single annotator; the authors state that they cannot provide any inter-annotator agreement details.

## 💾 Data

**Source**: Annotated from the ILCI Tourism domain (Jha, 2010) and a subset of the news domain corpus from Goldhahn et al. (2012).

**Size**: 108,608 sentences; 2,137,199 words. Splits: Training 76,025 sentences (70%), Development 10,861 sentences (10%), Testing 21,722 sentences (20%).

**Format**: I-O-B encoding (CoNLL-2003 guidelines)

**Annotation**: Manual annotation by a single annotator; 11 entity tags (Person, Location, Organization, NUMEX, TIMEX, MISC, Language, Game, Literature, Religion, Festival).

## 🔬 Methodology

**Methods**:
- Model-based evaluation: fine-tuning pre-trained multilingual and Indic-focused language models (mBERT, XLM-R base, XLM-R large, IndicBERT, MuRIL)
- Cross-dataset evaluation (training on HiNER and testing on FIRE 2014)
- Zero-shot evaluation (transfer to FIRE 2014)
- Automated metrics evaluation using seqeval and nervaluate

**Metrics**:
- F1 Score (Micro, Macro, Weighted)
- Precision
- Recall
- Strict / Exact match F1 (Exact vs Strict evaluation schemas)

**Calculation**: Evaluation statistics computed using Seqeval and nervaluate. Models fine-tuned with hyper-parameter tuning on the development set; reported results are the mean and standard deviation over 5 runs. I-O-B encoding used as input format for training.

**Interpretation**: Higher F1 indicates better NER performance. Authors report that XLM-R large performs best across experiments; weighted F1 reported for all-tags and collapsed-tag settings as primary performance indicators.

**Baseline Results**: XLM-R large reported Weighted F1 = 88.78 (all 11 tags, test set, mean over 5 runs, std 0.57). On collapsed tagset (Person, Location, Organization) XLM-R large reported Weighted F1 = 92.22 (test set, mean over 5 runs, std 0.22).

**Validation**: Data split into 70% train / 10% dev / 20% test with stratification across tags. Hyper-parameter tuning performed on the development set; best hyper-parameters retrained and each experiment run 5 times to report mean and standard deviation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The annotation tool screenshot in the paper shows a redacted user name to preserve anonymity. No further privacy or anonymization procedures are discussed.

**Data Licensing**: CC-BY-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
