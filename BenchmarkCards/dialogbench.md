# DialogBench

## 📊 Benchmark Details

**Name**: DialogBench

**Overview**: DialogBench is a dialogue evaluation benchmark that contains 12 dialogue tasks to probe the capabilities of LLMs as human-like dialogue systems. It aims to standardize the evaluation of LLMs and identify their strengths and limitations.

**Data Type**: dialogue tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/kwai/DialogBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs as human-like dialogue systems across multiple dimensions of human-likeness.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Intent Classification
- Emotion Detection
- Commonsense-aware Response Generation
- Dialogue Natural Language Inference
- Offensive Detection
- Multi-turn Response Generation
- Personality-grounded Response Generation
- Slot Filling
- Dialogue Summarization
- Knowledge-grounded Response Generation
- Relation Classification

**Limitations**: DialogBench currently only supports evaluation in English and Chinese, limiting its multilingual applicability.

## 💾 Data

**Source**: Generated dialogues using GPT-4 as a surrogate to create evaluation instances based on human-like dialogue tasks.

**Size**: N/A

**Format**: JSON

**Annotation**: Automatically generated with manual filtering for quality control.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on multiple-choice question performance across various dialogue tasks.

**Interpretation**: Higher accuracy scores indicate better performance on dialogue tasks, reflecting a more human-like interaction capability.

**Baseline Results**: Human-level accuracy scores were used as a benchmark for comparison.

**Validation**: The constructed evaluation tasks were tested on 26 different LLMs.

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
- **Robustness**: Prompt injection attack, Data poisoning
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Care was taken to ensure no personal data was included in generated instances.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
