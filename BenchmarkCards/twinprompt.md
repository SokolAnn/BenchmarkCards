# TwinPrompt

## 📊 Benchmark Details

**Name**: TwinPrompt

**Overview**: TwinPrompt is a newly created dataset consisting of 100 pairs of harmful and harmless twin prompts, designed to analyze the safety alignment parameters in Large Language Models (LLMs). It is utilized to identify and prune parameters responsible for safety features in LLMs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HarmBench

**Resources**:
- [Resource](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for effectively pruning safety alignment mechanisms in LLMs while preserving model utility.

**Target Audience**:
- ML Researchers
- Safety Researchers
- Model Developers

**Tasks**:
- Text Classification
- Jailbreaking Detection

**Limitations**: N/A

## 💾 Data

**Source**: Created from HarmBench Dataset and manual crafting of harmless twin prompts.

**Size**: 100 twin prompt pairs

**Format**: N/A

**Annotation**: Manually crafted and validated using LLaMA 2

## 🔬 Methodology

**Methods**:
- Targeted Pruning
- Activation Analysis

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: The percentage of harmful prompts successfully answered after pruning.

**Interpretation**: Higher ASR indicates successful bypassing of LLM safety alignments.

**Baseline Results**: Unpruned models show low ASR; TwinBreak successfully increases ASRs across models.

**Validation**: ASR measured across various models after applying iterative pruning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Fairness**: Data bias

**Potential Harm**: ['Exploitative responses to harmful prompts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
