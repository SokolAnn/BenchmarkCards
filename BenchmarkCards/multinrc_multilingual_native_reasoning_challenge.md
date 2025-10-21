# MultiNRC (Multilingual Native Reasoning Challenge)

## 📊 Benchmark Details

**Name**: MultiNRC (Multilingual Native Reasoning Challenge)

**Overview**: MultiNRC is a benchmark designed to assess LLMs on more than 1,000 native, linguistic and culturally grounded reasoning questions written by native speakers in French, Spanish, and Chinese. It covers four core reasoning categories: language-specific linguistic reasoning, wordplay & riddles, cultural/tradition reasoning, and math reasoning with cultural relevance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- French
- Spanish
- Chinese

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- HellaSwag

**Resources**:
- [Resource](https://huggingface.co/datasets/ScaleAI/MultiNRC)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multilingual abilities of LLMs through linguistically and culturally-nuanced reasoning questions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions were created by native speakers for each target language, supplemented with automatic evaluation.

**Size**: 1,055 examples

**Format**: JSON

**Annotation**: Manual annotation by native speakers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on alignment with human judgment.

**Interpretation**: Scores above 50% indicate reasonable performance, while lower scores highlight significant challenges for the models.

**Validation**: Data was validated through review by native speakers who assessed the quality and difficulty of questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
