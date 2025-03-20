# Token Preference Optimization with Self-Calibrated Visual-Anchored Rewards for Hallucination Mitigation

## 📊 Benchmark Details

**Name**: Token Preference Optimization with Self-Calibrated Visual-Anchored Rewards for Hallucination Mitigation

**Overview**: This paper presents a novel Token Preference Optimization (TPO) model that employs self-calibrated visual-anchored rewards to mitigate hallucination issues in Large Vision Language Models (LVLMs) by improving token-level alignment with human preferences.

**Data Type**: Multi-modal

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AMBER
- MMHal-Bench
- HallusionBench
- SEED Bench
- MMBench
- LLaV A Bench
- MM-Vet

**Resources**:
- [Resource](arXiv:2412.14487v3)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the performance of Large Vision Language Models by aligning outputs more closely with human preferences and mitigating hallucination problems.

**Target Audience**:
- Researchers
- Developers in AI/ML
- Practitioners in Computer Vision

**Tasks**:
- Image captioning
- Visual question answering
- Complex visual reasoning

**Limitations**: The proposed approach may require further refinement to handle complex visual contexts and varying types of visual information.

**Out of Scope Uses**:
- Real-time applications without additional fine-tuning
- Use in sensitive or critical decision-making processes without sufficient testing

## 💾 Data

**Source**: RLHF-V dataset from Yu et al., 2024

**Size**: 5,000 preference pairs

**Format**: Dataset with pairs of responses

**Annotation**: No fine-grained manual annotations

## 🔬 Methodology

**Methods**:
- Token Preference Optimization (TPO)
- Direct Preference Optimization (DPO)
- Visual-Aware Training Objective

**Metrics**:
- F1 Score
- Accuracy
- Hallucination Rate

**Calculation**: Reward function based on logistic distributions conditioned on raw and corrupted images.

**Interpretation**: Higher scores reflect better alignment of generated tokens with input visual information.

**Baseline Results**: TPO achieves an absolute improvement on hallucination benchmarks compared to existing methods.

**Validation**: Extensive experiments conducted on stated benchmarks show improved performance from TPO.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy Risk
- Transparency Risk
- Fairness Risk

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets and models used are open source, following ethical guidelines.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
