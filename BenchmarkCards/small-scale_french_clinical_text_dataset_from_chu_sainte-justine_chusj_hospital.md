# small-scale French clinical text dataset from CHU Sainte-Justine (CHUSJ) Hospital

## 📊 Benchmark Details

**Name**: small-scale French clinical text dataset from CHU Sainte-Justine (CHUSJ) Hospital

**Overview**: The paper introduces a carefully curated, small-scale French clinical text dataset from CHU Sainte-Justine (CHUSJ) Hospital, which can serve as a valuable benchmark for resource-constrained NLP research in healthcare. The dataset consists of short clinical narratives (admission and evolution notes within the first 24 hours) used to detect cardiac failure.

**Data Type**: text (short clinical narratives / single-line clinical notes)

**Domains**:
- Natural Language Processing
- Healthcare
- Medical Diagnosis

**Languages**:
- French

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a curated small-scale French clinical text dataset from CHU Sainte-Justine and evaluate Mixture of Experts (MoE) Transformer models for clinical text classification under limited data and constrained computational resources, with a view to deploying in a Clinical Decision Support System.

**Target Audience**:
- ML Researchers
- Clinical Practitioners
- Model Developers
- Hospital Clinical Decision Support System (CDSS) Integrators

**Tasks**:
- Text Classification
- Clinical Narrative Classification
- Binary Classification (cardiac failure detection)

**Limitations**: Dataset comprises 5,444 short clinical narratives (580,000 unigrams) and is small-scale; computational resources are constrained to hospital server (NVIDIA Quadro P620, 2 GB); strict hospital privacy regulations prohibit transferring sensitive patient data off-site; MoE-Transformer does not surpass the best biomedical pre-trained models in all metrics; observed generalization gap and overfitting on small data.

**Out of Scope Uses**:
- Cloud-based inference or transferring patient data to external servers/APIs

## 💾 Data

**Source**: Curated French clinical notes from CHU Sainte-Justine (CHUSJ) Hospital (admission and evolution notes within the first 24 hours); study approved by CHUSJ research ethics board (protocol number: 2020-2253).

**Size**: 5,444 clinical note lines (580,000 unigrams); 1,941 positive cases and 3,503 negative cases.

**Format**: N/A

**Annotation**: Clinician analysis and confirmation of labels (manual clinician-reviewed annotation/confirmation as described in the paper).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Comparative model evaluation (training and testing multiple models including pre-trained BERT-based and from-scratch Transformer/MoE-Transformer models)
- Integrated Gradients for interpretability

**Metrics**:
- Accuracy
- Precision
- Recall
- F1-Score
- Area Under the Curve (AUC)

**Calculation**: Metrics calculated using standard definitions provided in the paper: Accuracy = (TP + TN) / (TP + TN + FP + FN); Precision = TP / (TP + FP); Recall = TP / (TP + FN); F1-Score = 2 * Precision * Recall / (Precision + Recall).

**Interpretation**: Higher values of Accuracy, Precision, Recall, and F1-Score indicate better classification performance; authors report MoE-Transformer results (Accuracy 0.87, Precision 0.87, Recall 0.85, F1-Score 0.86) and compare these values to other models.

**Baseline Results**: Baseline performance reported in Table III: DistillBERT: Accuracy 0.80, Precision 0.79, Recall 0.78, F1 0.78, Training Time 12.4 hours; CamemBERT: 0.83 / 0.82 / 0.83 / 0.82 / 25.1 hours; FlauBERT: 0.84 / 0.84 / 0.84 / 0.84 / 10.6 hours; FrALBERT: 0.83 / 0.82 / 0.81 / 0.81 / 30.2 hours; CamemBERT-bio: 0.87 / 0.86 / 0.88 / 0.87 / 31.7 hours; DrBERT: 0.87 / 0.84 / 0.90 / 0.87 / 45.2 hours; AliBERT: 0.86 / 0.87 / 0.84 / 0.86 / 39.3 hours; Transformer: 0.85 / 0.85 / 0.83 / 0.84 / 0.11 hours; MoE-Transformer: 0.87 / 0.87 / 0.85 / 0.86 / 0.17 hours.

**Validation**: Data split into 80% training, 10% validation, and 10% testing; early stopping was applied in some experiments; models trained on NVIDIA Quadro P620 GPU (2 GB).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Robustness
- Explainability
- Data Laws

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Robustness**: Hallucination
- **Explainability**: Unexplainable output
- **Data Laws**: Data transfer restrictions, Data usage restrictions

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Study approved by CHUSJ research ethics board (protocol number: 2020-2253). Data processing restricted to the hospital server; hospital privacy regulations prohibit transferring sensitive patient information to external servers or APIs (as stated).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The paper states strict hospital privacy regulations that preclude transferring sensitive patient information off-site; data processing must occur within the hospital infrastructure (as described).
