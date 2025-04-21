# SALAD-Bench

## 📊 Benchmark Details

**Name**: SALAD-Bench

**Overview**: SALAD-Bench is a safety benchmark specifically designed for evaluating large language models (LLMs), including attack and defense methods, featuring a hierarchical taxonomy with intricate levels of categorization.

**Data Type**: Text

**Domains**:
- Representation & Toxicity Harms
- Misinformation Harms
- Information & Safety Harms
- Malicious Use
- Human Autonomy & Integrity Harms
- Socioeconomic Harms

**Languages**:
- English

**Similar Benchmarks**:
- ToxicChat
- SAFETYPROMPTS
- SafetyBench
- Do-Not-Answer
- DoAnythingNow
- AdvBench

**Resources**:
- [GitHub Repository](https://github.com/OpenSafetyLab/SALAD-BENCH)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety capabilities of large language models through a comprehensive and hierarchical benchmarking method.

**Target Audience**:
- Researchers
- Developers
- Policy makers

**Tasks**:
- Safety evaluation of LLMs
- Assessment of attack methods
- Evaluation of defense strategies

**Limitations**: None

**Out of Scope Uses**:
- Non-safety related evaluations

## 💾 Data

**Source**: Publicly available data and self-instructed data.

**Size**: 21k test samples

**Format**: JSON

**Annotation**: Automatically labeled with human verification.

## 🔬 Methodology

**Methods**:
- Hierarchical Taxonomy Definition
- Data Collection
- Question Enhancement
- MD-Judge and MCQ-Judge Evaluators

**Metrics**:
- Safety Rates
- Attack Success Rates
- Precision
- Recall
- F1 Score

**Calculation**: Utilizes various evaluators to calculate safety rates and performance metrics.

**Interpretation**: Performance results are interpreted based on the accuracy of safety evaluations across different models.

**Validation**: Human-verified against a subset of 458 questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety Threats
- Misuse Risks
- Data Exploitation

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Transparency**: Lack of training data transparency
- **Privacy**: Personal information in data

**Potential Harm**: ['Potential for harmful outputs by LLMs', 'Risk of data misuse']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures taken to mitigate risks associated with sensitive content.

**Data Licensing**: Publicly available data for benchmark development.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complied with ethical guidelines to restrict access to harmful question datasets.
