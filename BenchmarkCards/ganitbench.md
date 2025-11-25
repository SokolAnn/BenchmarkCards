# GanitBench

## 📊 Benchmark Details

**Name**: GanitBench

**Overview**: GanitBench is a bi-lingual benchmark consisting of 1527 vision-only questions covering several topics in Mathematics, available in English and Hindi. The questions are collected from major examinations in India, including the JEE Advanced and CBSE Boards, and involve visual contexts and reasoning analysis for Vision Language Models.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi

**Similar Benchmarks**:
- GSM8K
- MATH
- MathPrompter
- Geometry3k
- JEEBench
- NTSEBench
- Mathify
- OlympiadBench
- MathVista
- EXAMS-V

**Resources**:
- [Resource](https://jeeadv.ac.in/archive.html)
- [Resource](https://www.cbse.gov.in/cbsenew/question-paper.html)

## 🎯 Purpose and Intended Users

**Goal**: To provide a bilingual mathematical benchmark for evaluating reasoning capabilities in Vision Language Models across multiple mathematical disciplines.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Educational Researchers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Collected from JEE Advanced and CBSE Board Examination papers available in both English and Hindi.

**Size**: 1,527 images

**Format**: Image (JPEG, PNG)

**Annotation**: Manually curated with correct final answers and metadata filled in CSV format.

## 🔬 Methodology

**Methods**:
- Zero-Shot Chain-of-Thought (CoT)
- Two-Shot Chain-of-Thought (CoT)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as number of correct answers divided by the total number of questions.

**Interpretation**: An accuracy of 40% indicates a reasonable performance for the model on challenging mathematical questions.

**Validation**: Evaluated the performance of models under normal conditions and with a 'Double Lock' constraint.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: Analysis of results in both English and Hindi provided.

**Potential Harm**: ['Potential for biased evaluations based on language proficiency.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
