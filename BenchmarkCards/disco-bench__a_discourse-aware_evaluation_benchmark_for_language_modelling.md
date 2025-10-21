# Disco-Bench: A Discourse-Aware Evaluation Benchmark for Language Modelling

## 📊 Benchmark Details

**Name**: Disco-Bench: A Discourse-Aware Evaluation Benchmark for Language Modelling

**Overview**: Disco-Bench is a benchmark to evaluate intra-sentence discourse properties across a diverse set of NLP tasks (understanding, translation, and generation). It consists of nine document-level testsets in the literature domain in Chinese and/or English (eight newly created and one expanded), a diagnostic test suite of 1,294 handcrafted contrastive examples, and a large-scale document-level pretraining corpus (400GB).

**Data Type**: text (document-level; question-answering pairs, translation pairs, generation examples, contrastive pairs)

**Domains**:
- Natural Language Processing
- Literature

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- SentEval
- DiscoEval
- GLUE
- SuperGLUE
- CLUE
- XGLUE
- LOT
- C3

**Resources**:
- [GitHub Repository](https://github.com/longyuewangdcu/Disco-Bench)
- [Resource](https://arxiv.org/abs/2307.08074)

## 🎯 Purpose and Intended Users

**Goal**: To provide a discourse-aware evaluation benchmark that measures models' abilities to model intra-sentence discourse phenomena (e.g., cohesion and coherence) across understanding, translation, and generation tasks using document-level literary texts.

**Target Audience**:
- ML Researchers

**Tasks**:
- Speaker Identification
- Zero Pronoun Recovery
- Machine Reading Comprehension
- Document-level Machine Translation (Novel Translation)
- Classical Chinese to Modern Chinese Translation (CCT)
- Poetry Translation
- Text Expansion
- Text Infilling
- Text Completion

**Limitations**: Reference-based automatic metrics are less reliable for open-ended generation; how to accurately measure open-ended text generation is an open question and is beyond the scope of this paper. METEOR resources are not available for Classical Chinese evaluation (explicitly stated).

## 💾 Data

**Source**: Document-level literary texts in Chinese and English including web fiction, novels, classical texts, poetry, books, movie subtitles, dialogues, and reading-comprehension examinations (e.g., Haihua2021). Benchmark datasets comprise nine document-level datasets (eight newly created and one expanded). Diagnostic test suite consists of handcrafted contrastive pairs. Pretraining corpus is drawn from literature texts in Chinese and English.

**Size**: Benchmark datasets: training sizes range from 26.4K examples to 2.4M examples (paper: 'data quantities (from 26.4K to 2.4M)'). Diagnostic test suite: 1,294 contrastive examples. Pretraining corpus: 400GB. Pretraining totals reported: Chinese ~140,327,150 documents (~84,699,369,004 characters), English ~39,844,197 documents (~30,406,144,834 words).

**Format**: N/A

**Annotation**: Combination of manual expert annotation for test sets (e.g., manually annotated 8K ZPR test set, manual supplement for MRC), semi-automatic generation and filtering for TE (Stanford Parser + rule-based deletion + LM perplexity filtering), automatic construction for large-scale ZPR training via word alignments, and human evaluation for benchmark quality (fluency and adequacy ratings).

## 🔬 Methodology

**Methods**:
- Automated metrics (BLEU, TER, METEOR, COMET, BERTScore, Perplexity, Dist-n, F1, Exact Match, Accuracy, Precision, Recall)
- Human evaluation (fluency and adequacy ratings; inter-annotator agreement measured with Cohen's kappa and Krippendorff’s alpha)
- Contrastive testing / diagnostic test suite (ranking correct vs incorrect candidates by model probability)
- Forced-decoding for translation diagnostic evaluation
- Fine-tuning of pretrained models and evaluation on downstream tasks

**Metrics**:
- F1 Score
- Exact Match
- Accuracy
- BLEU Score
- TER
- METEOR
- COMET
- BERTScore
- Perplexity
- Distinct-n (Dist-2, Dist-4)
- Precision
- Recall

**Calculation**: Standard metric calculations as described in the paper: BLEU measures n-gram precision with a brevity penalty; TER measures edit distance; METEOR includes exact, stem, and synonym matches; COMET is a learned neural evaluation metric trained on human rankings; Perplexity computed using a GPT-2 language model (as stated); diagnostic contrastive evaluation computes model probabilities for correct and incorrect candidates and measures whether the correct candidate is ranked higher (ranking accuracy); forced-decoding is used to compute hypothesis probabilities for translation diagnostic instances.

**Interpretation**: Higher values of BLEU, F1, Accuracy, BERTScore indicate better performance; lower TER and Perplexity indicate better performance. For the diagnostic test suite, higher accuracy (ranking correct candidate above incorrect) indicates better discourse modeling. The paper notes that reference-based metrics are less reliable for open-ended generation and that best models still have fairly low absolute scores, highlighting task difficulty.

**Baseline Results**: Representative baseline results reported in the paper (Table 7): Disco-Bench pretrained RoBERTa (large) achieves SI=89.6, ZPR=34.3, MRC=56.7. Disco-Bench pretrained BART (large) achieves TE=36.2 (BLEU), TI (BERTScore)=62.4, TC (BERTScore)=60.7. GPT-4 achieves MRC=63.2, TI=60.4, TC=59.6. The paper reports full baseline results across many models and tasks in Table 7 and additional metrics in Tables 8-10.

**Validation**: Human evaluation of benchmark quality: inter-annotator agreement for understanding tasks measured with Cohen's kappa (SI=0.76, ZPR=0.91, MRC=0.97). For translation and generation, two annotators assessed 100 random instances per task for fluency and adequacy (1-5); reported scores >4 with reasonable agreement; Krippendorff’s alpha used for some measures. Diagnostic test suite contains 250 MRC, 500 NT, and 250 TC instances across cohesion types to validate discourse probing.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
