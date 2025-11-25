# CACTUS (CBT-augmented Counseling ChatCorpus)

## 📊 Benchmark Details

**Name**: CACTUS (CBT-augmented Counseling ChatCorpus)

**Overview**: CACTUS is a multi-turn dialogue dataset that emulates real-life interactions using the goal-oriented and structured approach of Cognitive Behavioral Therapy (CBT). It captures the depth and flow of psychological counseling by designing client personas and applying CBT techniques in discussions.

**Data Type**: multi-turn counseling dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Psych8k
- SmileChat

**Resources**:
- [GitHub Repository](https://github.com/coding-groot/cactus)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset to train open-source language models as effective counseling agents by simulating real-life psychological counseling conversations.

**Target Audience**:
- ML Researchers
- Counseling Practitioners
- AI Developers

**Tasks**:
- Text Generation
- Dialog Generation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated using personas, thoughts, and patterns from the PatternReframe dataset.

**Size**: 31,577 dialogues

**Format**: JSON

**Annotation**: Manual curation and automated generation based on psychological principles.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Helpfulness
- Coherence
- Empathy
- Guidance

**Calculation**: Metrics are calculated based on manual evaluation and specific scaling for counseling dialogue criteria.

**Interpretation**: Higher scores indicate better performance in engagement and therapeutic quality.

**Validation**: Human evaluations conducted with experts and through Amazon Mechanical Turk.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: bypassing learning
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for misrepresentation of mental health advice']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is synthesized and does not include real client information; ethical standards for data use are followed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
