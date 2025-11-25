# Fine-Tuning Language Models for Scientific Writing Support

## 📊 Benchmark Details

**Name**: Fine-Tuning Language Models for Scientific Writing Support

**Overview**: We support scientific writers in determining whether a written sentence is scientific, to which section it belongs, and suggest paraphrasings to improve the sentence.

**Data Type**: text (sentences; parallel sentence pairs for paraphrasing)

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- GYAFC (Grammarly’s Yahoo Answers Formality Corpus)
- unarXive
- unarXive 2022

**Resources**:
- [GitHub Repository](https://github.com/JustinMuecke/SciSen)
- [Resource](http://portal.core.edu.au/conf-ranks/)
- [Resource](https://production-media.paperswithcode.com/about/papers-with-abstracts.json.gz)
- [Resource](https://files.pushshift.io/reddit/comments/)
- [Resource](https://www.kaggle.com/datasets/jannesklaas/scifi-stories-text-corpus)
- [Resource](https://www.kaggle.com/datasets/jojo1000/facebook-last-names-with-count)
- [Resource](https://huggingface.co/tuner007/pegasusparaphrase)
- [Resource](https://app.grammarly.com/)
- [Resource](https://openai.com/blog/chatgpt)

## 🎯 Purpose and Intended Users

**Goal**: Support scientific writers by (i) assigning a scientificness score to sentences, (ii) classifying sentences to paper sections, and (iii) suggesting paraphrases to improve scientific writing.

**Target Audience**:
- Scientific writers
- Researchers
- Students

**Tasks**:
- Regression (Scientificness Scoring)
- Multi-label Classification (Section Classification)
- Paraphrase Generation (Sentence Paraphrasing)

**Limitations**: Selection and labeling of the non-scientific datasets may pose a limitation. Unchanged (identity) outputs from paraphrasers can be a problem for general paraphrasing tasks but are acceptable for this application where inputs may already be scientific.

## 💾 Data

**Source**: Papers from arXiv (LaTeX available) accepted at A*, A, B, and C ranked conferences (CORE2021) mapped via Papers With Code; non-scientific sentences from Reddit comments, a sci-fi stories corpus, and Twitter subsets; paraphrasing parallel datasets Pegasus-DS (created using Pegasus fine-tuned for paraphrasing) and IDM-DS (created by inserting/deleting/modifying tokens using BERT MLM). GYAFC (Grammarly’s Yahoo Answers Formality Corpus) used for testing.

**Size**: 26,201 papers (21,774 A*, 3,665 A, 530 B, 232 C). Sentence counts reported: arXiv raw sentences 5,283,451 (4,958,863 remaining after filters); arXiv with section ID 2,864,755 (2,687,364 remaining); Books 1,763,465 (1,613,244 remaining); Reddit 279,288 (217,225 remaining); Twitter 268,419 (35,108 remaining). GYAFC test used: 1,332 sentences.

**Format**: Extracted sentence-level text from LaTeX sources (sentences split at ., ?, !). Citations replaced by <reference> tokens and math by <equation> tokens. Filtered to ASCII, 4–100 words, proper capitalization and end punctuation.

**Annotation**: Section labels obtained by extracting LaTeX \section{...} titles and mapping titles to predefined classes ("introduction", "related work", "method", "experiment", "result", "discussion", "conclusion"). Paraphrase parallel data created automatically: Pegasus-DS via Pegasus paraphraser, IDM-DS via random insert/delete/modify up to half tokens using BERT MLM. No manual expert annotation is described.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model fine-tuning (BERT, SciBERT, WideMLP, BART, T5, Pegasus, GPT-2)
- Regression
- Multi-label classification
- Paraphrase generation

**Metrics**:
- Mean Squared Error (MSE)
- Sample-based F1
- BLEU (n=4)
- METEOR
- BERTScore
- self-BLEU
- Word Error Rate (WER)

**Calculation**: Scientificness scored as regression evaluated with MSE. Section classification evaluated using sample-based F1 (following Galke et al.). BLEU computed with n-gram similarity (n=4). METEOR includes synonym matching. BERTScore computes cosine similarity of sentence embeddings using SciBERT. WER used to measure amount of changes for Pegasus-DS. self-BLEU computed between input and output.

**Interpretation**: Lower MSE indicates better scientificness scoring. Higher sample-based F1 indicates better section classification. Higher BLEU, METEOR, and BERTScore indicate paraphrase outputs closer to the gold standard. Lower self-BLEU indicates larger changes from the input (more aggressive paraphrasing). WER buckets indicate corruption/change levels.

**Baseline Results**: Scientificness MSE: fine-tuned BERT 0.181%, fine-tuned SciBERT 0.213%, WideMLP 0.049%. Section classification: BERT achieved up to 90.10% sample-based F1 (3-sentence input, all data). Paraphrasing: T5 Large performed best on fine-tuning datasets; T5 Base achieved highest BLEU on GYAFC test.

**Validation**: Random 70:20:10 train/validation/test split. Hyperparameter tuning on a 10% subset of train+validation. Early stopping for transformer fine-tuning (validation loss) and fixed epoch budgets described per task (e.g., BERT/SciBERT trained up to 5 epochs for regression). Test splits divided into buckets by amount of changes (0%–50%).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Robustness
- Value Alignment

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Robustness**: Hallucination
- **Value Alignment**: Over- or under-reliance

**Potential Harm**: ['Authorship concerns', 'Hallucinations (incorrect/invented content)', 'Extraction of training samples / exposing training data']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors note models were fine-tuned on publicly available papers only and pre-training checkpoints are public; they acknowledge the possibility of extracting training samples and advise users to verify suggested paraphrases.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
