# Reinforcement Learning on Pre-Training Data (RLPT)

## 📊 Benchmark Details

**Name**: Reinforcement Learning on Pre-Training Data (RLPT)

**Overview**: RLPT is a new training-time scaling paradigm for optimizing large language models (LLMs) through reinforcement learning. It utilizes a next-segment reasoning objective to derive reward signals from pre-training data without relying on human annotation, improving reasoning capabilities and generalization.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMLU
- MMLU-Pro
- GPQA-Diamond
- KOR-Bench
- AIME24
- AIME25

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of RLPT is to optimize large language models through reinforcement learning on a foundation of pre-training data, enhancing their reasoning capabilities without the need for human annotation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Text Completion

**Limitations**: N/A

## 💾 Data

**Source**: Web corpora including Wikipedia, arXiv, and community forum data, processed into training segments.

**Size**: N/A

**Format**: N/A

**Annotation**: Uses a generative reward model for evaluating predicted segments against ground-truth segments.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Policy Gradient Algorithms

**Metrics**:
- Accuracy
- Pass@1
- Pass@8

**Calculation**: Metrics are calculated based on the model's predictions evaluated against the correct segment.

**Interpretation**: Higher metrics indicate improved reasoning capabilities and model performance across evaluated benchmarks.

**Baseline Results**: Improvements on benchmarks such as MMLU and AIME were quantified.

**Validation**: Extensive experimentation on various reasoning benchmarks was conducted to validate RLPT's effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
