# Beyond Token Limits: Assessing Language Model Performance on Long Text Classification

## 📊 Benchmark Details

**Name**: Beyond Token Limits: Assessing Language Model Performance on Long Text Classification

**Overview**: This paper evaluates the performance of language models on the Comparative Agendas Project classification task involving long texts that exceed 512 tokens, comparing models including BERT and its versions, Longformer, and generative models like GPT-3.5, GPT-4, and Llama.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hungarian
- Dutch
- French
- Italian

**Resources**:
- [Resource](https://osf.io/w3fjn/?view_only=67372dd98f0b48349546752fee5b4e50)

## 🎯 Purpose and Intended Users

**Goal**: To assess the impact of input text length on language model performance for the multiclass classification task of the Comparative Agendas Project.

**Target Audience**:
- Researchers in NLP
- Academics in policy analysis
- Model developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Publicly accessible data from the Comparative Agendas Project website.

**Size**: 713,616 documents (Hungarian), 973,481 documents (English), 62,038 documents (Dutch), 12,694 documents (French), 10,025 documents (Italian)

**Format**: N/A

**Annotation**: Hand-coded using 21 Comparative Agendas Project (CAP) labels.

## 🔬 Methodology

**Methods**:
- Fine-tuning
- Zero-shot classification
- One-shot classification

**Metrics**:
- Weighted macro F1-score
- Precision
- Recall

**Calculation**: Weighted macro F1-score combines precision and recall into a single measure, averaged with contributions of each class weighted by the number of examples.

**Interpretation**: Higher F1 scores indicate better model performance in classification tasks.

**Baseline Results**: xlm-roberta-base fine-tuned achieved 0.94 weighted macro F1 (English), and 0.76 (Hungarian).

**Validation**: Model validation involved early stopping based on validation loss.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
