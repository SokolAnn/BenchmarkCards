# MusicInstruct (MI)

## 📊 Benchmark Details

**Name**: MusicInstruct (MI)

**Overview**: The MusicInstruct dataset comprises 60,493 Q&A pairs covering general questions related to music summarisation, as well as specific questions about music genres, moods, and instruments.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Music Information Retrieval

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/m-a-p/Music-Instruct/tree/main)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for training models capable of answering open-ended questions about music compositions.

**Target Audience**:
- ML Researchers
- Music Information Retrieval Researchers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from music captions in the MusicCaps datasets using prompt engineering with ChatGPT.

**Size**: 60,493 Q&A pairs

**Format**: JSON

**Annotation**: Automatically generated using few-shot learning techniques.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Human evaluation of answer quality

**Metrics**:
- BLEU
- METEOR
- ROUGE
- BERT-Score

**Calculation**: Metrics are calculated by comparing generated Q&A pairs to reference ones.

**Interpretation**: Higher scores indicate better alignment of generated responses to expected answers.

**Validation**: Quality assessment conducted on a random 1% sample with metrics for clarity, feasibility, and practicality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: cc-by-nc-4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
