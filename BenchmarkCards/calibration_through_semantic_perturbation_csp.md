# Calibration through Semantic Perturbation (CSP)

## 📊 Benchmark Details

**Name**: Calibration through Semantic Perturbation (CSP)

**Overview**: CSP is a novel framework for training Vision-Language Models (VLMs) to improve object-level verbalized confidence calibration by simulating visual uncertainty through semantic perturbations.

**Data Type**: image-query-response pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- AMBER

**Resources**:
- [Resource](https://arxiv.org/abs/2504.14848)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework that enhances the reliability and interpretability of VLMs through improved confidence calibration in response to object-centric queries.

**Target Audience**:
- ML Researchers
- Model Developers
- Data Scientists

**Tasks**:
- Object Detection
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Modified RLAIF dataset augmented with semantic perturbations for training.

**Size**: N/A

**Format**: N/A

**Annotation**: Confidence labels assigned based on the level of visual noise introduced.

## 🔬 Methodology

**Methods**:
- Supervised Fine-tuning
- Preference Optimization

**Metrics**:
- Accuracy
- F1 Score
- Expected Calibration Error (ECE)

**Calculation**: Evaluation metrics calculated based on model predictions compared with ground truth from confidence-labeled samples.

**Interpretation**: Increased accuracy and F1 Score indicate better calibration and task alignment, while lower ECE reflects improved confidence accuracy.

**Baseline Results**: Models trained using CSP show accuracy improvements from 70.1% to 73.6% in AMBER.

**Validation**: Extensive validation through experiments on benchmark datasets POPE and AMBER.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License for POPE and Apache License for AMBER.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
