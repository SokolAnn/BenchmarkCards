# News Category Dataset

## 📊 Benchmark Details

**Name**: News Category Dataset

**Overview**: We present a News Category Dataset that contains around 210k news headlines from the year 2012 to 2022 obtained from HuffPost, along with useful metadata (category, publication date, authors, link, short description) to enable various Natural Language Processing tasks.

**Data Type**: text (news headlines and short descriptions) 

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- News Headlines Sarcasm Dataset
- News Headlines Dataset For Sarcasm Detection

**Resources**:
- [Resource](https://www.huffpost.com/archive/)
- [Resource](https://rishabhmisra.github.io/publications/)
- [Resource](https://www.theonion.com/)
- [Resource](https://www.kaggle.com/datasets/rmisra/news-category-dataset/code)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale and high-quality source of authentic news articles with published category information and metadata to enable various Natural Language Processing tasks and analyses of journalistic trends.

**Target Audience**:
- Researchers
- Kaggle community

**Tasks**:
- Semantic Tagging
- Named Entity Recognition
- Word Sense Disambiguation
- Text Classification

**Limitations**: HuffPost stopped maintaining an extensive archive after May 2018; the dataset contains about 200k headlines between 2012 and May 2018 and about 10k headlines between May 2018 and September 2022, so the authors recommend using the period 2012 to 2017 for temporal analyses. Categories with fewer than 1,000 articles were removed to reduce data skew.

## 💾 Data

**Source**: HuffPost (Huffington Post) archive (https://www.huffpost.com/archive/)

**Size**: 210,294 news headlines

**Format**: N/A

**Annotation**: Category labels, publication date, authors, headline, short description and link as provided by HuffPost (no additional annotation performed by authors).

## 🔬 Methodology

**Methods**:
- Data curation via web scraping using BeautifulSoup and Selenium
- Exploratory Data Analysis and descriptive visualizations

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
