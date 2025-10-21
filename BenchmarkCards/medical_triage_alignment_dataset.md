# Medical Triage Alignment Dataset

## 📊 Benchmark Details

**Name**: Medical Triage Alignment Dataset

**Overview**: A novel medical triage decision-making dataset containing various scenarios labeled with Decision-Maker Attributes (DMAs) that influence human judgments.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- ETHICS
- MoralChoice
- MoCA

**Resources**:
- [GitHub Repository](https://github.com/ITM-Kitware/llm-alignable-dm)

## 🎯 Purpose and Intended Users

**Goal**: To quantify model alignment using a new attribute-dependent accuracy metric and to demonstrate LLMs as ethical decision-makers in medical triage.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- AI Ethics Researchers

**Tasks**:
- Decision-Making

**Limitations**: N/A

## 💾 Data

**Source**: Custom-written scenarios by cognitive scientists to elicit responses for various DMAs.

**Size**: 62 scenarios

**Format**: N/A

**Annotation**: Labeled by scenario authors and reviewed by at least one other researcher.

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Weighted self-consistency

**Metrics**:
- Alignment Accuracy

**Calculation**: Accuracy measures the selection of the correct choice(s), conditioned on a target attribute value (high or low).

**Interpretation**: High alignment accuracy indicates better alignment of LLM decisions to specified DMAs.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
