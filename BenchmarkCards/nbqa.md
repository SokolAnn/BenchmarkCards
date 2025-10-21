# NbQA

## 📊 Benchmark Details

**Name**: NbQA

**Overview**: NbQA is a large-scale dataset of standardized task-solution pairs extracted from Jupyter notebooks, designed to enhance multi-step reasoning capabilities in data analysis workflows.

**Data Type**: task-solution pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- InfiAgent-DABench
- DSBench
- AIME

**Resources**:
- [Resource](https://huggingface.co/datasets/opencompass/NbQA)

## 🎯 Purpose and Intended Users

**Goal**: To improve large language models' capabilities in performing multi-step data analysis tasks through a dataset of standardized task-solution pairs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Data Scientists

**Tasks**:
- Data Analysis
- Multi-Step Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: 1.6 million Jupyter notebooks collected from GitHub

**Size**: 38,635 task-solution pairs

**Format**: CSV

**Annotation**: Automatically extracted and annotated through a pipeline utilizing GPT-4o.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Overall accuracy is calculated based on the number of tasks correctly solved by models on evaluation benchmarks.

**Interpretation**: Higher accuracy indicates better performance in data analysis and reasoning tasks.

**Baseline Results**: Comparison with Qwen2.5-7B and Qwen2.5-14B Instruct models, showing significant accuracy improvements after fine-tuning on NbQA.

**Validation**: Validation is performed through rigorous testing on InfiAgent-DABench to ensure the effectiveness of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
