# LIFB ENCH (Long-context Instruction Following Benchmark)

## 📊 Benchmark Details

**Name**: LIFB ENCH (Long-context Instruction Following Benchmark)

**Overview**: LIFB ENCH is a scalable benchmark designed to evaluate large language models' instruction-following capabilities and stability in long-context scenarios, encompassing three scenarios and eleven diverse tasks.

**Data Type**: instruction-following pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Longbench
- FollowBench

**Resources**:
- [GitHub Repository](https://github.com/SheldonWu0327/LIF-Bench-2024)

## 🎯 Purpose and Intended Users

**Goal**: To assess instruction-following capabilities in long-context scenarios and provide insights for future LLM advancements.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction Following
- Text Generation
- Question Answering

**Limitations**: The benchmark comprises fewer than 3,000 samples and is tested across only three perspectives.

## 💾 Data

**Source**: Dataset constructed through an automated instruction expansion method and manual template crafting.

**Size**: 2,766 instructions

**Format**: N/A

**Annotation**: Manually crafted instruction templates and automated generation methods.

## 🔬 Methodology

**Methods**:
- Automated Rubric-based Scoring

**Metrics**:
- Instruction Following Stability (IFS)
- Accuracy

**Calculation**: Combined scoring from multiple facets including instruction metrics and stability assessments.

**Interpretation**: The scores reflect how well models can follow instructions across variable contexts.

**Baseline Results**: N/A

**Validation**: The evaluation process incorporates programmatic validation of model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
