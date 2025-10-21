# CRiskEval (Chinese Multi-Level Risk Evaluation Benchmark Dataset for Large Language Models)

## 📊 Benchmark Details

**Name**: CRiskEval (Chinese Multi-Level Risk Evaluation Benchmark Dataset for Large Language Models)

**Overview**: CRiskEval is a Chinese dataset designed for gauging the risk proclivities inherent in LLMs, evaluating their tendencies through fine-grained multiple-choice question answering based on a taxonomy of 7 types of frontier risks and 4 safety levels.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- AraTrust
- R-Judge
- SafetyBench

**Resources**:
- [GitHub Repository](https://github.com/lingshi6565/Risk_eval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the risk tendencies of large language models by using a fine-grained dataset that captures various behavioral responses to hypothetical scenarios.

**Target Audience**:
- ML Researchers
- AI Safety Researchers
- Model Developers

**Tasks**:
- Risk Evaluation
- Behavioral Analysis

**Limitations**: The dataset may not cover all potential future risks as AI capabilities evolve.

## 💾 Data

**Source**: Questions are generated through a combination of translation from prior datasets and newer question generation methods utilizing AI assistance.

**Size**: 14,888 questions

**Format**: JSON

**Annotation**: Questions are manually annotated with risk levels by experts.

## 🔬 Methodology

**Methods**:
- Tendency evaluation
- Multiple-choice evaluation

**Metrics**:
- Comprehensive Risk Indicator (CRI)
- Specific Risk Indicator (SRI)

**Calculation**: Metrics are calculated based on the weighted proportions of answer choices across risk levels.

**Interpretation**: Higher scores indicate greater risk tendencies of the evaluated LLMs.

**Validation**: Dataset was validated through expert reviews, achieving an average score of 86.6.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Ethics

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes scenarios that may involve sensitive behaviors; care was taken to assess potential issues.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
