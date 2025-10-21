# WiCkeD (Wild-CardDistractor)

## 📊 Benchmark Details

**Name**: WiCkeD (Wild-CardDistractor)

**Overview**: WiCkeD is a method to increase the complexity of existing multiple-choice benchmarks by randomly replacing a choice with 'None of the above'. It can be automatically applied to any existing benchmark to evaluate true reasoning capabilities of models.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- MMLU-Pro
- Commonsense-QA
- TruthfulQA
- Arc-challenge

**Resources**:
- [GitHub Repository](https://github.com/ahmedselhady/wicked-benchmarks)

## 🎯 Purpose and Intended Users

**Goal**: To create challenging variants of existing MCQ benchmarks that better gauge the reasoning capabilities of large language models.

**Target Audience**:
- ML Researchers
- Practitioners

**Tasks**:
- Multiple Choice Question Answering

**Limitations**: WiCkeD's effectiveness may vary across benchmarks that require further verification. Closed models like GPT-4 and Claude were not evaluated.

## 💾 Data

**Source**: Existing multiple-choice benchmarks including MMLU, MMLU-Pro, Commonsense-QA, Truthful-QA, and Arc-challenge.

**Size**: 6 benchmarks

**Format**: Modified MCQ format

**Annotation**: Automatic selection of options to replace with 'None of the above'.

## 🔬 Methodology

**Methods**:
- Automated benchmarking
- Statistical analysis

**Metrics**:
- Accuracy

**Calculation**: Performance metrics calculated based on model responses to original vs. WiCkeD benchmarks.

**Interpretation**: A significant drop in performance indicates increased challenge and potential limitations in reasoning capabilities.

**Validation**: Validation through multiple experiments across different model families.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misalignment of model responses due to increased difficulty.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
