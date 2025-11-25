# StudyChat

## 📊 Benchmark Details

**Name**: StudyChat

**Overview**: The StudyChat dataset captures real-world student interactions with an LLM-powered tutoring chatbot during a semester-long AI course, enabling analysis of student behaviors and their correlation with course outcomes.

**Data Type**: dialogue acts annotations

**Domains**:
- Natural Language Processing
- Computer Science Education

**Languages**:
- English

**Similar Benchmarks**:
- TalkMoves
- NCTE
- MathDial

**Resources**:
- [Resource](https://huggingface.co/datasets/wmcnicho/StudyChat)

## 🎯 Purpose and Intended Users

**Goal**: To provide insights into student behavior with LLMs and their impact on learning outcomes in higher education.

**Target Audience**:
- Researchers
- Educators
- Data Scientists

**Tasks**:
- Dialogue Analysis
- Data Annotation

**Limitations**: This dataset was collected from a single AI course at a US university, limiting generalizability.

## 💾 Data

**Source**: Collected from student interactions in a university AI course using an LLM-powered chatbot.

**Size**: 16,851 utterances

**Format**: JSON

**Annotation**: Annotated using a dialogue act labeling schema based on student interactions.

## 🔬 Methodology

**Methods**:
- Regression Analysis
- Clustering Analysis
- Human Evaluation

**Metrics**:
- Cohen's Kappa
- R-squared

**Calculation**: Performance metrics calculated using regression models to analyze relationships between usage patterns and course outcomes.

**Interpretation**: Higher R-squared values indicate better explanatory power in predicting student performance.

**Validation**: Inter-rater agreement reached kappa values of 0.910 for broad labels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset includes a diverse range of students from upper-division AI coursework.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: PII was filtered out using systematic analysis and scripts to ensure privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Students provided consent for data collection and usage.

**Compliance With Regulations**: Not Applicable
