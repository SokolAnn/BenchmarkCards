# FRIDA (Field Reasoning and Instruction Decoding Agent)

## 📊 Benchmark Details

**Name**: FRIDA (Field Reasoning and Instruction Decoding Agent)

**Overview**: This paper presents a dataset and pipeline to create FRIDA models, focusing on generating synthetic data for fine-tuning small language models (LLMs) specific to disaster response scenarios, particularly in assessing object reasoning in disastrous environments.

**Data Type**: instruction pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mshich1/FRIDA)

## 🎯 Purpose and Intended Users

**Goal**: To improve the physical common sense reasoning capabilities of smaller LLMs in disaster response scenarios by utilizing a specially designed dataset and fine-tuning pipeline.

**Target Audience**:
- ML Researchers
- Robotics Developers
- Disaster Response Professionals

**Tasks**:
- Object Reasoning
- Instruction Following

**Limitations**: Training and evaluation are conducted on template-generated data rather than naturally occurring language.

## 💾 Data

**Source**: Synthetic data generated from expert-guided templates focused on object reasoning in disaster scenarios.

**Size**: 25,000 instructions

**Format**: JSON

**Annotation**: Expert-in-the-loop annotation process involves domain experts curating the synthetic data.

## 🔬 Methodology

**Methods**:
- Ablation Study
- Customized Evaluation Metrics

**Metrics**:
- SemScore

**Calculation**: SemScore is calculated using cosine similarity between model response vectors and gold standard responses.

**Interpretation**: Higher SemScore indicates better semantic similarity and understanding of the task-relevant instructions.

**Baseline Results**: FRIDA models achieved a SemScore accuracy of 94.6% compared to the base model.

**Validation**: Models evaluated using a custom set of at least four evaluation questions per template.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
