# RealVideoQuest

## 📊 Benchmark Details

**Name**: RealVideoQuest

**Overview**: RealVideoQuest is a benchmark designed to evaluate the capabilities of text-to-video (T2V) models in answering real-world, visually grounded user queries. It consists of 7.5K user queries with video response intents sourced from Chatbot-Arena and builds 4.5K high-quality query-video pairs through a multistage retrieval and refinement process.

**Data Type**: query-video pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Openvid-1m

**Resources**:
- [Resource](https://lmarena.ai/)

## 🎯 Purpose and Intended Users

**Goal**: To assess the quality and capabilities of text-to-video generation models in responding to complex user queries that necessitate visual demonstrations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text-to-Video Generation
- Question Answering

**Limitations**: The evaluation is constrained by the quality and diversity of retrieved YouTube videos, which may not fully represent ideal responses. Additionally, only a single video per query was evaluated, limiting capture of model variability.

## 💾 Data

**Source**: Chatbot-Arena

**Size**: 7,531 queries, 4,611 QA pairs

**Format**: N/A

**Annotation**: Manual annotation through a video intent recognizer using GPT-3.5-Turbo.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Relevance
- Correctness
- Coherence
- Completeness

**Calculation**: Each metric is rated on a scale from 0 to 4, evaluating the video’s quality in response to user queries.

**Interpretation**: Higher scores indicate better alignment and addressal of user queries by the generated videos.

**Baseline Results**: Various T2V models were evaluated, with notable challenges in correctly addressing user requests.

**Validation**: Results were validated through comparison against ground truth videos.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Only publicized YouTube URLs with their start and end timestamps to ensure indirect video information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
