# All-Angles Bench

## 📊 Benchmark Details

**Name**: All-Angles Bench

**Overview**: All-Angles Bench is a benchmark of over 2,100 human carefully annotated multi-view question-answer pairs across 90 diverse real-world scenes, designed to evaluate the multi-view understanding of Multi-Modal Large Language Models (MLLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VideoMME
- VSI-Bench
- MV-Bench

**Resources**:
- [Resource](https://danielchyeh.github.io/All-Angles-Bench/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the multi-view understanding capabilities of MLLMs.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Counting
- Attribute Identification
- Relative Distance
- Relative Direction
- Object Manipulation
- Camera Pose Estimation

**Limitations**: N/A

## 💾 Data

**Source**: Curated selection of 90 diverse multi-view scenes from Ego-Exo4D and EgoHumans datasets.

**Size**: 2,100 question-answer pairs

**Format**: JSON

**Annotation**: Manually annotated by human evaluators to ensure accuracy and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Performance was measured by comparing MLLM responses to the correct answers determined by human evaluators.

**Interpretation**: A higher accuracy indicates better multi-view understanding capabilities of the evaluated models.

**Baseline Results**: Human-level performance achieved 95.7% accuracy across tasks.

**Validation**: The benchmark was validated through extensive testing against representative MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
