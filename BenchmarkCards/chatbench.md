# ChatBench

## 📊 Benchmark Details

**Name**: ChatBench

**Overview**: ChatBench is a new dataset comprising AI-alone, user-alone, and user-AI data for 396 questions, including 144K answers and 7,336 user-AI conversations, converted from the MMLU benchmark to facilitate human-AI evaluation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [Resource](https://huggingface.co/datasets/microsoft/ChatBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how humans interact with LLMs and how these interactions change evaluation conclusions compared to traditional AI-alone benchmarks.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: ChatBench is compiled from a user study involving human interactions with AI and data from MMLU.

**Size**: 144,029 total answers

**Format**: JSON

**Annotation**: Manually verified user interactions and AI responses.

## 🔬 Methodology

**Methods**:
- User study
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed as the fraction of correct answers over total answers.

**Interpretation**: A higher accuracy indicates better model performance in user-AI interactions compared to individual performances.

**Baseline Results**: N/A

**Validation**: User data was validated through attention checks and filtering criteria for quality assurance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Exposing personal information

**Demographic Analysis**: Data includes various user demographics for a representative sampling.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was anonymized to protect participant privacy, with personal information checked and removed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all participants.

**Compliance With Regulations**: The study complies with GDPR regulations regarding participant data.
