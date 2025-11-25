# VaxxHesitancy: A Dataset for Studying Hesitancy towards COVID-19 Vaccination on Twitter

## 📊 Benchmark Details

**Name**: VaxxHesitancy: A Dataset for Studying Hesitancy towards COVID-19 Vaccination on Twitter

**Overview**: A publicly available dataset of over 3,101 English tweets annotated with users' attitudes towards COVID-19 vaccination (stance). The dataset reframes vaccine stance classification as a four-way task (pro-vaxx, anti-vaxx, vaxx-hesitant, irrelevant) and is intended to enable analysis and detection of vaccine hesitancy distinct from pro- and anti-vaccine stance.

**Data Type**: text (tweets)

**Domains**:
- Natural Language Processing
- Healthcare
- Computational Social Science

**Languages**:
- English

**Similar Benchmarks**:
- Cotfas et al. (2021)
- Poddar et al. (2022a)
- Chen, Chen, and Pang (2022)
- Di Giovanni et al. (2022)
- Delcea et al. (2022)

**Resources**:
- [GitHub Repository](https://github.com/GateNLP/VaxxHesitancy)
- [Resource](https://doi.org/10.5281/zenodo.7601328)
- [Resource](https://huggingface.co/GateNLP/covid-vaccine-twitter-bert)
- [GitHub Repository](https://github.com/GateNLP/gate-teamware)

## 🎯 Purpose and Intended Users

**Goal**: Re-frame vaccine stance classification as a four-way classification that includes a separate vaccine hesitancy category; provide a publicly available annotated dataset (3,101 tweets) and a domain-specific pre-trained language model (VaxxBERT) to support research and analysis of COVID-19 vaccine hesitancy.

**Target Audience**:
- ML Researchers
- Social Scientists
- Psychologists
- Policy Makers
- Public Health Researchers

**Tasks**:
- Stance Classification
- Text Classification
- Linguistic Analysis

**Limitations**: Annotated dataset size is limited to 3,101 tweets; dataset is monolingual (English); training set contains single-annotated tweets that may be noisier; multimodal information (images, video) is not included (noted as future work).

## 💾 Data

**Source**: Collected via the Twitter streaming COVID-19 API using a manually curated list of COVID-19 vaccine-related hashtags. Initial unlabelled collection D contains over 175 million tweets (October 2020 to May 2022). A temporally and topically stratified sample T was created and filtered; final annotated subset contains 3,101 English tweets.

**Size**: 175 million tweets (unlabelled collection D); 3,101 annotated tweets (final dataset T)

**Format**: CSV (11 columns) containing tweet IDs and annotation metadata; original tweets retrievable via Twitter API using tweet IDs

**Annotation**: Manual annotation by 18 volunteer annotators using GATE Teamware with annotator training and test sessions. Annotation protocol included single and double annotations, confidence scores (1-5) recorded per annotation, and quality control via inter-annotator agreement (Cohen's kappa). Test set comprises double-agreed tweets with confidence > 3.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation on held-out test set
- Model fine-tuning (BERT, COVID-BERT, VaxxBERT)
- Domain-adaptive pretraining for VaxxBERT
- Statistical significance testing (t-test)

**Metrics**:
- Accuracy
- Precision
- Recall
- F1-score

**Calculation**: Metrics are reported as the mean (and standard deviation) over five training runs with different random seeds. CrossEntropyLoss was used for training; models use early stopping. Test set defined as tweets where both annotators agree with confidence > 3.

**Interpretation**: Higher Accuracy and F1-score indicate better performance on the four-way vaccine stance classification task. The authors report that using higher-confidence annotations improves model performance and that domain-adaptive pretraining (VaxxBERT) yields better predictive performance than baselines.

**Baseline Results**: Set 3 (higher confidence selection): VaxxBERT: 73.04 ± 0.94% Accuracy, 69.29 ± 1.31 F1-score; COVID-BERT: 71.14 ± 0.94% Accuracy, 65.05 ± 1.17 F1-score; BERT (bert-large): 59.07 ± 0.74% Accuracy, 54.95 ± 1.32 F1-score.

**Validation**: Validation of annotations via inter-annotator agreement measured by Cohen's kappa across annotator pairs. Test set composed of double-annotated tweets where both annotators agree with confidence > 3. Experiments conducted across subsets with different annotation confidence thresholds to assess label quality effects on model performance.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotator names replaced with identifiers; only tweet IDs are shared in compliance with Twitter API policy; ethical approval obtained (University Research Ethics Committee #037567).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data collection and sharing comply with the Twitter data policies for research; ethical approval #037567.
