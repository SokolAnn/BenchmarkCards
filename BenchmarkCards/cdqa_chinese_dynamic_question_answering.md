# CDQA (Chinese Dynamic Question Answering)

## 📊 Benchmark Details

**Name**: CDQA (Chinese Dynamic Question Answering)

**Overview**: CDQA is a Chinese Dynamic QA benchmark containing question-answer pairs related to the latest news on the Chinese Internet, aimed at improving the capabilities of Large Language Models (LLMs) in answering dynamic questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Alibaba-NLP/CDQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the ability of Chinese LLMs to answer dynamic questions based on the latest factual knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset is focused solely on the Chinese language.

## 💾 Data

**Source**: Automatically generated queries from the latest Chinese news and manually labeled by crowd-sourced workers.

**Size**: 1,339 question-answer pairs

**Format**: N/A

**Annotation**: Semi-automated with human verification and manual labeling.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Answer Rate

**Calculation**: F1-recall calculated as the ratio of common tokens between model-generated responses and ground truth; answer rate is the ratio of effectively answered questions to total questions.

**Interpretation**: A higher F1 Score indicates better model alignment with correct answers; a lower answer rate might indicate more hallucination.

**Baseline Results**: GPT-4 outperforms other models in F1-recall scores.

**Validation**: The benchmark is validated through evaluation on multiple Chinese LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Societal Impact
- Misuse

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on education: plagiarism
- **Misuse**: Spreading disinformation

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data collected does not contain any information that would cause moral risks such as politically sensitive or private data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Human annotators are contracted with a legal agreement and are compensated above market rates.

**Compliance With Regulations**: Not Applicable
