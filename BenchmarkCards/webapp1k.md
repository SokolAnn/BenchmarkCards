# WebApp1K

## 📊 Benchmark Details

**Name**: WebApp1K

**Overview**: WebApp1K is a novel benchmark for evaluating large language models (LLMs) in test-driven development (TDD) tasks, where test cases serve as both prompt and verification for code generation. It comprises 1000 diverse challenges across 20 application domains.

**Data Type**: code generation prompts and verification tests

**Domains**:
- Software Engineering

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/spaces/onekq-ai/WebApp1K-models-leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To identify key LLM capabilities for TDD task success and evaluate the performance of LLMs on TDD tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated using human-designed tasks across various application domains.

**Size**: 1000 tasks

**Format**: JSON

**Annotation**: Human-generated test cases and expected outputs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- pass@1
- pass@5
- pass@10

**Calculation**: Metrics are calculated based on the ratio of successful test passes to total test cases attempted.

**Interpretation**: Higher scores indicate better performance in generating correct code that passes the provided tests.

**Baseline Results**: N/A

**Validation**: Evaluation over multiple iterations on each task.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
