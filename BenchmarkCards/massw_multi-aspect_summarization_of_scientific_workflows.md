# MASSW (Multi-Aspect Summarization of Scientific Workflows)

## 📊 Benchmark Details

**Name**: MASSW (Multi-Aspect Summarization of Scientific Workflows)

**Overview**: MASSW is a comprehensive text dataset focused on Multi-Aspect Summarization of Scientific Workflows, including structured summaries extracted from over 152,000 peer-reviewed publications. The dataset is designed to enable various machine-learning tasks that predict and recommend steps in scientific research workflows.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/xingjian-zhang/massw)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured dataset that facilitates the exploration and optimization of scientific workflows through AI-assisted methods.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Workflow Prediction
- Title Prediction

**Limitations**: The dataset is limited to AI-related computer science publications and may not generalize across other domains.

## 💾 Data

**Source**: Automated extraction from over 152,000 peer-reviewed publications collected from 17 leading computer science conferences.

**Size**: 152,000 publications

**Format**: TSV

**Annotation**: Automatically generated through Large Language Models (LLMs) with validation against human annotations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BLEU Score
- ROUGE-L
- BERTScore

**Calculation**: Metrics are calculated by comparing automated summaries to human-generated reference summaries.

**Interpretation**: Higher scores in BLEU and ROUGE indicate better alignment with human summaries.

**Baseline Results**: GPT-4 outperformed other models in semantic evaluation metrics.

**Validation**: The dataset's summaries were validated against human annotations to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: None explicitly mentioned in the paper.

**Potential Harm**: Potential biases introduced by the selection of top-tier conferences in the dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open Academic Graph (OAG) dataset is publicly released under the ODC-BY license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
