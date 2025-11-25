# RAD-Bench (Retrieval Augmented Dialogue Benchmark)

## 📊 Benchmark Details

**Name**: RAD-Bench (Retrieval Augmented Dialogue Benchmark)

**Overview**: RAD-Bench is a comprehensive benchmark designed to evaluate Large Language Models' capabilities in multi-turn dialogues following retrievals, focusing on Retrieval Synthesis and Retrieval Reasoning across various practical scenarios.

**Data Type**: multi-turn dialogue samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mtkresearch/RAD-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the retrieval capabilities of large language models in multi-turn dialogue scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Knowledge Query Answering
- Knowledge Summarization
- Chain of Reasoning
- Planning

**Limitations**: N/A

## 💾 Data

**Source**: Curated from real-world dialogue data for multi-turn interaction scenarios.

**Size**: 89 multi-turn question samples, 267 turns total

**Format**: JSON

**Annotation**: Manual inspection and scoring through the LLM-as-a-Judge framework.

## 🔬 Methodology

**Methods**:
- LLM-as-a-Judge framework
- Automated scoring
- Human evaluation

**Metrics**:
- Accuracy
- Consistency
- Coherence
- Informativeness

**Calculation**: Metrics are derived from evaluating responses based on scenario-specific criteria.

**Interpretation**: Higher scores indicate stronger performance in effectively utilizing retrieved context for dialogue.

**Baseline Results**: Comparison of evaluated models across scenarios using Elo ratings.

**Validation**: Evaluated against multiple prevalent language models to assess benchmark effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential for model bias if scenarios are not representative of diverse dialogue contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
