# MoCa (Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks)

## 📊 Benchmark Details

**Name**: MoCa (Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks)

**Overview**: We collected a dataset of causal and moral judgment tasks from 24 cognitive science papers and developed a system to annotate each story with the factors they investigated. Using this dataset, we test whether large language models (LLMs) make causal and moral judgments about text-based scenarios that align with those of human participants.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Psychology

**Languages**:
- English

**Similar Benchmarks**:
- Moral Machine Dataset

**Resources**:
- [GitHub Repository](https://github.com/cicl-stanford/moca)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the alignment of large language models with human judgments regarding causal and moral scenarios, utilizing insights from cognitive science.

**Target Audience**:
- ML Researchers
- Psychologists
- Ethicists
- AI Developers

**Tasks**:
- Causal Judgment
- Moral Judgment

**Limitations**: The dataset focuses on specific aspects of alignment and may not generalize to broader contexts of moral reasoning.

## 💾 Data

**Source**: Collected and annotated stories from 24 cognitive science papers.

**Size**: 5,150 human responses

**Format**: text

**Annotation**: Annotated by experts with the factors investigated in each story.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Statistical analysis

**Metrics**:
- Accuracy
- Average Marginal Component Effect (AMCE)

**Calculation**: AMCE is computed to reveal implicit tendencies for each factor from human and LLM judgments.

**Interpretation**: Higher alignment indicates better agreement between model outputs and human judgments.

**Validation**: Cross-validation with human responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset includes demographic variation in human responses but does not analyze demographic bias directly.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Participants gave consent through a notification form at the beginning of each study.

**Compliance With Regulations**: IRB approval obtained for the data collection process.
