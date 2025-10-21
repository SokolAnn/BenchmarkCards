# MATH-TUTOR BENCH

## 📊 Benchmark Details

**Name**: MATH-TUTOR BENCH

**Overview**: MATH-TUTOR BENCH is an open-source benchmark designed for holistic evaluation of dialog tutoring models for math tutoring, providing datasets and metrics to assess pedagogical capabilities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8k

**Resources**:
- [GitHub Repository](https://github.com/eth-lre/mathtutorbench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating dialog tutoring models in terms of their pedagogical abilities in math tutoring.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Problem Solving
- Socratic Questioning
- Student Solution Correctness
- Student Mistake Location
- Student Mistake Correction
- Scaffolding Generation
- Pedagogical Instruction Following

**Limitations**: Our work focuses on high school math tutoring and does not evaluate long conversations or dimensions related to safety.

## 💾 Data

**Source**: Consists of datasets like Bridge and MathDial, focusing on real teacher-student tutoring conversations.

**Size**: Over 10,000 examples

**Format**: JSON

**Annotation**: Manually annotated by experts and derived from real teacher-student interactions.

## 🔬 Methodology

**Methods**:
- Metrics for evaluating problem-solving and pedagogical responses
- Reward model for scoring tutoring responses

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score

**Calculation**: Metrics are calculated based on the alignment of model responses with expert teacher responses and calibrated through pairwise comparisons.

**Interpretation**: Models are assessed on their ability to scaffold student learning and achieve desired pedagogical outcomes.

**Baseline Results**: Results are provided for various models evaluated against the benchmark tasks.

**Validation**: The benchmark was validated using data collected from real teacher interactions and tested against human-generated responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to prevent suboptimal tutoring behavior and mitigate risks from using AI in educational contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collected is anonymized, with the intent of protecting user privacy.

**Data Licensing**: The dataset is released under the CC-BY-4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
