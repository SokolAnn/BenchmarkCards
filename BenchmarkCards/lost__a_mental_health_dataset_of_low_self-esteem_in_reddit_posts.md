# LOST: A Mental Health Dataset of Low Self-esteem in Reddit Posts

## 📊 Benchmark Details

**Name**: LOST: A Mental Health Dataset of Low Self-esteem in Reddit Posts

**Overview**: A psychology-grounded and expertly annotated dataset, LoST (Low Self esTeem), to study and detect low self-esteem on Reddit. The dataset comprises gold-standard annotations created using standardized clinical questionnaires (Rosenberg Self-Esteem Scale, Coopersmith Self-Esteem Inventory, INQ-18) and expert-driven annotation guidelines to enable supervised learning for binary low self-esteem detection.

**Data Type**: text (Reddit posts)

**Domains**:
- Natural Language Processing
- Mental Health
- Public Health

**Similar Benchmarks**:
- CAMS

**Resources**:
- [GitHub Repository](https://github.com/drmuskangarg/LoST)
- [Resource](https://arxiv.org/abs/2306.05596)
- [Resource](https://praw.readthedocs.io/en/stable/)
- [Resource](https://huggingface.co/bert-base-uncased)
- [Resource](https://huggingface.co/roberta-base)
- [Resource](https://huggingface.co/xlnet-base-cased)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate public health surveillance and health applications by releasing a psychology-grounded, expertly annotated dataset of Reddit posts for detecting low self-esteem and to analyze current AI models for low self-esteem detection.

**Target Audience**:
- Research community
- Therapists
- Public Health practitioners
- Model developers

**Tasks**:
- Text Classification
- Binary Classification

**Limitations**: Annotations may contain biases due to the subjective nature of the task; no user metadata is released to protect privacy which limits certain analyses; machine learning predictions from this dataset cannot replace professional mental health diagnostics, counseling, or therapy.

**Out of Scope Uses**:
- Clearly, machine learning predictions cannot replace professional mental health diagnostics, counseling, or therapy.

## 💾 Data

**Source**: Collected from Reddit subreddits r/depression and r/SuicideWatch using the Python Reddit API Wrapper (PRAW) from 2 December 2021 to 4 January 2022; candidate posts were filtered (body length > 0, removal of generic supportive posts, removal of posts showing intent of self-harm without context) to obtain final corpus.

**Size**: 3,251 posts

**Format**: CSV (comma-separated format)

**Annotation**: Manual annotation by three trained postgraduate students under supervision of a clinical psychologist and a social NLP researcher using guidelines grounded in Rosenberg Self-Esteem Scale (RSS), Coopersmith Self-Esteem Inventory (CSEI), and INQ-18; trial sessions and training conducted; final labels determined by majority voting; inter-annotator agreement reported as Fleiss' Kappa κ = 78.52%.

## 🔬 Methodology

**Methods**:
- Automated classification using baseline models (LSTM, GRU, BERT, RoBERTa, XLNet)
- 10-fold cross-validation
- Data augmentation (Easy Data Augmentation, Back Translation)

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy
- Matthews Correlation Coefficient (MCC)

**Calculation**: Metrics (Precision, Recall, F1, Accuracy) are averaged over 10-fold cross-validation. MCC is computed for imbalance assessment and interpreted on its standard scale from -1 to +1 as described in the paper.

**Interpretation**: MCC values closer to +1 indicate stronger prediction, values near 0 indicate random prediction, and values near -1 indicate poor models. Higher Accuracy/F1/MCC are treated as better; authors report improvements with augmented data and identify RoBERTa as best on original data and BERT as best on augmented data.

**Baseline Results**: Reported average accuracies (10-fold CV): LSTM: Original 77%, Augmented 78%; GRU: Original 76%, Augmented 82%; BERT: Original 81%, Augmented 88%; RoBERTa: Original 82%, Augmented 85%; XLNet: Original 81%, Augmented 85%. (Precision/Recall/F1 for each class are reported in Table I of the paper.)

**Validation**: Annotation reliability validated via Fleiss' Kappa inter-observer agreement κ = 78.52%. Experimental results are averaged over 10-fold cross-validation; hyperparameters and training procedures described (padding, 150 epochs, early stopping, learning rate 1e-5, batch size 16).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Early detection of low self-esteem to help prevent progression to clinical depression and suicidal ideation', 'Facilitate public health surveillance and mental health triaging']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset contains only publicly available posts; no user metadata is released; examples are anonymized, obfuscated, and paraphrased to prevent misuse; authors state commitment to protecting privacy and anonymity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
