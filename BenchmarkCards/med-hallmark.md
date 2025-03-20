# Med-HallMark

## 📊 Benchmark Details

**Name**: Med-HallMark

**Overview**: The first benchmark specifically designed for hallucination detection and evaluation within the medical multimodal domain.

**Data Type**: medical image data

**Domains**:
- healthcare
- medical imaging

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/path-to-med-hallmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for detecting and evaluating hallucinations in large vision language models in medical applications.

**Target Audience**:
- Researchers
- Medical practitioners
- AI developers

**Tasks**:
- Evaluating hallucinations in medical contexts
- Assessing the performance of large vision language models

**Limitations**: Currently supports only English and may not cover all potential hallucination types in medical texts.

**Out of Scope Uses**:
- Non-medical applications
- General-purpose vision-language tasks

## 💾 Data

**Source**: Derived from datasets including Slake, VQA-RAD, MIMIC, and OpenI

**Size**: Data partitioned with 57.57% for Med-VQA and 42.43% for IRG

**Format**: N/A

**Annotation**: Detailed annotations for hallucination types, sentence-level assessments, and correctness of model outputs are provided.

## 🔬 Methodology

**Methods**:
- Multi-task hallucination support
- Multifaceted hallucination data
- Hierarchical hallucination categorization

**Metrics**:
- MediHall Score
- BERTScore
- METEOR
- ROUGE-1
- ROUGE-2
- BLEU

**Calculation**: MediHall Score is calculated by averaging scores derived from hallucination categorization across multi-dimensional tasks.

**Interpretation**: The MediHall Score offers insight into the severity and implications of hallucinations in medical contexts.

**Baseline Results**: Establishes baselines for popular LVLMs indicating their performance in hallucination detection.

**Validation**: Validation through extensive experimental evaluations across various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misrepresentation of medical information
- Clinical misdiagnosis due to hallucinations

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Potential Harm**: Potential harm includes misdiagnosis or misleading medical information leading to incorrect clinical decisions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sourced from publicly available medical datasets with privacy compliance.

**Data Licensing**: The textual content is provided under the CC-BY-4.0 license. Medical images are derived from open datasets and their licensing applies.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with the requirements of the source datasets regarding the use of medical images.
