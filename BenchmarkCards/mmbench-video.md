# MMBench-Video

## 📊 Benchmark Details

**Name**: MMBench-Video

**Overview**: MMBench-Video introduces a quantitative benchmark designed to rigorously evaluate large vision-language models' proficiency in video understanding, incorporating lengthy videos from YouTube with free-form questions to assess temporal reasoning skills.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MSVD-QA
- MSRVTT-QA
- ActivityNet-QA

**Resources**:
- [Resource](https://huggingface.co/datasets/opencompass/MMBench-Video)
- [GitHub Repository](https://github.com/open-compass/VLMEvalKit)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of large vision-language models in video understanding using long-form, diverse video content.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Videos collected from YouTube, with questions and answers annotated by volunteers.

**Size**: 609 video clips, 1,998 question-answer pairs

**Format**: JSON

**Annotation**: Human-annotated by volunteers

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Scores range from 0 to 3 based on semantic similarity between model outputs and ground-truth answers.

**Interpretation**: A higher score indicates better alignment with human judgments for correctness.

**Baseline Results**: N/A

**Validation**: Evaluation includes a robust assessment of various LVLMs using the MMBench-Video dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
