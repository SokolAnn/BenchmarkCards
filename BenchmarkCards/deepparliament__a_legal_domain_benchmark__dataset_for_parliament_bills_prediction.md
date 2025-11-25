# DeepParliament: A Legal domain Benchmark & Dataset for Parliament Bills Prediction

## 📊 Benchmark Details

**Name**: DeepParliament: A Legal domain Benchmark & Dataset for Parliament Bills Prediction

**Overview**: This paper introduces DeepParliament, a legal domain Benchmark Dataset that gathers bill documents and metadata and performs various bill status classification tasks. The work proposes two new benchmarks: Binary and Multi-Class Bill Status classification, covering parliament bills from 1986 to the present, and provides dataset collection, detailed statistics, analyses, baseline models, and reproducible code and data.

**Data Type**: text (parliament bill documents and metadata)

**Domains**:
- Legal
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CAIL2018
- CUAD

**Resources**:
- [GitHub Repository](https://github.com/monk1337/DeepParliament)
- [Resource](https://paperswithcode.com/dataset/deepparliament)
- [Resource](https://openlegalai.github.io/DeepParliament)
- [Resource](https://loksabhaph.nic.in)
- [Resource](https://prsindia.org/billtrack)
- [Resource](https://pypi.org/project/pdfminer3)

## 🎯 Purpose and Intended Users

**Goal**: Provide a benchmark dataset (DeepParliament) for parliament bill status prediction (Binary and Multi-Class classification) to evaluate domain-specific language models on long, information-rich parliamentary bills and to catalyze research in legal NLP for bill document understanding and prediction.

**Target Audience**:
- Members of Parliament
- Members of the Legislative Assembly
- Presidents
- Legal practitioners
- Legal Natural Language Processing researchers
- Model developers

**Tasks**:
- Text Classification
- Binary Bill Status Classification
- Multi-Class Bill Status Classification

**Limitations**: DeepParliament is limited to evaluating English models at this time. The current version is limited by size. Documents in the dataset are long and unstructured, and current Transformer models are limited by their input size and cannot process full documents at once. Extended sequence models such as Longformer and BigBird are not evaluated in this work.

**Out of Scope Uses**:
- The proposed dataset and benchmark are not meant to replace or compete with the decisions of the Houses of Parliament and the President by any means

## 💾 Data

**Source**: Constructed from raw data collected from official and open websites aggregating parliament bills from 1986 to the present (sources: https://loksabhaph.nic.in and https://prsindia.org/billtrack). Bill PDFs were fetched from these sources; text was extracted using pdfminer3 and OCR was applied for image PDFs. Additional metadata (title, type of bill, source, pdf URL, status) were collected from the same sources.

**Size**: 5,329 documents total (4,223 train, 1,106 test); 284,103 tokens total (train vocab 243,393; test vocab 86,616); Avg document tokens 3,932.99; Max document tokens up to 227,407 as reported.

**Format**: Processed CSV (dataset converted into CSV format and combined into a single dataset) with original source PDFs; dataset published on HuggingFace Datasets for reproducibility.

**Annotation**: Labels (bill status) derived from metadata/status available on the official sources (Passed, Failed for Binary; Passed, Negatived, Lapsed, Removed, Withdrawn for Multi-Class). No manual crowdsourced annotation procedure is described.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (baseline models including LSTM, BiLSTM, CNN, CNN+Glove, BERT, RoBERTa, ALBERT, Legal-BERT, Legal-RoBERTa, Custom Legal-BERT)
- Repeated runs with different random seeds (five runs per method)

**Metrics**:
- Macro-averaged F1 Score
- Macro-averaged Precision
- Macro-averaged Recall
- Accuracy
- Recall

**Calculation**: Macro-averaging: compute the metric per label and then average across labels. For binary classification loss: binary cross-entropy. For multi-class classification loss: categorical cross-entropy. Reported scores are the average over five runs with different seeds.

**Interpretation**: Higher Macro-F1 / Accuracy indicates better performance. The paper states the dataset is challenging; the best baseline obtained 59.79% accuracy, indicating difficulty for current methods. Improvements reported when using more tokens from the start and middle portions of documents.

**Baseline Results**: Best baseline accuracy reported in the paper: 59.79% (paper notes dataset difficulty). Binary test set examples: Legal-RoBERTa Base Macro-F1 93.1% (Table 4). Multi-Class test set examples: Legal-BERT Base Macro-F1 61.4% and Bert Base Macro-F1 58.0% (Table 5).

**Validation**: Five runs with different seeds for each method; report average scores. Train/test split provided (4,223 train, 1,106 test).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Misuse

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Misuse**: Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: The paper states that a lapse of a bill has a negative impact on legislative work and that models could help reduce time wasted when bills lapse, implying the dataset aims to help mitigate legislative inefficiency caused by lapsed or delayed bills.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study states there is no privacy concern since all bill documents are collected from open-access databases. The documents do not include personal or sensitive information, except minor information provided by authorities (names of presidents, Union Council of Ministers, and other official administrative organisations).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
