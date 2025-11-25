# BizBench: A Quantitative Reasoning Benchmark for Business and Finance

## 📊 Benchmark Details

**Name**: BizBench: A Quantitative Reasoning Benchmark for Business and Finance

**Overview**: BizBench is a benchmark for evaluating models’ ability to reason about realistic financial problems, comprising eight quantitative reasoning tasks focusing on question-answering (QA) over financial data via program synthesis.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinQA
- TAT-QA
- ConvFinQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the development of better models for business and finance by evaluating financial quantitative reasoning.

**Target Audience**:
- ML Researchers
- Finance Professionals
- AI Developers

**Tasks**:
- Question Answering
- Code Generation
- Quantity Extraction

**Limitations**: The benchmark does not span the entire domains of business and finance and currently only contains English text.

## 💾 Data

**Source**: Derived from financial datasets and annotated by financial professionals.

**Size**: 8 tasks across various datasets including 8,845 data points for SEC-Num

**Format**: mixed-format including tables and natural language questions

**Annotation**: Combination of manual annotation by financial professionals and code generation by LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Program synthesis evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is measured by comparing model-generated outputs with ground truth reference values.

**Interpretation**: An answer is considered correct if it is within 1% of the reference output.

**Baseline Results**: GPT-4 achieved significant improvements in performance on BizBench tasks.

**Validation**: Validation was performed via comparison against ground truth answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data primarily consists of public records under strict government regulations.

**Data Licensing**: Not Applicable

**Consent Procedures**: All annotators were informed of and consented to the intended use of their data.

**Compliance With Regulations**: Not Applicable
