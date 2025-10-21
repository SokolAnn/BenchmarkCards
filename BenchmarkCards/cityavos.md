# CityAVOS

## 📊 Benchmark Details

**Name**: CityAVOS

**Overview**: CityAVOS is the first benchmark dataset for autonomous search of common urban objects, comprising 2,420 tasks across six object categories with varying difficulty levels to evaluate UAV agents’ search capabilities.

**Data Type**: task data involving object identification

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/CityAVOS-3DF8)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation benchmark for the Aerial Visual Object Search (AVOS) tasks in urban environments.

**Target Audience**:
- ML Researchers
- Robotics Researchers
- Urban Planning Experts

**Tasks**:
- Object Search

**Limitations**: N/A

## 💾 Data

**Source**: Developed based on the EmbodiedCity platform built on Unreal Engine 5.3, featuring high-fidelity simulations of urban environments.

**Size**: 2,420 tasks

**Format**: N/A

**Annotation**: Tasks involve searching for objects based on visual and textual cues without external guidance.

## 🔬 Methodology

**Methods**:
- Automated evaluation and empirical testing with UAV agents

**Metrics**:
- Success Rate (SR)
- Success Rate Weighted by Inverse Path Length (SPL)
- Mean Search Steps (MSS)
- Navigation Error (NE)

**Calculation**: Metrics are calculated based on the results of AVOS tasks where the UAV agent's performance is evaluated across defined success and efficiency criteria.

**Interpretation**: Higher SR and SPL indicate better search efficiency and accuracy in identifying target objects, while lower NE suggests optimal navigation.

**Validation**: Results validated through empirical testing against established baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
