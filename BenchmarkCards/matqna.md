# MatQnA

## 📊 Benchmark Details

**Name**: MatQnA

**Overview**: MatQnA is the first multi-modal benchmark dataset specifically designed for material characterization techniques, including ten mainstream characterization methods. It constructs high-quality question-answer pairs through a hybrid approach combining LLMs and human validation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Materials Science

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/richardhzgg/matQnA)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate and enhance the domain expertise of large language models in materials characterization and analysis.

**Target Audience**:
- ML Researchers
- Materials Scientists
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark focuses primarily on objective questions and may not fully represent complex reasoning tasks in real-world materials science workflows.

## 💾 Data

**Source**: Curated from over 400 peer-reviewed journal articles published between late 2024 and early 2025.

**Size**: 4,968 questions

**Format**: Parquet

**Annotation**: Hybrid approach combining model-assisted generation using OpenAI’s GPT-4.1 API with manual verification by experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is measured by analyzing the percentage of correct responses to question-answer pairs across evaluated models.

**Interpretation**: Higher accuracy indicates better performance of models in interpreting materials science data.

**Validation**: A two-stage human validation process was implemented to ensure the accuracy and relevance of generated question-answer pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Data Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
