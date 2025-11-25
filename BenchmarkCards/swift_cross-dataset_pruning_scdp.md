# Swift Cross-Dataset Pruning (SCDP)

## 📊 Benchmark Details

**Name**: Swift Cross-Dataset Pruning (SCDP)

**Overview**: Swift Cross-Dataset Pruning (SCDP) enhances fine-tuning efficiency for NLP tasks in cross-dataset scenarios by rapidly evaluating sample importance using TF-IDF embeddings and applying dataset size-adaptive pruning to maintain diversity across various tasks and scales.

**Data Type**: N/A

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/he-y/NLP-Dataset-Pruning)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SCDP is to enhance fine-tuning efficiency for NLP tasks in cross-dataset scenarios while reducing computational resources.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Paraphrase Identification
- Natural Language Inference
- Sentiment Analysis
- Question Answering
- Reasoning

**Limitations**: While tested on six NLU tasks, the method’s performance on more complex tasks such as text generation is unknown.

## 💾 Data

**Source**: Experimental evaluation on six diverse datasets (RTE, MRPC, CoLA, SST-2, SWAG, QNLI) for demonstrating the effectiveness of SCDP.

**Size**: 2.49k to 105k examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Frequency Distance scores are calculated by assessing the importance of samples based on TF-IDF embeddings with geometric median.

**Interpretation**: Higher frequency distance scores indicate more important samples for dataset pruning.

**Validation**: Validation through extensive experiments on multiple datasets with varying tasks and scales.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
