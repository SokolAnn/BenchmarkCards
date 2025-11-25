# KGQuiz

## 📊 Benchmark Details

**Name**: KGQuiz

**Overview**: KGQuiz is a scalable framework to comprehensively investigate the knowledge generalization abilities of large language models across three knowledge domains and five tasks with increasing complexity.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/leopoldwhite/KGQuiz)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the knowledge abilities of large language models across varying complexity of tasks and knowledge domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- True-or-False
- Multiple Choice
- Blank Filling
- Factual Editing
- Open-Ended Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated from triplet-based knowledge graphs from three diverse domains: commonsense, encyclopedic, and biomedical.

**Size**: 41,000 questions

**Format**: N/A

**Annotation**: Automatically generated questions from knowledge graphs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Semantic Match

**Calculation**: Metrics are calculated based on model outputs compared to the ground truth defined in the knowledge graphs.

**Interpretation**: Higher scores indicate better performance in knowledge retrieval and generalization tasks.

**Baseline Results**: N/A

**Validation**: Validation involved extensive evaluations of model outputs against generated knowledge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy concerns may arise from sensitive information contained in knowledge graphs.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
