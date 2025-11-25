# TUBench (Trustworthiness Benchmark for Unanswerable Questions)

## 📊 Benchmark Details

**Name**: TUBench (Trustworthiness Benchmark for Unanswerable Questions)

**Overview**: TUBench is a benchmark specifically designed to evaluate the reliability of Large Vision-Language Models (LVLMs) using unanswerable questions. It contains high-quality, unanswerable questions crafted using ten distinct strategies across four visual domains: code snippets, natural images, geometry diagrams, and statistical tables.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Mathematics

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MME
- POPE

**Resources**:
- [GitHub Repository](https://github.com/NLPCode/TUBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a new perspective for assessing the trustworthiness and hallucination of LVLMs through the lens of unanswerable questions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Code Reasoning
- Geometry Question Answering
- Mathematical Word Problems

**Limitations**: N/A

## 💾 Data

**Source**: Images from MSCOCO dataset and custom code screenshots

**Size**: 2,354 questions

**Format**: JSON

**Annotation**: Manually crafted by experts using various strategies

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the models' ability to identify whether questions are answerable or unanswerable and the corresponding correctness of the answers provided.

**Interpretation**: Higher scores indicate better performance in distinguishing between answerable and unanswerable questions.

**Baseline Results**: Gemini-1.5-Pro achieves an average accuracy of 69.2% in determining question answerability.

**Validation**: Comprehensive quantitative evaluation of 28 leading LVLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
