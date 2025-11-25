# Ordered CommonGen

## 📊 Benchmark Details

**Name**: Ordered CommonGen

**Overview**: A benchmark designed to evaluate the compositional generalization and instruction-following abilities of LLMs by measuring ordered coverage of generated sentences in response to specified concept orders.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CommonGen

**Resources**:
- [Resource](https://hf.co/datasets/allenai/commongen_lite)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capability of LLMs to generate sentences that follow explicit instructions regarding the order of concepts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Generation
- Compositional Generalization

**Limitations**: N/A

## 💾 Data

**Source**: CommonGen-lite dataset and instruction templates from FLAN.

**Size**: 27,648 instances

**Format**: JSON

**Annotation**: Automatically generated using LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Ordered Rate
- Coverage without order
- Diversity
- Perplexity

**Calculation**: Metrics are calculated based on the percentage of concepts correctly generated in specified order and overall diversity of outputs.

**Interpretation**: Higher scores in Ordered Rate indicate better adherence to specified order of concepts.

**Baseline Results**: N/A

**Validation**: Comprehensive benchmarking across 36 LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache License 2.0 for FLAN templates, MIT License for CommonGen.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
