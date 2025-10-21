# Reasoning Beyond Labels: Measuring LLM Sentiment in Low-Resource, Culturally Nuanced Contexts

## 📊 Benchmark Details

**Name**: Reasoning Beyond Labels: Measuring LLM Sentiment in Low-Resource, Culturally Nuanced Contexts

**Overview**: This paper presents a diagnostic framework for evaluating how large language models (LLMs) reason about sentiment in culturally nuanced and informal WhatsApp messages. The study operationalizes sentiment analysis as a context-dependent, culturally embedded construct, utilizing human-annotated data and synthetic sentiment-flipped examples for evaluations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Swahili

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM reasoning about sentiment in informal, culturally nuanced contexts and to propose a framework for more accurate sentiment analysis in low-resource settings.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Sentiment Analysis

**Limitations**: While this diagnostic framework offers a deeper lens into sentiment reasoning, several limitations remain, including challenges in operationalizing sentiment and preserving context in synthetic data.

## 💾 Data

**Source**: WhatsApp Chat Dataset originally collected by Karusala et al. (2021) and annotated by Mondal et al. (2021)

**Size**: 6,197 messages

**Format**: text

**Annotation**: Using a structured annotation protocol focused on culturally grounded sentiment, interpretive ambiguity, and context-specific expression by trained annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-as-judge evaluation
- Counterfactual generation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are computed based on the model’s outputs for sentiment classification and explanation quality.

**Interpretation**: Higher scores indicate better model performance in terms of explainability and accuracy regarding sentiment classification.

**Baseline Results**: Top-performing models achieved average F1 scores around 0.90 or higher with varying confidence and coverage across datasets.

**Validation**: The evaluation methods were validated through structured protocols involving human annotators rating sentiment and explanation quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The dataset includes youth from Nairobi living with HIV, with cultural and contextual considerations emphasized in annotation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data were anonymized and collected with consent under prior research protocols, with all identifying information removed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided consent for their messages to be used in research.

**Compliance With Regulations**: The study complied with ethical research standards, as mentioned in prior documentation.
