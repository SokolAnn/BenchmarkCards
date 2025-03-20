# Multilingual Hallucination Removal (MHR)

## 📊 Benchmark Details

**Name**: Multilingual Hallucination Removal (MHR)

**Overview**: This paper presents a two-stage Multilingual Hallucination Removal framework to mitigate hallucination in Large Vision-Language Models (LVLMs), specifically targeting both high-resource and low-resource languages.

**Data Type**: multilingual image-query pairs

**Domains**:
- vision-language models
- multimodal learning

**Languages**:
- english
- spanish
- french
- german
- chinese
- japanese
- russian
- ukrainian
- bulgarian
- turkish
- korean
- arabic

**Similar Benchmarks**:
- POPE
- MME
- AMBER

**Resources**:
- [GitHub Repository](https://github.com/ssmisya/MHR)

## 🎯 Purpose and Intended Users

**Goal**: To improve the performance of LVLMs by mitigating multilingual hallucinations.

**Target Audience**:
- Researchers in AI and machine learning
- Developers of vision-language models

**Tasks**:
- Multilingual hallucination mitigation
- Evaluating model performance on multilingual datasets

**Limitations**: None

## 💾 Data

**Source**: POPE benchmark datasets, MME benchmark datasets

**Size**: 2.08M instruction-answer pairs

**Format**: image-query pairs

**Annotation**: Multilingual annotation for hallucination-aware datasets

## 🔬 Methodology

**Methods**:
- Multilingual Supervised Fine-tuning
- Direct Preference Optimization
- Cross-lingual alignment

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 score

**Calculation**: Metrics calculated on extended benchmark evaluations

**Interpretation**: Improvements in model accuracy for hallucination response handling

**Baseline Results**: Average improvement of 19.0% on the POPE benchmark across 13 languages

**Validation**: Experimental results demonstrated significant improvements in reducing hallucinations

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Privacy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Data privacy rights alignment
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Potential Harm**: Potential for model misuse leading to misinformation or data privacy issues

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used is anonymized and follows ethical guidelines.

**Data Licensing**: The datasets used are compliant with applicable data usage rights.

**Consent Procedures**: All data is collected in accordance with consent procedures.

**Compliance With Regulations**: The framework adheres to relevant legal and data protection regulations.
