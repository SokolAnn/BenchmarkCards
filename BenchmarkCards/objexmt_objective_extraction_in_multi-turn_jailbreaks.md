# ObjexMT (Objective EXtraction in Multi-Turn jailbreaks)

## 📊 Benchmark Details

**Name**: ObjexMT (Objective EXtraction in Multi-Turn jailbreaks)

**Overview**: ObjexMT is a benchmark that isolates and measures an LLM’s ability to recover the base objective of a multi-turn jailbreak conversation and calibrate its confidence in that recovery.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hyunjun1121/ObjexMT_dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a test for LLM judges on their ability to extract objectives from multi-turn dialogues and evaluate their self-reported confidence.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Objective Extraction

**Limitations**: N/A

## 💾 Data

**Source**: SafeMTData_Attack600, SafeMTData_1K, MHJ, CoSafe

**Size**: 4,345 examples

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Expected Calibration Error (ECE)
- Brier Score
- Wrong@High-Conf

**Calculation**: Accuracy computed via LLM-judge semantic similarity to gold objectives, calibrated via a threshold derived from human-aligned data.

**Interpretation**: Higher accuracy and lower ECE indicate better performance in objective extraction and confidence calibration.

**Baseline Results**: claude-sonnet-4 achieves the highest accuracy (0.515) and calibration (ECE 0.296), while gpt-4.1 and Qwen3-235B-A22B-FP8 tie at 0.441 accuracy.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
