# TRACE

## 📊 Benchmark Details

**Name**: TRACE

**Overview**: TRACE is a novel benchmark designed to evaluate continual learning in large language models (LLMs), consisting of 8 distinct datasets spanning challenging tasks including domain-specific tasks, multilingual capabilities, code generation, and mathematical reasoning.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- German

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- Big-Bench

**Resources**:
- [GitHub Repository](https://github.com/BeyonderXX/TRACE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of continual learning for LLMs, assessing their capabilities in various domains after sequential training.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Continual Learning Evaluation
- Mathematical Reasoning
- Code Generation
- Multilingual Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Eight standardized datasets covering various tasks including ScienceQA, FOMC, MeetingBank, C-STANCE, 20Minuten, Py150, NumGLUE, and more.

**Size**: 40,000 training examples and 16,000 testing examples

**Format**: Standardized format for unified evaluation

**Annotation**: Curated for specific knowledge and reasoning capabilities, ensuring diversity and challenge.

## 🔬 Methodology

**Methods**:
- Sequential Full-Parameter Fine-Tuning
- LoRA-based Sequential Fine-Tuning
- Replay-based Sequential Fine-Tuning
- In-Context Learning

**Metrics**:
- General Ability Delta
- Instruction Following Delta
- Safety Delta

**Calculation**: Metrics are calculated based on performance shifts in task-specific evaluations and general tasks pre- and post-training.

**Interpretation**: Higher scores indicate better retention of general abilities and instruction-following capabilities.

**Baseline Results**: Compared against multiple LLMs including LLaMA-2 and Vicuna models across various tasks.

**Validation**: Evaluated based on rigorous testing against the outlined metrics using multiple LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Fairness**
- **Robustness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
