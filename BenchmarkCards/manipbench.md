# ManipBench

## 📊 Benchmark Details

**Name**: ManipBench

**Overview**: ManipBench is a novel open-source benchmark to evaluate the low-level robot manipulation reasoning capabilities of Vision-Language Models (VLMs) through multiple-choice questions covering various dimensions of robotic manipulation. It includes 12,617 questions across different tasks.

**Data Type**: multiple-choice questions

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- NEWTON
- PhysBench
- VLABench

**Resources**:
- [Resource](https://manipbench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate Vision-Language Models for predicting robot actions and identify the best models for robotic manipulation tasks.

**Target Audience**:
- Researchers in Robotics
- Machine Learning Practitioners
- Model Developers

**Tasks**:
- Low-Level Robot Manipulation Reasoning

**Limitations**: Due to limited resources, not all possible model variants were evaluated. The benchmark does not cover all aspects of manipulation and lacks emphasis on high-level task planning.

## 💾 Data

**Source**: Generated from real-world robotic manipulation data, in-house fabric manipulation datasets, and simulation environments.

**Size**: 12,617 questions

**Format**: N/A

**Annotation**: Questions are based on pre-processed data from various sources, including annotated images and pre-trained trajectories.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Measured the percentage of correct answers from models on multiple-choice questions.

**Interpretation**: Higher accuracy indicates better reasoning capabilities of VLMs in robotic manipulation tasks.

**Validation**: Evaluation against human performance on a subset of questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
