# LongBench v2

## 📊 Benchmark Details

**Name**: LongBench v2

**Overview**: LongBench v2 is a benchmark designed to assess LLMs' ability to handle long-context problems requiring deep understanding and reasoning across realistic multitasks. It consists of 503 multiple-choice questions with contexts ranging from 8k to 2M words, across six major task categories.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LongBench

**Resources**:
- [Resource](https://longbench2.github.io)
- [GitHub Repository](https://github.com/THUDM/LongBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging multitask benchmark for long-context understanding and reasoning, enhancing the evaluation standards for LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Single-document Question Answering
- Multi-document Question Answering
- Long In-context Learning
- Long-dialogue History Understanding
- Code Repository Understanding
- Long Structured Data Understanding

**Limitations**: The benchmark’s size may be small, limiting stability; it is currently available only in English; and the length distribution across tasks is uneven.

## 💾 Data

**Source**: Collected from nearly 100 highly educated individuals with diverse professional backgrounds, combining automated and manual review processes.

**Size**: 503 questions

**Format**: Multiple-choice format

**Annotation**: Data was annotated by academic annotators through a detailed process, ensuring high quality and appropriate difficulty.

## 🔬 Methodology

**Methods**:
- Automated review
- Manual review

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed based on the percentage of correct answers provided by models compared to the groundtruth answers.

**Interpretation**: A higher accuracy percentage indicates better performance on the long-context reasoning tasks.

**Baseline Results**: The best-performing model achieves 57.7% accuracy, surpassing human experts' performance of 53.7% under a 15-minute time constraint.

**Validation**: Data points were subjected to both automated and manual review to ensure correctness and appropriate difficulty.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All reviewers are required to ensure that submitted data do not contain sensitive information related to privacy or copyrights.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
