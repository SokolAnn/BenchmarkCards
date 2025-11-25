# Postcondition Testing Benchmark

## 📊 Benchmark Details

**Name**: Postcondition Testing Benchmark

**Overview**: This paper proposes a code LLM maturity model that utilizes a postcondition generation problem to assess a broader range of capabilities in code LLMs, augmenting the existing EvalPlus dataset to include postcondition testing.

**Data Type**: postcondition generation pairs

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- EvalPlus

**Resources**:
- [GitHub Repository](https://github.com/MatureModel/PostcondGen)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive assessment of code LLM maturity and capabilities through postcondition generation.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Code Generation
- Postcondition Generation

**Limitations**: The maturity model may not cover all possible scenarios and edge cases encountered in real-world programming tasks.

## 💾 Data

**Source**: Augmented EvalPlus Dataset

**Size**: 164 coding problems

**Format**: JSON

**Annotation**: Manual annotation with few-shot examples

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Correct Postcondition Count (CPC)
- Coverage@k (C@k)
- Bug Detection Rate (BDR)
- Bug Coverage Rate (BCR)

**Calculation**: Metrics were calculated based on the number of problems for which the code LLM generated correct postconditions.

**Interpretation**: Higher values indicate better performance in generating precise and accurate postconditions.

**Baseline Results**: Previous models evaluated against the original EvalPlus dataset.

**Validation**: The benchmark was validated through extensive evaluation of several open-sourced models using specific metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
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
