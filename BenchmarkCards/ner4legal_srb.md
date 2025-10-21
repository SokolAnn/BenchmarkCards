# NER4Legal SRB

## 📊 Benchmark Details

**Name**: NER4Legal SRB

**Overview**: This paper presents a novel dataset for Named Entity Recognition (NER) specifically designed for Serbian legal documents. It details the dataset development, methodology, and performance metrics achieved by adapting a pre-trained BERT model to this domain.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- Serbian

**Resources**:
- [Resource](https://huggingface.co/kalusev/NER4Legal SRB)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to facilitate the automation of named entity recognition tasks within Serbian legal documents by providing a labeled dataset for training and evaluating NLP models.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- NLP Developers

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Annotated dataset was derived from 75 unique appellate court rulings available from the official Ministry of Justice of the Republic of Serbia.

**Size**: 2172 sentences

**Format**: JSON

**Annotation**: Manually annotated using the BIO scheme.

## 🔬 Methodology

**Methods**:
- Cross-validation
- Model fine-tuning

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated as mean values from cross-validation tests performed across different folds of the dataset.

**Interpretation**: An F1 Score above 0.90 indicates strong model performance, and variations in metrics help evaluate different NE categories.

**Baseline Results**: Mean F1 Score of 0.96 and accuracy of 0.99 across NER categories.

**Validation**: Cross-validation with 5 subsets to ensure model robustness and mitigate overfitting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
