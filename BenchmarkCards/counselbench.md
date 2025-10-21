# CounselBench

## 📊 Benchmark Details

**Name**: CounselBench

**Overview**: CounselBench is a large-scale benchmark developed to evaluate and stress-test large language models in realistic help-seeking mental health scenarios, consisting of two main components: COUNSEL-BENCH-EVAL with expert evaluations of answers and COUNSEL-BENCH-ADV for adversarial testing.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- MedMCQA

**Resources**:
- [GitHub Repository](https://github.com/llm-eval-mental-health/CounselBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a clinically grounded framework for benchmarking large language models in the context of mental health question answering.

**Target Audience**:
- ML Researchers
- Mental Health Professionals
- Model Developers

**Tasks**:
- Open-ended Question Answering
- Expert Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Questions sourced from the public forum CounselChat and evaluated by licensed mental health professionals.

**Size**: 2,000 evaluations

**Format**: N/A

**Annotation**: 100 licensed mental health professionals provided evaluations, span-level annotations, and written rationales.

## 🔬 Methodology

**Methods**:
- Expert evaluation
- Adversarial testing

**Metrics**:
- Overall Quality
- Empathy
- Specificity
- Medical Advice
- Factual Consistency
- Toxicity

**Calculation**: Metrics were calculated based on expert ratings on a 5-point or 4-point Likert scale, with specific categorizations for Medical Advice.

**Interpretation**: Higher scores indicate better performance in providing appropriate, empathetic, and informative responses to mental health queries.

**Baseline Results**: N/A

**Validation**: Expert evaluations were conducted by 100 licensed professionals across diverse mental health disciplines to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**

**Demographic Analysis**: N/A

**Potential Harm**: Potential harm from unauthorized medical advice, overgeneralization, and lack of empathy in responses.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from CounselChat was anonymized, and identifiers were removed prior to analysis.

**Data Licensing**: All data is sourced from MIT-licensed CounselChat dataset.

**Consent Procedures**: Human annotators provided informed consent for participation and data release.

**Compliance With Regulations**: The study was approved as exempt by the Institutional Review Board of the University of Southern California.
