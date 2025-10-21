# CMoralEval (A Moral Evaluation Benchmark for Chinese Large Language Models)

## 📊 Benchmark Details

**Name**: CMoralEval (A Moral Evaluation Benchmark for Chinese Large Language Models)

**Overview**: CMoralEval is a benchmark dataset curated for moral evaluation of Chinese LLMs, consisting of explicit moral scenarios and moral dilemma scenarios. It aims to assess the ethical decision-making capabilities of these models based on traditional and contemporary Chinese moral norms.

**Data Type**: multiple-choice moral evaluation scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/tjunlp-lab/CMoralEval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the moral reasoning capabilities of Chinese large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Moral Evaluation
- Ethical Decision Making

**Limitations**: N/A

## 💾 Data

**Source**: Curated from a Chinese TV program discussing moral norms and a collection of Chinese moral anomies from newspapers and academic papers.

**Size**: 30,388 instances

**Format**: JSON

**Annotation**: Manual annotation by experts with a platform for AI-assisted generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on the highest probability outputs chosen by the models from the given scenarios.

**Interpretation**: Higher scores indicate better moral reasoning aligned with ethical standards.

**Baseline Results**: Performance evaluated across various Chinese LLMs.

**Validation**: Multiple annotators and expert reviews ensured data quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
