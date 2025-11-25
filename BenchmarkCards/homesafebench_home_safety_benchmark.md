# HOMESAFEBENCH (Home Safety Benchmark)

## 📊 Benchmark Details

**Name**: HOMESAFEBENCH (Home Safety Benchmark)

**Overview**: HOMESAFEBENCH is a benchmark for evaluating safety inspection performance of embodied Vision-Language Models (VLMs) under free exploration with visual feedback. It provides 12,900 dynamic first-person perspective images from simulated home environments, covering five common home safety hazards: fire, electric shock, falling object, trips, and child safety.

**Data Type**: first-person perspective images

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of embodied VLMs in identifying safety hazards in home environments through dynamic, exploratory tasks.

**Target Audience**:
- ML Researchers
- Domain Experts
- VLM Developers

**Tasks**:
- Safety Hazard Identification

**Limitations**: Existing VLMs are demonstrated to have significant limitations in performing safety inspections accurately.

## 💾 Data

**Source**: Generated using the VirtualHome simulation environment combining manual annotation and rule-based generation.

**Size**: 12,900 instances

**Format**: N/A

**Annotation**: Human annotation and rule-based generation.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated by comparing the reported hazards against the ground-truth hazards using precision, recall, and F1 scores.

**Interpretation**: A hazard is considered correctly reported if both its category and the name of the associated item are correct.

**Baseline Results**: Current VLMs achieved significantly low performance scores, with even the best-performing model scoring below 20% across Precision, Recall, and F1.

**Validation**: Ensured through human reviews and quality control during data construction.

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

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
