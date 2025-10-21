# MaRs-VQA (Matrix Reasoning Visual Question Answering)

## 📊 Benchmark Details

**Name**: MaRs-VQA (Matrix Reasoning Visual Question Answering)

**Overview**: MaRs-VQA is a new visual question answering dataset designed to evaluate the visual cognition capabilities of Multimodal Large Language Models (MLLMs) in matrix reasoning tasks. It allows for direct comparison between MLLMs and human performance on a scale larger than previous benchmarks.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Cognitive Psychology

**Languages**:
- English

**Similar Benchmarks**:
- RAVEN

**Resources**:
- [Resource](https://huggingface.co/datasets/IrohXu/VCog-Bench)
- [GitHub Repository](https://github.com/IrohXu/Cognition-MLLM)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the visual cognitive abilities of MLLMs and identify the performance gap between MLLMs and human intelligence in matrix reasoning tasks.

**Target Audience**:
- ML Researchers
- Psychologists
- AI Developers

**Tasks**:
- Visual Question Answering
- Matrix Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Psychologist-designed questionnaire from the Matrix Reasoning Item Bank (MaRs-IB)

**Size**: 1,440 image instances

**Format**: JSON

**Annotation**: Annotated with multi-stage cognition reasoning steps and options

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Models evaluated based on accuracy of correctly identifying the missing piece in matrix reasoning tasks.

**Interpretation**: Higher accuracy indicates better performance in visual cognition tasks relative to human benchmarks.

**Baseline Results**: Human performance achieved 81% accuracy while top-performing model reached 72.71%.

**Validation**: Validated across multiple existing MLLMs and compared against human results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinterpretation of intelligence comparisons between AI and humans']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Attribution-NonCommercial 3.0 license for MaRs-IB, MIT License for study results.

**Consent Procedures**: All human studies in the source dataset approved by relevant ethical committees.

**Compliance With Regulations**: Not Applicable
