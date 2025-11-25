# EMBER (Epistemic Marker Benchmark for Evaluator Robustness)

## 📊 Benchmark Details

**Name**: EMBER (Epistemic Marker Benchmark for Evaluator Robustness)

**Overview**: EMBER is a benchmark designed to assess the robustness of LLM-judges to epistemic markers in both single and pairwise evaluation settings, focusing on how these markers influence the judging performance of LLMs.

**Data Type**: question-answering pairs, instruction-following pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DongryeolLee96/EMBER)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of LLM-judges against epistemic markers and assess how these markers affect their judgment on model-generated outputs.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering
- Instruction Following

**Limitations**: The study focuses on two specific evaluation tasks, leaving other potential influences of epistemic markers across various tasks unexplored.

## 💾 Data

**Source**: The EVOUNA dataset (Wang et al., 2024) for question-answering and MIXINSTRUCT (Jiang et al., 2023) for instruction-following.

**Size**: 2,000 instances for EMBER QA and 823 instances for EMBER IF

**Format**: JSON

**Annotation**: Manually annotated by human evaluators after augmentation with epistemic markers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Verdict Switch Rate (VSR)

**Calculation**: Accuracy is defined as the match rate between LLM-judges and ground-truth labels. VSR indicates the percentage of samples that changed verdicts due to the presence of epistemic markers.

**Interpretation**: Ideally, a robust LLM-judge should demonstrate zero changes in verdicts due to epistemic markers.

**Baseline Results**: Results from five LLM-judges (GPT-3.5-turbo, GPT-4-turbo, GPT-4o, Llama-3-8B-Instruct, Llama-3-70B-Instruct) indicate biases against epistemic markers, particularly weakeners, affecting evaluation accuracy.

**Validation**: Human evaluators assessed the correctness of model outputs augmented with epistemic markers to ensure validity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
