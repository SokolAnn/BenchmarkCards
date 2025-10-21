# The Combined Corpus

## 📊 Benchmark Details

**Name**: The Combined Corpus

**Overview**: An evaluation corpus created by merging two publicly available scholarly-abstract relation corpora (SemEval18 and SciERC) to provide a larger, more diverse and realistic evaluation scenario of large and heterogeneous data for scientific relation classification.

**Data Type**: text (manually annotated scholarly abstracts with scientific term pairs and relation labels)

**Domains**:
- Artificial Intelligence
- Natural Language Processing
- Speech
- Machine Learning
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- The SemEval18 Corpus
- The SciERC Corpus

**Resources**:
- [Resource](https://www.orkg.org/orkg/comparison/R38012)
- [GitHub Repository](https://github.com/google-research/bert)
- [GitHub Repository](https://github.com/allenai/scibert)

## 🎯 Purpose and Intended Users

**Goal**: Help stakeholders of digital libraries select appropriate techniques (BERT-based variants and classification strategies) to implement knowledge-graph-based systems for enhanced scholarly information organization by empirically evaluating scientific relation classification models.

**Target Audience**:
- Stakeholders of digital libraries

**Tasks**:
- Relation Classification
- Information Extraction
- Knowledge Graph Construction

**Limitations**: Evaluations are performed on corpora that cover the Artificial Intelligence research area (AI) only; labeled data exhibit label biases and unbalanced distributions across relation types; evaluation covers seven predefined relation types (limited relation set).

## 💾 Data

**Source**: C1: SemEval18 Corpus (SemEval-2018 shared task dataset of scholarly abstracts from the ACL Anthology); C2: SciERC Corpus (500 manually annotated abstracts from 12 AI conference/workshop proceedings); C3: The Combined Corpus created by merging C1 and C2 with unified relation labels.

**Size**: SemEval18: 500 abstracts; SemEval18 relation instances: 1,562 examples. SciERC: 500 abstracts; SciERC relation instances: 4,648 examples. Combined: 1,000 abstracts; Combined relation instances: 6,210 examples.

**Format**: N/A

**Annotation**: Manually annotated scholarly abstracts for scientific terms and the semantic relations between pairs of terms (human annotations from the original corpus creators).

## 🔬 Methodology

**Methods**:
- Fine-tuning of pre-trained BERT variants (BERT BASE cased/uncased; SciBERT cased/uncased)
- Single-relation-at-a-time classification (SRC)
- Multiple-relations-at-a-time classification (MRC)
- Automated evaluation on pre-partitioned train/dev/test splits

**Metrics**:
- Precision
- Recall
- F1-score (macro F1)
- Accuracy

**Calculation**: Standard classification metrics (Precision, Recall, F1, Accuracy) computed on the pre-partitioned test sets provided by the original corpora. F1 reported is macro F1. Class probabilities from SRC are normalized with softmax and label assigned by maximum probability. Models trained with tuned learning rates (values searched: 2e-5, 3e-5, 5e-5); other training parameters used default values from the pretrained models.

**Interpretation**: Higher Accuracy and F1 indicate better relation classification. SRC generally achieves higher classification accuracy than MRC, while MRC demonstrates more consistent (robust) performance on smaller or sparser-annotation corpora. Domain-specific pre-training (SciBERT) and uncased variants tend to yield better and more stable performance on scholarly data.

**Baseline Results**: Table 2 reports per-model Accuracy and macro-F1 across three corpora. Example aggregated result: SciBERT uncased averaged Accuracy 82.91 (±2.04) and averaged F1 78.99 (±1.54) across corpora. Detailed per-corpus and per-model numbers are provided in Table 2 of the paper.

**Validation**: Used original train/dev/test splits from the source corpora (SemEval18: 350 training / 150 testing; SciERC: 350/50/100 train/dev/test). Models were evaluated on the provided test splits; learning rate was tuned over specified values; other training parameters used defaults from BERT/SciBERT.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of testing diversity

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
