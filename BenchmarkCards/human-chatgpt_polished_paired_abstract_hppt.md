# Human-ChatGPT Polished Paired abstracT (HPPT)

## 📊 Benchmark Details

**Name**: Human-ChatGPT Polished Paired abstracT (HPPT)

**Overview**: We introduce a novel dataset termed HPPT (ChatGPT-polished academic abstracts), facilitating the construction of more robust detectors. It diverges from extant corpora by comprising pairs of human-written and ChatGPT-polished abstracts instead of purely ChatGPT-generated texts. We also propose the Polish Ratio method to measure the degree of modification made by ChatGPT compared to the original human-written text.

**Data Type**: text (paired academic abstracts: human-written and ChatGPT-polished)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HC3 (Human ChatGPT Comparison Corpus)
- CDB (ChatGPT-Detector-Bias Dataset)

**Resources**:
- [GitHub Repository](https://github.com/Clement1290/ChatGPT-Detection-PR-HPPT)
- [Resource](https://huggingface.co/datasets/Hello-SimpleAI/HC3/tree/main)
- [Resource](https://huggingface.co/datasets/WxWx/ChatGPT-Detector-Bias)

## 🎯 Purpose and Intended Users

**Goal**: Detect ChatGPT-polished texts and quantify the degree of ChatGPT involvement using the Polish Ratio to build more robust detectors.

**Target Audience**:
- Users

**Tasks**:
- Text Classification
- Regression

**Limitations**: N/A

## 💾 Data

**Source**: Collected human-written abstracts from the ACL Anthology (ACL, EMNLP, COLING, NAACL) from 2018-2022; each abstract was polished using ChatGPT to create paired examples.

**Size**: 6,050 pairs of abstracts

**Format**: N/A

**Annotation**: Polish Ratio labels provided: Jaccard Distance and normalized Levenshtein Distance computed between original human-written abstracts and corresponding ChatGPT-polished abstracts. Human-written abstracts are assigned PR value 0.

## 🔬 Methodology

**Methods**:
- Roberta-based binary classification (black-box detector)
- Polish Ratio regression (Roberta features + MLP)
- GLTR explanation baseline
- In-domain and out-of-domain evaluation

**Metrics**:
- Accuracy
- Area Under ROC Curve (AUROC)
- Mean Absolute Error (MAE)
- Jaccard Distance
- Levenshtein Distance (normalized)

**Calculation**: Datasets are randomly partitioned into train:test:validation = 6:3:1. Accuracy and AUROC computed on test sets for detection. Polish Ratio regression optimized with Mean Square Error (MSE) and evaluated using Mean Absolute Error (MAE).

**Interpretation**: Polish Ratio (PR) value close to 0 indicates human-written text. PR > 0.2 indicates ChatGPT involvement. PR > 0.6 indicates ChatGPT generates most words. Higher Accuracy/AUROC indicate better detection; lower MAE indicates better PR regression.

**Baseline Results**: Results from Table 2: GPTZero ACC: - , - , 0.4406 ; AUROC: - , - , 0.6818. OpenAI-GPT-2 ACC: - , - , 0.4633 ; AUROC: - , - , 0.5604. OriginalityAI ACC: - , - , 0.4967 ; AUROC: - , - , 0.5721. DetectGPT ACC: HPPT 0.5129, HC3 0.8309, CDB 0.4593 ; AUROC: HPPT 0.6876, HC3 0.9058, CDB 0.7308. Roberta-HC3 ACC: HPPT 0.5285, HC3 0.9991, CDB 0.5848 ; AUROC: HPPT 0.7946, HC3 1.0000, CDB 0.7526. Roberta-HPPT (ours) ACC: HPPT 0.9465, HC3 0.9671, CDB 0.8825 ; AUROC: HPPT 0.9947, HC3 0.9931, CDB 0.9518.

**Validation**: Train/validation/test split = 6:3:1. The best model selected on the validation set. Models evaluated in-domain on HPPT and out-of-domain on HC3 and CDB; additional generalization experiments on Chinese CSL data and Llama2-polished texts reported.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Explainability
- Accuracy
- Societal Impact
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Explainability**: Untraceable attribution
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on education: plagiarism
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinformation', 'Phishing', 'Academic dishonesty']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
