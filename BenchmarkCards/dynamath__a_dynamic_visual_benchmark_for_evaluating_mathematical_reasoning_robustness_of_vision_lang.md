# DYNAMATH: A DYNAMIC VISUAL BENCHMARK FOR EVALUATING MATHEMATICAL REASONING ROBUSTNESS OF VISION LANGUAGE MODELS

## 📊 Benchmark Details

**Name**: DYNAMATH: A DYNAMIC VISUAL BENCHMARK FOR EVALUATING MATHEMATICAL REASONING ROBUSTNESS OF VISION LANGUAGE MODELS

**Overview**: DYNAMATH is a dynamic visual math benchmark designed to evaluate the reasoning robustness of Vision-Language Models (VLMs) by generating diverse questions with varying visual and textual conditions from a set of high-quality seed questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MATHVISTA
- MATHVERSE
- MATH-V

**Resources**:
- [Resource](https://dynamath.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To assess the mathematical reasoning robustness of Vision-Language Models (VLMs) through a dynamic benchmark that generates a variety of problem instances from high-quality seed questions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Educators

**Tasks**:
- Mathematical Reasoning
- Visual Question Answering

**Limitations**: The current design limits the complexity of questions due to human curation efforts.

## 💾 Data

**Source**: Seed questions collected from visual math datasets and educational resources.

**Size**: 5,010 questions generated from 501 seed questions

**Format**: Python programs for dynamic question generation

**Annotation**: Annotated by college STEM students for creating concrete variants.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Average-case accuracy
- Worst-case accuracy
- Repetition consistency

**Calculation**: Average-case accuracy is calculated as the overall accuracy across all generated question variants; worst-case accuracy is the percentage of correctly answered seed questions across all variants.

**Interpretation**: High average-case accuracy and low worst-case accuracy indicate robustness weaknesses in VLMs.

**Baseline Results**: Comparison of various state-of-the-art VLMs with varying performance metrics.

**Validation**: Results validated through extensive experiments on 14 VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: Analysis on variations and robustness across problem types and difficulty levels.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
