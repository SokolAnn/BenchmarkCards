# Code Review Without Borders: Evaluating Synthetic vs. Real Data for Review Recommendation

## 📊 Benchmark Details

**Name**: Code Review Without Borders: Evaluating Synthetic vs. Real Data for Review Recommendation

**Overview**: The paper presents a novel approach utilizing Large Language Models (LLMs) to generate synthetic code review datasets by translating Java code changes into C++. This allows for training supervised classifiers in low-resource settings where labeled data is scarce, demonstrating that LLM-generated data can effectively approximate real-world review patterns.

**Data Type**: code review datasets

**Domains**:
- Natural Language Processing

**Languages**:
- Java
- C++

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To automate the classification of code changes that require manual review using synthetic and real data.

**Target Audience**:
- Software Engineers
- Machine Learning Researchers
- Developers

**Tasks**:
- Code Review Classification

**Limitations**: The models trained on real data outperform those trained on synthetic data, but the gap suggests that synthetic data can be a practical substitute when real labeled data is scarce.

## 💾 Data

**Source**: Java code changes dataset from Automating Code Review Activities by Large-Scale Pre-training.

**Size**: 50,000 code changes

**Format**: CSV

**Annotation**: Labels indicating whether each code change requires manual review.

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Data translation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated by evaluating the classifier's predictions against a held-out test set of C++ code changes.

**Interpretation**: Higher values of accuracy, precision, recall, and F1 score indicate better performance in correctly classifying review needs.

**Baseline Results**: Accuracy: 0.65, Precision: 0.64, Recall: 0.65, F1 Score: 0.64 for real data; Accuracy: 0.65, Precision: 0.65, Recall: 0.68, F1 Score: 0.66 for synthetic data.

**Validation**: The performance of the classifier trained on synthetic and real data is compared using the same held-out test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate code reviews leading to potential bugs and inconsistencies in software.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
