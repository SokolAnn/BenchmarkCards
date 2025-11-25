# Benchmarking Search Algorithms for Generating NLP Adversarial Examples

## 📊 Benchmark Details

**Name**: Benchmarking Search Algorithms for Generating NLP Adversarial Examples

**Overview**: This paper performs a fine-grained analysis of several black-box search algorithms for generating adversarial examples in natural language processing, assessing their performance across different search spaces and budget constraints.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/QData/TextAttack)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of various search algorithms for generating adversarial examples and propose recommendations for future research.

**Target Audience**:
- ML Researchers
- Adversarial NLP Practitioners

**Tasks**:
- Adversarial Attacks

**Limitations**: N/A

## 💾 Data

**Source**: Three datasets: Yelp polarity reviews, Movie Reviews, Stanford Natural Language Inference.

**Size**: 1,500 samples (1,000 from two datasets and 500 from the third)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Attack success rate

**Calculation**: Attack success rate calculated as the number of successful attacks divided by the total number of attacks.

**Interpretation**: A higher attack success rate indicates better performance of the search algorithm.

**Baseline Results**: N/A

**Validation**: Consistent comparison of search algorithms across defined search spaces.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
