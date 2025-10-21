# STL-Diversity-Enhanced (STL-DivEn)

## 📊 Benchmark Details

**Name**: STL-Diversity-Enhanced (STL-DivEn)

**Overview**: The STL-DivEn dataset is designed to enhance the transformation of natural languages into Signal Temporal Logic (STL) through a diverse collection of 16,000 manually crafted and LLM-generated natural language (NL) and STL pairs, ensuring improved accuracy and reduced ambiguity in complex constraints.

**Data Type**: NL-STL pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DeepSTL

**Resources**:
- [GitHub Repository](https://github.com/YueFang0618/STL-DivEn)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and diverse dataset for improving the automatic transformation of natural language to Signal Temporal Logic in cyber-physical systems.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Natural Language to Logic Transformation

**Limitations**: The dataset may not fully capture the temporal property patterns of real-world cyber-physical systems due to its reliance on LLM-generated data.

## 💾 Data

**Source**: Manually created seed set of NL-STL pairs, enhanced through LLM augmentation.

**Size**: 16,000 samples

**Format**: JSON

**Annotation**: Manual annotation by experts and LLM-generated pairs validated through human checks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- STL Formula Accuracy
- Template Accuracy
- BLEU Score

**Calculation**: Metrics calculated based on strict alignment of predicted STL formulas with reference STL.

**Interpretation**: Higher accuracy scores indicate better alignment and correct transformations from NL to STL.

**Baseline Results**: Scores achieved on STL-DivEn dataset: STL Formula Accuracy 0.5587, Template Accuracy 0.5627, BLEU Score 0.2142.

**Validation**: The dataset was validated through human assessment ensuring semantic consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: The dataset aims for a comprehensive representation of temporal requirements but may introduce bias from LLM outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
