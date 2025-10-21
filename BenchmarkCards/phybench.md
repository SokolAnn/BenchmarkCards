# PHYBench

## 📊 Benchmark Details

**Name**: PHYBench

**Overview**: PHYBench is a benchmark of 500 original physics problems ranging from high school to Physics Olympiad difficulty. It addresses limitations in current evaluation frameworks by providing original content and a systematic curation pipeline for high-quality assessments.

**Data Type**: physics problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MathArena
- AIME 2024
- OlympiadBench
- GPQA

**Resources**:
- [Resource](https://www.phybench.cn/)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate models' reasoning capabilities using physics problems and to provide a platform for examining models' reasoning robustness.

**Target Audience**:
- ML Researchers
- Physics Educators
- AI Practitioners

**Tasks**:
- Reasoning Evaluation

**Limitations**: Focus primarily on Olympiad-level difficulty and uneven distribution across diverse physics topics.

## 💾 Data

**Source**: Curated from original physics exercises designed for human learners, with contributions from students and reviewers.

**Size**: 500 problems

**Format**: JSON

**Annotation**: Manual review and curation by expert physics educators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Expression Edit Distance (EED) Score

**Calculation**: EED Score is calculated based on the tree edit distance between model-generated and ground truth expressions.

**Interpretation**: The score reflects the correctness and similarity of model-generated expressions to reference answers, with higher scores indicating better performance.

**Baseline Results**: Gemini 2.5 Pro achieved 36.9% accuracy and an EED Score of 49.5.

**Validation**: The benchmark's performance was validated through evaluations against a human baseline consisting of undergraduate physics students.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Data contamination, Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
