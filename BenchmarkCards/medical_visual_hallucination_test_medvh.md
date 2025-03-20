# Medical Visual Hallucination Test (MedVH)

## 📊 Benchmark Details

**Name**: Medical Visual Hallucination Test (MedVH)

**Overview**: The MedVH benchmark dataset is designed to evaluate the hallucination of domain-specific Large Vision Language Models (LVLMs) in the medical context, comprising five tasks that assess visual and textual understanding along with long text generation.

**Data Type**: Text and images

**Domains**:
- Healthcare
- Medical Imaging

**Languages**:
- English

**Similar Benchmarks**:
- RAD-VQA
- SLAKE
- PMC-VQA
- MIMIC-Diff-VQA
- Path-VQA

**Resources**:
- [GitHub Repository](https://github.com/dongzizhu/MedVH)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the hallucination capabilities of LVLMs in the medical context.

**Target Audience**:
- Researchers
- Healthcare Professionals
- AI Developers

**Tasks**:
- Multi-choice Visual Question Answering (MC-VQA)
- Medical Report Generation
- False Confidence Justification

**Limitations**: Existing models show susceptibility to hallucinations despite accuracy in standard tasks.

**Out of Scope Uses**:
- General application outside of medical context

## 💾 Data

**Source**: Constructed from various publicly available datasets including MIMIC-CXR, RAD-VQA, and others.

**Size**: 500 questions from four public medical VQA datasets.

**Format**: JSON

**Annotation**: Medical text and images with corresponding questions and answers.

## 🔬 Methodology

**Methods**:
- Multi-choice question answering
- Long text generation

**Metrics**:
- Accuracy on hallucination tasks (acch)
- Baseline accuracy (accb)
- Characterization score (char_score)

**Calculation**: Characterization score is a weighted harmonic mean of hallucination accuracy and baseline accuracy.

**Interpretation**: Higher scores indicate better resistance to hallucinations while maintaining accuracy.

**Baseline Results**: N/A

**Validation**: Comparison with existing benchmarks (e.g., MC-VQA tasks).

## ⚠️ Targeted Risks

**Risk Categories**:
- Data contamination
- Unrepresentative data
- Poor model accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: Susceptibility to hallucinations can lead to misdiagnosis or inappropriate treatment plans.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All patient data has been anonymized to comply with HIPAA standards.

**Data Licensing**: Dataset constructed from publicly available sources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
