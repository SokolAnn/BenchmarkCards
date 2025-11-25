# MMATH (A Multilingual Benchmark for Mathematical Reasoning)

## 📊 Benchmark Details

**Name**: MMATH (A Multilingual Benchmark for Mathematical Reasoning)

**Overview**: MMATH is a benchmark for multilingual complex reasoning spanning 374 high-quality math problems across 10 typologically diverse languages. It aims to evaluate the capabilities of large language models (LLMs) in multilingual reasoning tasks.

**Data Type**: question-answering pairs

**Domains**:
- Mathematics
- Natural Language Processing

**Languages**:
- English
- Chinese
- Arabic
- Spanish
- French
- Japanese
- Korean
- Portuguese
- Thai
- Vietnamese

**Similar Benchmarks**:
- MGSM
- AIME
- CNMO
- MATH-500

**Resources**:
- [GitHub Repository](https://github.com/RUCAIBox/MMATH)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multilingual complex reasoning capabilities of large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Complex Reasoning

**Limitations**: Balancing accuracy and language consistency remains a significant challenge.

## 💾 Data

**Source**: High-quality math problems sourced from AIME, CNMO, and MATH-500, translated into 10 languages.

**Size**: 3,740 examples

**Format**: text

**Annotation**: Translated and validated through a pipeline combining LLM output and human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Answer Accuracy
- Language Consistency Ratio

**Calculation**: Answer Accuracy measures the proportion of instances in which the model produces the correct final answer. Language Consistency Ratio quantifies the alignment between input and output languages.

**Interpretation**: Higher scores in answer accuracy and LCR indicate better multilingual reasoning capabilities.

**Baseline Results**: AIME (16.67), DeepSeek-R1 (71.67), QwQ-32B (79.43)

**Validation**: The benchmark was validated through extensive human evaluation with linguistic experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The benchmark covers a diverse set of languages which helps assess multilingual capabilities across different linguistic demographics.

**Potential Harm**: Potential for underperformance in lower-resource languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
