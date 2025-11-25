# MotionBench

## 📊 Benchmark Details

**Name**: MotionBench

**Overview**: MotionBench is a comprehensive evaluation benchmark designed to assess the fine-grained motion comprehension of video understanding models through six primary categories of motion-oriented question types.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MVBench
- LVBench
- VideoMME

**Resources**:
- [Resource](https://motion-bench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To thoroughly evaluate the motion-level capability of current video models and motivate the development of more capable video understanding models.

**Target Audience**:
- Researchers in Computer Vision
- ML Practitioners

**Tasks**:
- Motion Recognition
- Location-related Motion
- Action Order
- Repetition Count
- Motion-related Objects
- Camera Motion

**Limitations**: N/A

## 💾 Data

**Source**: Diverse video sources including web videos, movies, and synthetic videos from various datasets.

**Size**: 5,385 videos and 8,052 question-answer pairs

**Format**: N/A

**Annotation**: Manually annotated with distinct question types focused on fine-grained motion.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the percentage of correctly answered questions.

**Interpretation**: Higher scores indicate better motion-level comprehension capabilities.

**Baseline Results**: State-of-the-art models achieve less than 60% accuracy on MotionBench.

**Validation**: Evaluated on various existing video benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
