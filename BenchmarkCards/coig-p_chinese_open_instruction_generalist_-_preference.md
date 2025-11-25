# COIG-P (Chinese Open Instruction Generalist - Preference)

## 📊 Benchmark Details

**Name**: COIG-P (Chinese Open Instruction Generalist - Preference)

**Overview**: COIG-P is a high-quality, large-scale Chinese preference dataset comprising 1,006k preference pairs generated using LLMs, aimed at aligning LLMs with human values in the Chinese context.

**Data Type**: chosen-rejected response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- ZAKE

**Resources**:
- [GitHub Repository](https://github.com/multimodal-art-projection/COIG-P)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive Chinese preference dataset that enhances the performance of LLMs in aligning with human values.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Preference Alignment

**Limitations**: N/A

## 💾 Data

**Source**: Generated via LLMs from crawled and filtered Chinese queries.

**Size**: 1,006,946 samples

**Format**: N/A

**Annotation**: Automatically generated using a pipeline with no human intervention.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Scores based on LLM-generated responses compared to human evaluations.

**Interpretation**: Higher scores indicate better alignment with human preferences.

**Baseline Results**: Performance compared to other existing Chinese preference datasets.

**Validation**: Results validated through comparison with AlignBench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
