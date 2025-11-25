# a custom dataset comprising clinical notes for medical imaging protocol assignment

## 📊 Benchmark Details

**Name**: a custom dataset comprising clinical notes for medical imaging protocol assignment

**Overview**: We present an approach to evaluate the performance and trustworthiness of a GPT3.5 model for medical image protocol assignment. Our evaluation dataset consists of 4,700 physician entries across 11 imaging protocol classes spanning the entire head.

**Data Type**: clinical physician order text (reason for exam)

**Domains**:
- Medical Imaging
- Natural Language Processing

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the performance and trustworthiness of GPT3.5 for medical image protocol assignment, compare it with fine-tuned models (BERT, BioBERT, RoBERTa) and a radiologist, analyze explanations and word importance, and assess calibration.

**Tasks**:
- Text Classification
- Explainability
- Model Calibration

**Limitations**: Dataset comprised of neuroradiologic orders from a single center and may be limited in its representation of the racial, social, and ethnic diversity of other regions; limited number of protocols (the ten/eleven most commonly used protocols) which may not capture the full breadth of clinical protocols; protocols assigned by multiple radiologists with varying experience (inter-operator variability); dataset not publicly available; evaluation dataset size (4,730 entries) may still limit model performance.

## 💾 Data

**Source**: Deidentified order entries and assigned protocols for magnetic resonance (MR) neuroradiology studies conducted at the authors' institution between June 2018 and July 2021. Each row includes the 'reason for exam', patient age and gender, and the protocol assigned by the radiologist.

**Size**: 4,730 recorded notes

**Format**: N/A

**Annotation**: Expert-annotated imaging protocols reviewed by an experienced radiologist (ET) with 10 years of experience.

## 🔬 Methodology

**Methods**:
- Prompting GPT3.5 via OpenAI API to output predicted protocol and explanation
- Fine-tuning and evaluation of pretrained models (BERT, BioBERT, RoBERTa) using HuggingFace Transformers
- Integrated gradients for word importance attribution for BERT
- Radiologist (human) word-importance scoring
- Model calibration evaluation using log probabilities and binning
- Error analysis via review of GPT3.5 explanations by a radiologist

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy
- Calibration (accuracy per confidence bin using log probabilities)

**Calculation**: Predicted protocol from each model was compared against ground truth to measure precision, recall, and accuracy for each class. Log probabilities from GPT3.5 were transformed into a confidence value and entries were divided into bins in [0,1] with intervals of 0.1; for each bin accuracy was calculated. Integrated gradients aggregated average attribution values across texts per protocol; GPT3.5 word importance used a weighted average (1, 0.66, 0.33 for top three words). Words appearing in fewer than five texts were filtered out for reliability.

**Interpretation**: Higher F1 scores and accuracy indicate better protocol assignment performance. Calibration curves closer to the diagonal indicate better alignment between predicted probabilities and observed accuracy; well-calibrated models give more reliable confidence estimates. Agreement of top words with radiologist indicates better interpretability/clinical relevance.

**Baseline Results**: Weighted average F1 scores reported in the paper: BERT 0.89, BioBERT 0.92, RoBERTa 0.90, GPT3.5 0.72. Per-class F1 scores and accuracies are provided (e.g., per-table values; GPT3.5 generally underperformed compared to fine-tuned models).

**Validation**: Radiologist review by an experienced radiologist (ET) for data quality and for reviewing GPT3.5 explanations; model outputs compared to radiologist-assigned ground truth; calibration evaluated via confidence bins; word-importance lists filtered to exclude words appearing in fewer than five texts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Explainability
- Robustness
- Value Alignment

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment
- **Explainability**: Unexplainable output
- **Robustness**: Hallucination
- **Value Alignment**: Over- or under-reliance

**Demographic Analysis**: The dataset comprised of neuroradiologic orders from a single center and may be limited in its representation of the racial, social, and ethnic diversity of other regions.

**Potential Harm**: ['Safety risks in clinical settings due to systematic errors (incomplete understanding of protocols, anatomy, medical terminology)', 'Overconfidence in model explanations leading to reliance on incorrect predictions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets utilized during this study are not publicly available due to reasonable privacy and security concerns. The data is not easily redistributable to researchers other than those engaged in Institutional Review Board-approved research collaborations with Stanford University.

**Data Licensing**: Not Applicable

**Consent Procedures**: Study conducted with approval of the Stanford Institutional Review Board and under a waiver of informed consent.

**Compliance With Regulations**: Study approved by Stanford Institutional Review Board (IRB); data sharing restricted to IRB-approved collaborations.
