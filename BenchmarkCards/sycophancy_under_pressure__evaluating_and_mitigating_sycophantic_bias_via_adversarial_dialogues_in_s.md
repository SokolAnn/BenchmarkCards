# Sycophancy under Pressure: Evaluating and Mitigating Sycophantic Bias via Adversarial Dialogues in Scientific QA

## 📊 Benchmark Details

**Name**: Sycophancy under Pressure: Evaluating and Mitigating Sycophantic Bias via Adversarial Dialogues in Scientific QA

**Overview**: This paper introduces a unified evaluation framework to quantify the impact of sycophantic context on model behavior in scientific question answering, measuring how much user-imposed social pressure distorts model outputs.

**Data Type**: multiple-choice question answering

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ARC-Challenge
- GPQA-Diamond

**Resources**:
- [Resource](https://arxiv.org/abs/2508.13743)

## 🎯 Purpose and Intended Users

**Goal**: To systematically investigate sycophantic behavior in large language models within the context of scientific question answering and to propose an evaluation framework and method for mitigation.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The training data was constructed from the ARC-Challenge training set, augmented with synthetic dialogues demonstrating user-induced pressure.

**Size**: 11,190 dialogue instances

**Format**: N/A

**Annotation**: Synthetic adversarial dialogues prompted for factual reasoning

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Misleading Resistance Rate
- Sycophancy Resistance Rate

**Calculation**: Metrics are calculated based on model's accuracy under direct misleading conditions and the proportion of correct rejections of misleading cues.

**Interpretation**: A higher Sycophancy Resistance Rate indicates a stronger ability to resist user-imposed distortion.

**Baseline Results**: Not specified.

**Validation**: Evaluation conducted on ARC-Challenge and GPQA-Diamond datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Reinforcing misinformation', 'Misleading users']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
