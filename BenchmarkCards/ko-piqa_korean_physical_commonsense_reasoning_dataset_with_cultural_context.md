# Ko-PIQA (Korean Physical Commonsense Reasoning Dataset with Cultural Context)

## 📊 Benchmark Details

**Name**: Ko-PIQA (Korean Physical Commonsense Reasoning Dataset with Cultural Context)

**Overview**: Ko-PIQA is a Korean physical commonsense reasoning dataset that incorporates cultural context, featuring 441 high-quality PIQA-style questions, with 19.7% containing culturally specific elements.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Similar Benchmarks**:
- PIQA

**Resources**:
- [GitHub Repository](https://github.com/HAERAE-HUB/Ko-PIQA)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a benchmark for evaluating Korean language models in physical commonsense reasoning and promote culturally aware AI systems.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Physical Commonsense Reasoning

**Limitations**: The dataset contains only 441 questions, which is smaller than existing benchmarks, potentially limiting its utility for model fine-tuning.

## 💾 Data

**Source**: 3.01 million web-crawled Korean questions from Naver Knowledge iN

**Size**: 441 question-answer pairs

**Format**: N/A

**Annotation**: Human validated by native Korean speakers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Exact match accuracy, where a response is correct only if it exactly matches the ground truth label.

**Interpretation**: Accuracy levels are reported across all questions and broken down by cultural specificity.

**Baseline Results**: Best model achieved 83.22% accuracy, weakest at 59.86%.

**Validation**: Human validation and deduplication were performed before finalizing the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes cultural specificity which may impact evaluation and performance.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
