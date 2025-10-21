# QALB (Q Arabic Language Benchmark)

## 📊 Benchmark Details

**Name**: QALB (Q Arabic Language Benchmark)

**Overview**: The benchmark evaluates the performance of large language models (LLMs) in grammatical error correction (GEC) for Arabic, focusing on the complexities of Arabic grammar and morphology.

**Data Type**: sentence-level error correction examples

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://arxiv.org/abs/2312.08400)

## 🎯 Purpose and Intended Users

**Goal**: To advance the evaluation of Arabic grammatical error correction systems and provide insights into the effectiveness of instruction-finetuned large language models.

**Target Audience**:
- ML Researchers
- Linguists
- Educators

**Tasks**:
- Grammatical Error Correction

**Limitations**: 

## 💾 Data

**Source**: The QALB corpus, containing annotated Arabic texts including online commentaries from Aljazeera articles and texts produced by L1 and L2 learners of Arabic.

**Size**: 19,411 sentences in QALB-2014 training set, 310 sentences in QALB-2015 testing set

**Format**: JSON

**Annotation**: Manually corrected by experts

## 🔬 Methodology

**Methods**:
- Evaluation using F1 Score and Exact Match
- Instruction fine-tuning of LLMs
- Error type analysis using the Automatic Error Type Annotation tool (ARETA)

**Metrics**:
- F1 Score
- Exact Match

**Calculation**: Metrics were calculated based on precision, recall, and F1 score derived from the textual corrections made by the models compared to the ground truth.

**Interpretation**: Higher scores indicate better performance in correction tasks, with a focus on F1 score due to its balance between precision and recall in GEC.

**Validation**: Cross-validated against existing benchmarks such as QALB-2014 and QALB-2015.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: Analysis of errors across different demographic groups, focusing on L1 vs. L2 Arabic speakers.

**Potential Harm**: Potential for bias in error correction leading to misinterpretation of language use in various contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets used are publicly available, with no privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
