# LLMC+ (Large Vision-Language Model Compression Benchmark)

## 📊 Benchmark Details

**Name**: LLMC+ (Large Vision-Language Model Compression Benchmark)

**Overview**: LLMC+ is a comprehensive VLM compression benchmark with a versatile plug-and-play toolkit that supports over 20 algorithms across five representative VLM families, enabling systematic study of token-level and model-level compression.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GQA (Visual Question Answering)
- ScienceQA
- TextVQA
- OCRBench

**Resources**:
- [GitHub Repository](https://github.com/ModelTC/LightCompress)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate fair evaluation and inspire future research in efficient vision-language model compression.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Token Compression
- Model Compression

**Limitations**: Token reduction suffers from significant accuracy drops on fine-grained tasks, and prompt-dependent methods yield unsatisfactory results in multi-turn dialogue.

## 💾 Data

**Source**: Various image and video datasets, including GQA, OCRBench, and ScienceQA.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on performance comparisons of different compression techniques.

**Interpretation**: Higher accuracy indicates better retention of relevant information during compression.

**Baseline Results**: Performance of LLMC+ was evaluated against various benchmarks such as GQA and ScienceQA.

**Validation**: Extensive experiments conducted across multiple representative VLM families.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
