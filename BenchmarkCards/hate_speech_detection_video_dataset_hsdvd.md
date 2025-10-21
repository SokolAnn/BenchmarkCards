# Hate Speech Detection Video Dataset (HSDVD)

## 📊 Benchmark Details

**Name**: Hate Speech Detection Video Dataset (HSDVD)

**Overview**: This paper proposes the first multimodal deep learning framework to combine the auditory features representing emotion and the semantic features to detect hateful content. This paper also presents a new Hate Speech Detection Video Dataset (HSDVD) collected for the purpose of multimodal learning as no such dataset exists today.

**Data Type**: multimodal (video, audio, text)

**Domains**:
- Natural Language Processing
- Speech Processing

**Similar Benchmarks**:
- Hateful Memes challenge
- OffensEval 2019
- Waseem and Hovy 2016 (W&H)
- Davidson 2017
- IEMOCAP Dataset 2007
- Offensive Video Detection (dataset in Portuguese)

**Resources**:
- [GitHub Repository](https://github.com/tyiannak/pyAudioAnalysis)
- [Resource](https://ffmpeg.org/)
- [Resource](https://www.houndify.com/)
- [GitHub Repository](https://github.com/hanxiao/bert-as-service/)
- [Resource](https://hatebase.org/)
- [Resource](https://www.audacityteam.org/)
- [Resource](https://www.un.org/en/genocideprevention/documents/UN%20Strategy%20and%20Plan%20of%20Action%20on%20Hate%20Speech%2018%20June%20SYNOPSIS.pdf)

## 🎯 Purpose and Intended Users

**Goal**: To propose a multimodal deep learning framework that combines semantic features and auditory emotion attributes to detect hateful content in multimedia, and to present a new Hate Speech Detection Video Dataset (HSDVD) for multimodal learning.

**Tasks**:
- Text Classification
- Speech Emotion Recognition
- Multimodal Classification
- Binary Classification (Hate Speech Detection)

**Limitations**: Limited dataset size (HSDVD contains 1,000 records); limited visual feature usefulness in current dataset (only 15% contain distinguishable facial expressions); potential annotator bias and topic bias in existing datasets and HSDVD; data collection focused on specific target groups due to resource constraints.

**Out of Scope Uses**:
- HSDVD will be used only to compare relative performances.

## 💾 Data

**Source**: Collected from Twitter and YouTube using Twitter API and PyTube; 1,000 records of Tweet IDs and YouTube links compiled using a lexicon of sexist and ethnic slurs.

**Size**: 1,000 video recordings (25% labeled as hate speech)

**Format**: Tweet IDs and YouTube links; audio converted to WAV using ffmpeg; transcripts produced using Houndify API.

**Annotation**: Manual annotation by the two authors according to a pre-decided definition of hate speech; binary labels (hate speech / not hate speech); Cohen's kappa = 0.92.

## 🔬 Methodology

**Methods**:
- Transfer Learning
- Fine-tuning of pre-trained transformers (BERT, ALBERT) for text classification
- Multi-task learning (MTL) regression for emotion attribute prediction (valence, arousal, dominance)
- Multimodal joint representation via multilayer perceptron (MLP)
- Train/validation/test split with holdout test set (80/10/10)
- Hyperparameter tuning using validation set and early stopping

**Metrics**:
- Macro-average Precision
- Macro-average Recall
- Macro-average F1 Score
- Root Mean Squared Error (RMSE)

**Calculation**: Macro-average of precision, recall, and F1-score computed across both classes for hate speech classification. Emotion attributes evaluated using Root Mean Squared Error (RMSE). Binary prediction threshold set to 0.7 for final classification. Loss functions: weighted Mean Square Error (MSE) for the MTL emotion model; binary cross-entropy with L2 regularization for the multimodal model.

**Interpretation**: Higher macro-average Precision/Recall/F1 indicates better hate speech detection performance. Lower RMSE indicates better emotion attribute prediction. The authors interpret increases in precision and recall of the multimodal model relative to text-only baselines as evidence that incorporating speech emotion features improves multimedia hate speech detection.

**Baseline Results**: Baseline text model (examples): BERT_A baseline — Precision 90.50, Recall 91.73, F1 91.11; ALBERT_B baseline — Precision 90.20, Recall 91.99, F1 91.08. Multimodal top result (for comparison): BERT_A_CLS — Precision 93.00, Recall 92.89, F1 92.94.

**Validation**: Dataset split into training (80%), validation (10%), and testing (10%). Validation set used for hyperparameter tuning and selecting best epoch based on validation loss. Early stopping applied (stop if validation loss does not decrease for more than 10 epochs). Emotion model hyperparameters tuned using validation loss (hyperband).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Societal Impact**: Impact on human agency

**Potential Harm**: ['Incitement', 'Discrimination', 'Hostility', 'Violence']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
