# MMReason (Multi-Modal Multi-Step Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: MMReason (Multi-Modal Multi-Step Reasoning Benchmark)

**Overview**: MMReason is a new benchmark designed to precisely and comprehensively evaluate MLLM long-chain reasoning capability with diverse, open-ended, and challenging questions across various disciplines and difficulty levels.

**Data Type**: open-ended multi-step reasoning questions

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- MathVista
- MMMU
- OlympiadBench

**Resources**:
- [GitHub Repository](https://github.com/HJYao00/MMReason)

## 🎯 Purpose and Intended Users

**Goal**: To precisely and comprehensively evaluate long-chain reasoning capability of MLLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multi-Step Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Combines questions from existing benchmarks and newly collected questions from various educational levels.

**Size**: 2,941 instances

**Format**: N/A

**Annotation**: Questions annotated with detailed step-by-step solutions.

## 🔬 Methodology

**Methods**:
- Multi-model voting
- Reference-based scoring

**Metrics**:
- Final Answer Reasoning Accuracy
- Intermediate Steps Reasoning Score

**Calculation**: Scores based on a ternary scoring mechanism assessing correctness of intermediate steps.

**Interpretation**: Higher scores indicate better reasoning capabilities in both final answers and intermediate steps.

**Baseline Results**: GPT-4o achieves 25.7% final answer reasoning accuracy.

**Validation**: Results validated through multi-model comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
