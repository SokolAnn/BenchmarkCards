# Dr.Academy

## 📊 Benchmark Details

**Name**: Dr.Academy

**Overview**: Dr.Academy is a benchmark developed to evaluate the questioning capability in education for Large Language Models (LLMs) through assessing the quality of generated educational questions based on Anderson and Krathwohl's taxonomy across various domains.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- SQuAD

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the questioning capability in education as a teacher for Large Language Models (LLMs) through assessing generated educational questions.

**Target Audience**:
- ML Researchers
- Educational Technologists

**Tasks**:
- Question Generation

**Limitations**: The benchmark primarily focuses on the questioning ability and does not encompass the full range of teaching interactions.

## 💾 Data

**Source**: Generated contexts from the SQuAD dataset and the MMLU dataset.

**Size**: 20,000 contexts

**Format**: text

**Annotation**: Manual evaluation conducted by experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Relevance
- Coverage
- Representativeness
- Consistency

**Calculation**: Scores are calculated based on the established metrics through evaluations performed by both automated systems and human assessors.

**Interpretation**: Higher scores indicate better educational quality and alignment with the educational taxonomy.

**Baseline Results**: N/A

**Validation**: Validated through comparative assessments with expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
