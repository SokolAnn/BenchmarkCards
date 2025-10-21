# MedConceptsQA

## 📊 Benchmark Details

**Name**: MedConceptsQA

**Overview**: MedConceptsQA is an open-source benchmark for evaluating the understanding and reasoning abilities of Large Language Models on medical concepts across diagnoses, procedures, and drugs. It includes over 800,000 questions categorized into various difficulty levels.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- BioASQ-QA
- EmrQA
- PubMedQA

**Resources**:
- [Resource](https://huggingface.co/datasets/ofir408/MedConceptsQA)
- [GitHub Repository](https://github.com/nadavlab/MedConceptsQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the understanding and reasoning capabilities of Large Language Models regarding medical concepts.

**Target Audience**:
- Research Scientists
- ML Researchers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MedConceptsQA benchmark database comprising over 800,000 medical concept Q&A.

**Size**: 800,000 questions

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Zero-shot learning
- Few-shot learning

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the proportion of correctly answered questions among the total number of questions.

**Interpretation**: Higher accuracy indicates better understanding and reasoning of medical concepts by the evaluated models.

**Baseline Results**: GPT-4 achieves the highest accuracy among all models tested.

**Validation**: Evaluations conducted on various medical concept questions across difficulty levels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
