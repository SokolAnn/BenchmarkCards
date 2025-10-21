# MDD-5k: A New Diagnostic Conversation Dataset for Mental Disorders

## 📊 Benchmark Details

**Name**: MDD-5k: A New Diagnostic Conversation Dataset for Mental Disorders

**Overview**: MDD-5k is the largest Chinese mental disorders diagnosis dataset, consisting of 5000 high-quality long conversations generated through a neuro-symbolic multi-agent framework based on 1000 anonymized patient cases.

**Data Type**: dialogue conversations

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- D4
- CPsyCounD

**Resources**:
- [GitHub Repository](https://github.com/lemonsis/MDD-5k)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to facilitate AI applications in mental healthcare through the simulation of diagnostic conversations.

**Target Audience**:
- ML Researchers
- Mental Health Professionals

**Tasks**:
- Dialog Generation
- Mental Disorder Diagnosis

**Limitations**: The dataset primarily addresses a limited range of mental health conditions and may not fully represent the diversity of patient symptoms.

## 💾 Data

**Source**: 1000 anonymized patient cases from Shanghai Mental Health Center

**Size**: 5000 conversations

**Format**: N/A

**Annotation**: Conversations are labeled with diagnosis results and treatment opinions from professional psychiatrists.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Professionalism
- Communication
- Fluency
- Similarity
- Safety

**Calculation**: Metrics are calculated based on scores provided by human evaluators.

**Interpretation**: Higher scores in evaluation metrics indicate better performance and closer simulation of real diagnostic processes.

**Validation**: The dataset quality was validated through comprehensive human evaluation against related datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: 65% of patients are female, with a majority aged between 20-40 years.

**Potential Harm**: The dataset aims to mitigate risks associated with poor diagnostic conversations in clinical settings.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All patient cases underwent data masking to ensure the privacy of individuals.

**Data Licensing**: Not Applicable

**Consent Procedures**: Patients were informed their data would be used for research purposes.

**Compliance With Regulations**: The data masking procedures adhere to the Chinese information security guidelines (GB/T 39725-2020).
