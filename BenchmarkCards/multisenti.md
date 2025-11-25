# MultiSenti

## 📊 Benchmark Details

**Name**: MultiSenti

**Overview**: A labeled dataset called MultiSenti for sentiment classification of code-switched informal short text (Roman Urdu). The paper presents the dataset, explores adapting resources from a resource-rich language for an informal one, and proposes a deep learning model (McM) for sentiment classification of code-switched informal short text without lexical normalization, translation, or code-switching indication.

**Data Type**: Short social media text (tweets) labeled for sentiment

**Domains**:
- Natural Language Processing

**Languages**:
- Roman Urdu
- English
- Mixed

**Resources**:
- [GitHub Repository](https://github.com/haroonshakeel/multisenti)

## 🎯 Purpose and Intended Users

**Goal**: Provide an annotated dataset (MultiSenti) for sentiment classification of Roman Urdu code-switched informal short text and to evaluate/adapt embedding and model choices for this task.

**Tasks**:
- Sentiment Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Twitter during and after the general elections of Pakistan in 2018.

**Size**: 20,735 examples (manually annotated gold-standard); combined corpus for multilingual embeddings: more than 6.5 million words (used to train embeddings).

**Format**: N/A

**Annotation**: Manually annotated into 'negative', 'positive', and 'neutral' by two annotators under supervision of a domain-expert; domain-expert decision used in case of annotator conflict. Class-based stratified sampling (80-20%) used for train/test splits.

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision (macro-averaged)
- Recall (macro-averaged)
- F1 Score (macro-averaged)

**Calculation**: Metrics are computed on the test split. Precision, recall, and F1 are reported as macro-averaged across classes. Class-based stratified sampling (80-20%) is used to generate train and test splits.

**Interpretation**: The paper focuses discussion and comparison primarily on macro-averaged F1-score.

**Baseline Results**: Proposed model McM achieves F1-score 0.65 with ELMo finetuning (With Finetuning McM ELMo F1=0.65). McM multilingual without finetuning achieves F1-score 0.65. ConvNet best reported F1-score 0.61. Attention-LSTM best reported F1-score 0.64. SimpleConv best reported F1-score 0.63. (See Table 2 in paper for full results.)

**Validation**: Class-based stratified sampling with an 80-20 train/test split. A 20% stratified validation set (taken from the training set) was used for hyperparameter grid search. Early stopping was used (training stopped if testing error did not decrease for 10 epochs) and checkpoints of learned weights were saved at the epoch with best predictive performance on the test split.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
