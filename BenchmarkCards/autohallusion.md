# AUTOHALLUSION

## 📊 Benchmark Details

**Name**: AUTOHALLUSION

**Overview**: The first automated benchmark generation approach that employs several key strategies to create a diverse range of hallucination examples in vision-language models.

**Data Type**: visual-question pairs

**Domains**:
- vision-language models

**Languages**:
- N/A

**Similar Benchmarks**:
- CHAIR
- POPE
- OpenCHAIR
- HalluionBench
- Hal-Eval
- CorrelationQA

**Resources**:
- [GitHub Repository](https://github.com/wuxiyang1996/AutoHallusion)

## 🎯 Purpose and Intended Users

**Goal**: To create hallucination benchmarks automatically and evaluate LVLMs against these benchmarks.

**Target Audience**:
- Researchers in AI and machine learning
- Practitioners in computer vision

**Tasks**:
- Evaluating hallucination rates
- Improving reliability of vision-language models

**Limitations**: The inability to explore attributes of objects aside from existence and spatial relations.

**Out of Scope Uses**:
- Non-hallucination related benchmarks

## 💾 Data

**Source**: Generated synthetic and real-world datasets

**Size**: 200 synthetic, 126 real-world

**Format**: visual-question pairs

**Annotation**: Manually inspected for performance evaluation

## 🔬 Methodology

**Methods**:
- Scene generation
- Image manipulation
- Question construction
- Hallucination detection

**Metrics**:
- Manipulation Attack Success Rate (MASR)
- Conflict Attack Success Rate (CASR)
- Overall Attack Success Rate (ASR)

**Calculation**: Success rates are calculated based on correctness and consistency of model responses.

**Interpretation**: Interested in probing hallucination rates based on various attack strategies.

**Baseline Results**: Success rates of LVLMs on benchmarks created by AUTOHALLUSION

**Validation**: Validated through comparison with ground-truth answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal data was used during the benchmark creation.

**Data Licensing**: Generated images from DALL-E and COCO dataset are under respective licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
