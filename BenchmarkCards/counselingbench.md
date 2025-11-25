# CounselingBench

## 📊 Benchmark Details

**Name**: CounselingBench

**Overview**: CounselingBench is a novel NCMHCE-based benchmark evaluating 22 general-purpose and medical-finetuned LLMs across five key competencies in mental health counseling. It systematically assesses how well LLMs can process and apply domain-specific knowledge from case studies to address questions evaluating these key competencies.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- CBT-BENCH

**Resources**:
- [GitHub Repository](https://github.com/cuongnguyenx/CounselingBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM performance in mental health counseling in alignment with essential competencies.

**Target Audience**:
- Mental Health Professionals
- AI Researchers
- Academics

**Tasks**:
- Question Answering

**Limitations**: Evaluating LLM competency via multiple-choice exams may not fully capture the complexities of real-world mental health counseling. The dataset may not adequately represent the diversity of situations encountered by mental health professionals.

## 💾 Data

**Source**: The National Clinical Mental Health Counseling Examination (NCMHCE) questions and case studies.

**Size**: 1612 unique questions across 138 case studies

**Format**: N/A

**Annotation**: Manually annotated by medical doctors specializing in psychiatry for competency mapping.

## 🔬 Methodology

**Methods**:
- Zero-shot
- Few-shot
- Chain-of-thought

**Metrics**:
- Accuracy
- F1 Score
- BERTScore

**Calculation**: Accuracy is calculated by comparing responses of the LLMs against the correct answers in the benchmark.

**Interpretation**: Higher scores indicate a better alignment with expert-level knowledge in mental health counseling. Models exceeding 63% accuracy are considered capable of passing the NCMHCE.

**Baseline Results**: gpt4o achieved a zero-shot accuracy of 78%, the best performing among tested models.

**Validation**: The benchmark was validated through comparison with human expert performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: The dataset includes case studies representing diverse ethnic and cultural backgrounds.

**Potential Harm**: Potential overreliance on AI systems could compromise patient care and erode therapeutic alliance.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
