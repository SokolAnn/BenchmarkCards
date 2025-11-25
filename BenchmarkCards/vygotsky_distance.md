# Vygotsky Distance

## 📊 Benchmark Details

**Name**: Vygotsky Distance

**Overview**: This paper presents a theoretical instrument and a practical algorithm to calculate similarity between benchmark tasks, called Vygotsky distance. It helps to significantly reduce the evaluation tasks while maintaining high validation quality and increases the generalization potential of future NLP models.

**Data Type**: task similarity measure

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- CLUE
- RussianSuperGLUE

**Resources**:
- [Resource](https://arxiv.org/abs/2402.14890)

## 🎯 Purpose and Intended Users

**Goal**: To provide a method for evaluating the similarity of benchmark tasks to optimize resource usage in NLP evaluations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task Similarity Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: GLUE, SuperGLUE, CLUE, RussianSuperGLUE benchmarks and data from Papers With Code.

**Size**: Over 30 benchmarks with approximately 2600 divisions.

**Format**: tabular representation of model scores on tasks

**Annotation**: Model evaluation results from existing datasets.

## 🔬 Methodology

**Methods**:
- Graph Representation Analysis
- Benchmark Compression Algorithm

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall
- ROC-AUC

**Calculation**: Vygotsky distance is calculated based on the relative ranking of models on benchmark tasks.

**Interpretation**: A lower Vygotsky distance indicates higher similarity between tasks.

**Baseline Results**: N/A

**Validation**: Rigorously tested using model evaluation results from NLP benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
