# HRM8K

## 📊 Benchmark Details

**Name**: HRM8K

**Overview**: HRM8K is a bilingual benchmark comprising 8,011 English-Korean parallel mathematics problems, aimed at assessing multilingual mathematical reasoning capabilities.

**Data Type**: bilingual math problems

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Korean

**Similar Benchmarks**:
- MATH
- GSM8K
- MMMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/HAERAE-HUB/HRM8K)

## 🎯 Purpose and Intended Users

**Goal**: To investigate and bridge the performance gap in multilingual mathematical reasoning, specifically for Korean using English as an anchor language.

**Target Audience**:
- ML Researchers
- Education Professionals
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing Korean mathematics problems and established English benchmarks, including translations.

**Size**: 8,011 questions

**Format**: JSON

**Annotation**: Manually curated and verified translations from Korean to English and vice versa using GPT-4o.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the proportion of correct answers derived from model outputs.

**Interpretation**: Higher accuracy indicates better performance in mathematical reasoning for bilingual problems.

**Baseline Results**: The UST-trained model achieves 50.43% accuracy on the HRM8K benchmark.

**Validation**: Evaluated against existing benchmarks (e.g., KMMLU, MATH) for comparative performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
