# OlympiadBench

## 📊 Benchmark Details

**Name**: OlympiadBench

**Overview**: OlympiadBench is an Olympiad-level bilingual multimodal scientific benchmark, featuring 8,476 problems from Olympiad-level mathematics and physics competitions, designed to assess the capabilities of large models in mathematical and physical reasoning.

**Data Type**: bilingual multimodal scientific problems

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MATH
- GSM8K
- MMMU

**Resources**:
- [GitHub Repository](https://github.com/OpenBMB/OlympiadBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capabilities of large models in mathematical and physical reasoning with a challenging benchmark.

**Target Audience**:
- ML Researchers
- AI Developers
- Education Researchers

**Tasks**:
- Mathematical Problem Solving
- Physics Problem Solving
- Multimodal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Problems sourced from International Olympiads, Chinese Olympiads, and the Chinese College Entrance Exam (GaoKao).

**Size**: 8,476 problems

**Format**: Markdown, images

**Annotation**: Expert-level annotations for step-by-step reasoning and problem type categorization.

## 🔬 Methodology

**Methods**:
- Automated scoring pipeline
- Human evaluation for theorem proving

**Metrics**:
- Average accuracy
- Error types analysis

**Calculation**: Accuracy based on percentage of correctly answered questions.

**Interpretation**: Lower scores indicate a greater challenge posed by the benchmark to models.

**Baseline Results**: The best-performing model, GPT-4V, achieved an average score of 17.97% on OlympiadBench.

**Validation**: Cross-validation with expert evaluations and automated scoring methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data derived should not have identifiable information due to use of official competition sources.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
