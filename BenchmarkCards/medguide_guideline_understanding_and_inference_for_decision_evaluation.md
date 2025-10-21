# MedGUIDE (Guideline Understanding and Inference for Decision Evaluation)

## 📊 Benchmark Details

**Name**: MedGUIDE (Guideline Understanding and Inference for Decision Evaluation)

**Overview**: MedGUIDE is a benchmark designed to evaluate whether Large Language Models (LLMs) can make diagnostic decisions in accordance with established medical guidelines, constructed from 55 decision trees curated from NCCN oncology protocols across 17 cancer types.

**Data Type**: multiple-choice questions

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- IFEval
- MMLU-Professional Medicine

**Resources**:
- [Resource](https://huggingface.co/datasets/MedGUIDE/MedGUIDE-MCQA-8K)
- [Resource](https://anonymous.4open.science/r/Submission-MedGUIDE-187A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the clinical reasoning abilities of LLMs grounded in standardized medical guidelines.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Clinical Decision-Making
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from 55 decision trees curated from NCCN oncology protocols across 17 cancer types.

**Size**: 7,747 high-quality multiple-choice questions

**Format**: JSON

**Annotation**: Annotated via a quality-based selection framework involving medical experts and LLM-as-a-judge models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Weighted Accuracy

**Calculation**: Weighted accuracy accounts for the difficulty of each multiple-choice question based on the number of answer options.

**Interpretation**: A higher weighted accuracy indicates better adherence to clinical decision-making guidelines.

**Baseline Results**: N/A

**Validation**: Evaluation involved 25 diverse LLM models across standard accuracy and weighted accuracy metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
