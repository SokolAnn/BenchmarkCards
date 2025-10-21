# FlowExplainBench

## 📊 Benchmark Details

**Name**: FlowExplainBench

**Overview**: FlowExplainBench is a novel benchmark for evaluating flowchart attributions across diverse styles, domains, and question types, specifically designed for fine-grained flowchart attribution tasks.

**Data Type**: flowchart images with question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- FlowchartQA
- FlowVQA

**Resources**:
- [GitHub Repository](https://github.com/flowvqa/flowvqa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of flowchart attribution methods and improve the reliability of LLM responses in flowchart-based tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Flowchart Attribution

**Limitations**: FlowExplainBench does not encompass all real-world variations of flowcharts, such as hand-drawn diagrams.

## 💾 Data

**Source**: Constructed using FlowVQA dataset as a base for flowchart images and annotations.

**Size**: 1,238 samples

**Format**: JSON

**Annotation**: Initial attributions performed by GPT-4 and verified through human annotators.

## 🔬 Methodology

**Methods**:
- Graph-based reasoning
- Human evaluation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated through micro-averaging based on identified attributed paths in flowcharts.

**Interpretation**: Higher F1 scores indicate more accurate and relevant attributions between flowchart nodes and provided statements.

**Baseline Results**: FlowPathAgent outperformed baseline models by 10-14% according to the F1 Score on FlowExplainBench.

**Validation**: The benchmark was validated by comparing model outputs against human-annotated ground truths.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information (PII) is used; confidentiality for annotators is maintained.

**Data Licensing**: The FlowVQA dataset is distributed under the MIT License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
