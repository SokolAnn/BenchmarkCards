# Financial Education Corpus IN SpAnish (FEINA)

## 📊 Benchmark Details

**Name**: Financial Education Corpus IN SpAnish (FEINA)

**Overview**: A novel dataset for text simplification in Spanish financial education, consisting of 5,314 complex and simplified sentence pairs aimed at enhancing understanding for visually impaired audiences.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- Spanish

**Similar Benchmarks**:
- SIMPLEXT
- Aligned Newsela corpus (Spanish)

**Resources**:
- [Resource](https://huggingface.co/datasets/saul1917/FEINA)

## 🎯 Purpose and Intended Users

**Goal**: To create an accessible text simplification dataset for individuals with visual impairments, aiding comprehension of financial education materials.

**Target Audience**:
- ML Researchers
- Domain Experts
- Non-profit organizations focused on accessibility

**Tasks**:
- Text Simplification

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from selected financial education books designed to release a dataset to the scientific community.

**Size**: 5,314 pairs

**Format**: N/A

**Annotation**: Manually simplified by six advanced philology students using defined simplification rules.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- SARI
- BLEU Score
- Fernandez-Huerta
- Gutierrez-Polini
- Szigriszt-Pazos

**Calculation**: Metrics are computed using automated methods and human evaluators to determine simplification quality.

**Interpretation**: Lower scores in simplicity metrics indicate better simplification. Higher scores in BLEU and SARI indicate better performance.

**Validation**: Evaluation of manually generated dataset against outputs from GPT-3, MT5, and Tuner for quality assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Dataset designed to cater specifically to visually impaired individuals.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from human evaluators in the study.

**Compliance With Regulations**: Not Applicable
