# JDDC (Jing Dong Dialogue Corpus)

## 📊 Benchmark Details

**Name**: JDDC (Jing Dong Dialogue Corpus)

**Overview**: We construct a large-scale real scenario Chinese E-commerce conversation corpus, JDDC, with more than 1 million multi-turn dialogues, 20 million utterances, and 150 million words. The dataset reflects characteristics of human-human conversations (e.g., goal-driven, long-term dependency), covers various dialogue types including task-oriented, chitchat and question-answering, provides extra intent information and three well-annotated challenge sets, and is intended to serve as an effective testbed for multi-turn dialogue research.

**Data Type**: multi-turn dialogue text (user and customer service utterances)

**Domains**:
- Natural Language Processing
- E-commerce

**Languages**:
- Chinese

**Similar Benchmarks**:
- Twitter Corpus
- Weibo Corpus
- Ubuntu Corpus
- Douban Corpus
- PERSONA-CHAT
- DuConv
- SGD Corpus
- ECD Corpus

**Resources**:
- [Resource](http://jddc.jd.com/auth_environment)
- [GitHub Repository](https://github.com/fxsjy/jieba)
- [Resource](https://www.jd.com)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale multi-turn Chinese E-commerce dialogue dataset and three challenge sets to serve as an effective testbed and benefit the development of fundamental research in multi-turn dialogue tasks and evaluation of dialogue systems.

**Target Audience**:
- ML Researchers
- Dialogue System Researchers
- Model Developers

**Tasks**:
- Response Generation
- Dialogue Response Selection (Retrieval)
- Question Answering
- Context Modeling
- Intent Classification

**Limitations**: The dataset currently does not include annotations for emotions and external knowledge (these will be added in future work).

## 💾 Data

**Source**: Conversations between users and customer service staff from Jing Dong (JD) E-commerce website, crawled, deduplicated, desensitized and anonymized.

**Size**: 1,024,196 multi-turn sessions; 20,451,337 utterances; 150,716,172 words

**Format**: N/A

**Annotation**: Intent labels for each query produced by a high-precision in-house classifier covering 289 intents (classifier trained on 578,127 professionally annotated instances with classification accuracy 93%); three human-annotated Challenge Sets with multiple ground-truth answers and weighted candidate answers (Challenge Set I: 300 dialogues / 300 questions with 10 candidate answers each; Challenge Set II: 15 dialogues / 168 questions with 10 candidate answers each; Challenge Set III: 108 dialogues / 500 questions with 3 candidate answers each).

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Baseline model evaluation (Retrieval-based and Generative models)

**Metrics**:
- BLEU
- ROUGE-L
- Distinct-1 (Distinct-1)
- Distinct-2 (Distinct-2)

**Calculation**: BLEU and ROUGE scores are used to measure the quality of generated responses via comparison with ground truths. Distinct-1/2 measures diversity by calculating the ratio of unique unigrams and bigrams in generated responses. For Challenge Sets, multiple candidate answers with weights are provided to allow more accurate calculation of metrics.

**Interpretation**: Higher BLEU/ROUGE indicate greater similarity to ground-truth responses; higher Distinct-1/2 indicate greater diversity of generated responses. Comparisons between retrieval and generative baselines are used as reference baselines.

**Baseline Results**: Automatic evaluation results (BLEU / ROUGE-L / Dist-1 / Dist-2): BM25: 9.94 / 19.47 / 5.03% / 28.89%; BERT-Retrieval: 10.27 / 19.90 / 5.23% / 30.85%; Vanilla Seq2Seq: 9.02 / 17.11 / 1.49% / 4.25%; Seq2Seq-Attention: 14.15 / 22.17 / 1.79% / 6.31%; Seq2Seq-Copy: 14.27 / 23.62 / 1.79% / 6.14%.

**Validation**: Dataset split for experiments: Training: 963,358 sessions (1,522,859 I-R pairs); Validation: 4,992 sessions (5,000 I-R pairs); Test: 4,992 sessions (5,000 I-R pairs). Three human-annotated Challenge Sets used for additional evaluation (Challenge Set I: 300 dialogues / 300 questions; Challenge Set II: 15 dialogues / 168 questions; Challenge Set III: 108 dialogues / 500 questions).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data desensitized and anonymized: private information replaced (e.g., all numbers replaced with token <NUM>, order IDs replaced with <ORDER-ID>).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
