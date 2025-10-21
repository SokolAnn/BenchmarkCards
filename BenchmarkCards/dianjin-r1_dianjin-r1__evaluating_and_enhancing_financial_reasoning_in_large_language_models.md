# DianJin-R1 (DianJin-R1: Evaluating and Enhancing Financial Reasoning in Large Language Models)

## 📊 Benchmark Details

**Name**: DianJin-R1 (DianJin-R1: Evaluating and Enhancing Financial Reasoning in Large Language Models)

**Overview**: DianJin-R1 introduces a reasoning-enhanced framework and a high-quality dataset, DianJin-R1-Data, constructed from CFLUE, FinQA, and a proprietary compliance corpus to enhance financial reasoning in large language models (LLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- CFLUE
- FinQA
- CCC

**Resources**:
- [Resource](https://huggingface.co/DianJin)
- [Resource](https://modelscope.cn/organization/tongyi_dianjin)
- [GitHub Repository](https://github.com/aliyun/qwen-dianjin)
- [Resource](https://tongyi.aliyun.com/dianjin)

## 🎯 Purpose and Intended Users

**Goal**: To enhance financial reasoning capabilities in LLMs through structured supervision and reinforcement learning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from CFLUE, FinQA, and a proprietary compliance corpus (CCC).

**Size**: 38,638 multiple-choice questions from CFLUE, 8,281 financial question-answer pairs from FinQA, and 1,800 dialogues from CCC.

**Format**: Structured text format with <think> and <answer> tags.

**Annotation**: Manual verification using GPT-4o to ensure alignment between generated answers and reasoning steps.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning (SFT)
- Reinforcement Learning (RL)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is defined as the proportion of correctly answered questions.

**Interpretation**: Higher accuracy implies better reasoning capability in models.

**Baseline Results**: N/A

**Validation**: Evaluated on benchmarks including CFLUE, FinQA, and CCC.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-sourced except for sensitive CCC scenario data.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
