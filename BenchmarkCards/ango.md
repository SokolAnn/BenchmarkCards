# ANGO

## 📊 Benchmark Details

**Name**: ANGO

**Overview**: ANGO introduces a Chinese multi-choice question evaluation benchmark that uses Keypoint categorization for enhanced interpretability of evaluation results, with questions divided into 9 difficulty levels based on human performance.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- CMMLU
- AGI-Eval

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and reliable evaluation benchmark for generation-oriented language models in the Chinese domain.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Administrative Proficiency Test (AAT) used in the Chinese civil service examination, covering both official and mock exams conducted between 2008 and 2023.

**Size**: 71,149 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Dynamic length example sampling
- Few-shot evaluation strategies

**Metrics**:
- Accuracy
- Human Hit
- Human Value

**Calculation**: Metrics calculated based on model outputs in relation to human performance and accuracy for question categorization.

**Interpretation**: Results are compared against human performance to assess model accuracy and alignment with common misconceptions.

**Baseline Results**: Not specified

**Validation**: Dynamic updates to the test set and seasonal evaluations to ensure ongoing fairness and effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
