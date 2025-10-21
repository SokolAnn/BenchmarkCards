# Institutional Books 1.0

## 📊 Benchmark Details

**Name**: Institutional Books 1.0

**Overview**: This technical report introduces Institutional Books 1.0, a large collection of public domain books originally digitized through Harvard Library’s participation in the Google Books project, processed into an extensive dataset of historic texts, enabling easier access for research and machine learning applications.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education
- Historical Research

**Languages**:
- English
- German
- French
- Italian
- Spanish
- Latin
- Russian
- Dutch
- Portuguese
- Hebrew
- Chinese
- Swedish
- Greek
- Japanese
- Arabic

**Resources**:
- [Resource](https://huggingface.co/datasets/instdin/institutional-books-1.0)
- [GitHub Repository](https://github.com/instdin/institutional-books-1-pipeline)
- [Resource](https://huggingface.co/instdin/institutional-books-topic-classifier-bert)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, well-documented dataset of public domain texts to improve accessibility and usability for both humans and machines.

**Target Audience**:
- ML Researchers
- Academic Researchers
- Library Scientists
- Data Scientists

**Tasks**:
- Text Classification
- Information Retrieval
- Language Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Digitized books from Harvard Library’s collections via the Google Books project.

**Size**: 983,004 volumes, 242B tokens

**Format**: JSONL, CSV

**Annotation**: Processed through OCR extraction and additional data cleaning methods.

## 🔬 Methodology

**Methods**:
- Text classification
- Data extraction
- OCR processing
- Statistical analysis

**Metrics**:
- Token count
- Word count
- Unique word count
- Lexical diversity
- OCR quality scores

**Calculation**: Metrics are calculated based on the total number of characters, words and other textual elements extracted from the dataset.

**Interpretation**: High token counts and lexical diversity scores are indicative of rich text content suitable for training language models.

**Baseline Results**: N/A

**Validation**: Manual review and automated statistical analysis were conducted to ensure quality and accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes texts in over 250 different languages, which may have varying representation across topics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Public domain with restrictions on the use of copyrighted material.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All datasets are released in compliance with applicable laws regarding public domain works.
