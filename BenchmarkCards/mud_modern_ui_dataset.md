# MUD (Modern UI Dataset)

## 📊 Benchmark Details

**Name**: MUD (Modern UI Dataset)

**Overview**: MUD is a large-scale and noise-filtered dataset for modern style UI modeling, comprising 18,000 human-annotated UIs collected from 3,300 apps.

**Data Type**: UI screenshots with view hierarchies

**Domains**:
- Human-Computer Interaction

**Languages**:
- English

**Similar Benchmarks**:
- Rico

**Resources**:
- [GitHub Repository](https://github.com/sidongfeng/MUD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for UI modeling that reflects modern design standards.

**Target Audience**:
- UI Researchers
- Machine Learning Researchers
- App Developers

**Tasks**:
- UI element detection
- UI retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Collected from popular Android apps using automated app exploration techniques.

**Size**: 18,132 unique UIs

**Format**: N/A

**Annotation**: Human annotation for validation of UI quality.

## 🔬 Methodology

**Methods**:
- Automated app exploration
- Human validation

**Metrics**:
- Activity coverage
- Average Precision (AP)

**Calculation**: Performance metrics calculated based on the accuracy of UI element detection and retrieval tasks.

**Interpretation**: Higher AP indicates better performance in detecting UI elements.

**Baseline Results**: Compared to the Rico dataset, MUD demonstrated a 10.5% improvement in average precision.

**Validation**: Manual validation of the collected UIs to ensure data quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
