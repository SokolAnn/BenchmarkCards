# EmoAgent

## 📊 Benchmark Details

**Name**: EmoAgent

**Overview**: EmoAgent is a multi-agent AI framework designed to evaluate and mitigate mental health hazards in human-AI interactions. It consists of EmoEval, which assesses risk of mental health deterioration in users after interactions with AI, and EmoGuard, which monitors and provides interventions to mitigate identified risks.

**Data Type**: simulated human-AI conversational interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/1akaman/EmoAgent)

## 🎯 Purpose and Intended Users

**Goal**: To develop AI-native solutions to protect human-AI interactions and mitigate psychosocial risks in vulnerable individuals.

**Target Audience**:
- ML Researchers
- Mental Health Professionals

**Tasks**:
- Risk Assessment
- Human-AI Interaction Evaluation

**Limitations**: The study focuses on three mental health conditions (depression, delusion, psychosis) and may not address other important psychological disorders.

## 💾 Data

**Source**: Simulated conversations with character-based AI agents using cognitive models based on psychiatric assessments.

**Size**: 400 simulated interactions

**Format**: N/A

**Annotation**: Automatically generated simulations based on cognitive models.

## 🔬 Methodology

**Methods**:
- Simulated Interaction Evaluation
- Psychological Assessment

**Metrics**:
- Deterioration Rate
- Psychological Test Score Change

**Calculation**: The deterioration rate is calculated based on the percentage of users whose psychological test scores worsen post-interaction.

**Interpretation**: A higher deterioration rate indicates a greater risk of psychological harm from the AI interactions.

**Baseline Results**: Simulated deterioration rates exceed 34.4% based on character interactions.

**Validation**: Validation conducted through controlled simulations and assessment of psychological impacts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential for inducing psychological distress in vulnerable users through engaging interactions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User simulations do not contain personal data or identifiers.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
