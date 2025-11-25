# BOSS (Benchmark suite for Out-of-distribution robustness evaluation)

## 📊 Benchmark Details

**Name**: BOSS (Benchmark suite for Out-of-distribution robustness evaluation)

**Overview**: Introduces BOSS, a benchmark suite for Out-of-distribution robustness evaluation covering 5 tasks and 20 datasets, constructed via a protocol that ensures clear differentiation and challenging distribution shifts to better evaluate OOD robustness in NLP.

**Data Type**: text (classification examples, token-level NER sequences, and extractive question-answering pairs)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- GLUE-X
- GLUE
- Adversarial GLUE

**Resources**:
- [GitHub Repository](https://github.com/lifan-yuan/OOD_NLP)
- [Resource](https://arxiv.org/abs/2306.04618v2)

## 🎯 Purpose and Intended Users

**Goal**: Establish a benchmark construction protocol and introduce BOSS to provide a holistic and challenging evaluation suite for out-of-distribution robustness in NLP.

**Target Audience**:
- NLP Researchers

**Tasks**:
- Sentiment Analysis
- Toxic Detection
- Natural Language Inference
- Named Entity Recognition
- Extractive Question Answering

**Limitations**: Some datasets may have been included in the pre-training corpus of LLMs, limiting suitability for testing LLM generalizability; only five tasks are included, not a comprehensive collection of NLP tasks.

## 💾 Data

**Source**: Curated collection of 20 public NLP datasets (per Table 4) used to form BOSS: Sentiment Analysis (Amazon, Dynasent, SemEval, SST), Toxic Detection (Civil Comments, AdvCivil [constructed in this work], Implicit Hate, ToxiGen), Natural Language Inference (MNLI, ANLI, ContractNLI, WANLI), Named Entity Recognition (Few-NERD, CoNLL, E-NER, WNUT), Extractive Question Answering (SQuAD, AdvQA, NewsQA, SearchQA).

**Size**: 20 datasets

**Format**: Text datasets in task-specific formats: classification datasets aligned to a three-class setup for sentiment; NER datasets converted to BIO token-label format; extractive QA normalized to SQuAD-style extractive format.

**Annotation**: Existing dataset annotations retained; several OOD/adversarial datasets (e.g., AdvCivil, Dynasent, ANLI, AdvQA) are constructed or collected using human-and-model-in-the-loop or automated adversarial generation with human verification (explicitly stated for AdvCivil and cited adversarial datasets).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (training and testing pre-trained models like T5 and DeBERTa)
- Probing experiments (semantic similarity via SimCSE and performance-drop based selection)
- LLM evaluation paradigms: zero-shot, in-context learning, few-shot fine-tuning, full-data fine-tuning

**Metrics**:
- Accuracy
- Micro F1
- F1 Score

**Calculation**: Metrics computed on test splits of selected ID and OOD datasets using standard task-specific measures: Accuracy for classification/NLI, Micro F1 for NER, F1 for extractive QA. Semantic similarity measured via SimCSE using a supervised RoBERTa-large checkpoint (Huggingface).

**Interpretation**: ID vs OOD performance correlations are categorized into three types observed in experiments: (Type I) monotonic linear positive correlation, (Type II) monotonic piecewise linear positive correlation, and (Type III) non-monotonic V-shaped correlation. Results indicate vanilla fine-tuning remains a strong baseline; LLMs with in-context learning often perform better on OOD while fine-tuned domain models perform better on ID when sufficient data is available.

**Baseline Results**: Baseline vanilla fine-tuning results are reported per dataset (see Table 5/Table 6). Examples explicitly reported: Vanilla accuracy on Amazon (AZ) = 90.94; Dynasent (DS) = 47.38; SQuAD (ID) F1 = 93.14.

**Validation**: Dataset selection validated via two probing experiments: (1) semantic similarity measured with SimCSE (supervised RoBERTa-large checkpoint from Huggingface) using dataset centroid cosine similarity, and (2) quantifying challenge by training a T5-large model (DeBERTa-large for NER) on ID datasets and selecting OOD datasets that provoke the largest performance drop.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Governance

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Governance**: Lack of testing diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
