# GLGE (General Language Generation Evaluation)

## 📊 Benchmark Details

**Name**: GLGE (General Language Generation Evaluation)

**Overview**: GLGE is a new multi-task benchmark for evaluating the generalization capabilities of NLG models across eight language generation tasks, designed to encourage research on pretraining and transfer learning in natural language generation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE

**Resources**:
- [GitHub Repository](https://github.com/microsoft/glge)
- [Resource](https://microsoft.github.io/glge/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the development, evaluation, and comparison of new NLG models across diverse tasks and difficulty levels.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Summarization
- Question Generation
- Generative Question Answering
- Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: Combination of six existing popular NLG datasets and two new datasets selected from real-world scenarios.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BLEU-4
- METEOR
- F1 Score

**Calculation**: Metrics are aggregated based on performance across all tasks.

**Interpretation**: The scores represent the level of success in generating coherent and contextually relevant outputs for each task.

**Baseline Results**: Comparative results with models such as MASS, BART, and ProphetNet on the GLGE benchmarks.

**Validation**: Performance on different levels of task difficulty (Easy, Medium, Hard) is evaluated to determine model generalization capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
