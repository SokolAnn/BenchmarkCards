# GVGAI-LLM

## 📊 Benchmark Details

**Name**: GVGAI-LLM

**Overview**: GVGAI-LLM is a video game benchmark for evaluating the reasoning and problem-solving capabilities of large language models (LLMs). It features a diverse collection of arcade-style games designed to test a model’s ability to handle tasks that differ from most existing LLM benchmarks.

**Data Type**: game environments

**Domains**:
- Artificial Intelligence
- Gaming

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- HumanEval
- HELM
- BabyAI

**Resources**:
- [GitHub Repository](https://github.com/doveliyuchen/GVGAI)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the decision-making competence of large language models in structured symbolic games and highlight their limitations in areas like spatial reasoning and planning.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Game Playing
- Decision Making

**Limitations**: N/A

## 💾 Data

**Source**: General Video Game AI framework with over one hundred 2D video games defined using VGDL.

**Size**: 118 games

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Structured prompting

**Metrics**:
- Meaningful Step Ratio
- Step Efficiency
- Win Rate
- Overall Score

**Calculation**: Metrics are calculated based on agent performance measures including actions taken, successful game completions, and average steps.

**Interpretation**: Higher scores indicate better agent behavior and effectiveness in completing games.

**Validation**: Evaluated across multiple agent types under the same experimental conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
