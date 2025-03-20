# DefAn: Definitive Answer Dataset for LLMs

## 📊 Benchmark Details

**Name**: DefAn: Definitive Answer Dataset for LLMs

**Overview**: A comprehensive benchmark dataset to evaluate hallucination in large language models (LLMs) with over 75,000 prompts across eight domains.

**Data Type**: Text

**Domains**:
- Sports
- Census Australia
- Nobel Prize
- Entertainment
- World Organizations
- QS Ranking
- Conference Venue
- Math

**Languages**:
- English

**Similar Benchmarks**:
- FELM
- HaluEval
- HaluEval-Wild

**Resources**:
- [GitHub Repository](https://github.com/ashikiut/DefAn)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the hallucination in LLMs and measure their factual accuracy, faithfulness to prompts, and response consistency.

**Target Audience**:
- Researchers
- AI developers
- Data scientists

**Tasks**:
- Evaluate LLMs for hallucination
- Assess factuality and consistency of LLM responses

**Limitations**: N/A

**Out of Scope Uses**:
- General sentiment analysis
- Non-factual question answering

## 💾 Data

**Source**: Official publications and academic sources

**Size**: Over 75,000 samples

**Format**: CSV and JSON

**Annotation**: Manually curated and checked by human experts

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation for initial annotation

**Metrics**:
- Factual Hallucination Rate (FCH)
- Prompt Misalignment Hallucination Rate (PMH)
- Response Consistency (RC)

**Calculation**: Metrics calculated based on comparison with reference answers and prompts.

**Interpretation**: Higher rates indicate more hallucination and less adherence to prompts.

**Baseline Results**: N/A

**Validation**: Validation performed by comparing output to expected answers and measuring coherence across paraphrases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Factual accuracy
- Prompt fidelity
- Response consistency

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset sourced from publicly available information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
