# SWE-Bench

## 📊 Benchmark Details

**Name**: SWE-Bench

**Overview**: SWE-Bench is a benchmark designed to evaluate LLM-based repair systems using real issues and pull requests mined from 12 popular open-source Python repositories. It maintains public leaderboards for tracking progress and comparing solutions.

**Data Type**: issue instances for repair tasks

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- Defects4J

**Resources**:
- [GitHub Repository](https://github.com/SWE-bench/swe-bench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and compare Automated Program Repair techniques using real-world issues from popular Python repositories.

**Target Audience**:
- Researchers
- Developers
- Industry Practitioners

**Tasks**:
- Automated Program Repair

**Limitations**: N/A

## 💾 Data

**Source**: Issues and pull requests from 12 popular open-source Python repositories

**Size**: 2,294 instances

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Precision
- % Resolved

**Calculation**: Calculating precision as the percentage of resolved issues out of total attempts.

**Interpretation**: Higher precision indicates more effective automated repair solutions.

**Baseline Results**: N/A

**Validation**: Results validated using the public leaderboards for submitting repair solutions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
