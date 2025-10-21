# WebWalkerQA

## 📊 Benchmark Details

**Name**: WebWalkerQA

**Overview**: WebWalkerQA is designed to assess the ability of Large Language Models (LLMs) to perform web traversal by evaluating their capacity to systematically extract high-quality data from a website’s subpages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education
- Conference
- Organization
- Game

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- Mind2Web
- WebArena
- AssistantBench

**Resources**:
- [GitHub Repository](https://github.com/Alibaba-NLP/WebAgent)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' web traversal abilities in complex, multi-step information-seeking tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The current dataset comprises 680 high-quality QA pairs, which is limited compared to some existing benchmarks.

## 💾 Data

**Source**: 680 question-answer pairs collected from various official websites across different domains.

**Size**: 680 examples

**Format**: JSON

**Annotation**: Combines initial LLM-based annotations followed by human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the evaluation of the correctness of answers against the ground truth.

**Interpretation**: A higher accuracy indicates a better ability of LLMs to perform web traversal and extract information.

**Baseline Results**: The best-performing LLMs achieved accuracies below 40% in web traversal tasks.

**Validation**: Performance is validated through both quantitative and qualitative metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
