# MedHallTune

## 📊 Benchmark Details

**Name**: MedHallTune

**Overview**: A large-scale benchmark designed specifically to evaluate and mitigate hallucinations in medical vision-language models, containing over 100,000 images and 1,000,000 instruction pairs.

**Data Type**: Multimodal

**Domains**:
- Healthcare
- Medical Imaging

**Languages**:
- English

**Similar Benchmarks**:
- Med-Halu
- Med-Halt
- MedVH
- MedHallMark
- Med-HVL
- CARES

**Resources**:
- [Resource](Dataset and Codes available at MedHallTune)

## 🎯 Purpose and Intended Users

**Goal**: To enhance and evaluate the ability of vision-language models to handle hallucinations in medical contexts.

**Target Audience**:
- Researchers
- Healthcare professionals

**Tasks**:
- Medical image captioning
- Clinical decision support
- Visual question answering

**Limitations**: N/A

**Out of Scope Uses**:
- Non-medical applications

## 💾 Data

**Source**: Sourced from well-annotated datasets including PubMed.

**Size**: Over 100,000 images and 1,000,000 instruction pairs

**Format**: Multimodal image and text pairs

**Annotation**: Ground-truth annotations for both hallucination and non-hallucination samples.

## 🔬 Methodology

**Methods**:
- Instruction-following data generation using GPT-4o
- Quality control mechanisms

**Metrics**:
- Clinical Accuracy
- Clinical Relevance
- Detail Level
- Risk Level

**Calculation**: Scores rated on a scale from 1 to 10.

**Interpretation**: Higher scores indicate better performance.

**Baseline Results**: Initial evaluations based on outputs from LLaVA-Med.

**Validation**: Evaluated using a testing split with hallucination and non-hallucination instruction pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Medical hallucination

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: Potential risks to patient diagnosis and treatment due to hallucinations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
