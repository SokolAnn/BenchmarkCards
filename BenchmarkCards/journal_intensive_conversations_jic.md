# Journal Intensive Conversations (JIC)

## 📊 Benchmark Details

**Name**: Journal Intensive Conversations (JIC)

**Overview**: A novel dataset with around 400,000 dialogues designed to capture human personality traits more effectively than existing datasets by generating personalized conversations using long-form journal entries from Reddit.

**Data Type**: dialogue data

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Persona Chat (PC)
- Synthetic Persona Chat (SPC)
- Blended Skill Talk (BST)

**Resources**:
- [GitHub Repository](https://github.com/buffaloedu/JIC)

## 🎯 Purpose and Intended Users

**Goal**: To create a conversational dataset that captures the dynamic and evolving nature of human personalities, enhancing the performance of large language models in generating more nuanced dialogues.

**Target Audience**:
- ML Researchers
- Converse AI Developers
- Domain Experts

**Tasks**:
- Dialogue Generation
- Personality Trait Recognition

**Limitations**: Optimizing parameters for filtration remains an open challenge; potential biases from synthetic data generation.

## 💾 Data

**Source**: Reddit journal entries

**Size**: 418,476 dialogues

**Format**: JSON

**Annotation**: Automated data generation with human verification of personality traits.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Based on model predictions compared to ground truth personality trait scores and compute metrics such as BLEU and ROUGE for dialogue quality assessment.

**Interpretation**: Higher scores indicate better alignment with human personality traits and more coherent dialogues.

**Baseline Results**: Pre-trained LLaMA and Mistral models evaluated on JIC showed improvements in capturing personality traits.

**Validation**: Model fine-tuning and evaluation were performed with cross-validation with separate test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: Analysis of personality trait distributions revealed high neuroticism as a potential data bias issue.

**Potential Harm**: ['Over-representation of certain personality traits due to dataset sourcing.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All journal entries used were publicly available and anonymized to protect user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
