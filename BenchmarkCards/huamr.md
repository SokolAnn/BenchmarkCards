# HuAMR

## 📊 Benchmark Details

**Name**: HuAMR

**Overview**: HuAMR is the first Abstract Meaning Representation (AMR) dataset for Hungarian, providing a valuable resource for semantic parsing research in non-English languages. It includes manually refined silver-standard AMR annotations generated using Llama-3.1-70B.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Hungarian

**Similar Benchmarks**:
- AMR 3.0

**Resources**:
- [GitHub Repository](https://github.com/botondbarta/HuAMR)

## 🎯 Purpose and Intended Users

**Goal**: To create a Hungarian AMR dataset that enhances semantic parsing capabilities for the Hungarian language.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Semantic Parsing

**Limitations**: N/A

## 💾 Data

**Source**: Translated from AMR 3.0 dataset and generated silver-standard annotations.

**Size**: 40,000 instances for training, 3,811 instances for testing

**Format**: N/A

**Annotation**: Automatically generated AMR graphs, refined manually for quality.

## 🔬 Methodology

**Methods**:
- Evaluation using Smatch scores

**Metrics**:
- Smatch Score

**Calculation**: Smatch scores are calculated based on the overlap of matched triples between AMR graphs.

**Interpretation**: Higher Smatch scores indicate better performance in semantic parsing accuracy.

**Baseline Results**: N/A

**Validation**: Evaluated the generated graphs against PropBank frame argument descriptions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
