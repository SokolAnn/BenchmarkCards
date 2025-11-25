# StreamingBench

## 📊 Benchmark Details

**Name**: StreamingBench

**Overview**: StreamingBench is the first comprehensive benchmark designed to evaluate the streaming video understanding capabilities of Multimodal Large Language Models (MLLMs). It consists of 900 videos and 4,500 human-curated QA pairs divided into 18 tasks, assessing real-time visual understanding, omni-source understanding, and contextual understanding.

**Data Type**: video-question-answer pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VStream-QA

**Resources**:
- [GitHub Repository](https://github.com/THUNLP-MT/StreamingBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to evaluate and facilitate advancements for MLLMs in achieving human-level streaming video comprehension and interaction.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Real-Time Visual Understanding
- Omni-Source Understanding
- Contextual Understanding

**Limitations**: N/A

## 💾 Data

**Source**: 900 YouTube videos across eight categories, covering diverse scenarios for streaming video understanding tasks.

**Size**: 900 videos and 4,500 question-answer pairs

**Format**: N/A

**Annotation**: Hybrid annotation pipeline; QA pairs are generated using GPT-4o and manually annotated by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Each question's accuracy is calculated based on the model's performance on the provided multiple-choice answers.

**Interpretation**: Results are interpreted as the percentage of questions answered correctly.

**Baseline Results**: Human performance average is reported at 91.66% across all tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
