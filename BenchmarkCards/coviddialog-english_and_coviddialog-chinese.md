# CovidDialog-English and CovidDialog-Chinese

## 📊 Benchmark Details

**Name**: CovidDialog-English and CovidDialog-Chinese

**Overview**: We collect two dialogue datasets (CovidDialog-English and CovidDialog-Chinese) containing conversations between doctors and patients about COVID-19 and related pneumonia to facilitate development of COVID-19-targeted dialogue systems and to train/evaluate dialogue generation models for COVID-19 consultations.

**Data Type**: text (doctor-patient dialogue utterance pairs)

**Domains**:
- Healthcare
- Medical Diagnosis

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- Reddit dialogues (used for DialoGPT pretraining)
- Chinese Chatbot Corpus
- 500k-Chinese-Dialog
- Large Scale Chinese Corpus for NLP

**Resources**:
- [GitHub Repository](https://github.com/UCSD-AI4H/COVID-Dialogue)
- [Resource](https://www.icliniq.com/en_US/)
- [Resource](https://www.healthcaremagic.com/)
- [Resource](https://www.healthtap.com/)
- [Resource](https://www.haodf.com/)
- [GitHub Repository](https://github.com/yangjianxin1/GPT2-chitchat)
- [GitHub Repository](https://github.com/codemayq/chinese_chatbot_corpus)
- [Resource](https://drive.google.com/file/d/1nEuew_KNpTMbyy7BO4c8bXMXN351RCPp/view)
- [GitHub Repository](https://github.com/brightmart/nlp_chinese_corpus)
- [GitHub Repository](https://github.com/huggingface/transformers)
- [Resource](https://arxiv.org/abs/2005.05442)

## 🎯 Purpose and Intended Users

**Goal**: To develop dialogue systems that can provide COVID-19-related consultations by collecting and releasing two medical dialogue datasets and evaluating dialogue generation models on them.

**Target Audience**:
- Researchers and developers of medical dialogue systems
- Model developers working on conversational AI for healthcare

**Tasks**:
- Dialogue Generation
- Conversational Response Generation

**Limitations**: The CovidDialog datasets are small in size, incurring a high risk of overfitting. The authors note that Chinese dialogues are more noisy (incorrect grammar, abbreviations, semantic ambiguities), making development more challenging. Informativeness of generated responses lags behind groundtruth, indicating need for incorporating medical knowledge.

## 💾 Data

**Source**: English dialogs crawled from online healthcare forums including https://www.icliniq.com/en_US/, https://www.healthcaremagic.com/, and https://www.healthtap.com/. Chinese dialogs crawled from https://www.haodf.com/. Duplicated and incomplete dialogues were removed. Dialogues were processed into (source, target) pairs where the source is the concatenation of previous utterances and the target is the doctor response.

**Size**: English: 603 consultations, 1,232 utterances, 90,664 tokens (English words). Chinese: 1,088 consultations, 9,494 utterances, 406,550 tokens (Chinese characters).

**Format**: N/A

**Annotation**: Converted into (source, target) pairs for dialogue generation (target = doctor response; source = concatenation of preceding utterances). Duplicated and incomplete dialogues removed. No additional manual annotation procedure described.

## 🔬 Methodology

**Methods**:
- Fine-tuning of pretrained Transformer encoder-decoder models
- Fine-tuning of pretrained GPT-family models (DialoGPT, GPT2-chitchat)
- Fine-tuning of BERT-GPT (encoder-decoder with pretrained BERT encoder and GPT decoder)
- Automatic evaluation using n-gram and diversity metrics
- Human evaluation with 5 annotators rating responses on Relevance, Informativeness, and Doctor-like (1-5 scale)

**Metrics**:
- Perplexity
- NIST-4
- BLEU-2
- BLEU-4
- METEOR
- Entropy-4
- Dist-1
- Dist-2
- Average Response Length
- Human ratings: Relevance (1-5), Informativeness (1-5), Doctor-like (1-5)

**Calculation**: Automatic metrics: Perplexity (lower is better). NIST (n=4), BLEU (n=2 and 4), METEOR compare n-gram overlap (higher is better). Entropy-4 and Dist-n (n=1,2) measure lexical diversity. Human evaluation: five undergraduate/graduate annotators rate responses from 1 to 5 on Relevance, Informativeness, and Doctor-like; ratings averaged across annotators.

**Interpretation**: For perplexity lower is better. For NIST, BLEU, METEOR, Entropy, and Dist higher is better. Human rating scale 1-5 with higher indicating better performance. The paper notes automatic metrics are not completely reliable for dialogue evaluation and complements them with human evaluation.

**Baseline Results**: English test set (Table 4): Perplexity - Transformer: 263.1, DialoGPT-small: 28.3, DialoGPT-medium: 17.5, DialoGPT-large: 18.9, BART: 15.3. NIST-4 - Transformer: 0.71, DialoGPT-small: 1.90, medium: 2.01, large: 2.29, BART: 1.88. BLEU-2 - Transformer: 7.3%, DialoGPT-small: 9.6%, medium: 9.4%, large: 11.5%, BART: 8.9%. BLEU-4 - Transformer: 5.2%, DialoGPT-small: 6.1%, medium: 6.0%, large: 7.6%, BART: 6.0%. METEOR - Transformer: 5.6%, DialoGPT-small: 9.0%, medium: 9.5%, large: 11.0%, BART: 10.3%. Dist-1 and Dist-2 and Entropy values also reported in Table 4. Human evaluation on English test set (Table 5) average scores: Relevance - Transformer: 2.45, DialoGPT-large: 2.98, BART: 3.04, Ground truth: 3.59; Informativeness - Transformer: 2.66, DialoGPT-large: 2.60, BART: 2.77, Ground truth: 3.53; Doctor-like - Transformer: 2.32, DialoGPT-large: 3.20, BART: 3.36, Ground truth: 3.50. Chinese test set (Table 8): Perplexity - Transformer: 53.3, DialoGPT-noMMI: 22.1, DialoGPT-MMI: 25.7, BERT-GPT: 10.8. Other automatic metrics in Table 8. Human evaluation on Chinese (Table 9) reported similarly.

**Validation**: English and Chinese datasets split by dialogs into train/validation/test with ratio 8:1:1. Hyperparameters tuned on validation set. For English, pretrained models fine-tuned for 5 epochs and un-pretrained Transformer trained for 50 epochs; checkpoint with lowest validation perplexity selected. For Chinese, training stopped when validation loss stopped decreasing. Human evaluation conducted on test set (English: full test; Chinese: 100 randomly-sampled test examples).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Governance**: Incorrect risk testing

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: For human evaluation, responses were de-identified so annotators did not know which method generated a response. No other privacy or anonymization procedures are described in the paper.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
