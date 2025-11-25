# A Large-scale Class-level Benchmark Dataset for Code Generation with LLMs

## 📊 Benchmark Details

**Name**: A Large-scale Class-level Benchmark Dataset for Code Generation with LLMs

**Overview**: This paper introduces a large-scale, Python class-level dataset curated from 13,174 real-world open-source projects to better assess the capabilities of LLMs in generating realistic and structurally coherent class-level code.

**Data Type**: class skeletons

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- ClassEval

**Resources**:
- [Resource](https://anonymous.4open.science/r/class-level-benchmark-dataset-B132/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust benchmark dataset for evaluating LLMs on class-level code generation, addressing the gap in existing function-level benchmarks.

**Target Audience**:
- ML Researchers
- Software Developers
- AI Practitioners

**Tasks**:
- Code Generation

**Limitations**: The dataset may exhibit structural bias and incomplete documentation, potentially affecting code generation quality.

## 💾 Data

**Source**: Curated from real-world open-source projects extracted from the CodeSearchNet dataset.

**Size**: 842,656 class skeletons

**Format**: N/A

**Annotation**: Automated extraction from Python code using Abstract Syntax Trees.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE
- BLEU
- Tree Similarity of Edit Distance (TSED)

**Calculation**: Metrics compare LLM-generated classes against human-written classes using textual and structural similarity metrics.

**Interpretation**: Higher scores indicate greater similarity between the generated and reference code.

**Baseline Results**: N/A

**Validation**: Evaluated using class skeletons as structured prompts for GPT-4.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
