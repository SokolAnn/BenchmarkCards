# User eXperience Perception Insights Dataset (UXPID)

## 📊 Benchmark Details

**Name**: User eXperience Perception Insights Dataset (UXPID)

**Overview**: The User eXperience Perception Insights Dataset (UXPID) is a dataset consisting of 7130 artificially synthesized and anonymized user feedback branches extracted from a public industrial automation forum, designed to facilitate research in user requirements and user experience (UX) analysis.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://zenodo.org/records/17091284)
- [GitHub Repository](https://github.com/MikhailKulyabin/UXPID)

## 🎯 Purpose and Intended Users

**Goal**: To provide a valuable resource for advancing natural language processing (NLP) methods within industrial product support and software engineering domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Sentiment Analysis
- Requirements Extraction

**Limitations**: N/A

## 💾 Data

**Source**: User comments extracted from a company-operated forum dedicated to automation product hardware and software components.

**Size**: 7130 branches, over 36,000 comments

**Format**: JSON

**Annotation**: Automatically generated insights through Large Language Models (LLMs) validated by human assessment.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated through classification tasks using the DistilBERT model as a baseline.

**Interpretation**: Higher metrics indicate better model performance in classifying user experience feedback.

**Baseline Results**: Predictive metrics for topic classification tasks yielded results with AUC scores indicating varying levels of success across scenarios.

**Validation**: Technical validation conducted through classification experiments using the DistilBERT model.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Bias

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes anonymization techniques to protect user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
