# HIDDENBENCH (Assessing Collective Reasoning in Multi-Agent LLMs via Hidden Profile Tasks)

## 📊 Benchmark Details

**Name**: HIDDENBENCH (Assessing Collective Reasoning in Multi-Agent LLMs via Hidden Profile Tasks)

**Overview**: HIDDENBENCH is the first benchmark for evaluating collective reasoning in multi-agent LLMs, formalizing the Hidden Profile paradigm with 65 tasks to assess decision-making and information integration failures.

**Data Type**: text

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/YuxuanLi1225/HiddenBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reproducible framework for assessing collective reasoning capabilities in multi-agent LLMs and highlight systematic failures.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Collective Reasoning Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Generated tasks based on the Hidden Profile paradigm

**Size**: 65 tasks

**Format**: N/A

**Annotation**: Automatically generated with validation against the formal model

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Post-discussion accuracy is measured against pre-discussion accuracy to evaluate improvements in collective reasoning.

**Interpretation**: Higher post-discussion accuracy compared to pre-discussion indicates successful integration of distributed knowledge.

**Baseline Results**: N/A

**Validation**: Tasks validate if pre-discussion accuracy is ≥80% in the Full Profile condition and ≤20% in the Hidden Profile condition.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
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
