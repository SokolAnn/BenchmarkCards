# TrajVL

## 📊 Benchmark Details

**Name**: TrajVL

**Overview**: TrajVL is the first benchmark dataset specifically designed for the Text-to-TrajVis domain, containing 18,140 (question, TVL) pairs aimed at transforming natural language questions into trajectory data visualizations.

**Data Type**: question-Trajectory Visualization Language (TVL) pairs

**Domains**:
- Natural Language Processing
- Data Visualization

**Languages**:
- English

**Similar Benchmarks**:
- nvBench
- Dial-NVBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for benchmarking the Text-to-TrajVis task, facilitating the translation of natural language queries into trajectory visualizations.

**Target Audience**:
- ML Researchers
- Data Visualization Practitioners

**Tasks**:
- Text-to-Visualization

**Limitations**: The dataset is limited to trajectory data from a single source (GeoLife project dataset), which may not cover all real-world spatio-temporal scenarios exhaustively.

## 💾 Data

**Source**: GeoLife project dataset

**Size**: 18,140 question-TVL pairs

**Format**: N/A

**Annotation**: Generated using Large Language Models with manual verification

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Visual Accuracy
- Axis Accuracy
- Data Accuracy
- Area Accuracy
- Time Accuracy
- SQL Accuracy
- TVL Accuracy

**Calculation**: Metrics are calculated based on the model's ability to accurately generate specified visual types, recognize geographic areas, and handle temporal information within generated TVLs.

**Interpretation**: Higher accuracy rates indicate better model performance in generating accurate and contextually appropriate trajectory visualizations from natural language inputs.

**Baseline Results**: Baseline performance established by multiple LLMs, with the highest achieving 74.61% TVL accuracy under normal conditions.

**Validation**: The model's evaluations involved multiple experiments with diverse LLMs under varying configurations to assess performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
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
