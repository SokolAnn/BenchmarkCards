# MultiTrust

## 📊 Benchmark Details

**Name**: MultiTrust

**Overview**: MultiTrust is the first comprehensive and unified benchmark to evaluate the trustworthiness of Multimodal Large Language Models (MLLMs) across five main aspects: truthfulness, safety, robustness, fairness, and privacy, implementing 32 diverse tasks with self-curated datasets.

**Data Type**: text and image

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- ToViLaG
- PrivQA
- GOAT-Bench
- MM-SafetyBench
- BenchLMM
- SafeBench
- Unicorn
- RTVLM

**Resources**:
- [Resource](https://multi-trust.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation framework for assessing the trustworthiness of Multimodal Large Language Models (MLLMs) across various tasks and risks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Truthfulness Evaluation
- Safety Evaluation
- Robustness Evaluation
- Fairness Evaluation
- Privacy Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: MultiTrust comprises datasets curated from literature, adapted from existing datasets, and newly synthesized data via generative methods and manual collection.

**Size**: 23,000 image-text pairs

**Format**: N/A

**Annotation**: Manually curated and automatically generated samples for accuracy and relevance of tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Recall
- Precision
- Toxicity Score
- Refuse-to-Answer Rate

**Calculation**: Metrics calculated as per specific tasks mentioned in the evaluations, using different evaluative metrics suited to each task type.

**Interpretation**: Higher metrics indicate better performance in the respective tasks assessing the MLLMs' trustworthiness and reliability across various aspects.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through extensive systematic evaluations with diverse MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

**Potential Harm**: This benchmark aims to address issues related to privacy leaks, bias in AI systems, and overall impact on user trust.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 for the datasets constructed from scratch; licensing follows original datasets for adapted samples.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
