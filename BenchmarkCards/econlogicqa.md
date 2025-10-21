# EconLogicQA

## 📊 Benchmark Details

**Name**: EconLogicQA

**Overview**: EconLogicQA is a rigorous benchmark designed to assess the sequential reasoning capabilities of large language models (LLMs) within the intricate realms of economics, business, and supply chain management, focusing on the logical sequencing of interconnected events.

**Data Type**: multi-choice questions

**Domains**:
- Economics
- Business
- Supply Chain Management

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- Financial Language Understanding Evaluation (FLUE)
- AQA-Bench

**Resources**:
- [Resource](https://huggingface.co/datasets/yinzhu-quan/econ_logic_qa)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously assess the logical reasoning capabilities of LLMs within economics, business, and supply chain management contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering
- Logical Reasoning

**Limitations**: The effectiveness of the benchmark is currently validated using a specific dataset of economic news articles, which may limit generalizability.

## 💾 Data

**Source**: Curated from a wide range of business news articles from 2011 to 2022, sourced from Kaggle.

**Size**: 650 questions

**Format**: N/A

**Annotation**: Questions are generated using GPT-4 and refined through a rigorous human review process.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correctly sequenced events in the questions.

**Interpretation**: Higher accuracy indicates better performance in sequenced reasoning tasks within economic contexts.

**Baseline Results**: GPT-4-Turbo achieved the highest accuracy of 56.92% in the 1-shot scenario.

**Validation**: Evaluation of performance across various LLMs to assess their reasoning capabilities in economic scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is derived from public domain sources under CC0 Public Domain license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
