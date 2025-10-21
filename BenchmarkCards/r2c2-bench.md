# R2C2-Bench

## 📊 Benchmark Details

**Name**: R2C2-Bench

**Overview**: R2C2-Bench is a more challenging repository-level code completion benchmark with training, validation, and testing splits designed to enhance the real-world repository-level code completion abilities of code Large Language Models.

**Data Type**: code completion samples

**Domains**:
- Computer Science

**Languages**:
- Python
- Java
- TypeScript
- C#

**Similar Benchmarks**:
- CrossCodeEval

**Resources**:
- [Resource](https://arxiv.org/abs/2406.01359)

## 🎯 Purpose and Intended Users

**Goal**: To enhance and benchmark the real-world repository-level code completion abilities of code Large Language Models.

**Target Audience**:
- ML Researchers
- Developers
- Industry Practitioners

**Tasks**:
- Code Completion

**Limitations**: N/A

## 💾 Data

**Source**: Permissively licensed repositories collected from GitHub with stars >= 3.

**Size**: 400,000 examples (100,000 per language)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- Edit Similarity (ES)

**Calculation**: Metrics are calculated based on the predictions vs. actual code completions.

**Interpretation**: Higher scores in EM and ES indicate better code completion accuracy.

**Baseline Results**: Results from various models are reported; for StarCoder-7B, best performance after fine-tuning is 40.3% EM and 70.0% ES.

**Validation**: Evaluated on validation and test splits of R2C2-Bench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
