# ToxicBias

## 📊 Benchmark Details

**Name**: ToxicBias

**Overview**: A curated dataset (ToxicBias) derived from the Kaggle "Jigsaw Unintended Bias in Toxicity Classification" dataset to detect social biases in toxic language. The dataset is annotated for presence of social bias, five bias categories (gender, race/ethnicity, religion, political, LGBTQ), targeted groups, and bias implications. The paper also trains transformer-based models and reports baseline performance for bias identification, target generation, and implication generation, and discusses model bias mitigation via counter-narrative data augmentation.

**Data Type**: text (Wikipedia/social media comments with annotations: bias label, bias category, target terms, free-text implication)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Jigsaw Unintended Bias in Toxicity Classification
- CONAN
- Multi-target CONAN
- Toxigen
- StereoSet
- Crows-pairs

**Resources**:
- [GitHub Repository](https://github.com/sahoonihar/ToxicBias_CoNLL_2022)

## 🎯 Purpose and Intended Users

**Goal**: To extract and release a curated dataset for detecting unintended social biases from toxic language datasets; to provide annotations for bias presence, bias categories, targets, and bias implications; and to present methods (including counter-narrative augmentation) to reduce lexical overfitting/model bias.

**Target Audience**:
- Researchers working the problem of social bias detection on any form of text
- ML Researchers
- Model Developers

**Tasks**:
- Bias Detection (Binary Text Classification)
- Bias Category Detection (Multi-label Text Classification)
- Target Generation (Text Generation)
- Implication Generation (Text Generation)

**Limitations**: Lack of external context and small-sized dataset; only five types of social biases considered; only English language; dataset oriented toward western culture and annotations may not be relevant to non-western cultures; multilingual bias not taken into account.

## 💾 Data

**Source**: Curated from the Kaggle competition dataset "Jigsaw Unintended Bias in Toxicity Classification" (Wikipedia comments).

**Size**: 5,409 examples

**Format**: N/A

**Annotation**: Manual annotation by two trained annotators with adjudication by an expert. Annotated for presence of social bias (bias/neutral), bias category (five categories: gender, religion, race, LGBTQ, political), target terms (120 distinct target terms), and free-text bias implications. Inter-annotator agreement (first 2,500 instances) Cohen's Kappa = 64.3. Disagreements resolved by adjudication with expert.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (classification and generation models: Logistic Regression, SVM, Bi-LSTM+GloVe, BERT hierarchical, BERT multi-task, GPT-2)
- Automated metrics
- Data augmentation experiments (counter-narrative augmentation using CONAN and Multi-target CONAN)

**Metrics**:
- Accuracy
- Precision
- Recall
- Macro F1-score
- Area Under ROC Curve (AUC) - Subgroup AUC, Background Positive and Subgroup Negative AUC (AUC_bpsn), Background Negative and Subgroup Positive AUC (AUC_bnsp)
- BLEU-2
- ROUGE-L (F-measure)

**Calculation**: AUC-based metrics follow Borkan et al. (2019): Subgroup AUC computes AUC on instances containing a specified community word; AUC_bpsn uses biased background instances and neutral subgroup examples; AUC_bnsp uses neutral background instances and biased subgroup examples. AUC refers to Area Under the ROC curve (tradeoff between true positive rate and false positive rate). BLEU-2 and ROUGE-L were used for generation tasks. Macro F1 was used for bias classification evaluation.

**Interpretation**: Low Subgroup AUC indicates the model struggles to differentiate between biased and neutral comments for a community word. Low AUC_bpsn indicates high false positive rate (model misclassifies neutral subgroup mentions as biased). Low AUC_bnsp indicates high false negative rate (model misses biased comments mentioning the community). High AUC values indicate reduced lexical overfitting/model bias. Low F1 indicates high false positive and false negative rates.

**Baseline Results**: Logistic Regression (TF-IDF): Precision 0.67, Recall 0.50, F1 0.46, Accuracy 0.84. SVM: P 0.42, R 0.50, F1 0.46, Acc 0.84. Bi-LSTM + GloVe: P 0.59, R 0.58, F1 0.58, Acc 0.78. BERT (Hierarchical): P 0.62, R 0.66, F1 0.64, Acc 0.86. Transformer experiments with counter-narrative augmentation report improved AUC-based subgroup scores and BERT/GPT-2 variants with augmentation show higher P/R/F1 (examples: BERT multi-task with augmentation P 0.86, R 0.86, F1 0.86, Acc 0.87; GPT-2 with augmentation P 0.81, R 0.86, F1 0.84, Acc 0.81). Category detection per-category results are provided in the paper (see Table 5).

**Validation**: Dataset split into train/dev/test using an 80:8:12 stratified split. Inter-annotator agreement measured on first 2,500 instances (Cohen's Kappa = 64.3). Disagreements adjudicated by an expert. AUC-based subgroup metrics were used to evaluate resilience to data skews.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Robustness
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on affected communities
- **Robustness**: Hallucination

**Demographic Analysis**: Paper reports subgroup distributions and bias percentages for identity terms (Table 9) including counts and percent biased for identities such as black, jewish, lgbt, muslim, female. It also provides distribution across train/dev/test splits (Table 3).

**Potential Harm**: ['Potential for violence and hate crimes arising from toxic content', 'Harm to affected communities due to biased/toxic content', 'Potential harm to annotators due to exposure to toxic content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
