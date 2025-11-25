# VM14K (First Vietnamese Medical Benchmark)

## 📊 Benchmark Details

**Name**: VM14K (First Vietnamese Medical Benchmark)

**Overview**: The first Vietnamese medical benchmark features 14,000 multiple-choice questions across 34 medical specialties, designed to evaluate the capabilities of language models in healthcare for non-English-speaking communities.

**Data Type**: multiple-choice questions

**Domains**:
- Healthcare

**Languages**:
- Vietnamese

**Similar Benchmarks**:
- MedQA
- MMLU Medical
- cMedQA2

**Resources**:
- [Resource](https://arxiv.org/abs/2506.01305)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the quality of language models in the medical domain for Vietnamese speakers and to foster multilingual standards in medical benchmarks.

**Target Audience**:
- Researchers
- Medical Practitioners
- AI Developers

**Tasks**:
- Medical Question Answering

**Limitations**: The benchmark primarily includes multiple-choice questions, which may not fully capture the complexities of clinical reasoning.

## 💾 Data

**Source**: Curated from verified medical textbooks, exams, and records.

**Size**: 14,000 questions

**Format**: JSON

**Annotation**: Annotated by medical experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Pass@k

**Calculation**: Metrics are calculated based on the percentage of correct answers across various difficulty levels.

**Interpretation**: A higher score indicates better performance of the language models in medical question answering.

**Baseline Results**: Various models were tested, specifics include performance metrics comparing multiple language models.

**Validation**: The benchmark was validated using responses from language models and agreements from medical experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: The benchmark includes questions across different specialties to ensure fairness and representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
