# COLUMBUS

## 📊 Benchmark Details

**Name**: COLUMBUS

**Overview**: COLUMBUS is a synthetic benchmark that evaluates visual lateral thinking through multiple-choice question-answering tasks using rebus puzzles. It comprises over 1,000 puzzles designed to test the lateral thinking capabilities of vision-language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- REBUS

**Resources**:
- [GitHub Repository](https://github.com/koen-47/COLUMBUS)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the visual lateral thinking abilities of vision-language models using creatively designed rebus puzzles.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: The scale and difficulty of COLUMBUS is still limited and its coverage of icon and text puzzles is imbalanced.

## 💾 Data

**Source**: Puzzles generated from public collections of phrases (e.g., idioms and compounds), utilizing web scraping and manual curation methods.

**Size**: 1,005 puzzles

**Format**: JSON

**Annotation**: Automatically generated with human verification

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is defined as the percentage of puzzles solved correctly.

**Interpretation**: A higher accuracy indicates better lateral thinking ability in models.

**Baseline Results**: GPT-4o reached an accuracy of 80.89% on COLUMBUS- TEXT.

**Validation**: Evaluated in a zero-shot setting against human performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
