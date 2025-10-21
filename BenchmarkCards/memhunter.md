# MemHunter

## 📊 Benchmark Details

**Name**: MemHunter

**Overview**: MemHunter is an automated, verifiable technique for detecting memorization in large language models (LLMs) at both sample and dataset scales. It employs a memory-inducing LLM to automatically generate prompts for efficient detection of memorized content, significantly improving performance and reducing computational costs compared to existing methods.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2412.07261)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to provide an effective tool for assessing privacy risks in large language models by detecting memorized content from datasets.

**Target Audience**:
- Researchers
- Data Owners
- ML Practitioners

**Tasks**:
- Memorization Detection

**Limitations**: Training on specific datasets may yield different memorization detection results, and the method may not outperform sample-wise optimization in cases where time constraints are relaxed.

## 💾 Data

**Source**: Subsets from Common Crawl, news articles from AP News, code snippets from StackOverflow, and user discussions from Reddit were used for training and testing.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Hypothesis Testing
- Automated extraction

**Metrics**:
- ROUGE-L

**Calculation**: Memorization score based on ROUGE-L precision, measuring the ratio of the longest common subsequence to the length of generated text.

**Interpretation**: Higher memorization scores indicate better performance in identifying memorized content from training datasets.

**Baseline Results**: MemHunter extracts up to 40% more memorized training data than existing methods under constrained time resources.

**Validation**: Validation procedures involve comparing memorization behavior between trained and untrained LLMs via hypothesis testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Accuracy**: Data contamination, Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: MemHunter implements hypothesis testing to ensure the verifiable detection of memorized content, addressing privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
