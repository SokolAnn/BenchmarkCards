# MedExQA (Medical Question Answering Benchmark with Multiple Explanations)

## 📊 Benchmark Details

**Name**: MedExQA (Medical Question Answering Benchmark with Multiple Explanations)

**Overview**: This paper introduces MedExQA, a novel benchmark in medical question-answering, to evaluate large language models’ (LLMs) understanding of medical knowledge through explanations. By constructing datasets across five distinct medical specialties that are underrepresented in current datasets and further incorporating multiple explanations for each question-answer pair, it addresses a major gap in current medical QA benchmarks.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- MedQA
- MedMCQA

**Resources**:
- [GitHub Repository](https://github.com/knowlab/MedExQA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a comprehensive evaluation of LLMs' ability to generate nuanced medical explanations and improve understanding of medical knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Healthcare Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually collected from diverse freely accessible online sources, including mock tests and online exams tailored to each medical professional specialty.

**Size**: 965 questions

**Format**: N/A

**Annotation**: Data was manually validated to ensure the explanations provided comprehensible reasoning for the correct answers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- METEOR
- BERTScore

**Calculation**: Metrics were calculated based on the relationship between generated responses and reference responses, considering both classification accuracy and explanation generation performance.

**Interpretation**: Higher scores indicate better performance of models in generating accurate and coherent explanations.

**Baseline Results**: MedPhi-2 outperformed medical LLMs based on Llama2-70B in generating explanations.

**Validation**: Human evaluation was conducted on a small scale using three annotators assessing the quality of generated explanations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-Non Commercial-ShareAlike 4.0 International License for MedExQA, MIT license for MedPhi-2.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
