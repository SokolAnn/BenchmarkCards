# VarBench (Variable Benchmarking for Language Models)

## 📊 Benchmark Details

**Name**: VarBench (Variable Benchmarking for Language Models)

**Overview**: VarBench is a dynamic benchmark designed to mitigate data contamination issues in language model evaluations by variabilizing existing datasets. It uses a variable perturbation technique to create new test cases, thus providing a more accurate assessment of language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- CommonsenseQA
- TruthfulQA
- ARC

**Resources**:
- [GitHub Repository](https://github.com/qbetterk/VarBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more robust evaluation framework for language models by addressing issues of data contamination in existing benchmarks through dynamic variable perturbation.

**Target Audience**:
- ML Researchers
- Language Model Developers
- AI Practitioners

**Tasks**:
- Mathematical Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: GSM8K, Commonsense QA, Truthful QA, ARC

**Size**: Variable based on the number of test cases generated for each benchmark

**Format**: N/A

**Annotation**: Automatic generation with human verification

## 🔬 Methodology

**Methods**:
- Dynamic variable perturbation

**Metrics**:
- Accuracy

**Calculation**: Performance is assessed based on the accuracy of language models on newly generated test cases compared to original benchmarks.

**Interpretation**: Lower accuracy on VarBench than on original benchmarks indicates potential data contamination effects.

**Baseline Results**: Comparative accuracy results on original versus perturbed benchmarks.

**Validation**: Validated through human verification of generated test cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
