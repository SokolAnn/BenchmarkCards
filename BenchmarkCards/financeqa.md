# FinanceQA

## 📊 Benchmark Details

**Name**: FinanceQA

**Overview**: FinanceQA is a testing suite that evaluates LLMs’ performance on complex numerical financial analysis tasks that mirror real-world investment work.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinanceBench

**Resources**:
- [Resource](https://huggingface.co/datasets/AfterQuery/FinanceQA)

## 🎯 Purpose and Intended Users

**Goal**: To address the limitations of current LLMs in financial applications by providing a benchmark that emphasizes technical precision and analytical reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Finance Professionals

**Tasks**:
- Financial Analysis

**Limitations**: Limited to evaluating LLMs using solely tactical questions based on data from specific companies.

## 💾 Data

**Source**: Created by human annotators with experience at hedge funds, private equity firms, or investment banks based on primary financial documents.

**Size**: 9,078 questions

**Format**: N/A

**Annotation**: Manually verified and created by financial professionals who developed useful questions for their real-world work.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Exact correct matches for evaluating performance.

**Interpretation**: A score of 1 for correctly factored assumptions and lines of reasoning, 0 for incorrect matches.

**Baseline Results**: Top SOTA model, o1, performed at a ~48.7% accuracy rate.

**Validation**: Statistical significance tests were performed to validate improvements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
