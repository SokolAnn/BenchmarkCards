# ChatbotManip (Chatbot Manipulation Dataset)

## 📊 Benchmark Details

**Name**: ChatbotManip (Chatbot Manipulation Dataset)

**Overview**: This paper introduces ChatbotManip, a novel dataset for studying manipulation in Chatbots. It contains simulated generated conversations between a chatbot and a (simulated) user, where the chatbot is explicitly asked to showcase manipulation tactics, persuade the user towards some goal, or simply be helpful. Each conversation is annotated by human annotators for both general manipulation and specific manipulation tactics.

**Data Type**: conversational text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MentalManip

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To investigate and monitor manipulative behavior in chatbot interactions.

**Target Audience**:
- AI Safety Researchers
- NLP Researchers
- Technology Developers

**Tasks**:
- Manipulation Detection
- Text Classification

**Limitations**: The dataset relies on AI-generated rather than real human-AI interactions, potentially missing important aspects of real-world manipulation.

## 💾 Data

**Source**: Simulated conversations generated using various LLMs (GPT-4, Gemini, Llama).

**Size**: 553 conversations

**Format**: N/A

**Annotation**: Conversations were annotated by 7 human participants using a 7-point Likert scale for perceived manipulation.

## 🔬 Methodology

**Methods**:
- Human annotation
- Text classification

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics were calculated based on annotator agreement and classification performance of the models.

**Interpretation**: Higher scores indicate better models in detecting manipulation in conversational AI.

**Baseline Results**: Fine-tuned BERT+BiLSTM achieved comparable performance to larger models like Gemini.

**Validation**: The dataset includes inter-annotator agreement metrics to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Participant demographics are provided in the appendix, showing a diverse respondent group involved in the annotation process.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: N/A - Not discussed.

**Data Licensing**: N/A - Not specified.

**Consent Procedures**: N/A - Not discussed.

**Compliance With Regulations**: N/A - Not discussed.
