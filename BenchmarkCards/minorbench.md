# MinorBench

## 📊 Benchmark Details

**Name**: MinorBench

**Overview**: MinorBench is an open-source benchmark designed to evaluate LLMs on their ability to refuse unsafe or inappropriate queries from children.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- AILuminate
- AIR-Bench

**Resources**:
- [Resource](https://huggingface.co/datasets/govtech/MinorBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess large language models (LLMs) on handling age-inappropriate questions and to provide a benchmark for testing AI moderation systems in educational contexts.

**Target Audience**:
- AI Researchers
- Educators
- Child Safety Advocates

**Tasks**:
- Safety Assessment
- Content Moderation

**Limitations**: MinorBench is relatively small compared to other benchmarks, but is designed for high-quality datasets.

## 💾 Data

**Source**: Curated dataset of 299 user queries categorized by content-based risks for children.

**Size**: 299 user queries

**Format**: N/A

**Annotation**: Manually curated with a focus on queries children may ask regarding unsafe or inappropriate content.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual curation

**Metrics**:
- Refusal Rate

**Calculation**: Refusal Rate = (Number of refused prompts / Number of prompts in the category) × 100.

**Interpretation**: Higher refusal rates indicate stricter adherence to content-safety guidelines for child-unsafe requests.

**Baseline Results**: Results vary significantly by model and system prompt variations, with some models achieving over 90% refusal rates.

**Validation**: Testing was conducted across various prompts using six different LLMs under four variations of system prompts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Content Safety
- Child-Specific Risks

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
