# PerHalluEval (Persian Hallucination Evaluation)

## 📊 Benchmark Details

**Name**: PerHalluEval (Persian Hallucination Evaluation)

**Overview**: PerHalluEval is the first dynamic hallucination evaluation benchmark for the Persian language, aimed at detecting extrinsic and intrinsic hallucinations in large language models through a three-stage LLM-driven pipeline with human validation. It evaluates performance on QA and summarization tasks specific to Persian culture.

**Data Type**: question-answering and summarization pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs’ hallucinations in Persian regarding extrinsic and intrinsic categories of hallucination and to create a comprehensive resource for future NLP research in Persian.

**Target Audience**:
- NLP Researchers
- Model Developers

**Tasks**:
- Question Answering
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark is constructed using existing Persian datasets: PN-Summary (for summarization) and PQuAD (for QA), with new hallucinated instances generated through a model-driven pipeline.

**Size**: 8,000 instances (4,000 for QA and 4,000 for summarization)

**Format**: N/A

**Annotation**: Annotated by three human annotators based on majority vote.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Factual Recall
- Hallucination Recall
- Hamming Score

**Calculation**: Metrics are calculated by evaluating model predictions against the ground truth using definitions of True Positives, False Positives, True Negatives, and False Negatives.

**Interpretation**: High Factual Recall indicates accuracy in identifying factual content; high Hallucination Recall shows robustness in detecting hallucinations.

**Validation**: Inter-annotator agreement assessed using Gwet’s AC1 with high indices of 0.89 for QA and 0.91 for summarization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All annotators were instructed to maintain confidentiality, and participant inputs were processed without personal identification.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participation was informed and voluntary.

**Compliance With Regulations**: Not Applicable
