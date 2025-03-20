# MedHEval

## 📊 Benchmark Details

**Name**: MedHEval

**Overview**: MedHEval is a benchmark designed to systematically evaluate hallucinations and mitigation strategies in medical large vision-language models (Med-LVLMs) by categorizing hallucinations into three underlying causes: visual misinterpretation, knowledge deficiency, and context misalignment.

**Data Type**: medical visual question answering (VQA)

**Domains**:
- Medical Imaging
- Radiology

**Languages**:
- English

**Similar Benchmarks**:
- MedVH
- CARES
- Med-HallMark
- MedHallBench

**Resources**:
- [GitHub Repository](GitHub: https://github.com/Aofei-Chang/MedHEval)

## 🎯 Purpose and Intended Users

**Goal**: To establish a standardized framework for evaluating and mitigating medical hallucinations, guiding the development of more trustworthy Med-LVLMs.

**Target Audience**:
- AI researchers
- Medical professionals
- Data scientists

**Tasks**:
- Evaluating hallucinations
- Testing mitigation strategies
- Improving Med-LVLM reliability

**Limitations**: None

## 💾 Data

**Source**: Comprises diverse medical datasets including SLAKE, VQA-RAD, IU-Xray, MIMIC-CXR, and MIMIC-IV.

**Size**: 15,976 VQA pairs

**Format**: VQA pairs generated as close-ended and open-ended questions

**Annotation**: Automatically annotated using various medical benchmarks.

## 🔬 Methodology

**Methods**:
- Visual grounding techniques
- Contrastive decoding

**Metrics**:
- Accuracy
- Hallucination rates
- CheXbert
- RadGraph
- RaTEScore

**Calculation**: Evaluation based on accuracy and hallucination metrics

**Interpretation**: Higher accuracy indicates better performance in resisting hallucinations.

**Validation**: Cross-validation across various medical models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Visual misinterpretation
- Knowledge deficiency
- Context misalignment

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data source ensures privacy for participants through de-identification.

**Data Licensing**: All datasets are publicly available under defined licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adheres to ethical standards in medical data usage.
