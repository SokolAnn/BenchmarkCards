# Jailbreak Distillation (JBDISTILL)

## 📊 Benchmark Details

**Name**: Jailbreak Distillation (JBDISTILL)

**Overview**: Jailbreak Distillation (JBDISTILL) is a novel benchmark construction framework that distills jailbreak attacks into high-quality and easily-updatable safety benchmarks, addressing challenges in existing safety evaluations by ensuring fair comparisons and reproducibility.

**Data Type**: safety benchmarks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HarmBench

**Resources**:
- [Resource](https://aka.ms/jailbreak-distillation)

## 🎯 Purpose and Intended Users

**Goal**: Provide a renewable safety evaluation framework for large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Derived prompts from existing jailbreak attack algorithms and development models.

**Size**: 500 prompts

**Format**: N/A

**Annotation**: Minimal human effort required for running the JBDISTILL pipeline to produce updated benchmarks.

## 🔬 Methodology

**Methods**:
- Prompt selection algorithms (RANK BYSUCCESS, BESTPERGOAL, COMBINED SELECTION)

**Metrics**:
- Effectiveness
- Separability
- Diversity

**Calculation**: Average Attack Success Rate (ASR) across evaluation models to measure effectiveness; confidence intervals for separability.

**Interpretation**: Effective benchmarks are those that provide high ASR and clear separability between model performances.

**Baseline Results**: Baseline benchmarks include HarmBench, DAN prompts, WildJailbreaks, showing lower effectiveness compared to JBDISTILL.

**Validation**: Empirical validation of benchmark performance across diverse LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Adversarial prompts intended for safety evaluation, with a focus on preventing harmful applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: HarmBench dataset is under MIT license; WildJailbreaks dataset is under ODC-BY license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
