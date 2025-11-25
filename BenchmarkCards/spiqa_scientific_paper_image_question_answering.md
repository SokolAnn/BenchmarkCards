# SPIQA (Scientific Paper Image Question Answering)

## 📊 Benchmark Details

**Name**: SPIQA (Scientific Paper Image Question Answering)

**Overview**: SPIQA is the first large-scale QA dataset specifically designed to interpret complex figures and tables within the context of scientific research articles across various domains of computer science.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Robotics
- AI/ML

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/google/spiqa)
- [GitHub Repository](https://github.com/google/spiqa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale benchmark for evaluating QA systems' abilities to interpret figures and tables in scientific papers.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collection of 25,859 scientific research papers from 19 top-tier conferences in computer science published between 2018 and 2023.

**Size**: 270,194 question-answer pairs

**Format**: JSON

**Annotation**: Questions are generated using a combination of human expertise and automated models, with manual filtering to ensure quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- METEOR
- L3Score

**Calculation**: Metrics are computed based on standard evaluation techniques alongside the proposed L3Score which evaluates the semantic meaning of answers.

**Interpretation**: Higher scores indicate better understanding and reasoning capabilities in answering complex questions.

**Baseline Results**: N/A

**Validation**: Extensive experiments conducted across various multimodal models to explore their comprehension abilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution License (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
