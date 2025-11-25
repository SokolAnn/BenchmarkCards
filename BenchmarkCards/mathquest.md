# MathQuest

## 📊 Benchmark Details

**Name**: MathQuest

**Overview**: MathQuest is a comprehensive mathematics dataset sourced from the 11th and 12th standard Mathematics NCERT textbooks, encompassing a wide range of mathematical challenges of varying complexity. It aims to enhance the mathematical problem-solving capabilities of large language models (LLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- GSM-8K
- DeepMind
- NumGLUE
- SimulEq

**Resources**:
- [GitHub Repository](https://github.com/midas-research/mathify)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the mathematical problem-solving capabilities of large language models through fine-tuning on a dataset that includes complex mathematical problems.

**Target Audience**:
- ML Researchers
- Educational Researchers
- Model Developers

**Tasks**:
- Mathematical Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from the 11th and 12th standard Mathematics NCERT textbooks.

**Size**: 223 samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Fine-tuning with LLaMA-2, WizardMath, and MAmmoTH

**Metrics**:
- Exact Match Accuracy

**Calculation**: Evaluation based on measuring the accuracy of generated answers against ground truth for various datasets.

**Interpretation**: Higher accuracy indicates better performance in solving mathematical problems.

**Baseline Results**: MAmmoTH-13B achieved the highest accuracy of 24.0% after fine-tuning on the MathQuest dataset.

**Validation**: Validation via performance evaluation on multiple datasets including MathQuest.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
