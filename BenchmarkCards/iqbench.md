# IQBench

## 📊 Benchmark Details

**Name**: IQBench

**Overview**: IQBench is a novel benchmark specifically designed to evaluate the fluid intelligence of Vision-Language Models (VLMs) using curated visual IQ test questions. It emphasizes both the accuracy of predictions and the interpretability of the reasoning process.

**Data Type**: visual IQ questions and annotations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Visual Question Answering
- VQA
- GQA
- ScienceQA
- MathVista
- MMMU

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To advance research on the fluid intelligence of VLMs by evaluating their reasoning capabilities on visual IQ tests.

**Target Audience**:
- ML Researchers
- AI Developers
- Cognitive Scientists

**Tasks**:
- Reasoning Evaluation
- Visual Intelligence Assessment

**Limitations**: The dataset contains 500 samples, which may limit diversity in evaluation.

## 💾 Data

**Source**: Manually curated from various sources, including educational materials and online repositories.

**Size**: 500 examples

**Format**: PNG images with associated questions and reasoning patterns

**Annotation**: Manually annotated with reasoning patterns and correct answers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- LLM-as-judge strategy

**Metrics**:
- Accuracy Score
- Reasoning Score

**Calculation**: Accuracy is calculated as an exact match of the model’s prediction to the correct answer. Reasoning score is derived by comparing model explanations with annotated reasoning patterns.

**Interpretation**: Scores reflect both the correctness of the final answer and the coherence of the reasoning process.

**Baseline Results**: o4-mini achieved the highest accuracy of 0.615 on IQBench tasks.

**Validation**: Evaluation involved both automated metrics and human assessments for reasoning quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
