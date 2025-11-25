# MATINF (Maternal and Infant Dataset)

## 📊 Benchmark Details

**Name**: MATINF (Maternal and Infant Dataset)

**Overview**: We propose MATINF, the first jointly labeled large-scale dataset for classification, question answering and summarization. MATINF contains 1.07 million question-answer pairs with human-labeled categories and user-generated question descriptions and is applicable for three major NLP tasks: text classification, question answering, and summarization.

**Data Type**: text (question-answering pairs with fields: question, description, answer; plus human-labeled class labels; supports description->question summarization)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- SQuAD
- CNN / DM
- AG News
- LCSTS
- DuReader
- MS-MARCO
- LCQMC
- ImageNet

**Resources**:
- [GitHub Repository](https://github.com/WHUIR/MATINF)
- [Resource](https://arxiv.org/abs/2004.12302)
- [GitHub Repository](https://github.com/fxsjy/jieba)

## 🎯 Purpose and Intended Users

**Goal**: Provide a jointly labeled large-scale dataset to support and benchmark multi-task learning for text classification, question answering, and summarization within the maternity and baby caring domain.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts in Healthcare

**Tasks**:
- Text Classification
- Question Answering
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Crawled from a large Chinese maternity and baby caring QA site (user-generated QA forum). Each entry includes question (Q), description (D), class (C) and answer (A).

**Size**: 1.07 million question-answer pairs

**Format**: N/A

**Annotation**: Class labels are selected by users on submission and manually re-categorized by forum administrators when needed; the asker selects the best answer from candidate answers; descriptions and answers are user-generated. The authors performed automatic and manual data cleaning (removing classes with insufficient samples, entries with description shorter than question, fields longer than 256 characters, and human-spotted ill-formed data).

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Benchmarking of existing baseline models
- Evaluation of proposed multi-task model (MTF-S2S) against single-task baselines

**Metrics**:
- Accuracy
- ROUGE-1 (character-level)
- ROUGE-2 (character-level)
- ROUGE-L (character-level)

**Calculation**: Accuracy measured on test splits for classification tasks. ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L) are calculated on the character level for generation tasks. Training optimization uses Cross-Entropy loss and Adam optimizer; total loss for multi-task training is a weighted sum of task losses as described in the paper.

**Interpretation**: Results are interpreted via comparison to baseline methods: higher Accuracy or higher ROUGE indicates better performance. The paper reports relative improvements of the multi-task baseline (MTF-S2S) over single-task baselines; no absolute performance thresholds are provided.

**Baseline Results**: Classification (MATINF-C): DPCNN: 91.02 (AGE), 65.92 (TOPIC); BERT-Base: 90.33 (AGE), 66.95 (TOPIC); MTF-S2S (multi-task): 90.29 (AGE), 63.59 (TOPIC). Question Answering (MATINF-QA): Best Passage (upper bound) R-1:58.32 R-2:36.42 R-L:49.00; BERT Matching R-1:18.66 R-2:3.28 R-L:10.78; Seq2Seq R-1:16.62 R-2:4.53 R-L:10.37; Seq2Seq+Att R-1:19.62 R-2:5.87 R-L:13.34; MTF-S2S R-1:21.66 R-2:6.58 R-L:14.26. Summarization (MATINF-SUMM): TextRank R-1:35.53 R-2:25.78 R-L:36.84; Seq2Seq+Att R-1:43.05 R-2:28.03 R-L:38.58; BertAbs R-1:57.31 R-2:44.05 R-L:55.93; MTF-S2S R-1:48.59 R-2:35.69 R-L:43.28.

**Validation**: Data randomly split into train/validation/test with proportion 7:1:2. Experiments run with three random seeds and reported averages. Early stopping applied for some models. Multi-task co-training run for one epoch then fine-tuned for each task separately.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
