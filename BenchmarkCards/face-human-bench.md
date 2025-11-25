# FACE-HUMAN-BENCH

## 📊 Benchmark Details

**Name**: FACE-HUMAN-BENCH

**Overview**: The FACE-HUMAN-BENCH is a benchmark designed to evaluate the face and human understanding abilities of multi-modal assistants. It is constructed based on a hierarchical ability taxonomy and includes various evaluation problems derived from publicly available datasets in the face and human community.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMBench
- SEED-Bench
- LAMM

**Resources**:
- [Resource](https://face-human-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of multi-modal assistants in understanding faces and humans, enabling improvements in application contexts such as media forensics, social interaction, and more.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Facial Attribute Recognition
- Age Estimation
- Facial Expression Recognition
- Face Attack Detection
- Face Recognition
- Human Attribute Recognition
- Action Recognition
- Spatial Relation Understanding
- Social Relation Understanding
- Person Re-Identification
- Crowd Counting

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from 16 public datasets in the face and human community.

**Size**: Development set with 900 problems and test set with 1800 problems.

**Format**: N/A

**Annotation**: Semi-automatically generated with manual verification of problems.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Weighted accuracy of multiple-choice problems based on different abilities.

**Interpretation**: Higher scores indicate better performance in understanding faces and humans.

**Validation**: The benchmark was validated through comprehensive evaluations over various mainstream multi-modal large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
