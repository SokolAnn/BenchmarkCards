# SynthTRIPs (Synthetic Travel Queries for Personalized Recommenders)

## 📊 Benchmark Details

**Name**: SynthTRIPs (Synthetic Travel Queries for Personalized Recommenders)

**Overview**: SynthTRIPs is a novel framework for generating synthetic travel queries using Large Language Models (LLMs), grounded in a curated knowledge base. It aims to enhance personalized travel recommendations by incorporating user preferences and sustainability factors.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Tourism

**Languages**:
- English

**Resources**:
- [Resource](https://bit.ly/synthTRIPs)
- [GitHub Repository](https://github.com/baturin/wikivoyage-listings)

## 🎯 Purpose and Intended Users

**Goal**: To produce a synthetic dataset of travel queries that captures realistic travel constraints, aiding in the development of personalized travel recommender systems.

**Target Audience**:
- ML Researchers
- Domain Experts
- Recommender System Developers

**Tasks**:
- Text Generation
- Query Generation

**Limitations**: The potential for subjective persona interpretation and a trade-off between personalization and groundedness.

## 💾 Data

**Source**: Curated knowledge base and synthesized queries from various travel-related datasets.

**Size**: 4,604 queries

**Format**: JSON

**Annotation**: Automatically generated queries using LLMs with validation from human experts.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics
- Human expert evaluations

**Metrics**:
- Groundedness
- Persona Alignment
- Sustainability Compliance
- Diversity

**Calculation**: Metrics are derived from comparisons between generated queries and target features stipulated in travel filters.

**Interpretation**: High groundedness scores indicate alignment with travel filters and context; high persona alignment shows coherence with user personas.

**Baseline Results**: Performance is benchmarked against existing datasets and evaluated through expert judgments.

**Validation**: Cross-validated through expert assessments and automated LLM evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Synthetic persona data may lack diversity and realism, impacting fairness in recommendations.

**Potential Harm**: Potential for misalignment between user queries and recommended destinations, especially regarding popularity bias.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
