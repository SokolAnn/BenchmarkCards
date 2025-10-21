# MIRAGE -BENCH (Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems)

## 📊 Benchmark Details

**Name**: MIRAGE -BENCH (Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems)

**Overview**: A synthetic arena-based RAG benchmark for 18 diverse languages on Wikipedia focused on multilingual answer generation evaluation, coupling heuristic features and LLM evaluations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Bengali
- German
- English
- Spanish
- Farsi
- Finnish
- French
- Hindi
- Indonesian
- Japanese
- Korean
- Russian
- Swahili
- Telugu
- Thai
- Yoruba
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/vectara/mirage-bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a multilingual RAG benchmark for evaluating multilingual generation in RAG systems, improving understanding and performance across various languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MIRACL (a multilingual retrieval dataset) focusing on multilingual generation tasks using queries and passages judged by humans.

**Size**: 11,195 evaluation pairs and 39,763 training pairs across 18 languages.

**Format**: N/A

**Annotation**: Reused relevance judgments and queries from MIRACL dataset.

## 🔬 Methodology

**Methods**:
- Heuristic-based evaluation
- Pairwise LLM as judge

**Metrics**:
- Kendall Tau
- Recall @k
- MAP @k
- ROUGE-L
- SacreBLEU

**Calculation**: Metrics are computed using human-generated queries and relevance judgments, evaluated by LLMs.

**Interpretation**: A higher Kendall Tau score indicates better performance correlation between the surrogate judge and LLM evaluations.

**Baseline Results**: N/A

**Validation**: Validation via pairwise comparisons using LLM as a judge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
