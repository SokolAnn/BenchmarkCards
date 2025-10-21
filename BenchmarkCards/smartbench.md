# SmartBench

## 📊 Benchmark Details

**Name**: SmartBench

**Overview**: SmartBench is the first benchmark designed to evaluate the capabilities of on-device LLMs in Chinese mobile contexts, featuring 2973 question-answer pairs across five categories.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- CMRC
- CLUE
- C-Eval

**Resources**:
- [GitHub Repository](https://github.com/vivo-ai-lab/SmartBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized framework for evaluating on-device LLMs in Chinese mobile scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Summarization
- Text Q&A
- Information Extraction
- Content Creation
- Notification Management

**Limitations**: With advancements in technology, functions of on-device LLMs will evolve, and the current benchmark reflects capabilities up to December 2024.

## 💾 Data

**Source**: Constructed from open-source datasets, manual collections, and generated pairs using LLMs.

**Size**: 2,973 question-answer pairs

**Format**: N/A

**Annotation**: Constructed using screening open-source datasets and manual collection.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-as-a-Judge

**Metrics**:
- Accuracy
- Coherence
- Creativity
- Language quality

**Calculation**: Scores are assigned by an LLM (e.g. GPT-4 Turbo) that assesses responses against reference answers.

**Interpretation**: Scores reflect the model's performance in generating coherent and contextually appropriate responses.

**Baseline Results**: N/A

**Validation**: Evaluations conducted on multiple on-device LLMs across defined tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licenses for open-source datasets used in benchmark are provided in the appendix.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
