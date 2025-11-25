# RoLargeSum

## 📊 Benchmark Details

**Name**: RoLargeSum

**Overview**: RoLargeSum is a large-scale summarization dataset for the Romanian language, containing more than 615K news articles from various news websites, along with their summaries, headlines, keywords, dialect information, and other metadata.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Romanian

**Similar Benchmarks**:
- CNN/Daily Mail
- NY Times
- XSum
- DACSA
- RoSummary

**Resources**:
- [GitHub Repository](https://github.com/avramandrei/rolargesum)

## 🎯 Purpose and Intended Users

**Goal**: Create a high-quality summarization dataset for the Romanian language to support the development of summarization models.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Text Summarization
- Headline Generation
- Keyword Extraction

**Limitations**: The distribution of dialects in RoLargeSum is not uniform, mainly due to the varying number of newspapers in Romania and Moldova.

## 💾 Data

**Source**: Crawled from various publicly available news websites in Romania and Moldova.

**Size**: 615,679 news articles

**Format**: N/A

**Annotation**: Data manually cleaned and organized; summaries and metadata attached where available.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L

**Calculation**: ROUGE scores calculated based on unigram and bigram overlap as well as longest common subsequence.

**Interpretation**: Higher ROUGE scores indicate better summarization performance.

**Baseline Results**: mBART-large achieved the highest scores of ROUGE-1: 44.57, ROUGE-2: 24.03, ROUGE-L: 36.10 for the RO+MD task.

**Validation**: Evaluation on training, validation, and testing splits with metrics reported.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Ethical Compliance

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Data includes a dialect classification of news articles, with a significant imbalance between Romanian and Moldovan articles.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collected from publicly accessible news websites, with citations and URLs for verification.

**Data Licensing**: Data used strictly for academic and research purposes; respects copyright and intellectual property rights.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data collection complies with relevant ethical guidelines.
