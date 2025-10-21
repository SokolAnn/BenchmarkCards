# Dataset of Jailbreaks

## 📊 Benchmark Details

**Name**: Dataset of Jailbreaks

**Overview**: This paper introduces a dataset of jailbreaks where each example can be input in both a single or a multi-turn format, providing a tool to study the vulnerabilities of large language models against both forms of attacks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/tom-gibbs/multi-turn_jailbreak_attack_datasets)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for studying vulnerabilities in large language models related to jailbreak attacks using both single-turn and multi-turn input formats.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification

**Limitations**: The dataset has limitations in sample size, and prompts were only run once.

## 💾 Data

**Source**: Constructed from user-side interaction prompts intended to elicit harmful information from LLMs, alongside benign prompts for control.

**Size**: 6,536 examples

**Format**: JSON

**Annotation**: Hand-labeled by authors as either jailbroken or not, alongside understanding labels for each prompt.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Jailbreak success rate

**Calculation**: Metrics are calculated based on hand-labeling the outputs of the models as jailbroken or not.

**Interpretation**: A higher success rate indicates a model's increased vulnerability to the type of attack being tested.

**Validation**: The dataset was tested across multiple leading LLMs to compare attack success rates.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset does not include demographic breakdowns.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
