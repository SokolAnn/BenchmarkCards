# SciDA (Scientific Dynamic Assessor of LLMs)

## 📊 Benchmark Details

**Name**: SciDA (Scientific Dynamic Assessor of LLMs)

**Overview**: SciDA is a multidisciplinary benchmark consisting of over 1,000 Olympic-level numerical computation problems with randomized numerical initializations. It aims to mitigate data contamination and provide truthful assessments of the numerical reasoning capabilities of large language models.

**Data Type**: numerical computation problems

**Domains**:
- Natural Language Processing
- Science

**Languages**:
- English

**Similar Benchmarks**:
- GSM8k
- MATH
- MMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/m-a-p/SciDA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and challenging dynamic scientific benchmark allowing truthful assessments of LLMs' reasoning capabilities.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Numerical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Olympiad-level problems collected from competitions, university textbooks, and original problems.

**Size**: 1,000 problems

**Format**: N/A

**Annotation**: Annotated by enclosing variables within '$' symbols and functionalized into Python code.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the accuracy of LLMs in solving the benchmark problems.

**Interpretation**: Higher accuracy indicates better reasoning capabilities of LLMs.

**Baseline Results**: Initial accuracy rates of various models ranged from 20% to 50% under randomized initialization.

**Validation**: Benchmark validated through performance evaluations of leading LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
