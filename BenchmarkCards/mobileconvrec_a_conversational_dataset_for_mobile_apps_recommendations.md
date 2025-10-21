# MobileConvRec (A Conversational Dataset for Mobile Apps Recommendations)

## 📊 Benchmark Details

**Name**: MobileConvRec (A Conversational Dataset for Mobile Apps Recommendations)

**Overview**: MobileConvRec is a dataset tailored for conversational mobile app recommendations. It integrates users' historical interactions within multi-turn dialogs, providing a holistic view of user preferences with over 12.2K multi-turn dialogs involving 11.8K unique users across 1,730 apps spanning 45 categories.

**Data Type**: multi-turn conversations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MobileRec

**Resources**:
- [Resource](https://huggingface.co/datasets/recmeapp/MobileConvRec)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in conversational mobile app recommendations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Conversational Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: User interactions with mobile apps on the Google Play store, captured in the MobileRec dataset.

**Size**: 12,200 conversations

**Format**: JSON

**Annotation**: Automatically generated through simulation of dialogues derived from real user interactions.

## 🔬 Methodology

**Methods**:
- Comparative study with pre-trained large language models
- Simulation of user-system dialogues

**Metrics**:
- Hit@K
- NDCG@K
- BLEU Score

**Calculation**: Metrics calculated based on success in generating app names, ranking candidate apps, and evaluating response generation.

**Interpretation**: Higher metrics indicate better model performance in generating recommendations and responses.

**Baseline Results**: Models like GPT-2 and Flan-T5 were evaluated with various inputs showing significant improvements.

**Validation**: Data partitioned into training, validation, and testing sets based on the date of interaction.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential biases inherent in developer-provided information may affect user trust.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: UIDs anonymize user identities.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
