# RecBench+

## 📊 Benchmark Details

**Name**: RecBench+

**Overview**: RecBench+ is a new dataset benchmark designed to access LLMs’ ability to handle intricate user recommendation needs in the era of LLMs, comprising approximately 30,000 high-quality and complex user queries that vary in difficulty.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jiani-huang/RecBench.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the potential of LLMs as personalized recommendation assistants.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Personalized Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Movielens-1M dataset and Amazon Book dataset.

**Size**: 30,000 queries

**Format**: N/A

**Annotation**: Manually constructed and varied based on user interaction history.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- Condition Match Rate (CMR)

**Calculation**: Metrics are calculated based on the evaluation of LLM recommendations against the ground truth derived from user queries.

**Interpretation**: Higher values in precision and recall indicate better performance, while CMR assesses the alignment of recommendations with user-specified conditions.

**Baseline Results**: N/A

**Validation**: Extensive experiments with seven widely used LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Models show varying performance across different user demographics, particularly for female users.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
