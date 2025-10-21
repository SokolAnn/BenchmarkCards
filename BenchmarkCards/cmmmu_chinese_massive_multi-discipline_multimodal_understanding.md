# CMMMU (Chinese Massive Multi-discipline Multimodal Understanding)

## 📊 Benchmark Details

**Name**: CMMMU (Chinese Massive Multi-discipline Multimodal Understanding)

**Overview**: CMMMU is a new Chinese Massive Multi-discipline Multimodal Understanding benchmark designed to evaluate large multimodal models on tasks demanding college-level subject knowledge and deliberate reasoning in a Chinese context. It includes 12k manually collected multimodal questions across multiple disciplines.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education
- Computer Science
- Medical Diagnosis

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMMU (Massive Multi-discipline Multimodal Understanding)

**Resources**:
- [Resource](https://cmmmu-benchmark.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large multimodal models on college-level knowledge and reasoning tasks in a Chinese context and enhance the development of next-generation models for expert AI.

**Target Audience**:
- ML Researchers
- Education Professionals
- AI Developers

**Tasks**:
- Multimodal Question Answering
- Reasoning with Complex Perceptions
- Evaluation of Language Models

**Limitations**: The benchmark mainly focuses on college-level content, which may not cover the entire range of human knowledge and cognitive skills.

## 💾 Data

**Source**: Manually collected multimodal questions from college exams, quizzes, and textbooks, covering six core disciplines

**Size**: 12,000 examples

**Format**: JSON

**Annotation**: Manually curated by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: The F1 Score is calculated based on the precision and recall of the models evaluated on the dataset.

**Interpretation**: Higher scores indicate better model performance on the tasks presented in the benchmark.

**Baseline Results**: Baseline results vary for different models tested, with GPT-4V achieving 43% accuracy on the benchmark.

**Validation**: The benchmark has been validated through rigorous testing against multiple language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes a consideration of demographic factors in performance evaluation, concentrating on the efficacy of models across various academic disciplines.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection and usage comply with ethical guidelines and legal regulations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
