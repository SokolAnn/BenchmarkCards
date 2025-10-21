# RABAK BENCH (Localized Multilingual Safety Benchmark)

## 📊 Benchmark Details

**Name**: RABAK BENCH (Localized Multilingual Safety Benchmark)

**Overview**: RABAK BENCH is a new multilingual safety benchmark localized to Singapore's unique linguistic context, covering Singlish, Chinese, Malay, and Tamil. It comprises over 5,000 safety-labeled examples across four languages and six fine-grained safety categories with severity levels.

**Data Type**: safety-labeled examples

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Malay
- Tamil

**Resources**:
- [Resource](https://huggingface.co/datasets/govtech/RabakBench)
- [GitHub Repository](https://github.com/govtech-responsibleai/RabakBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust safety evaluation in Southeast Asian multilingual settings and offer a reproducible framework for constructing localized safety datasets in low-resource environments.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Safety Evaluation

**Limitations**: The cultural specificity may limit generalizability to other regions without adaptation.

## 💾 Data

**Source**: Collected from real-world web content enriched with LLM-driven red teaming and translations verified by native speakers.

**Size**: 5,364 examples

**Format**: JSON

**Annotation**: Semi-automated multi-label safety annotation using majority-voted LLM labelers aligned with human judgments.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on the performance of guardrail classifiers as evaluated on the RABAK BENCH dataset.

**Interpretation**: A higher F1 Score indicates better safety classification performance.

**Validation**: Evaluated against 11 popular open-source and closed-source guardrail classifiers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Evaluation includes demographic factors across multilingual contexts.

**Potential Harm**: The benchmark aims to address safety risks in multilingual settings, particularly in low-resource languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data was sourced from public forums or generated via LLM red-teaming and reviewed for coherence and cultural appropriateness.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
