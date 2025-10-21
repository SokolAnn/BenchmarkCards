# Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning

## 📊 Benchmark Details

**Name**: Aya Dataset: An Open-Access Collection for Multilingual Instruction Tuning

**Overview**: We create the largest human-annotated multilingual instruction fine-tuning dataset to date, consisting of over 204K instances that cover 65 languages. We include a data card for the AyaDataset.

**Data Type**: instruction-following pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Arabic
- Hindi
- Tamil
- Turkish
- Bengali
- Russian
- Malay
- Indonesian
- Swahili
- Zulu
- Ukrainian
- French
- Portuguese
- Japanese
- German

**Similar Benchmarks**:
- xP3
- FLAN
- Dolly

**Resources**:
- [Resource](https://huggingface.co/datasets/CohereForAI/aya_dataset)

## 🎯 Purpose and Intended Users

**Goal**: To bridge the language gap by building a human-curated instruction-following dataset spanning 65 languages.

**Target Audience**:
- Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering
- Natural Language Generation

**Limitations**: There is still only a tiny fraction of the world’s linguistic diversity covered.

## 💾 Data

**Source**: Crowd-sourced through volunteer annotations

**Size**: 204,114 instances

**Format**: JSON

**Annotation**: Human-annotations

## 🔬 Methodology

**Methods**:
- Crowd-sourced annotations

**Metrics**:
- Approval Ratio

**Calculation**: The average approval ratio as T+/T, where T+ is the total number of thumbs up and T is the total number of votes.

**Interpretation**: Average approval ratio of 1.0 indicates perfect quality.

**Baseline Results**: N/A

**Validation**: The dataset was validated through peer review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**

**Demographic Analysis**: The contributor pool is diverse in terms of geography, age, and dilogue.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache 2.0

**Consent Procedures**: Participants volunteered for contribution.

**Compliance With Regulations**: Not Applicable
