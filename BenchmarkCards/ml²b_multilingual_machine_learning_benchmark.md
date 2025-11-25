# ML²B (Multilingual Machine Learning Benchmark)

## 📊 Benchmark Details

**Name**: ML²B (Multilingual Machine Learning Benchmark)

**Overview**: ML²B is the first benchmark for evaluating multilingual ML code generation, consisting of 30 Kaggle competitions translated into 13 natural languages. It provides insights into cross-lingual model performance and evaluates how task type interacts with multilingual ML code generation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese
- Spanish
- French
- German
- Japanese
- Korean
- Russian
- Turkish
- Italian
- Polish
- Kazakh
- Romanian

**Similar Benchmarks**:
- MLE-bench
- DA-Code
- Weco-Kaggle

**Resources**:
- [GitHub Repository](https://github.com/enaix/ml2b)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation framework for multilingual ML code generation.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Code Generation
- Data Processing

**Limitations**: N/A

## 💾 Data

**Source**: 30 Kaggle competitions translated to 13 languages.

**Size**: 390 unique evaluation instances

**Format**: Structured metadata

**Annotation**: Human-reviewed translations

## 🔬 Methodology

**Methods**:
- Automated metrics
- Generalized assessments

**Metrics**:
- Accuracy
- F1 Score
- AUC

**Calculation**: Percentile rank based on Kaggle leaderboard performances.

**Interpretation**: Lower percentiles indicate better performance.

**Baseline Results**: Performance comparison among five LLMs.

**Validation**: Systematic validation of translations by native language speakers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety
- Compliance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Potential for demographic bias in performance across languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
