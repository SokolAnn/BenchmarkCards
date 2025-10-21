# Safe-Child-LLM

## 📊 Benchmark Details

**Name**: Safe-Child-LLM

**Overview**: Safe-Child-LLM is a comprehensive benchmark and dataset for systematically assessing LLM safety across two developmental stages: children (7–12) and adolescents (13–17). It includes a dataset of 200 adversarial prompts with human-annotated labels for jailbreak success and a standardized ethical refusal scale.

**Data Type**: adversarial prompts

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- JailbreakBench
- HarmBench

**Resources**:
- [GitHub Repository](https://github.com/The-Responsible-AI-Initiative/Safe_Child_LLM_Benchmark.git)

## 🎯 Purpose and Intended Users

**Goal**: To create a developmentally sensitive benchmark that systematically evaluates LLM behaviors with child and teen prompts.

**Target Audience**:
- AI Safety Researchers
- Developers
- Policymakers
- Educators

**Tasks**:
- Safety Assessment
- Adversarial Prompt Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from red-teaming corpora such as SG-Bench and HarmBench, alongside developmentally appropriate adaptations.

**Size**: 200 prompts

**Format**: N/A

**Annotation**: Human-annotated labeling for jailbreak success and ethical refusal categorized on a 0–5 scale.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the binary harmfulness indicator (0/1) and action scores (0-5) reflecting the ethical and developmental significance.

**Interpretation**: Evaluation reflects how LLMs handle child-appropriate interactions with nuanced labeling rather than simple binary classifications.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through systematic human evaluation of model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Ethics

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Evaluation reflects risks specific to minors' interactions with LLMs, acknowledging developmental differences.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
