# HULK: An Energy Efﬁciency Benchmark Platform for Responsible Natural Language Processing

## 📊 Benchmark Details

**Name**: HULK: An Energy Efﬁciency Benchmark Platform for Responsible Natural Language Processing

**Overview**: HULK is a multi-task energy efficiency benchmarking platform for responsible natural language processing that compares pretrained models' energy efficiency from the perspectives of time and cost and provides baseline benchmarking results for pretraining, fine-tuning and inference.

**Data Type**: text (sentence-level classification and token-level labeling datasets)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- SQuAD
- MLPerf
- DAWNBenchmark
- Efficient NMT shared task

**Resources**:
- [Resource](https://sites.engineering.ucsb.edu/~xiyou/hulk/)
- [GitHub Repository](https://github.com/huggingface/transformers)

## 🎯 Purpose and Intended Users

**Goal**: Provide a practical multi-task reference for selecting pretrained NLP models by quantifying end-to-end energy efficiency (time and cost) in pretraining, fine-tuning and inference phases.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Industry Practitioners
- Natural Language Processing researchers

**Tasks**:
- Named Entity Recognition
- Natural Language Inference
- Sentiment Analysis

**Limitations**: Carbon emission and electricity usage are hard to track or hardware-dependent. Current benchmark uses a selected set of datasets (CoNLL-2003, MNLI, SST-2); adding more datasets requires additional computing resources.

## 💾 Data

**Source**: CoNLL-2003 (English Reuters newswire NER dataset), MNLI (Multi-Genre Natural Language Inference Corpus), SST-2 (Stanford Sentiment Treebank)

**Size**: CoNLL-2003: 14,041 train examples, 3,250 dev examples; MNLI: 392,702 train examples, 19,647 dev examples; SST-2: 67,349 train examples, 872 dev examples

**Format**: N/A

**Annotation**: CoNLL-2003: labeled named entities (Reuters Corpus); MNLI: crowdsourced textual entailment annotations; SST-2: human annotations of sentiment

## 🔬 Methodology

**Methods**:
- Automated measurement of time and cost for pretraining, fine-tuning and inference
- Normalized efficiency scoring relative to BERT LARGE
- Leaderboard submissions via CodaLab with required code, training logs and development set outputs
- Baseline experiments on controlled hardware (single GTX 2080 Ti GPU for fine-tuning/inference experiments)

**Metrics**:
- F1 Score
- Accuracy
- Time (seconds for fine-tuning/pretraining, milliseconds for inference)
- Cost (dollars)
- Normalized efficiency score (ratio to BERT LARGE time/cost)

**Calculation**: Time and cost are measured for pretraining, fine-tuning and inference. Normalization is computed by dividing BERT LARGE's time and cost by each model's time and cost. The efficiency score for a model on a task is the sum of normalized time and cost; overall score is the sum across tasks.

**Interpretation**: Models that require less time or cost to reach the task-specific cut-off performance are considered more energy-efficient. Higher normalized scores (BERT_LARGE_time_or_cost / model_time_or_cost) indicate better efficiency. Models faster or cheaper to pretrain are recommended.

**Baseline Results**: Baseline multi-task fine-tuning costs (Table 3) and inference costs (Table 4) provided for pretrained models. Examples from Table 3 (fine-tuning overall scores): BERT BASE: 2.53; BERT LARGE: 3.00; XLNet BASE: 3.42; XLNet LARGE: 10.31; RoBERTa BASE: 10.82; RoBERTa LARGE: 25.11; ALBERT BASE: 0.29; ALBERT LARGE: 0.13. Examples from Table 4 (inference overall scores): BERT BASE: 9.5; BERT LARGE: 3.00; XLNet BASE: 5.01; XLNet LARGE: 1.71; RoBERTa BASE: 9.53; RoBERTa LARGE: 3.01; ALBERT BASE: 9.53; ALBERT LARGE: 2.97.

**Validation**: Submissions to the HULK benchmark (CodaLab competition) must include source code, training/fine-tuning logs with time consumption and development set performance after steps, and development set outputs for result validation. Cut-off performance is measured on development sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Energy Efficiency
- Environmental Impact
- Reproducibility

**Atlas Risks**:
- **Societal Impact**: Impact on the environment

**Demographic Analysis**: N/A

**Potential Harm**: Carbon emission and environmental impact from computation-intensive model training and inference

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
