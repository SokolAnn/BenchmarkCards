# Video Thinking Test (Video-TT)

## 📊 Benchmark Details

**Name**: Video Thinking Test (Video-TT)

**Overview**: Video-TT assesses the correctness and robustness of video large language models in understanding complex real-world videos, specifically addressing the ability to interpret visual narratives and handle adversarial conditions.

**Data Type**: video-question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MVBench
- VideoMME

**Resources**:
- [Resource](https://zhangyuanhan-ai.github.io/video-tt/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for video language models regarding their understanding of complex narratives and their robustness in adversarial settings.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 1,000 YouTube Shorts videos, each with one main question and four related adversarial questions.

**Size**: 1,000 videos with 5,000 questions

**Format**: Video

**Annotation**: Structured by human annotators focusing on visual and narrative complexity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Robustness

**Calculation**: Accuracy is based on the percentage of correct answers across various question types.

**Interpretation**: Higher accuracy indicates better performance of models in understanding video content compared to human benchmarks.

**Baseline Results**: Human performance at 84.3% accuracy; models significantly lag behind.

**Validation**: The benchmark was tested against several leading video LLMs to validate its efficacy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
