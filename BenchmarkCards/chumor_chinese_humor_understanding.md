# Chumor (Chinese Humor Understanding)

## 📊 Benchmark Details

**Name**: Chumor (Chinese Humor Understanding)

**Overview**: Chumor is the first Chinese humor explanation dataset that poses significant challenges to existing LLMs and aims to improve humor understanding in non-English contexts.

**Data Type**: humor explanation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- Global-MMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/dnaihao/Chumor)
- [Resource](https://dnaihao.github.io/Chumor-dataset/)
- [Resource](https://huggingface.co/spaces/dnaihao/Chumor)
- [GitHub Repository](https://github.com/dnaihao/Chumor-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To advance the understanding of humor in Chinese and evaluate the performance of LLMs in humor reasoning.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners

**Tasks**:
- Humor Explanation

**Limitations**: The dataset primarily showcases the challenges LLMs face in understanding humor, particularly in non-English contexts.

## 💾 Data

**Source**: Ruo Zhi Ba (RZB), a Chinese platform sharing culturally specific jokes.

**Size**: 3,339 instances

**Format**: JSON

**Annotation**: Manually annotated by five native Chinese speakers

## 🔬 Methodology

**Methods**:
- Direct prompting
- Chain-of-thought prompting

**Metrics**:
- Accuracy
- Matthew's Correlation Coefficient (MCC)

**Calculation**: Accuracy is calculated based on correct prediction labels compared to human-annotated labels.

**Interpretation**: A higher accuracy indicates better humor understanding by the model.

**Validation**: The performance of ten LLMs was evaluated on the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Efforts were made to filter out excessively offensive content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
