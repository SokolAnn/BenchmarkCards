# Bengali Fake Review Detection (BFRD) dataset

## 📊 Benchmark Details

**Name**: Bengali Fake Review Detection (BFRD) dataset

**Overview**: Introduces the Bengali Fake Review Detection (BFRD) dataset for identifying fake food-related reviews in Bengali; also proposes a text conversion pipeline (translation and back-transliteration) and a weighted ensemble detection model combining pre-trained Bengali transformers.

**Data Type**: text (food-related reviews)

**Domains**:
- Natural Language Processing
- Social Media

**Languages**:
- Bengali

**Similar Benchmarks**:
- Ott dataset
- Yelp dataset
- Yelp Chi
- Yelp NYC
- Yelp ZIP
- Yelp Consumer Electronic
- BAD (Bengali aggressive text dataset)

**Resources**:
- [GitHub Repository](https://github.com/shahariar-shibli/Bengali-Fake-Reviews-A-Benchmark-Dataset-and-Detection-System)
- [GitHub Repository](https://github.com/sagorbrur/bnaug)
- [GitHub Repository](https://github.com/porimol/bnbphoneticparser)
- [Resource](https://pastebin.ubuntu.com/p/8gQMnCtRVw/)
- [Resource](https://gs.statcounter.com/social-media-stats/all/bangladesh)
- [Resource](https://abiword.github.io/enchant/)
- [Resource](https://py-googletrans.readthedocs.io/en/latest/)
- [GitHub Repository](https://github.com/sagorbrur/bangla-bert)
- [Resource](https://huggingface.co/neuropark/sahajBERT)

## 🎯 Purpose and Intended Users

**Goal**: Create a publicly accessible dataset (BFRD) and detection system to identify fake food-related reviews in Bengali.

**Target Audience**:
- Consumers
- Businesses
- Online review industry

**Tasks**:
- Text Classification
- Binary Classification
- Fake Review Detection

**Limitations**: Dataset is imbalanced; limited to food/restaurant reviews; limited number of skilled annotators; resource constraints resulted in shorter sequence lengths for some models.

## 💾 Data

**Source**: Manually collected food-related reviews in Bengali from social media (15 public Bengali Facebook groups and two YouTube channels), including posts and comments, collected between January 2019 and January 2023.

**Size**: 9,049 reviews (1,339 fake, 7,710 non-fake)

**Format**: N/A

**Annotation**: Manual annotation by four expert annotators (native Bengali speakers). Each review was annotated by three annotators; disagreements were resolved by an expert annotator via discussion; annotation quality measured using Fleiss' kappa (average 0.81). Annotation followed six predefined criteria for labeling a review as fake.

## 🔬 Methodology

**Methods**:
- Human annotation
- Model-based evaluation
- Automated metrics
- Explainable AI (LIME)

**Metrics**:
- Precision
- Recall
- F1-score
- Weighted F1-score
- Accuracy
- ROC-AUC
- Matthews Correlation Coefficient (MCC)

**Calculation**: Metrics computed using standard definitions: Precision = tp/(tp+fp); Recall = tp/(tp+fn); F1 = 2*(Precision*Recall)/(Precision+Recall). Weighted F1 computed by taking each class as positive separately and averaging. ROC-AUC and MCC computed as described in Appendix D of the paper.

**Interpretation**: Higher weighted F1 indicates better overall performance on the imbalanced binary task. The paper notes that a ROC-AUC between 0.7 and 0.8 is considered good. MCC close to 1 indicates robust performance across all confusion matrix entries.

**Baseline Results**: Best single-model without augmentation: BanglaBERT WF1 = 0.809 (Approach-1). With nlpaug augmentation BanglaBERT achieved WF1 = 0.981 (Approach-2). Proposed weighted ensemble achieved WF1 = 0.9843 on the nlpaug-augmented set (13,390 reviews) and WF1 = 0.9558 when using bnaug augmentation.

**Validation**: Dataset split into train/validation/test with 80%/10%/10%. Models were validated on the validation set and evaluated on a held-out test set. Annotation quality validated using Fleiss' kappa (average 0.81).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Explainability
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Explainability**: Unexplainable output
- **Societal Impact**: Impact on affected communities

**Potential Harm**: Detecting fake reviews aims to prevent deception of customers and damage to the reputation of products or services.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
