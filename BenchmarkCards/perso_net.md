# PERSO NET

## 📊 Benchmark Details

**Name**: PERSO NET

**Overview**: PERSO NET is the first labeled dataset for situated and fine-grained personality understanding of fictional characters during book reading. It is constructed by annotating user notes from online reading apps as proxies for the original books, and targets situated personality prediction where a local snippet and preceding book history are used to predict a character's personality trait in a multi-choice setting.

**Data Type**: text (book snippets and user notes; sentence-level snippets with long-context history)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- NarrativeQA
- BookSum
- FairytaleQA
- MBTI personality prediction

**Resources**:
- [GitHub Repository](https://github.com/Gorov/personet_acl23)
- [Resource](http://ideonomy.mit.edu/essays/traits.html)
- [Resource](https://cidian.youdao.com/)
- [Resource](https://book.douban.com)
- [Resource](https://www.ireader.com.cn)
- [GitHub Repository](https://github.com/facebookresearch/LASER)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate situated and fine-grained personality understanding of book characters by predicting personality traits reflected by a local book snippet given all previous book content as background (situated personality prediction).

**Tasks**:
- Question Answering
- Machine Reading Comprehension
- Text Classification

**Limitations**: Annotation strategy accuracy may vary when generalizing to other problems beyond personality prediction; the unsupervised training technique does not support the Longformer reader with character history (Char-Hist Longformer); dataset focuses on classic literature for reproducibility which may introduce temporal biases and fairness considerations.

## 💾 Data

**Source**: User notes from online reading apps (underlined texts linked to notes) collected for public books (Gutenberg project) and their Chinese translations; trait vocabulary from the MIT Ideonomy project translated via Youdao; notes filtered to contain trait words and person names and clustered by position.

**Size**: Dataset covers 33 books and 274 unique characters. Reported totals: 51,803 English instances and 52,002 Chinese instances. Collections: 100 Gutenberg books initially collected, filtered to 33 books and 194 Chinese translations; 110,114 notes containing 140,268 trait mentions; 27,678 note clusters; 113,026 samples after clustering; 65,521 additional notes for weak supervision producing 154,030 paired examples and 31,346 recognized positive weakly-supervised examples. Annotation cost: $2,400 and 471.8 hours by annotators.

**Format**: N/A

**Annotation**: Manual annotation by human annotators: annotators read user notes (Chinese) and judge whether a note discusses a character's trait and mark the target character and trait. Annotators: 11 annotators; median 23.7 seconds per sample. Inter-annotator agreement: 88.67% agreement; Cohen's Kappa = 0.849. Bilingual projection: sentence alignment with vecalign and LASER; manual projection of 377 frequent character names.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model-based evaluation

**Metrics**:
- Accuracy
- Cohen's Kappa (inter-annotator agreement)

**Calculation**: Evaluation is performed in a multi-choice setting: for each instance the correct trait t is combined with 4 sampled negative candidates to form candidate set T; Accuracy is measured as top-1 selection of t from T. Reported results include mean and standard deviation over 5 runs for trained models. Cohen's Kappa computed on a duplicated set of 3,000 notes for inter-annotator agreement.

**Interpretation**: Higher Accuracy indicates better situated personality prediction. Human performance with book history is substantially higher than model performance (human w/ history ≈69.8% dev, 65.8% test; best models ≈45% test), and ambiguous instances imply an approximate upper bound of ~87.2% accuracy.

**Baseline Results**: Selected results on PERSO NET-en (Accuracy %): BERT (no-history) Dev 45.01 ±0.64 Test 42.96 ±1.07; Longformer Char-Hist + unsupervised Dev 46.39 ±0.63 Test 45.85 ±0.72; Human w/ history Dev 69.77 Test 65.75; GPT-davinci and ChatGPT few/zero-shot perform worse than supervised models. Chinese results (PERSO NET-zh): BERT Reader Test 48.70, BERT w/ Trait-History Test 51.25, Human w/ history Test 68.92. Fine-tuned LLMs (LLaMA + LoRA-sft) reported dev/test up to 47.67/49.32 on English subset.

**Validation**: Quality validated via human studies: 89.1% of sampled notes were judged accurate to book content, 9.7% ambiguous, 1.2% incorrect. Inter-annotator agreement: 88.67% and Cohen's Kappa 0.849. Bilingual alignment quality: >97% of sampled instances rated as perfect or high overlap. Note classifier cross-validation accuracy: 91.1% (dev) and 90.2% (test).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Data Laws

**Atlas Risks**:
- **Fairness**: Data bias
- **Data Laws**: Data usage restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Notes are anonymized for human annotation; user IDs masked in examples shown.

**Data Licensing**: Authors state they used Chinese-translated book versions for which they have licenses of usage; no explicit license types provided for the dataset in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
