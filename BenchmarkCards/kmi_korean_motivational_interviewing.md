# KMI (Korean Motivational Interviewing)

## 📊 Benchmark Details

**Name**: KMI (Korean Motivational Interviewing)

**Overview**: KMI is a synthetic dataset containing 1,000 high-quality Korean Motivational Interviewing dialogues generated through a framework that simulates MI sessions with the expertise of professional therapists.

**Data Type**: dialogue pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Korean

**Similar Benchmarks**:
- AnnoMI

**Resources**:
- [GitHub Repository](https://github.com/hjkim811/KMI)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a resource for developing mental health chatbots grounded in Motivational Interviewing theory.

**Target Audience**:
- ML Researchers
- Mental Health Practitioners
- Model Developers

**Tasks**:
- Dialogue Generation
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Generated using a framework simulating Motivational Interviewing sessions based on context data collected from a Korean psychological counseling platform.

**Size**: 1,000 dialogues

**Format**: JSON

**Annotation**: Each therapist utterance is annotated with a therapist behavior label derived from MITI coding.

## 🔬 Methodology

**Methods**:
- Expert evaluation
- Human evaluation
- Automated metrics

**Metrics**:
- Quality adherence to MI principles
- Consistency
- Fluency
- On-topic relevance

**Calculation**: Metrics are calculated through expert evaluations using a Likert scale to assess MI quality and general quality.

**Interpretation**: Higher scores indicate better adherence to MI principles and overall dialogue quality.

**Validation**: Expert evaluation by professional counselors to assess dataset quality and utility.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was collected from publicly available posts without interacting with users.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
