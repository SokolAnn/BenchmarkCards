# FedOA (Federated Adapter on Foundation Models)

## 📊 Benchmark Details

**Name**: FedOA (Federated Adapter on Foundation Models)

**Overview**: FedOA is a novel framework that adapts invariant learning for out-of-distribution (OOD) generalization in Federated Foundation Models (FedFM) using adapter-based parameter-efficient fine-tuning methods to enhance OOD generalization through feature distance-based regularization.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FedIT

**Resources**:
- [Resource](https://arxiv.org/abs/2505.01075)

## 🎯 Purpose and Intended Users

**Goal**: To address OOD generalization in Federated Foundation Models using personalized adapters and feature distance-based regularization.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Constructed federated datasets derived from the Flan dataset, each centered around distinct tasks and designed for federated settings.

**Size**: 6000 training examples, 1200 testing examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on the performance of personalized models during the federated learning process.

**Interpretation**: Higher accuracy indicates better generalization performance on OOD tasks.

**Baseline Results**: FedOA demonstrated better OOD generalization than existing methods like FedIT, pFedMe, and FedLoRA.

**Validation**: FedOA was validated through empirical experiments on benchmark datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
