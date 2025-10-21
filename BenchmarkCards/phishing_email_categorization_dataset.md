# Phishing Email Categorization Dataset

## 📊 Benchmark Details

**Name**: Phishing Email Categorization Dataset

**Overview**: A dataset of human categorizations of emails as either dangerous (phishing) or safe (ham), introduced to evaluate the Instance-Based Individualized Similarity (IBIS) metric, which integrates cognitive models and LLM embeddings.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://osf.io/wbg3r/)

## 🎯 Purpose and Intended Users

**Goal**: To provide personalized metrics of subjective concepts that can determine the similarity between sets of text, particularly in educational and recommendation settings.

**Target Audience**:
- Researchers in NLP
- Educational Technologists
- Cognitive Scientists

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Human categorizations of emails collected from an experiment involving 433 participants, assessing emails authored by human cybersecurity experts and GPT-4.

**Size**: 39,230 human judgments

**Format**: CSV

**Annotation**: Manual annotation by human participants

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Cosine Similarity
- Semantic Similarity
- Individualized Similarity (IBIS)

**Calculation**: Similarity is calculated using human judgments of categorization along with metrics based on embeddings and cognitive models.

**Interpretation**: Higher similarity scores indicate greater agreement with human subjective similarity measures.

**Validation**: Comparison with existing similarity metrics to validate the effectiveness of the IBIS method.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis included demographic factors of participant responses.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided informed consent prior to participating in the study.

**Compliance With Regulations**: The study was approved by the Carnegie Mellon University Institutional Review Board.
