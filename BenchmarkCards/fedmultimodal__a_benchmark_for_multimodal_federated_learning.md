# FedMultimodal: A Benchmark For Multimodal Federated Learning

## 📊 Benchmark Details

**Name**: FedMultimodal: A Benchmark For Multimodal Federated Learning

**Overview**: We introduce FedMultimodal, the first federated learning benchmark for multimodal learning covering five representative multimodal applications from ten commonly used datasets with a total of eight unique modalities. FedMultimodal offers a systematic end-to-end FL pipeline (data partition, feature extraction, FL algorithms, and model evaluation) and provides a standardized approach to assess robustness against three common data corruptions in real-life multimodal applications: missing modalities, missing labels, and erroneous labels.

**Data Type**: multimodal (audio, text, image/video, accelerometer, gyroscope, ECG)

**Domains**:
- Emotion Recognition
- Multimedia Action Recognition
- Human Activity Recognition
- Healthcare
- Social Media Classification

**Similar Benchmarks**:
- LEAF
- FedML
- FedScale
- FLUTE
- FedAudio
- FLamby
- FederatedScope

**Resources**:
- [GitHub Repository](https://github.com/usc-sail/fed-multimodal)
- [Resource](https://doi.org/10.1145/3580305.3599825)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in multimodal federated learning by providing the first FL benchmark for multimodal applications, including an end-to-end simulation framework, standardized datasets and pipelines, and robustness assessment modules for missing modalities, missing labels, and erroneous labels.

**Target Audience**:
- ML Researchers
- ML Practitioners
- Model Developers

**Tasks**:
- Emotion Recognition
- Multimedia Action Recognition
- Human Activity Recognition
- Healthcare (ECG Classification)
- Social Media Classification

**Limitations**: FedMultimodal currently does not cover several multimodal applications such as medical image analysis, autonomous driving, and virtual reality; the range of supported models is limited; only two basic fusion approaches (concatenation and attention) are included; label scarcity and privacy leakage remain open challenges noted for future work.

## 💾 Data

**Source**: Ten publicly available multimodal datasets included in FedMultimodal: MELD, CREMA-D, UCF101, MiT10, MiT51, UCI-HAR, KU-HAR, PTB-XL, Hateful-Memes, CrisisMMD.

**Size**: Dataset sizes as reported in the paper: MELD: 9,718 examples; CREMA-D: 4,798 examples; UCF101 (subset with audio+video): 6,837 videos; MiT10: 41,600 videos; MiT51: 157,600 videos; UCI-HAR: 8,979 examples; KU-HAR: 10,300 examples; PTB-XL: 21,700 ECG recordings; Hateful-Memes: 10,000 examples; CrisisMMD: 18,100 examples.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Federated simulation (end-to-end FL pipeline)
- Predefined train/validation/test splits (when provided)
- 5-fold cross-validation (when predefined splits are not provided)
- Repeated experiments with different random seeds

**Metrics**:
- Unweighted Average Recall (UAR)
- Accuracy
- F1 Score
- Area Under ROC Curve (AUC)

**Calculation**: Metrics are computed following established practices per dataset: for datasets with predefined partitions experiments are repeated 5 times with different seeds; for datasets without predefined partitions 5-fold cross-validation is performed. Evaluation metrics are computed on validation/test splits according to each dataset's protocol.

**Interpretation**: Attention-based fusion outperforms concatenation-based fusion in the majority of datasets and heterogeneity conditions; FedOpt often yields stronger baselines across tasks (with exceptions in low heterogeneity conditions); multimodal learning generally outperforms unimodal learning, though the performance gap is within 5% for most datasets. Missing modalities, missing labels, and erroneous labels each reduce performance, with erroneous labels causing the largest relative drops.

**Validation**: For datasets with pre-defined partitions, experiments are repeated 5 times using different seeds; for datasets without pre-defined partitions, 5-fold cross-validation is used.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Robustness

**Atlas Risks**:
- **Privacy**: Membership inference attack, Attribute inference attack, Reidentification
- **Robustness**: Data poisoning

**Potential Harm**: ['Privacy leakage: membership inference attacks', 'Privacy leakage: reconstruction attacks (reidentification)', 'Privacy leakage: attribute inference attacks', 'Label inference attacks']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper discusses privacy leakage risks in multimodal federated learning (membership inference, reconstruction, attribute inference, label inference) and suggests exploring privacy-enhancing techniques such as differential privacy and secure aggregation as future work.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
