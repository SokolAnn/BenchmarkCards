# FAULTY MATH

## 📊 Benchmark Details

**Name**: FAULTY MATH

**Overview**: The F AULTY MATH dataset includes faulty math problems of rich diversity: multiple mathematical categories, varying levels of difficulty, and different origins of faultiness. It is designed to evaluate the reasoning abilities of large language models (LLMs) in mathematical problem-solving.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH

**Resources**:
- [GitHub Repository](https://github.com/JunyiYe/FaultyMathProblem)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of LLMs to identify faulty math problems and transition from blind solvers to logical thinkers.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated from the MATH dataset using GPT-4 and verified by human annotators.

**Size**: 363 examples

**Format**: JSON

**Annotation**: Human annotation for verification of the problems.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Auto-evaluation using LLMs

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics were calculated based on the proportion of correctly identified faulty problems against total problems.

**Interpretation**: Higher accuracy indicates better performance in recognizing faulty math problems.

**Baseline Results**: Gemini-1.5-Pro achieved 33.33% accuracy on faulty math problems without hints.

**Validation**: Validation involved multiple iterations of evaluation against a gold standard established by human reviewers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
