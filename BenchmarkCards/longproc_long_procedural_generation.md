# LONGPROC (Long Procedural Generation)

## 📊 Benchmark Details

**Name**: LONGPROC (Long Procedural Generation)

**Overview**: LONGPROC is a new benchmark that consists of six diverse procedural generation tasks designed to evaluate long-context language models (LCLMs) on their ability to follow detailed procedural instructions, synthesize dispersed information, and generate structured long-form outputs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NIAH
- RULER
- ZeroScrolls
- ∞Bench
- SumHaystack
- HELMET
- LongGenBench 1
- LongGenBench 2
- LongWriter

**Resources**:
- [Resource](https://princeton-pli.github.io/LongProc)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive framework for evaluating the capabilities of long-context language models in handling complex procedural generation tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Information Extraction
- Code Generation
- Path Finding
- Theory-of-Mind Reasoning
- Arithmetic Problem Solving
- Travel Planning

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of six procedural generation task datasets specifically created for long-context language models.

**Size**: N/A

**Format**: N/A

**Annotation**: Manual annotation and automatic extraction processes were used across different tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Rule-based evaluation

**Metrics**:
- F1 Score
- Exact Match

**Calculation**: Metrics were calculated based on the correctness of outputs compared to the ground truth.

**Interpretation**: Higher scores indicate better model performance in following procedural instructions and generating coherent long-form outputs.

**Baseline Results**: N/A

**Validation**: Model performance was validated against human-created outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Highlighting limitations in long-context processing abilities of models.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
