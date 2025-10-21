# ESC-Eval (Emotion Support Conversation Evaluation)

## 📊 Benchmark Details

**Name**: ESC-Eval (Emotion Support Conversation Evaluation)

**Overview**: ESC-Eval is the first framework designed for evaluating Large Language Model (LLM)-based Emotion Support Conversations (ESC) using a role-playing model. It allows for efficient assessment through collected multi-turn dialogue data between role-playing models and ESC chatbots, aiming to improve emotional support and reduce reliance on traditional evaluation metrics.

**Data Type**: multi-turn dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- ESConv
- ExTES
- Smile

**Resources**:
- [GitHub Repository](https://github.com/AIFlames/Esc-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To provide an efficient framework for evaluating the effectiveness of LLM-based Emotion Support Conversation models through role-playing interactions.

**Target Audience**:
- ML Researchers
- Psychologists
- AI Developers

**Tasks**:
- Emotion Support Conversation Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 2,801 role-playing cards reconstructed from existing datasets

**Size**: 8,500 dialogues

**Format**: JSON

**Annotation**: Manual annotation by experts and crowdsourced evaluations

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Fluency
- Diversity
- Empathy
- Information
- Skill
- Humanoid
- Overall

**Calculation**: Metrics scored based on a 5-point scale across defined criteria for human-like interaction and support.

**Interpretation**: Higher scores indicate better performance in emotional support and human-like qualities.

**Baseline Results**: Compared against human evaluations and other established models like GPT-4 and Baichuan-NPC

**Validation**: Research findings validated through extensive human annotation and correlation analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Emotional distress caused by ineffective responses from AI models.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymization and compliance with ethical standards for psychological data usage.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
