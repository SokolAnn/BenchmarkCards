# HARP (Human Annotated Reasoning Problems for Math)

## 📊 Benchmark Details

**Name**: HARP (Human Annotated Reasoning Problems for Math)

**Overview**: HARP consists of 5,409 math problems from US national math competitions focusing on challenging reasoning. It includes multiple choice options and multiple human-written solutions, aiming to evaluate models on difficult math reasoning tasks.

**Data Type**: short answer and multiple choice problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8k
- Omni-MATH

**Resources**:
- [GitHub Repository](https://github.com/aadityasingh/HARP)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging benchmark for evaluating math reasoning capabilities of large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Math Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Problems sourced from A(J)HSME, AMC, AIME, and USA(J)MO competitions available on the AoPS Wiki.

**Size**: 5,409 problems (4,780 short answer, 4,110 multiple choice)

**Format**: Various (including JSON, CSV)

**Annotation**: Human-annotated difficulty levels and subject labels.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluations
- Few-shot evaluations

**Metrics**:
- Accuracy
- Pass@k

**Calculation**: Accuracy calculated based on the percentage of correctly solved problems out of total problems.

**Interpretation**: Higher accuracy indicates better performance on the benchmark.

**Baseline Results**: N/A

**Validation**: Models evaluated across multiple dimensions of difficulty and subjects.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
