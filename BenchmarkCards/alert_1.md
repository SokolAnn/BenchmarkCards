# ALERT

## 📊 Benchmark Details

**Name**: ALERT

**Overview**: ALERT is a large-scale benchmark to assess the safety of Large Language Models (LLMs) through red teaming methodologies. It consists of more than 45k instructions categorized using a fine-grained risk taxonomy designed to identify vulnerabilities and enhance the overall safety of language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Babelscape/ALERT)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for the safety assessment of Large Language Models (LLMs) based on a detailed risk taxonomy.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Red Teaming Assessment

**Limitations**: ALERT exclusively focuses on harmfulness, and does not assess evasive or unhelpful responses to harmless prompts.

## 💾 Data

**Source**: The dataset is derived from a red-team-attempts dataset and includes additional generated prompts based on a fine-grained safety risk taxonomy.

**Size**: 45,000 prompts

**Format**: N/A

**Annotation**: Prompts were categorized using keyword-matching and zero-shot classification strategies, followed by manual filtering.

## 🔬 Methodology

**Methods**:
- Red Teaming
- Automated metrics

**Metrics**:
- Safety scores based on prompt evaluations

**Calculation**: Safety scores are computed as the ratio of safe prompts to total prompts in each category, leading to overall scores across all categories.

**Interpretation**: A model is considered safe when outputs are safe at least 99% of the time.

**Baseline Results**: Evaluated 10 popular LLMs such as GPT-3.5, GPT-4, Llama 2, etc.

**Validation**: Models were validated using an auxiliary LLM for classifying responses as safe or unsafe.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Promotion of harmful behaviors', 'Encouragement of illegal activities']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
