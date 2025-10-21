# Dhoroni: Exploring Bengali Climate Change and Environmental Views

## 📊 Benchmark Details

**Name**: Dhoroni: Exploring Bengali Climate Change and Environmental Views

**Overview**: Dhoroni is a novel Bengali (Bangla) climate change and environmental news dataset, comprising a 2300 annotated Bangla news articles, offering multiple perspectives such as political influence, scientific/statistical data, authenticity, position detection, and stakeholder involvement.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.13695110)
- [Resource](https://huggingface.co/ciol-research/dhoroni-6723c1c675c6ef21285c0dda)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Dhoroni dataset is to enhance accessibility and analysis of climate discourse in Bengali, addressing crucial communication and research gaps in climate-impacted regions.

**Target Audience**:
- Researchers
- Policymakers
- NGOs
- Educators

**Tasks**:
- Stance Detection
- Political Influence Detection
- News Authenticity Identification
- Scientific Data Usage Detection
- Statistical Data Usage Detection
- Data Sources Detection
- Impacted Location or Countries Detection
- Climate/Environmental Topics Detection
- News Target Detection
- Authority Involvement Detection

**Limitations**: The dataset is limited to news articles, which may not capture the full spectrum of climate-related discussions occurring in other formats, such as social media, blogs, and community forums.

## 💾 Data

**Source**: The dataset comprises 2300 annotated Bengali news articles collected from various sources, focusing on climate change and environmental issues.

**Size**: 2300 articles

**Format**: text files

**Annotation**: Each article was independently annotated by three annotators based on ten different perspectives.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the performance of models fine-tuned on the Dhoroni dataset across various tasks.

**Interpretation**: Higher scores in metrics indicate better identification and understanding of elements in Bengali climate discourse.

**Baseline Results**: Models were fine-tuned based on the Dhoroni dataset with baseline models achieving varying accuracies across defined tasks.

**Validation**: Validation procedures involved testing models against split dataset samples to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures have been taken into consideration by maintaining the anonymity of news sources.

**Data Licensing**: The dataset is available under the MIT license.

**Consent Procedures**: All data collection followed ethical guidelines, ensuring proper attribution and citation.

**Compliance With Regulations**: The dataset complies with applicable ethical guidelines and practices.
