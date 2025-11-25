# ProSA (Prompt Sensitivity Assessment)

## 📊 Benchmark Details

**Name**: ProSA (Prompt Sensitivity Assessment)

**Overview**: ProSA is a framework designed to evaluate and comprehend prompt sensitivity in large language models (LLMs), incorporating a novel sensitivity metric called PromptSensiScore (PSS) that quantifies the variability in model responses to different prompts.

**Data Type**: prompt-response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LC AlpacaEval 2.0
- Arena Hard Auto

**Resources**:
- [GitHub Repository](https://github.com/open-compass/ProSA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of prompt sensitivity in LLMs, allowing for improved model robustness and better alignment with user expectations.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Prompt Sensitivity Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Multiple evaluation datasets including CommonsenseQA, ARC-Challenge, MATH, and HumanEval.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Objective evaluation
- Subjective evaluation

**Metrics**:
- Prompt Sensitivity Score (PSS)

**Calculation**: PSS is calculated as the average discrepancy in the model's responses when faced with different prompt variants for the same instruction.

**Interpretation**: A lower PSS indicates higher robustness of the model to prompt changes.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
