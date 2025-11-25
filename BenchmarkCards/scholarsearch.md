# ScholarSearch

## 📊 Benchmark Details

**Name**: ScholarSearch

**Overview**: ScholarSearch is the first dataset specifically designed to evaluate the complex information retrieval capabilities of Large Language Models (LLMs) in academic research. It includes 223 high-quality questions that require multi-hop searches for resolution, ensuring the questions posed are genuinely challenging and cannot be easily solved by current state-of-the-art models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BrowseComp
- MMLU
- GPQA
- SuperGPQA

**Resources**:
- [Resource](https://huggingface.co/datasets/PKU-DS-LAB/ScholarSearch)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate LLMs' complex information retrieval skills in academic contexts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from publicly accessible online academic publications and websites.

**Size**: 223 questions

**Format**: N/A

**Annotation**: Questions were verified for uniqueness, source accessibility, and academic correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Answers are verified against a ground-truth reference.

**Interpretation**: An answer is deemed correct if the model's output closely matches the ground-truth reference.

**Baseline Results**: N/A

**Validation**: Questions were screened and revised based on difficulty criteria and expert review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
