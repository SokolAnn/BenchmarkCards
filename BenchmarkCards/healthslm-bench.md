# HealthSLM-Bench

## 📊 Benchmark Details

**Name**: HealthSLM-Bench

**Overview**: HealthSLM-Bench is a comprehensive benchmark that systematically evaluates nine state-of-the-art Small Language Models (SLMs) on eight health prediction tasks across three real-world mobile and wearable datasets, employing zero-shot, few-shot, and instruction fine-tuning approaches.

**Data Type**: health prediction tasks

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MobileAIBench

**Resources**:
- [Resource](https://arxiv.org/abs/2509.07260)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate Small Language Models for healthcare monitoring tasks across various datasets and deployment scenarios.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Stress Prediction
- Readiness Prediction
- Fatigue Monitoring
- Sleep Quality Estimation
- Depression Detection
- Anxiety Estimation
- Physical Activity Classification
- Calorie Estimation

**Limitations**: Challenges remain, particularly in handling class imbalance and few-shot scenarios.

## 💾 Data

**Source**: PMData, GLOBEM, AW-FB datasets, which provide health wearable sensor data.

**Size**: Three datasets with various examples and features for different health tasks.

**Format**: N/A

**Annotation**: Self-reported data and physiological data annotations for health statuses.

## 🔬 Methodology

**Methods**:
- Zero-shot learning
- Few-shot learning
- Instruction tuning

**Metrics**:
- Mean Absolute Error (MAE)
- Accuracy

**Calculation**: Mean Absolute Error (MAE) is calculated by the average magnitude of prediction errors. Accuracy is the proportion of correctly predicted instances.

**Interpretation**: Lower MAE values indicate better performance, while accuracy reflects general correctness.

**Baseline Results**: SLMs generally perform comparably or better than LLMs across health tasks.

**Validation**: Top-performing models were deployed on an iPhone 15 Pro Max for real-world efficiency evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis of demographic factors is performed based on the datasets used.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study enhances protection of sensitive personal data through on-device inference.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
