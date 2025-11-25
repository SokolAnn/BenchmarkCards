# GTFS Understanding and Retrieval

## 📊 Benchmark Details

**Name**: GTFS Understanding and Retrieval

**Overview**: This research benchmarks the understanding of GTFS (General Transit Feed Specification) by LLMs (Large Language Models) and their ability to retrieve information from GTFS data using natural language instructions. It includes multiple-choice questions (MCQs) and information extraction tasks.

**Data Type**: question-answering pairs

**Domains**:
- Transportation

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/UTEL-UIUC/GTFS)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the comprehension of LLMs on GTFS data and their capabilities in information retrieval.

**Target Audience**:
- Researchers
- Transit planners
- Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Filtered GTFS feed from the Chicago Transit Authority.

**Size**: 195 multiple-choice questions, 88 information retrieval questions

**Format**: CSV

**Annotation**: Questions based on the official GTFS documentation and GTFS feeds.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correctly answered questions out of the total questions.

**Interpretation**: Higher accuracy indicates better understanding and retrieval capabilities of the LLMs.

**Baseline Results**: GPT-3.5-Turbo accuracy: 59.7%, GPT-4 accuracy: 73.3%.

**Validation**: Results are validated against a ground truth set of correct answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
