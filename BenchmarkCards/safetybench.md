# SafetyBench

## 📊 Benchmark Details

**Name**: SafetyBench

**Overview**: SafetyBench is a comprehensive benchmark for evaluating the safety of Large Language Models (LLMs), comprising 11,435 diverse multiple choice questions spanning across 7 distinct categories of safety concerns.

**Data Type**: multiple choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Resources**:
- [GitHub Repository](https://github.com/thu-coai/SafetyBench)
- [Resource](https://llmbench.ai/safety)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety abilities of Large Language Models (LLMs).

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Safety Assessment

**Limitations**: Some safety concerns, such as political issues, may be overlooked.

## 💾 Data

**Source**: Collected from various datasets, safety-related exams, and augmented using LLMs.

**Size**: 11,435 multiple choice questions

**Format**: JSON

**Annotation**: Validated through human verification and automatic checks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the proportion of correct answers to the total questions.

**Interpretation**: Higher accuracy indicates better safety understanding by the LLM.

**Baseline Results**: GPT-4 shows significant performance advantages over other LLMs.

**Validation**: Extensive testing over 25 popular LLMs in zero-shot and few-shot settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: SafetyBench contains no personal information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Crowd workers were informed in advance how the annotated data will be used.

**Compliance With Regulations**: Not Applicable
