# PAWS-X (Cross-lingual PAWS)

## 📊 Benchmark Details

**Name**: PAWS-X (Cross-lingual PAWS)

**Overview**: PAWS-X is a new dataset of human translated adversarial paraphrase identification evaluation pairs in six typologically distinct languages (French, Spanish, German, Chinese, Japanese, and Korean). It extends the Wikipedia portion of the original PAWS corpus with 23,659 (reported in abstract) human-translated evaluation pairs and is intended to measure multilingual models' sensitivity to word order, sentence structure, and context.

**Data Type**: text (sentence pairs with paraphrase labels)

**Domains**:
- Natural Language Processing

**Languages**:
- French
- Spanish
- German
- Chinese
- Japanese
- Korean

**Similar Benchmarks**:
- PAWS
- Multi30k
- Opusparcus

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/paws)
- [Resource](https://cloud.google.com/translate/)
- [Resource](http://goo.gl/language/bert)
- [Resource](https://fasttext.cc/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging cross-lingual paraphrase identification benchmark that probes models' ability to capture structure and context in multiple languages and to drive multilingual research on paraphrase identification.

**Target Audience**:
- Multilingual Natural Language Processing researchers
- Machine Learning researchers
- Model developers

**Tasks**:
- Paraphrase Identification

**Limitations**: Human translation was only applied to a random sample of 4,000 development pairs per language (2,000 dev + 2,000 test) due to time and cost constraints; the training set is machine-translated. The paper reports translation noise and inconsistent entity translations; the authors note some incorrect gold labels inherited from the original PAWS data. (Paper states <2% of pairs were not translated and final delivery guaranteed to have less than 5% word-level error rate.)

## 💾 Data

**Source**: Human translations of the Wikipedia portion of the original PAWS development and test sets for six languages (French, Spanish, German, Chinese, Japanese, Korean); neural machine translation used to translate the original PAWS English training set into the target languages. Original PAWS paraphrase labels are mapped to the translations.

**Size**: 23,659 human translated evaluation pairs (abstract) / PAWS-X includes 23,459 human-translated pairs (body); training set: original PAWS English training set of 49,401 pairs machine-translated (as stated in paper).

**Format**: N/A

**Annotation**: Paraphrase labels inherited from original PAWS (paraphrase / not paraphrase) and mapped to translated pairs. Human translations performed by in-house native speakers; a randomly sampled subset was validated by a second worker; authors verified translation quality on random samples.

## 🔬 Methodology

**Methods**:
- Automated metrics (model evaluation via fine-tuning and evaluation)
- Cross-lingual evaluation strategies (Translate Train, Translate Test, Zero Shot, Merged)

**Metrics**:
- Accuracy
- Area Under Curve - Precision-Recall (AUC-PR)

**Calculation**: For BERT, probability scores for the positive class are used to compute AUC-PR. For BOW and ESIM, a cosine threshold of 0.5 is used to compute accuracy. Best model checkpoints chosen based on accuracy on development sets; reported results are on test sets.

**Interpretation**: Higher Accuracy and AUC-PR indicate better model performance on paraphrase identification. PAWS-X is intended to measure sensitivity to word order and syntactic structure; strong gains for multilingual BERT (especially in merged training) indicate effectiveness of deep multilingual pre-training and cross-lingual training strategies.

**Baseline Results**: Average results over six non-English languages (Table 5): BOW Translate Train: Accuracy 52.7%, AUC-PR 48.4%; BOW Translate Test: Accuracy 55.2%, AUC-PR 47.3%. ESIM Translate Train: Accuracy 61.7%, AUC-PR 59.2%; ESIM Translate Test: Accuracy 63.9%, AUC-PR 65.1%. BERT Translate Train: Accuracy 84.2%, AUC-PR 88.2%; BERT Translate Test: Accuracy 82.3%, AUC-PR 87.6%. BERT Zero Shot: Accuracy 78.6%, AUC-PR 83.1%. BERT Merged: Accuracy 87.2%, AUC-PR 90.2%. (Detailed per-language numbers reported in Table 4.)

**Validation**: Human translations: 10-20 in-house native speakers per language performed translations; a randomly sampled subset was validated by a second worker; final delivery guaranteed <5% word-level error rate; authors further verified translation quality for a random sample of ten pairs in each language. Untranslatable or ambiguous sentences (<2%) were excluded. Best checkpoints selected based on development set accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
