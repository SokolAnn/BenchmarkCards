# MCITlib (Multimodal Continual Instruction Tuning Library and Benchmark)

## 📊 Benchmark Details

**Name**: MCITlib (Multimodal Continual Instruction Tuning Library and Benchmark)

**Overview**: MCITlib is a comprehensive code library designed for continual instruction tuning of Multimodal Large Language Models, including implementations of various algorithms and careful selection of benchmarks to facilitate research.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GQA
- VQAv2

**Resources**:
- [GitHub Repository](https://github.com/Ghy0501/MCITlib)

## 🎯 Purpose and Intended Users

**Goal**: Facilitate research in the Multimodal Continual Learning field by providing a unified implementation and evaluation protocol.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Captioning

**Limitations**: Current version limited in base model diversity and scale; experiments only on LLaV A-1.5-7B.

## 💾 Data

**Source**: Benchmarks include UCIT and MLLM-DCL, selected to minimize information leakage.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Mean Finetune Accuracy (MFT)
- Mean Final Accuracy (MFN)
- Mean Average Accuracy (MAA)
- Backward Transfer (BWT)

**Calculation**: Metrics are calculated as specified in the evaluation protocol in the paper.

**Interpretation**: Higher metrics indicate better performance in continual learning tasks.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
