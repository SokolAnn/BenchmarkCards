# BugCraft-Bench

## 📊 Benchmark Details

**Name**: BugCraft-Bench

**Overview**: BugCraft-Bench is a curated dataset of Minecraft crash bug reports, designed to evaluate the BugCraft framework, which automates the reproduction of crash bugs in Minecraft from user-submitted reports.

**Data Type**: text

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [Resource](https://bugcraft2025.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized dataset for evaluating automated game bug reproduction systems, specifically focusing on Minecraft crash bugs.

**Target Audience**:
- ML Researchers
- Game Developers
- Software Engineers

**Tasks**:
- Bug Reproduction
- Software Testing

**Limitations**: N/A

## 💾 Data

**Source**: Mojira, Minecraft's official bug tracker

**Size**: 86 examples

**Format**: JSON

**Annotation**: Manually verified by researchers to ensure reproducibility and quality.

## 🔬 Methodology

**Methods**:
- Manual evaluation of bug reproduction
- Automated metrics monitoring

**Metrics**:
- Accuracy
- Success Rate

**Calculation**: Success rate calculated as the percentage of bugs successfully reproduced out of total attempts.

**Interpretation**: A higher success rate indicates better automated reproduction capabilities.

**Baseline Results**: N/A

**Validation**: Validation conducted through manual reviews comparing generated steps against original bug reports.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-ShareAlike 4.0 International License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
