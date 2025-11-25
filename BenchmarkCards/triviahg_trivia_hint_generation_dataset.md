# TriviaHG (Trivia Hint Generation Dataset)

## 📊 Benchmark Details

**Name**: TriviaHG (Trivia Hint Generation Dataset)

**Overview**: TriviaHG is a large-scale dataset featuring 160,230 hints corresponding to 16,645 factoid questions. The dataset employs automatic hint generation for cognitive engagement and reasoning skill development.

**Data Type**: hint-question pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DataScienceUIBK/TriviaHG)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of TriviaHG is to provide a dataset for automatic hint generation to assist users in answering factoid questions, fostering reasoning and cognitive engagement.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Hint Generation
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The TriviaHG dataset is generated based on factoid questions selected from the TriviaQA dataset, with hints produced by large language models leveraging online documents.

**Size**: 160,230 hints and 16,645 questions

**Format**: JSON

**Annotation**: Hints are generated automatically using a framework that employs LLMs for hint generation.

## 🔬 Methodology

**Methods**:
- Automated hints generation
- Human evaluation

**Metrics**:
- HInt COnvergence Score (HICOS)
- HInt FAmiliarity Score (HIFAS)

**Calculation**: HICOS is calculated based on the hint's ability to eliminate incorrect candidate answers, while HIFAS is determined using Wikipedia page views associated with the entities in the hints.

**Interpretation**: Higher HICOS values indicate better hint quality in resolving questions, while higher HIFAS reflects greater familiarity with the information.

**Validation**: The effectiveness of hints was validated through human evaluation and automatic metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
