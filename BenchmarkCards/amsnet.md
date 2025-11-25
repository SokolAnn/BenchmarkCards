# AMSNet

## 📊 Benchmark Details

**Name**: AMSNet

**Overview**: AMSNet is a dataset designed to facilitate the exploration of multimodal large language models (MLLMs) applications in Analog/Mixed-Signal (AMS) circuit generation by providing a comprehensive dataset delineating the schematic-netlist relationship.

**Data Type**: transistor-level schematics and SPICE format netlists

**Domains**:
- Electrical Engineering

**Languages**:
- English

**Resources**:
- [Resource](https://ams-net.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of AMSNet is to support automatic design generation of AMS circuits by providing a comprehensive dataset of schematics and their corresponding netlists.

**Target Audience**:
- ML Researchers
- Circuit Designers
- EDA Practitioners

**Tasks**:
- Circuit Generation
- Netlist Generation

**Limitations**: N/A

## 💾 Data

**Source**: Transistor-level schematics and corresponding SPICE format netlists created through an automatic technique for converting schematics into netlists

**Size**: N/A

**Format**: SPICE

**Annotation**: The data was collected through a combination of manual labeling and automatic detection processes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Component detection
- Net detection

**Metrics**:
- Accuracy

**Calculation**: Accuracy of component detection was measured by the proportion of correctly identified components against the total components labeled.

**Interpretation**: Accuracy is interpreted as the proportion of correct detections in both the component and netlist generation process.

**Baseline Results**: Component detection accuracy of 97.1% and net labeling accuracy of 96.7% were achieved during the dataset creation

**Validation**: The methodology has been tested by manually evaluating the accuracy of the trained models on labeled data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
