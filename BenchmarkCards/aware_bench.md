# AWARE BENCH

## 📊 Benchmark Details

**Name**: AWARE BENCH

**Overview**: AWARE BENCH is a benchmark designed to evaluate awareness in large language models (LLMs), categorizing awareness into five dimensions: capability, mission, emotion, culture, and perspective awareness using the AWARE EVAL dataset.

**Data Type**: question-and-answer pairs

**Domains**:
- Natural Language Processing
- Artificial Intelligence

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/HowieHwong/Awareness-in-LLM)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of AWARE BENCH is to evaluate the awareness of LLMs across five dimensions.

**Target Audience**:
- ML Researchers
- AI Ethicists
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset needs to be enriched conceptually and should include more real-world scenarios.

## 💾 Data

**Source**: Combination of existing datasets and newly generated queries through a human-AI collaborative framework.

**Size**: 200 capability awareness questions, 522 mission awareness questions, 200 emotion awareness questions, 500 culture awareness questions

**Format**: N/A

**Annotation**: Manual validation and generation through two main phases: seed curation and query generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the ratio of correctly answered questions to the total number of questions.

**Interpretation**: Higher accuracy indicates better awareness and alignment of LLMs with human values.

**Baseline Results**: Various models evaluated, performance varies with only GPT-4 and GLM-4 achieving an accuracy exceeding 80%.

**Validation**: Human quality check for generated questions to ensure pertinence and clarity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Ethics

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
