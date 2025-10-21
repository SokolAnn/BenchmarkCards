# DEPEND EVAL (Dependency Evaluation)

## 📊 Benchmark Details

**Name**: DEPEND EVAL (Dependency Evaluation)

**Overview**: DEPEND EVAL is a hierarchical benchmark designed to evaluate LLMs' ability to reason about structured code repositories through three progressively challenging tasks: Dependency Recognition, Repository Construction, and Multi-file Editing, across eight programming languages.

**Data Type**: code repositories

**Domains**:
- Software Engineering

**Languages**:
- C
- C++
- C#
- JavaScript
- Java
- PHP
- Python
- TypeScript

**Resources**:
- [GitHub Repository](https://github.com/ink7-sudo/DependEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' understanding capabilities at the code repository level, addressing repository-level reasoning for software development.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Dependency Recognition
- Repository Construction
- Multi-file Editing

**Limitations**: Not enough languages; currently focuses on only three core tasks.

## 💾 Data

**Source**: Real-world repositories collected from GitHub API.

**Size**: 15,576 repositories

**Format**: JSON

**Annotation**: Filtered and manually curated for quality and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match Rate (EMR)
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on predicted and ground truth outputs comparison.

**Interpretation**: Higher scores indicate better performance in correctly identifying dependencies and constructing repositories.

**Validation**: Evaluated across various models and programming languages.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Decision bias
- **Transparency**: Lack of training data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymized and stored securely with restricted access.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants can withdraw from the study at any time.

**Compliance With Regulations**: Not Applicable
