# Large Japanese Web Corpus

## 📊 Benchmark Details

**Name**: Large Japanese Web Corpus

**Overview**: This paper builds a large Japanese web corpus by extracting and refining text from the Common Crawl archive, consisting of approximately 312.1 billion characters and approximately 173 million pages. The corpus is the largest available for training Japanese LLMs and has been shown to improve the performance of base LLMs on Japanese benchmark datasets by 6.6–8.1 points.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Similar Benchmarks**:
- CC-100
- mC4
- OSCAR

**Resources**:
- [Resource](https://huggingface.co/tokyotech-llm)

## 🎯 Purpose and Intended Users

**Goal**: To construct a large-scale, high-quality Japanese web corpus useful for training Japanese large language models (LLMs).

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Question Answering
- Reading Comprehension
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Extracted and refined text from the Common Crawl archive (21 snapshots from 2020 to 2023).

**Size**: 312,093,428,689 characters (approximately 173 million pages)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Continual pre-training
- Evaluation on Japanese benchmark datasets

**Metrics**:
- Performance improvement measured in points on benchmark datasets

**Calculation**: Improvements measured on Japanese benchmark datasets after continual pre-training.

**Interpretation**: Improvements in model performance indicated the corpus's effectiveness for training.

**Baseline Results**: Performance gains of 6.6–8.1 points on benchmark datasets.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Ethics

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Article 30-4 of the Copyright Act in Japan allows use without the permission of the copyright holder as long as the use is not for personal enjoyment.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
