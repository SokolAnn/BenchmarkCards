# FIHA-v1

## 📊 Benchmark Details

**Name**: FIHA-v1

**Overview**: A benchmark for fine-grained hallucination evaluation in large vision-language models, utilizing Q&A pairs generated automatically without relying on LLMs or annotations.

**Data Type**: Q&A pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- NOPE
- AMBER
- HallusionBench

**Resources**:
- [Resource](https://anonymous.4open.science/r/FIHA-45BB)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate hallucinations in large vision-language models effectively.

**Target Audience**:
- Researchers
- Developers in AI and machine learning

**Tasks**:
- Assess hallucination levels in vision-language models
- Generate Q&A pairs for evaluation

**Limitations**: Does not evaluate non-visual inputs.

**Out of Scope Uses**:
- Application in real-time systems

## 💾 Data

**Source**: MSCOCO, Foggy dataset, Visual Genome

**Size**: N/A

**Format**: Q&A pairs

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Q&A pair generation from images
- Q&A pair generation from captions
- Dependency modeling using Davidson Scene Graph (DSG)

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- BERTScore

**Calculation**: Metrics calculated based on model responses to generated Q&A pairs.

**Interpretation**: Scores indicate the level of hallucinations detected in the models.

**Baseline Results**: N/A

**Validation**: Performance evaluated on multiple LVLMs with significant variations in results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data bias
- Output bias

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected aligns with privacy standards, minimizing personal data exposure.

**Data Licensing**: Open dataset, available for public use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Follows regulations concerning dataset usage.
