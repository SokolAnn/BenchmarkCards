# FaceXBench

## 📊 Benchmark Details

**Name**: FaceXBench

**Overview**: FaceXBench is a comprehensive benchmark designed to evaluate Multimodal Large Language Models (MLLMs) on complex face understanding tasks, comprising 5,000 multimodal multiple-choice questions derived from public datasets and a newly created dataset, FaceXAPI.

**Data Type**: multimodal multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMMU
- MM-Bench
- SEED-Bench
- MMAU

**Resources**:
- [Resource](https://kartik-3004.github.io/facexbench/)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the face understanding capabilities of MLLMs across various tasks and identify their limitations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Age Estimation
- Gender Prediction
- Race Estimation
- High-Resolution Face Recognition
- Low-Resolution Face Recognition
- Celebrity Identification
- Face Anti-Spoofing
- Deepfake Detection
- Attributes Prediction
- Facial Expression Recognition
- Headpose Estimation
- Crowd Counting
- Face Parsing
- Face Tools Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Derived from 25 public datasets and includes the newly created dataset FaceXAPI.

**Size**: 5,000 questions, 10,441 unique face images

**Format**: JSON

**Annotation**: Carefully and manually filtered VQA-type questions.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: No specific calculation details mentioned.

**Interpretation**: The benchmark scores indicate the models' capabilities across various face understanding tasks.

**Validation**: Extensive evaluation of 26 open-source MLLMs and 2 proprietary models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

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
