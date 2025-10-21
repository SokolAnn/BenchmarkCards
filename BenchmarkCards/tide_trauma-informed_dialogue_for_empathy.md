# TIDE (Trauma-Informed Dialogue for Empathy)

## 📊 Benchmark Details

**Name**: TIDE (Trauma-Informed Dialogue for Empathy)

**Overview**: TIDE is a novel dataset comprising 10,000 two-turn conversations across 500 diverse, clinically-grounded PTSD personas. It is designed to assess and improve the empathetic capabilities of small language models in trauma-informed contexts.

**Data Type**: dialogue pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/yenopoya/TIDE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate whether small language models can generate emotionally attuned, trauma-sensitive responses in therapeutic contexts.

**Target Audience**:
- ML Researchers
- Mental Health Professionals

**Tasks**:
- Empathetic Response Generation

**Limitations**: The synthetic TIDE dataset, while clinically validated, is derived from a single frontier model (Claude Sonnet 3.5) and may not capture the full complexity of real-world interactions.

## 💾 Data

**Source**: 10,000 two-turn dialogues derived from 500 diverse client personas, each grounded in characteristics associated with PTSD, created and clinically reviewed by psychologists.

**Size**: 10,000 dialogues

**Format**: CSV

**Annotation**: Clinically reviewed by co-author psychologists specializing in PTSD to ensure emotional plausibility and trauma sensitivity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Cosine Similarity
- BERTScore
- ROUGE-L
- Meteor

**Calculation**: Metrics are calculated based on the similarity between generated responses and ground-truth reference responses.

**Interpretation**: Higher scores indicate better alignment with expected empathetic responses.

**Baseline Results**: Claude Sonnet 3.5 serves as the gold standard reference, consistently outperformed all other small models.

**Validation**: Empathy ratings were collected through a controlled human evaluation study.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: Participants varied in age, sex, race, and education, affecting perceptions of empathy.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data is designed with ethical guidelines in mind, focusing on trauma-informed practices.

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
