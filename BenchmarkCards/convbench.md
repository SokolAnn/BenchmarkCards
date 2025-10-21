# ConvBench

## 📊 Benchmark Details

**Name**: ConvBench

**Overview**: ConvBench is a novel multi-turn conversation evaluation benchmark tailored for Large Vision-Language Models (LVLMs), assessing capabilities in perception, reasoning, and creativity.

**Data Type**: conversation

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LVLM-eHub
- MMMU
- Seed-Bench

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multi-turn conversational capabilities of Large Vision-Language Models (LVLMs) using a hierarchical assessment approach that measures perception, reasoning, and creativity.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Conversational Evaluation
- Task Completion
- Multi-Turn Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: Multi-turn conversation scenarios based on a curated set of tasks reflecting real-world demands.

**Size**: 577 multi-turn conversations

**Format**: JSON

**Annotation**: Human-verified responses and automatic evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score
- Mean Average Precision (MAP)
- Win Rate

**Calculation**: Scores are derived from the aggregated results of human evaluations and model outputs.

**Interpretation**: Higher scores indicate better performance in understanding and responding to complex conversational cues.

**Baseline Results**: Average scores for benchmark models like GPT-4-V in conversation tasks are reported.

**Validation**: The benchmark's reliability and validity are tested against established evaluation metrics and previous standards.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Membership inference attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection procedures ensure user information is anonymized and retained confidentially.

**Data Licensing**: The dataset is licensed under CC BY 4.0, allowing for redistribution and adaptation with proper attribution.

**Consent Procedures**: Informed consent was obtained from all participants involved in annotations, if applicable.

**Compliance With Regulations**: Research complies with all applicable ethical standards and guidelines.
