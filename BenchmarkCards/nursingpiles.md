# NursingPiles

## 📊 Benchmark Details

**Name**: NursingPiles

**Overview**: The paper introduces a novel Chinese nursing dataset called 'NursingPiles' aimed at enhancing large language model performance in nursing and elderly care tasks and establishes a benchmark test set for evaluating nursing knowledge and skills.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To develop AI-driven solutions tailored to nursing and elderly care, utilizing large language models for patient monitoring and personalized care.

**Target Audience**:
- NLP Researchers
- Healthcare Practitioners
- Nursing Professionals

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: The dataset is primarily Chinese-focused, limiting broader applicability across languages and cultures.

## 💾 Data

**Source**: Developed from textbooks, manuals, legal documents, and research papers.

**Size**: 1,000,000 question-answer pairs

**Format**: Text in markdown format, JSON

**Annotation**: Automatically annotated through data processing pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy

**Calculation**: Metrics were calculated based on evaluation of models through established nursing exam questions.

**Interpretation**: Higher scores indicate better model performance in nursing knowledge assessments.

**Baseline Results**: GLM4-Chat 9B + IPT + SFT achieved Precision of 86.78%, Recall of 85.65%, F1-score of 86.21%, and Accuracy of 58.9%.

**Validation**: The benchmark was validated through tests against authoritative nursing exam questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized to protect participant confidentiality.

**Data Licensing**: The dataset is released under an open-source license (e.g., CC BY-NC 4.0) for non-commercial research.

**Consent Procedures**: Informed consent was obtained from research team members for data collection.

**Compliance With Regulations**: The research complies with applicable laws and regulations.
