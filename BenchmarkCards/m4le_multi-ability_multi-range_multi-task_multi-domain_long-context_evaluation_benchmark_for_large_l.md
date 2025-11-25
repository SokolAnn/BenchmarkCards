# M4LE (Multi-Ability Multi-Range Multi-Task Multi-Domain Long-Context Evaluation Benchmark for Large Language Models)

## 📊 Benchmark Details

**Name**: M4LE (Multi-Ability Multi-Range Multi-Task Multi-Domain Long-Context Evaluation Benchmark for Large Language Models)

**Overview**: M4LE is a benchmark designed to evaluate the long-context capabilities of large language models across various tasks, domains, and input lengths. It encompasses 36 task types related to long-context understanding across 12 domains and 5 distinct abilities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- SCROLLS
- ZeroSCROLLS
- L-Eval
- LongBench

**Resources**:
- [GitHub Repository](https://github.com/KwanWaiChung/M4LE)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate large language models' long-context understanding capabilities through a varied set of tasks and scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Text Classification
- Summarization
- Retrieval
- Translation

**Limitations**: Current evaluation is limited to smaller models and lengths of up to 8K; future work could explore longer contexts.

## 💾 Data

**Source**: 36 established datasets in both English and Chinese from diverse NLP tasks and domains, including QA, summarization, classification, and translations.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation of models on extended context inputs
- Comparison of long-context capabilities across various scenarios and task types

**Metrics**:
- Accuracy
- F1 Score
- ROUGE-L
- BLEU

**Calculation**: Metrics are calculated based on model performance in different context lengths and across abilities, normalized against a baseline model (GPT-3.5-Turbo-16K).

**Interpretation**: Higher scores indicate better performance in understanding and processing long-context data, with significant drops noted at longer input lengths.

**Baseline Results**: Performance compared to 11 prominent LLMs, notably observed drops in accuracy correlated with longer contexts, particularly in tasks requiring multiple span attention.

**Validation**: Systematic evaluation across various models to assess their competencies in handling long inputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
