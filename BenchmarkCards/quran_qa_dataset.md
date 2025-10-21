# Quran QA Dataset

## 📊 Benchmark Details

**Name**: Quran QA Dataset

**Overview**: This work addresses the limitations of the original Qur'an QA dataset by expanding it from 251 to 1895 questions, diversifying and reformulating the questions to improve the question-answering system for the Holy Qur'an.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/ImruQays/Quran-Classical-Arabic-English-Parallel-texts)
- [Resource](https://www.kaggle.com/datasets/mobassir/quranqa/code)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the performance of question-answering systems for the Holy Qur'an by expanding the dataset and fine-tuning language models.

**Target Audience**:
- ML Researchers
- Islamic Studies Scholars
- NLP Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Original Quran QA dataset and additional sources including Kaggle datasets and Arabic Tafseer texts.

**Size**: 1,895 questions

**Format**: N/A

**Annotation**: Generated through question rephrasing and categorization.

## 🔬 Methodology

**Methods**:
- Fine-tuning
- Transfer learning
- Ensemble learning

**Metrics**:
- Mean Average Precision (MAP)
- Mean Reciprocal Rank (MRR)
- Recall

**Calculation**: Metrics are calculated based on the models' performance on retrieval tasks against baseline metrics.

**Interpretation**: Higher MAP and MRR scores indicate better retrieval accuracy and ranking.

**Baseline Results**: MAP@10 improved from 0.22 to 0.36; MRR improved from 0.37 to 0.59.

**Validation**: Extensive experiments conducted to assess model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
