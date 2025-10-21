# CMB (Comprehensive Medical Benchmark in Chinese)

## 📊 Benchmark Details

**Name**: CMB (Comprehensive Medical Benchmark in Chinese)

**Overview**: CMB is a localized medical benchmark designed to measure the effectiveness of large language models (LLMs) within the context of Chinese medical knowledge, integrating both traditional Chinese medicine and modern medical practices. It includes multiple-choice questions and complex clinical diagnostic questions.

**Data Type**: multiple-choice questions and clinical diagnostic questions

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MultiMedBench
- BioLAMA

**Resources**:
- [GitHub Repository](https://github.com/FreedomIntelligence/CMB)

## 🎯 Purpose and Intended Users

**Goal**: To establish a standardized benchmark for evaluating LLMs in medical contexts, specifically tailored to the Chinese healthcare environment.

**Target Audience**:
- ML Researchers
- Medical Professionals
- Model Developers

**Tasks**:
- Question Answering
- Medical Diagnosis

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available examination questions and clinical diagnostic materials vetted by medical experts.

**Size**: 280,839 questions

**Format**: N/A

**Annotation**: Expert-reviewed and curated medical questions and clinical cases.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Expert evaluation

**Metrics**:
- Accuracy
- Fluency
- Completeness
- Relevance
- Proficiency

**Calculation**: Metrics calculated based on answer matching against expert-curated solutions.

**Interpretation**: Higher scores indicate better performance in medical reasoning and knowledge application.

**Baseline Results**: N/A

**Validation**: Performance of models evaluated against expert benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential propagation of inaccuracies in medical information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data processed to ensure no personal information is included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
