# LaMP-QA (Language Model Personalized Question Answering)

## 📊 Benchmark Details

**Name**: LaMP-QA (Language Model Personalized Question Answering)

**Overview**: LaMP-QA is a benchmark designed for evaluating personalized long-form answer generation, focusing on user-centric personalized question answering.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SE-PQA

**Resources**:
- [Resource](https://hf.co/datasets/alireza7/LaMP-QA)
- [GitHub Repository](https://github.com/LaMP-Benchmark/LaMP-QA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to enable the evaluation of personalized question answering systems, particularly in generating tailored responses based on user-specific information.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: SE-PQA dataset adapted from StackExchange

**Size**: 9,349+ train questions, 800+ validation questions, 1,000+ test questions

**Format**: N/A

**Annotation**: Filtered and manually checked for quality by human annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Aspect-based evaluation

**Metrics**:
- Alignment with human judgment
- Normalizing scores across aspects

**Calculation**: The response quality is evaluated based on how well it addresses user-specific aspects extracted from question narratives.

**Interpretation**: Responses are assessed regarding their alignment with user needs and preferences, aiming for personal relevance and accuracy.

**Baseline Results**: Multiple benchmarks using models like Gemma 2, Qwen 2.5, and GPT-4o-mini, with varying performance metrics reported.

**Validation**: Data was validated through human assessments and comparison of multiple evaluation strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: ['User data handling issues related to personalization']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open access under cc-by-sa 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
