# TouchStone

## 📊 Benchmark Details

**Name**: TouchStone

**Overview**: TouchStone is a comprehensive visual dialogue dataset that evaluates large vision-language models (LVLMs) across five major categories of abilities and 27 subtasks, focusing on both fundamental recognition and comprehension as well as literary creation.

**Data Type**: visual dialogue pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VisIT-Bench
- MMBench

**Resources**:
- [GitHub Repository](https://github.com/OFA-Sys/TouchStone)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation method for LVLMs by utilizing detailed image annotations and advanced LLMs as evaluators.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Visual Question Answering
- Image Captioning
- Visual Storytelling

**Limitations**: N/A

## 💾 Data

**Source**: Curated from open-world images and manually annotated with questions covering various dialogue abilities.

**Size**: 908 questions

**Format**: JSON

**Annotation**: Manual annotation and verification by experts

## 🔬 Methodology

**Methods**:
- Automated metrics using LLMs
- Human evaluation for consistency

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Scores are based on pairwise comparisons of generated dialogues against reference answers from a strong LLM.

**Interpretation**: Scores reflect the correctness, relevance, and usefulness of LVLM outputs compared to human preferences.

**Validation**: Results are validated through comparisons with human judgments and automated assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
