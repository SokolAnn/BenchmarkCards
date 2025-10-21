# FinMMR (Financial Multimodal Reasoning)

## 📊 Benchmark Details

**Name**: FinMMR (Financial Multimodal Reasoning)

**Overview**: FinMMR is a novel bilingual multimodal benchmark designed to evaluate the reasoning capabilities of multimodal large language models (MLLMs) in financial numerical reasoning tasks. It introduces three advancements: multimodality, comprehensiveness across 14 financial subdomains, and a challenge requiring multi-step numerical reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- FinanceReasoning
- MMMU
- MMMU-Pro
- FAMMA

**Resources**:
- [GitHub Repository](https://github.com/BUPT-Reasoning-Lab/FinMMR)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multimodal reasoning capabilities of MLLMs in the financial domain.

**Target Audience**:
- ML Researchers
- Model Developers
- Finance Professionals

**Tasks**:
- Numerical Reasoning
- Visual Perception
- Knowledge Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Curated from existing financial reasoning benchmarks, transform existing questions, and construct novel multimodal financial tasks.

**Size**: 4,300 questions and 8,700 images

**Format**: Multimodal (Text + Images)

**Annotation**: Questions transformed from existing benchmarks and newly crafted with expert verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the correctness of numerical answers provided by models.

**Interpretation**: Results indicate the percentage of correctly answered questions.

**Validation**: Rigorous validation by comparing model outputs against ground truth answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
