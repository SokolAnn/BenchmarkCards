# SaRoHead (Satirical Romanian Headlines)

## 📊 Benchmark Details

**Name**: SaRoHead (Satirical Romanian Headlines)

**Overview**: The SaRoHead dataset consists of news headlines gathered from various Romanian news outlets and a known online publication for satirical content. It is specifically designed to evaluate approaches for detecting satire in headlines.

**Data Type**: titles only

**Domains**:
- Natural Language Processing

**Languages**:
- Romanian

**Similar Benchmarks**:
- SciTechBaitRo
- SaRoCo
- RoCliCo

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.1234567)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset for training and evaluating models that can detect satire in Romanian news headlines.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: Data collection is biased towards one source of satirical content.

## 💾 Data

**Source**: Headlines scraped from Romanian news outlets and a satirical news site.

**Size**: 20,725 examples

**Format**: N/A

**Annotation**: Distant supervision based on the source news outlet classifications.

## 🔬 Methodology

**Methods**:
- Standard Machine Learning Algorithms
- BERT Models
- Large Language Models

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated based on classifications for satire vs non-satire.

**Interpretation**: Higher F1 scores indicate better performance in detecting satire.

**Validation**: Evaluated through train/validation/test splits with balanced sample representation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes balanced categories (social, political, sport) for diversity.

**Potential Harm**: ['Potential reinforcement of satirical biases.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The data was collected in compliance with GDPR regulations.

**Consent Procedures**: Data sourced from publicly available headlines from news websites.

**Compliance With Regulations**: The research complies with Article 3 of the European Union directive 2019/790.
