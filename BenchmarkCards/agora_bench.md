# AGORA BENCH

## 📊 Benchmark Details

**Name**: AGORA BENCH

**Overview**: AGORA BENCH is a benchmark for evaluating LMs’ data generation capabilities through standardized settings and metrics across nine settings, combining three domains (math, instruction-following, code) with three data generation methods (instance generation, response generation, quality enhancement).

**Data Type**: training instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/neulab/data-agora)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LMs’ data generation capabilities and identify core capabilities that make an effective data generator.

**Target Audience**:
- ML Researchers
- Practitioners

**Tasks**:
- Data Generation

**Limitations**: Due to compute constraints and expensive API costs, the experimental setting does not cover scenarios with different base models beyond Llama-3.1-8B.

## 💾 Data

**Source**: Synthesized from various datasets for training LMs.

**Size**: 1,260,000 training instances

**Format**: N/A

**Annotation**: Automatically generated based on meta-prompts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Performance Gap Recovered (PGR)

**Calculation**: PGR measures the relative improvement of the student model trained on the generated data over its base model.

**Interpretation**: Higher PGR indicates better data generation capabilities of the model.

**Validation**: The evaluation results are validated through comparisons across multiple data generation methods and models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
