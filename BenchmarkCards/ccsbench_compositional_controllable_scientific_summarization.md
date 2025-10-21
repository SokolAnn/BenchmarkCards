# CCSBench (Compositional Controllable Scientific Summarization)

## 📊 Benchmark Details

**Name**: CCSBench (Compositional Controllable Scientific Summarization)

**Overview**: CCSBench is the first evaluation benchmark for compositional controllable summarization in the scientific domain, enabling fine-grained control over multiple attributes such as length and empirical focus.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CocoSciSum

**Resources**:
- [Resource](https://huggingface.co/datasets/dyxohjl666/CCSBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate compositional controllability in scientific document summarization by systematically assessing the ability of LLMs to generate controlled, contextually appropriate scientific summaries.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Summarization

**Limitations**: The benchmark presently does not support multilingual scientific summarization.

## 💾 Data

**Source**: Constructed from the arXiv dataset focusing on Computer Science and Artificial Intelligence papers.

**Size**: 7,800 examples

**Format**: CSV

**Annotation**: Generated using GPT-4 for readability and focus components.

## 🔬 Methodology

**Methods**:
- Human evaluation
- ROUGE evaluation
- Parameter-efficient fine-tuning

**Metrics**:
- ROUGE-L
- Mean Absolute Deviation (MAD)
- Pearson Correlation Coefficient (PCC)

**Calculation**: Metrics such as ROUGE scores are computed to assess fluency and content accuracy.

**Interpretation**: Higher ROUGE scores indicate better summary quality, while lower MAD indicates closer adherence to target lengths.

**Baseline Results**: Evaluated various LLMs against the CCSBench benchmark.

**Validation**: Involves both automated metrics and human evaluations for assessing summary quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
