# SalesBot 2.0

## 📊 Benchmark Details

**Name**: SalesBot 2.0

**Overview**: SalesBot 2.0 is an improved dataset that encompasses open-domain chit-chats, seamless transitions, and potential intent detection from contextual cues, significantly enhancing coherence and naturalness in sales-customer interactions.

**Data Type**: dialogue pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SalesBot 1.0
- MultiWoz
- SGD

**Resources**:
- [GitHub Repository](https://github.com/MiuLab/SalesAgent)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that improves the integration of task-oriented and open-domain dialogues for more effective sales conversational agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Generation
- Intent Detection

**Limitations**: The dataset is dependent on the quality of large language models used for generation, which may introduce noisy or inaccurate outputs.

## 💾 Data

**Source**: Generated using large language models through a specific data generation framework.

**Size**: N/A

**Format**: N/A

**Annotation**: Annotated for potential user intents, chit-chat context, and transition dialogues.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Naturalness
- Coherence
- Smoothness

**Calculation**: Metrics were calculated based on evaluating dialogue quality through comparison with baseline models.

**Interpretation**: Higher scores indicate better performance in generating human-like responses and maintaining coherent dialogues.

**Baseline Results**: The model trained on SalesBot 2.0 shows significant improvements over the previous version (SalesBot 1.0) across various evaluation metrics.

**Validation**: Evaluation against user simulators and prior baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
