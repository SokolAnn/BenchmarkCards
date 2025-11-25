# OmniThought

## 📊 Benchmark Details

**Name**: OmniThought

**Overview**: OmniThought is a large-scale dataset featuring 2 million Chain-of-Thought (CoT) processes generated and validated by two powerful LRMs as teacher models, annotated with Reasoning Verbosity and Cognitive Difficulty scores.

**Data Type**: CoT processes

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OpenThoughts
- DeepMath

**Resources**:
- [Resource](https://huggingface.co/datasets/alibaba-pai/OmniThought)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the development and training of large reasoning models for solving complex tasks through a comprehensive dataset of CoT processes.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Reasoning
- Problem Solving

**Limitations**: The dataset has a limited scope of reasoning tasks and a static construction process.

## 💾 Data

**Source**: Sourced from established datasets like OpenThoughts2-1M and DeepMath-103K.

**Size**: 2,059,000 CoT processes

**Format**: N/A

**Annotation**: Automatically generated and validated by LRMs with Reasoning Verbosity and Cognitive Difficulty scores.

## 🔬 Methodology

**Methods**:
- LLM-as-a-judge validation
- Automated scoring metrics

**Metrics**:
- Reasoning Verbosity (RV)
- Cognitive Difficulty (CD)

**Calculation**: RV and CD scores are calculated based on model evaluations and token counts normalized against dataset characteristics.

**Interpretation**: Scores indicate the appropriateness of CoT verbosity and cognitive difficulty level for optimal LRM training.

**Baseline Results**: N/A

**Validation**: Extensive benchmarking using Qwen2.5 models demonstrates improved training effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
