# NegBench

## 📊 Benchmark Details

**Name**: NegBench

**Overview**: NegBench is a benchmark designed to evaluate negation understanding across various task variations and examples in image, video, and medical datasets. It consists of two core tasks: Retrieval with Negation and Multiple Choice Questions with Negated Captions.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- CREPE
- CC-Neg

**Resources**:
- [Resource](https://NegBench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate negation understanding in vision-language models (VLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text-to-Image Retrieval
- Multiple Choice Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Various datasets adapted for the benchmark, including COCO, VOC2007, MSR-VTT, and CheXpert.

**Size**: 79,239 samples

**Format**: N/A

**Annotation**: Generated captions using LLaMA for linguistic diversity and verified with object detectors.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evaluation on Retrieval and MCQ tasks

**Metrics**:
- Accuracy
- Recall

**Calculation**: Metrics are calculated based on retrieval success rates and accuracy of selected answers in MCQ tasks.

**Interpretation**: Higher performance on these tasks indicates better understanding of negation by models.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
