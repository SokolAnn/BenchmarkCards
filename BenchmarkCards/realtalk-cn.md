# RealTalk-CN

## 📊 Benchmark Details

**Name**: RealTalk-CN

**Overview**: RealTalk-CN is the first Chinese multi-turn, multi-domain speech-text dual-modal task-oriented dialogue dataset, comprising 5.4k dialogues (60K utterances, 150 hours) with paired speech-text annotations. It captures diverse dialogue scenarios with annotated spontaneous speech disfluencies, designed to evaluate the robustness of speech-based language models.

**Data Type**: dialogue pairs with speech and text annotations

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- SpokenWOZ

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for evaluating speech-based language models in task-oriented dialogue systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task-Oriented Dialogue Modeling
- Cross-Modal Interaction Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Real human-to-human speech conversations collected and annotated to reflect natural spoken language characteristics.

**Size**: 5,400 dialogues with 60,000 utterances and 150 hours of audio

**Format**: N/A

**Annotation**: Annotated for spontaneous speech disfluencies and dialogue states (slots, intents).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics based on GPT-4

**Metrics**:
- Accuracy
- PANDA score
- F1 Score
- Joint Goal Accuracy (JGA)

**Calculation**: Metrics calculated using GPT-4-based evaluation methods, focusing on dialogue task performance.

**Interpretation**: Evaluation metrics reveal the effectiveness of speech-based LLMs in handling complex dialogue tasks.

**Baseline Results**: N/A

**Validation**: Extensive evaluations across multiple models with a focus on robustness to disfluencies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset includes diverse speaker characteristics to analyze the impact of age and regional accents.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures included ensuring participant anonymity during data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Full consent obtained from all participants involved in data collection.

**Compliance With Regulations**: Not Applicable
