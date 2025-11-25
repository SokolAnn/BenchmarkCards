# HumorBench

## 📊 Benchmark Details

**Name**: HumorBench

**Overview**: HumorBench is a benchmark designed to evaluate large language models’ (LLMs) ability to reason about and explain sophisticated humor in cartoon captions. It includes approximately 300 unique cartoon-caption pairs with expert-annotated evaluation rubrics identifying essential joke elements.

**Data Type**: cartoon-caption pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of HumorBench is to evaluate LLMs’ reasoning abilities in understanding humor by focusing on objective elements rather than subjective funniness.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Humor Comprehension

**Limitations**: The dataset size (499 unique elements) limits the statistical resolution of fine-grained analyses.

## 💾 Data

**Source**: Cartoon-caption pairs from the New Yorker Caption Contest and Cartoonstock.com.

**Size**: 300 pairs

**Format**: N/A

**Annotation**: Element annotations were hand-annotated to capture the objective components essential to understanding the joke.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Models are evaluated based on whether their explanations cover the essential components of the joke as verified by expert annotations.

**Interpretation**: A higher accuracy percentage indicates a better understanding and explanation of the humor.

**Baseline Results**: Top-performing models achieved accuracies around 60% on the HumorBench-hard subset.

**Validation**: Performance validated by comparing LLM outputs against human-generated explanations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
