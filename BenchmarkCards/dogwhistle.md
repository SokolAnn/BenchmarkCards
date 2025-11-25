# DogWhistle

## 📊 Benchmark Details

**Name**: DogWhistle

**Overview**: DogWhistle is a new Chinese dataset for cant creation, understanding, and decryption, intended to evaluate the performance of next-generation pretrained language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/JetRunner/dogwhistle)
- [Resource](https://competitions.codalab.org/competitions/30451)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for studying cant that evaluates the capabilities of pretrained language models and enhances understanding of natural language.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Named Entity Recognition
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from historical game records of Decrypto Online, a well-designed online board game.

**Size**: 230,220 cant phrases with 1,878 unique hidden words in training set

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Predictions are evaluated based on how accurately the model decodes cant to the hidden words.

**Interpretation**: Higher accuracy scores indicate better performance of the model in understanding and decoding cant.

**Validation**: The dataset was split into training, development, and test sets with no overlapping combinations of hidden words.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potentially toxic or offensive content in the dataset']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
