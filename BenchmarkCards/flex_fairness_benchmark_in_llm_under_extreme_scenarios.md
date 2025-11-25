# FLEX (Fairness Benchmark in LLM under Extreme Scenarios)

## 📊 Benchmark Details

**Name**: FLEX (Fairness Benchmark in LLM under Extreme Scenarios)

**Overview**: FLEX is designed to rigorously assess the fairness of LLMs when subjected to conditions that are likely to induce bias. It incorporates adversarial prompts that amplify potential biases into the fairness assessment.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BBQ
- CrowS-Pairs
- StereoSet

**Resources**:
- [GitHub Repository](https://github.com/ekgus9/FLEX)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of large language models in maintaining fairness when exposed to bias-inducing prompts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark does not cover all possible bias-inducing scenarios due to the infinite combinations.

## 💾 Data

**Source**: Constructed from existing fairness benchmark datasets including BBQ, CrowS-Pairs, and StereoSet via integration of adversarial prompts.

**Size**: 3,145 examples

**Format**: JSON

**Annotation**: Manually annotated based on responses generated under adverse conditions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Attack Success Rate (ASR)

**Calculation**: ASR is calculated based on the proportion of samples that are correct in the source dataset but incorrect in the FLEX dataset.

**Interpretation**: A lower ASR indicates a model's better robustness in extreme situations compared to regular scenarios.

**Baseline Results**: Compared with the source datasets BBQ, CrowS-Pairs, and StereoSet.

**Validation**: Performance of various LLMs is evaluated under zero-shot and few-shot conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark aims to assess fairness across various bias categories such as age, gender, nationality, race, religion, sexual orientation, and profession.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
