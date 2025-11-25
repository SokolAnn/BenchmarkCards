# Emo Pillarsemoπ

## 📊 Benchmark Details

**Name**: Emo Pillarsemoπ

**Overview**: A dataset created for fine-grained context-aware and context-less emotion classification, synthesized using LLMs and focused on 28 emotion classes. It includes 100K contextual and 300K context-less examples.

**Data Type**: emotional utterances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GoEmotions
- ISEAR
- IEMOCAP
- EmoContext

**Resources**:
- [GitHub Repository](https://github.com/alex-shvets/EmoPillars)
- [Resource](https://huggingface.co/datasets/alex-shvets/EmoPillars)
- [Resource](https://huggingface.co/collections/alex-shvets/EmoPillars)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for emotion recognition that accounts for context in utterances, enhancing the capabilities of NLP models in detecting emotions.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Emotion Classification

**Limitations**: N/A

## 💾 Data

**Source**: Synthesis from a corpus of narratives with LLMs

**Size**: 400,000 examples

**Format**: JSONL

**Annotation**: Utilizes soft labeling for emotional intensity, along with context-aware generation techniques.

## 🔬 Methodology

**Methods**:
- LLM-based generation
- Human evaluation
- Statistical analysis

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on classification results on validation datasets.

**Interpretation**: Higher scores indicate better performance in identifying emotions, particularly in context-aware scenarios.

**Validation**: Statistical analysis and human evaluation validate the success of utterance diversification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy
- **Privacy**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
