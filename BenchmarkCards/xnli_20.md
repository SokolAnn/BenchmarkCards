# XNLI 2.0

## 📊 Benchmark Details

**Name**: XNLI 2.0

**Overview**: In this work, we focus on improving the original XNLI dataset by re-translating the MNLI dataset in all of the 14 different languages present in XNLI, including the test and dev sets of XNLI using Google Translate. We also perform experiments by training models in all 15 languages and analyzing their performance on the task of natural language inference.

**Data Type**: text (natural language inference premise-hypothesis pairs with labels)

**Domains**:
- Natural Language Processing
- Natural Language Understanding

**Languages**:
- English
- French
- Spanish
- German
- Greek
- Bulgarian
- Russian
- Turkish
- Arabic
- Vietnamese
- Thai
- Chinese
- Hindi
- Swahili
- Urdu

**Similar Benchmarks**:
- XNLI
- MNLI
- GLUE
- XTREME

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Improve the original XNLI dataset by re-translating MNLI into the 14 XNLI languages using Google Translate and evaluate model performance on cross-lingual natural language inference, including analysis for low-resource languages such as Swahili and Urdu.

**Tasks**:
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: MNLI dataset machine-translated into 14 languages using Google Translate; test and dev sets re-translated using Google Translate; XNLI 2.0 consists of these machine-translated train sets and re-translated test and dev sets.

**Size**: 112,500 examples (XNLI total); 392,000 examples in the training set

**Format**: N/A

**Annotation**: Labels inherited from the MNLI annotations; text translations generated using Google Translate. Original XNLI test/dev translations were done by human translators but were retranslated using Google Translate for XNLI 2.0.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (fine-tuning XLM-RoBERTa base)
- Automated metrics (accuracy)

**Metrics**:
- Accuracy

**Calculation**: Accuracy reported as the accuracy score on test sets (percentage of correct NLI classification predictions) as tabulated in the paper's results tables.

**Interpretation**: The XNLI 2.0 test set yields approximately a 2.5%–3% higher average accuracy across the 15 languages compared to the original XNLI test set. Models trained on certain non-English high-resource languages (e.g., German) achieve higher average accuracy (German 78.15% vs English 76.63% on XNLI 2.0) indicating better cross-lingual transfer for some languages.

**Baseline Results**: Conneau 2020 XLM-R Base reported average accuracy 76.21 (table entries). The paper reports an English-trained model average accuracy of 73.11 on the original XNLI test set and 76.63 on the XNLI 2.0 test set. The German-trained model average accuracy on XNLI 2.0 is reported as 78.15.

**Validation**: Training/validation split used during fine-tuning: 80% of dataset for training and 20% for validation; models were fine-tuned for three epochs using the Adam optimizer and XLM-R tokenizer.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
