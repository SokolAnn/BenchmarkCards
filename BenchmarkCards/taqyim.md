# Taqyim

## 📊 Benchmark Details

**Name**: Taqyim

**Overview**: A novel Python library, named Taqyim, developed as an extension of the OpenAI evals library to facilitate and streamline the evaluation of Arabic NLP tasks (summarization, diacritization, part of speech tagging, sentiment analysis, transliteration, machine translation, and paraphrasing) on models such as GPT-3.5 and GPT-4. Taqyim is designed with three principles: (1) Ease of Use, (2) Robustness, and (3) Debugging.

**Data Type**: text (articles, tweets, tokenized sentences)

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Similar Benchmarks**:
- Orca
- WikiLingua
- EASC
- AJGT
- PADT
- APB
- UNv1
- BOLT
- WikiNews

**Resources**:
- [GitHub Repository](https://github.com/ARBML/Taqyim)
- [GitHub Repository](https://github.com/openai/evals)
- [GitHub Repository](https://github.com/huggingface/datasets)
- [Resource](https://arxiv.org/abs/2306.16322)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of GPT-3.5 and GPT-4 on seven Arabic NLP tasks and to provide a Python library (Taqyim) that simplifies, hardens, and aids debugging of model evaluations.

**Target Audience**:
- ML Researchers
- Model Developers
- Arabic NLP Practitioners

**Tasks**:
- Summarization
- Diacritization
- Part of Speech Tagging
- Sentiment Analysis
- Transliteration
- Machine Translation
- Paraphrasing

**Limitations**: Model Selection Bias; Limited Exploration of Fewshot Demonstrations

## 💾 Data

**Source**: EASC; AJGT; PADT; APB; UNv1; BOLT; WikiNews (datasets used for evaluation as stated in the paper)

**Size**: EASC: 153 articles (test set); AJGT: 360 test samples; PADT: 680 test samples; APB: 1,010 test sentences; UNv1: ~4,000 Arabic-English pairs (test); BOLT: 6,653 test samples; WikiNews: 393 test samples (also described as 70 articles comprising ~18,300 words)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Zero-shot evaluation
- Few-shot evaluation
- Prompt engineering
- Temperature tuning
- Sliding overlapping context window with voting (for diacritization)
- Post-processing heuristics (for generation tasks)

**Metrics**:
- ROUGE-L
- Accuracy
- BLEU
- Diacritic Error Rate (DER)
- Word Error Rate (WER)

**Calculation**: Summarization: RougeL used to calculate similarity between gold and predicted summaries. Diacritization: overlapping context window (sliding window of 20 words with stride 2) with a popularity voting mechanism per character as in Mubarak et al. (2019). Token counts computed using the tiktoken library for context size handling. Other metrics (Accuracy, BLEU, WER) computed on the respective test splits of each dataset.

**Interpretation**: Higher ROUGE-L, Accuracy, and BLEU indicate better performance; lower DER and WER indicate better diacritization. Results are compared against reported state-of-the-art (SoTA) for each dataset; the paper reports that GPT-4 outperforms GPT-3.5 on five out of seven tasks.

**Baseline Results**: Summarized results from Table 2: Summarization (EASC, RougeL) GPT-3.5: 23.5, GPT-4: 18.25, SoTA: 13.3. Sentiment Analysis (AJGT, Accuracy) GPT-3.5: 86.94, GPT-4: 90.30, SoTA: 96.11. PoS Tagging (PADT, Accuracy) GPT-3.5: 75.91, GPT-4: 86.29, SoTA: 96.83. Paraphrasing (APB, BLEU) GPT-3.5: 4.295, GPT-4: 6.104, SoTA: 17.52. Translation (UNv1, BLEU) GPT-3.5: 35.05, GPT-4: 38.83, SoTA: 53.29. Transliteration (BOLT, BLEU) GPT-3.5: 13.76, GPT-4: 27.66, SoTA: 65.88. Diacritization (WikiNews, DER) GPT-3.5: 10.29, GPT-4: 11.64, SoTA: 1.21.

**Validation**: Evaluations were performed on the test splits of established datasets and results were compared against reported SoTA results for those datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Governance
- Value Alignment
- Transparency

**Atlas Risks**:
- **Transparency**: Lack of training data transparency
- **Accuracy**: Poor model accuracy
- **Governance**: Lack of testing diversity
- **Robustness**: Hallucination
- **Value Alignment**: Toxic output

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
