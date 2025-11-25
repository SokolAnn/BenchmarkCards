# PEERSUM

## 📊 Benchmark Details

**Name**: PEERSUM

**Overview**: PEERSUM is a novel multi-document summarization dataset for generating meta-reviews of scientific papers. The meta-reviews are abstractive summaries of reviews, multi-turn discussions and the paper abstract, and the dataset exposes explicit hierarchical conversational structure, inter-document relationships, conflicts, and metadata (review ratings/confidence and paper acceptance outcome).

**Data Type**: text (multi-document: official reviews, public reviews, author comments/responses, paper abstracts; target summaries: meta-reviews)

**Domains**:
- Peer-review

**Similar Benchmarks**:
- WCEP
- Multi-News
- Multi-XScience
- WikiSum

**Resources**:
- [GitHub Repository](https://github.com/oaimli/PeerSum)
- [Resource](https://openreview.net/)
- [Resource](https://arxiv.org/abs/2305.01498)
- [GitHub Repository](https://github.com/maszhongming/UniEval)
- [Resource](https://huggingface.co/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a multi-document summarization dataset for automatic meta-review generation that (1) contains hierarchical conversational structure and inter-document relationships, (2) includes occasional conflicting source information and metadata (review ratings/confidences and acceptance outcome), and (3) serves as a probe to understand how machines can reason, aggregate and summarise potentially conflicting opinions.

**Target Audience**:
- ML Researchers
- Meta-reviewers / Conference Program Committee members
- Model Developers

**Tasks**:
- Meta-review Generation
- Multi-Document Summarization (Abstractive)

**Limitations**: Meta-review generation may require meta-reviewer judgement beyond source documents; limited inclusion of large closed-source models for comparison (possible contamination of training data); only explicit conversational structure considered; models still struggle to recognise and resolve conflicts in source documents.

## 💾 Data

**Source**: Peer-review data scraped from OpenReview for two conferences (ICLR 2018–2022 and NeurIPS 2021–2022), comprising official reviews, public reviews, author comments/responses, official/public responses, and paper abstracts; meta-reviews are used as reference summaries.

**Size**: 14,993 samples (train/validation/test: 11,995/1,499/1,499)

**Format**: N/A

**Annotation**: Constructed via scraping OpenReview with metadata extraction (review ratings, confidences, acceptance outcome, document types). A subset was manually annotated for faithfulness: 10 volunteers (PhD students) annotated 60 samples to link meta-review content to source documents; human evaluation (conflict recognition/resolution) was performed on selected test samples by recruited volunteers.

## 🔬 Methodology

**Methods**:
- Automated metrics (ROUGE, BERTScore, UniEval, ACC)
- Reference-free classifier-based evaluation (ACC)
- Human evaluation (conflict recognition and resolution judgments)
- Manual grounding annotation of meta-review statements to source documents

**Metrics**:
- ROUGE-L F1
- BERTScore F1
- UniEval - Consistency
- UniEval - Relevance
- Accuracy (ACC - acceptance prediction)

**Calculation**: ROUGE and BERTScore report F1 scores. UniEval frames evaluation as boolean question answering and reports 'consistency' and 'relevance'. ACC is computed by fine-tuning a BERT-based classifier on ground-truth meta-reviews and corresponding paper acceptance outcomes, then applying this classifier to generated meta-reviews and reporting prediction accuracy.

**Interpretation**: Higher metric values indicate better performance. ACC is intended as a reference-free measure of how consistent a generated meta-review is with the ground-truth meta-review's acceptance outcome.

**Baseline Results**: RAMMER (459M) outperforms baselines (BART, PEGASUS, PRIMERA, LED, PegasusX) across reported metrics. Example (CF∪Non-CF): RAMMER ROUGE-L 30.23, BERTScore 17.21, UniEval-Consistency 74.82, UniEval-Relevance 83.75, ACC 0.762.

**Validation**: Hyperparameters tuned on the validation partition (1,499 samples). Validation also includes held-out test partition (1,499 samples). Manual faithfulness annotation performed on 60 samples by 10 volunteers. Human evaluation for conflict recognition/resolution conducted on selected CF test samples with recruited volunteers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
