# RT V -Bench

## 📊 Benchmark Details

**Name**: RT V -Bench

**Overview**: RT V -Bench is a fine-grained benchmark for MLLM real-time video analysis that assesses perception, understanding, and reasoning through multi-timestamp question answering with evolving answers as scenes change.

**Data Type**: video-question answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Video-MME
- MSRVTT
- MSVD-QA
- MovieChat-1k
- MVBench
- ActivityNet-QA
- Vstream-Q
- StreamBench
- OVO-Bench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the continuous analysis capabilities of Multimodal Large Language Models (MLLMs) in real-time video contexts.

**Target Audience**:
- Researchers
- Practitioners
- Model Developers

**Tasks**:
- Temporal Perception
- Scene Perception
- Visual Perception
- Future Prediction
- Phenomenological Understanding
- Intent Analysis
- Global Understanding
- Spatiotemporal Reasoning

**Limitations**: Most existing models show accuracy below 50%, and performance is not significantly improved by increasing model size or frame sampling rates.

## 💾 Data

**Source**: Videos sourced from the internet, including EgoSchema and publicly available online videos, with a manual review process.

**Size**: 552 videos (167.2 hours)

**Format**: N/A

**Annotation**: Manually annotated by experts to ensure robustness and target dynamic scenes and temporal reasoning.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Score

**Calculation**: Accuracy measures the proportion of correct answers, while Score evaluates the model's ability to answer advanced-level questions contingent upon mastering prerequisite basic questions.

**Interpretation**: Higher scores indicate better hierarchical reasoning and deeper comprehension capabilities.

**Validation**: Evaluations ensured through multiple rounds of review and manual QA pairs checking.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
