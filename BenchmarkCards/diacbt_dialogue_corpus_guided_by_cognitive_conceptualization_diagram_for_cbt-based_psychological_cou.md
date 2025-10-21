# DiaCBT (Dialogue Corpus Guided by Cognitive Conceptualization Diagram for CBT-based Psychological Counseling)

## 📊 Benchmark Details

**Name**: DiaCBT (Dialogue Corpus Guided by Cognitive Conceptualization Diagram for CBT-based Psychological Counseling)

**Overview**: DiaCBT is a long-periodic dialogue corpus designed for counseling based on cognitive behavioral therapy (CBT). It incorporates structured cognitive conceptualization diagrams to guide client simulations in diverse counseling scenarios and evaluates the performance of psychotherapy-guided conversational agents.

**Data Type**: dialogue transcripts

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for training and evaluating psychological counseling models based on CBT techniques.

**Target Audience**:
- ML Researchers
- Psychological Researchers
- Mental Health Practitioners

**Tasks**:
- Dialogue Generation
- Psychological Counseling

**Limitations**: The dataset may not capture the full duration of typical therapy sessions, which last approximately 45 minutes each. Further iterations are needed to include longer dialogues.

## 💾 Data

**Source**: Public transcripts from cognitive behavioral therapy sessions sourced from the American Psychological Association and related resources.

**Size**: 108 cases with a total of 540 sessions

**Format**: JSON

**Annotation**: Annotated by trained volunteers and domain experts focusing on the application of 14 different CBT strategies.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Average Turns
- Success Rate (SR)
- Cognitive Therapy Rating Scale (CTRS)
- Positive and Negative Affect Scale (PANAS)

**Calculation**: Metrics are calculated based on user interactions and evaluations of dialogue performance.

**Interpretation**: Higher scores in metrics indicate better performance in simulating counseling sessions and achieving counseling goals.

**Validation**: The quality of data was validated through manual screening and expert evaluation, ensuring alignment with CBT principles.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Ethical Considerations

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Nonconsensual use
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

**Potential Harm**: The potential harm includes the risk of generating misleading advice or emotional distress if users over-rely on the chatbot instead of seeking professional help.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured through strict adherence to data protocols, using publicly available data to simulate client interactions.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from annotators for their contributions.

**Compliance With Regulations**: Not Applicable
