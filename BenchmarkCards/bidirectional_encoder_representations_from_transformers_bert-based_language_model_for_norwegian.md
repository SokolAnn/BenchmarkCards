# Bidirectional Encoder Representations from Transformers (BERT)-based language model for Norwegian

## 📊 Benchmark Details

**Name**: Bidirectional Encoder Representations from Transformers (BERT)-based language model for Norwegian

**Overview**: This work describes the effort to build a pre-training corpus and to use it to train a BERT-based language model for Norwegian, outpacing multilingual BERT in various tasks and demonstrating the feasibility of building high-quality models from digitized content in national libraries.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Norwegian
- English
- Swedish
- Danish

**Similar Benchmarks**:
- mBERT
- NorBERT

**Resources**:
- [Resource](https://huggingface.co/NbAiLab/nb-bert-base)
- [Resource](https://huggingface.co/NbAiLab/notram)

## 🎯 Purpose and Intended Users

**Goal**: To create a large Norwegian-only corpus for training state-of-the-art transformer-based language models, demonstrating effective use of digital collections in national libraries.

**Target Audience**:
- ML Researchers
- Language Technologists
- Linguists

**Tasks**:
- Named Entity Recognition
- Part-of-Speech Tagging
- Sentiment Analysis
- Political Affiliation Classification

**Limitations**: N/A

## 💾 Data

**Source**: Digital collections from the National Library of Norway

**Size**: 109GB

**Format**: Plain text

**Annotation**: Manually annotated with morphological features, syntactic functions, and hierarchical structures.

## 🔬 Methodology

**Methods**:
- Fine-tuning on specific tasks such as NER and sentiment classification
- Evaluation against prior models including mBERT and NorBERT

**Metrics**:
- F1 Score

**Calculation**: The evaluation metrics are calculated based on the performance of the model on validation datasets for various downstream tasks.

**Interpretation**: Higher F1 Score indicates better model performance on named entity recognition and sentiment classification tasks.

**Baseline Results**: The NB-BERT model outperformed mBERT on token and sequence classification tasks.

**Validation**: A grid search for optimal fine-tuning hyperparameters and performance comparison against baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
