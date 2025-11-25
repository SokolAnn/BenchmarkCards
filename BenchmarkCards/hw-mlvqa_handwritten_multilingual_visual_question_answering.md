# HW-MLVQA (Handwritten Multilingual Visual Question Answering)

## 📊 Benchmark Details

**Name**: HW-MLVQA (Handwritten Multilingual Visual Question Answering)

**Overview**: HW-MLVQA is a comprehensive benchmark designed for handwritten multilingual visual question answering, addressing the gap in multilingual document comprehension and the intricacy of handwriting. It enhances VQA systems' capabilities by enabling them to process and interpret handwritten questions across multiple languages.

**Data Type**: handwritten pages and question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Hindi

**Similar Benchmarks**:
- HW-SQuAD
- Bentham-QA

**Resources**:
- [Resource](https://arxiv.org/abs/2507.15655)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate pivotal advancements in multilingual handwritten document interpretation, fostering innovation and scholarly inquiry within this specialized domain.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of handwritten documents created from contexts drawn from the SQuAD and MLQA datasets, coupled with a web-based platform for transcription by volunteers.

**Size**: 1,600 handwritten pages and 2,400 question-answer pairs

**Format**: JSON

**Annotation**: Manual transcription by volunteers followed by an automatic annotation pipeline to generate and verify bounding boxes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score
- Average Normalized Levenshtein Similarity (ANLS)

**Calculation**: Metrics are calculated to evaluate the accuracy of generated answers and quality of evidence retrieval.

**Interpretation**: Higher scores indicate better performance in accurately answering questions and retrieving evidence from handwritten pages.

**Baseline Results**: Models evaluated include LLaMA 3.1 for text and Qwen2VL for vision-language tasks.

**Validation**: Rigorous verification of annotations and consistency checks during the annotation process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
