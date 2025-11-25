# AIDBench

## 📊 Benchmark Details

**Name**: AIDBench

**Overview**: AIDBench is a comprehensive benchmark designed to evaluate the authorship identification capabilities of large language models (LLMs). It incorporates several author identification datasets, including emails, blogs, reviews, articles, and research papers, to systematically study privacy risks associated with LLMs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To assess and demonstrate the potential privacy risks posed by large language models in identifying authorship of anonymous texts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Privacy Experts

**Tasks**:
- Authorship Identification

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark includes new and existing datasets such as research papers from arXiv, the Enron email dataset, blogs, IMDb reviews, and articles from The Guardian.

**Size**: 24,095 papers in the research dataset; approximately 500,000 emails in the Enron dataset; 19,320 blog posts; 3,100 IMDb reviews; 650 articles from The Guardian.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- One-to-one authorship identification
- One-to-many authorship identification
- Retrieval-Augmented Generation (RAG)-based evaluation

**Metrics**:
- Precision
- Recall
- Rank@x

**Calculation**: Metrics are calculated based on the proportion of correct identifications by LLMs evaluating candidate texts against known authorship.

**Interpretation**: High precision and recall indicate effective authorship identification capability, while lower rates highlight challenges in distinguishing authorship.

**Baseline Results**: N/A

**Validation**: The benchmark includes rigorous evaluation using multiple datasets under varied contexts and exploration of models' capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to detect potential harmful impacts on user privacy through authorship identification.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
