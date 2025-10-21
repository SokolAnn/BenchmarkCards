# GraphextQA (Graph-Enhanced Question Answering)

## 📊 Benchmark Details

**Name**: GraphextQA (Graph-Enhanced Question Answering)

**Overview**: GraphextQA is an open-domain question answering dataset that includes paired graphs sourced from Wikidata, designed to evaluate the integration of graph knowledge into language models for improved answer generation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/drt/graphext-qa)
- [GitHub Repository](https://github.com/happen2me/cross-gnn)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the ability of generative models to comprehend graphs and generate accurate answers.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset has limitations regarding the naturalness of questions and answers, as many are derived from existing question patterns and may not provide conversational responses.

## 💾 Data

**Source**: Derived from Lc-QuAD 2.0 and MCWQ datasets, which are existing knowledge base question answering datasets.

**Size**: 59,964 instances

**Format**: JSON

**Annotation**: Automatically constructed graphs from SPARQL queries with natural language questions.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score
- BLEU Score

**Calculation**: Metrics are calculated based on the generated answers compared to the ground truth.

**Interpretation**: Higher EM, F1, and BLEU scores indicate better understanding and generation capabilities of the models.

**Baseline Results**: The baseline T5 model achieves EM of 65.73 and F1 of 68.26, while the CrossGNN model achieves EM of 68.11 and F1 of 70.31.

**Validation**: The dataset includes validation through baseline experiments and comparison with generative models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of the dataset revealed that many questions do not encompass a diverse range of topics and entities, potentially leading to bias.

**Potential Harm**: ['The dataset could reinforce bias in generated responses based on the predominant patterns present in the sourced datasets.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was screened for harmful content using OpenAI moderation APIs, and no harmful questions were flagged.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
