# DStruct2Design (Data Structure Driven Generative Floor Plan Design)

## 📊 Benchmark Details

**Name**: DStruct2Design (Data Structure Driven Generative Floor Plan Design)

**Overview**: The benchmark facilitates the evaluation of floorplan generation models conditioned on numerical constraints, utilizing a new dataset and a structured representation of floorplans.

**Data Type**: JSON data structures representing floorplans

**Domains**:
- Architecture
- Generative Design

**Languages**:
- English

**Similar Benchmarks**:
- RPLAN
- ProcTHOR

**Resources**:
- [GitHub Repository](https://github.com/plstory/DS2D)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset and benchmarks specifically for the evaluation of floorplan generation models under numerical constraints.

**Target Audience**:
- ML Researchers
- Architecture Professionals

**Tasks**:
- Floorplan Generation

**Limitations**: N/A

## 💾 Data

**Source**: Merged datasets RPLAN and ProcTHOR-10k, converted into a structured JSON format for training and evaluation.

**Size**: 80,315 floorplans from RPLAN and 12,000 generated floorplans from ProcTHOR-10k

**Format**: JSON

**Annotation**: Automatically generated data structure from existing image-based datasets

## 🔬 Methodology

**Methods**:
- Metric-based evaluation
- Model-based evaluation

**Metrics**:
- Self Consistency Metrics
- Prompt Consistency Metrics
- Graph Edit Distance for Compatibility

**Calculation**: Metrics calculated involve comparison between generated floorplan attributes and specified constraints.

**Interpretation**: Higher scores in metrics indicate better adherence to specified constraints and correctness of generated structures.

**Baseline Results**: The best model variants demonstrate significant improvements over existing floorplan generation methods.

**Validation**: Validation data is utilized to measure the consistency of generated floorplans against specified constraints.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Societal Impact**: Impact on Jobs

**Demographic Analysis**: N/A

**Potential Harm**: ['Job displacement of architecture professionals']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data from the RPLAN dataset is anonymized to eliminate user and privacy information.

**Data Licensing**: ProcTHOR-10k dataset under Apache License 2.0. RPLAN dataset has redistribution restrictions.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
