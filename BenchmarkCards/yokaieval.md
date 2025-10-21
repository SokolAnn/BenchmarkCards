# YokaiEval

## 📊 Benchmark Details

**Name**: YokaiEval

**Overview**: YokaiEval is a benchmark dataset designed to evaluate language models' knowledge of Japanese folktales, specifically focusing on yokai, through 809 multiple-choice questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Resources**:
- [GitHub Repository](https://github.com/CyberAgentAILab/YokaiEval)
- [Resource](https://huggingface.co/datasets/cyberagent/YokaiEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cultural awareness and knowledge of large language models about Japanese yokai in folktales.

**Target Audience**:
- ML Researchers
- Cultural Studies Scholars
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset is limited to Japanese yokai and may not represent folktales from other cultures.

## 💾 Data

**Source**: Generated from Wikipedia articles about yokai utilizing GPT-4o for question generation and verification.

**Size**: 809 questions

**Format**: JSON

**Annotation**: Generated and curated using AI-assisted methods followed by manual verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Calculated as the number of correct answers over the total number of questions.

**Interpretation**: Higher accuracy indicates better knowledge of Japanese yokai among language models. Accuracy results are compared between different types of models.

**Validation**: Performance evaluated on 31 language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
