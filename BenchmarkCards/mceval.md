# MCEVAL

## 📊 Benchmark Details

**Name**: MCEVAL

**Overview**: MCEVAL is the first benchmark dataset and evaluation metrics specifically tailored for LLM-assisted motion control code, comprising 186 motion control programming tasks of varying complexity.

**Data Type**: motion control programming tasks

**Domains**:
- Industrial Automation

**Languages**:
- Python

**Resources**:
- [GitHub Repository](https://github.com/MCCodeAI/MCCoder)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MCEVAL is to provide a benchmark for evaluating the effectiveness and safety of generated motion control code using LLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Code Generation

**Limitations**: MCEVAL is currently limited to the WMX3 library with Python; future work will include more libraries and programming languages.

## 💾 Data

**Source**: The MCEVAL dataset was constructed by verifying each task manually and through soft-motion simulations.

**Size**: 186 tasks

**Format**: N/A

**Annotation**: Each task is defined by a TaskId, Instruction, CanonicalCode, and Difficulty.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- First Time Pass Rate (FTPR)
- MatchEndPoints
- Dynamic Time Warping (DTW)

**Calculation**: FTPR is calculated as the percentage of codes that pass on the first attempt.

**Interpretation**: High FTPR indicates effective code generation, especially for complex motion control tasks.

**Baseline Results**: MCCoder outperformed the baseline models, showing an overall FTPR improvement of 33.09% and 131.77% for more complex tasks.

**Validation**: Validation procedure was conducted through soft-motion simulations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
