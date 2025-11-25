# RJUA-QA: A Comprehensive QA Dataset for Urology

## 📊 Benchmark Details

**Name**: RJUA-QA: A Comprehensive QA Dataset for Urology

**Overview**: RJUA-QA is a novel medical dataset for question answering (QA) and reasoning with clinical evidence, derived from realistic clinical scenarios and aims to facilitate LLMs in generating reliable diagnostic and advice. It contains 2,132 curated Question-Context-Answer pairs covering 67 common urological disease categories.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/alipay/RJU_Ant_QA)

## 🎯 Purpose and Intended Users

**Goal**: To construct a high-quality and comprehensive medical specialty QA dataset which has patient consultation simulations with expert-level annotations and requires medical reasoning over the query contexts and clinical knowledge to answer the questions.

**Target Audience**:
- ML Researchers
- Medical Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from realistic clinical scenarios, including outpatient diagnoses and treatments, emergency, inpatient surgeries, and procedures.

**Size**: 2,132 question-context-answer pairs

**Format**: N/A

**Annotation**: Manual curation by a medical annotation team with clinical expertise, alongside expert-level verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- ROUGE-L

**Calculation**: F1 score is calculated as F1= 2×P×R/(P+R), where P=TP/(TP+FP) denotes precision and R=TP/(TP+FN) denotes recall.

**Interpretation**: Higher F1 scores indicate better performance of the models in providing accurate diagnoses and treatment advice.

**Baseline Results**: Results from Huatuo GPT, GPT-3.5, Baichuan, and ChatGLM show varying F1 and ROUGE-L scores across the dataset.

**Validation**: The dataset is subjected to manual verification to ensure accuracy and relevance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
