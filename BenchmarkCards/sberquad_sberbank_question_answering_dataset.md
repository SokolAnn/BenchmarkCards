# SberQuAD (Sberbank Question Answering Dataset)

## 📊 Benchmark Details

**Name**: SberQuAD (Sberbank Question Answering Dataset)

**Overview**: SberQuAD — a large scale analog of Stanford SQuAD in the Russian language. The paper provides a description, in-depth analysis, and baseline experimental results for SberQuAD to present the dataset to the scientific community and facilitate research in multilingual question answering.

**Data Type**: question-answering pairs (paragraph-question-answer triples, text)

**Domains**:
- Natural Language Processing

**Languages**:
- Russian

**Similar Benchmarks**:
- SQuAD (Stanford Question Answering Dataset)
- SQuAD 2.0
- XQuAD
- TriviaQA
- Natural Questions
- MS MARCO
- QuAC
- CoQA

**Resources**:
- [GitHub Repository](https://github.com/sberbank-ai/data-science-journey-2017)
- [GitHub Repository](https://github.com/sberbank-ai/data-science-journey-2017/tree/master/problem_B/)
- [Resource](http://docs.deeppavlov.ai/en/master/features/models/squad.html)
- [Resource](https://youtu.be/J5HOjC4Xn_Y?t=29830)
- [Resource](https://opendatascience.slack.com/)
- [Resource](https://toloka.yandex.com)
- [Resource](http://aot.ru)
- [GitHub Repository](https://github.com/deepmipt/ru_sentence_tokenizer)
- [Resource](https://yandex.ru/dev/mystem/)
- [Resource](https://fasttext.cc/docs/en/crawl-vectors.html)

## 🎯 Purpose and Intended Users

**Goal**: To describe, analyze, and provide baseline experimental results for SberQuAD, a large-scale Russian reading comprehension dataset, and to present this resource to the scientific community to support research in multilingual question answering.

**Target Audience**:
- ML Researchers
- Natural Language Processing researchers
- Scientific community

**Tasks**:
- Question Answering
- Reading Comprehension

**Limitations**: The original development set is not publicly available; the hold-out test set is private. SberQuAD does not provide which Wikipedia pages paragraphs belong to. Each answer is represented by a string without a respective starting position in the paragraph. The dataset may contain annotation quality issues (misspellings, incorrect answers, yes/no questions, incomplete answers) and has only a single correct answer variant per question.

## 💾 Data

**Source**: Created by Sberbank for the 2017 data science competition. Paragraphs were selected from Wikipedia, split into paragraphs, and presented to crowd workers on the Toloka crowdsourcing platform who generated questions and paragraph-span answers following the SQuAD procedure. A SQuAD JSON variant is available from the DeepPavlov QA project.

**Size**: 50,364 training examples; ~15,000 development examples (available during competition); 25,000 testing examples (hold-out, private). For experiments in the paper the DeepPavlov partition was used: 45,328 training and 5,036 testing examples.

**Format**: Original CSV format; variant available in SQuAD JSON format

**Annotation**: Crowdsourced via Toloka (crowd workers) following the SQuAD procedure. Answers are paragraph spans (contiguous sequences of paragraph words). Answers in the dataset are represented as strings without provided start positions.

## 🔬 Methodology

**Methods**:
- Automated metrics (Exact Match and token-level F1)
- Baseline model evaluation (simple baseline, ML baseline)
- Evaluation of multiple neural models including BiDAF, DrQA, R-Net, DocQA, BERT
- In-depth dataset analysis (statistical and qualitative)
- Manual annotation and qualitative error analysis (e.g., manual tagging of 1,000 answers for NER; manual inspection of 100 errors)

**Metrics**:
- Exact Match (EM)
- F1 Score (token-level, maximum overlap between system response and ground truth answer, averaged over questions)

**Calculation**: Exact Match (EM) is the percentage of system answers that exactly match any gold answer. F1 Score is computed as the maximum token-level overlap between system response and gold answer, averaged over all questions. Both metrics ignore punctuation and capitalization.

**Interpretation**: Higher EM and F1 scores indicate better reading comprehension performance. The paper notes that higher lexical overlap (measured via Jaccard similarity and LCMS) between question and answer-containing sentence corresponds to higher F1. Models perform worse on SberQuAD than on SQuAD, which the authors attribute to dataset differences such as single-answer variants, fewer named-entity answers, and annotation quality issues.

**Baseline Results**: SberQuAD results (EM / F1): simple baseline: 0.3 / 25.0; ML baseline: 3.7 / 31.5; BiDAF: 51.7 / 72.2; DrQA: 54.9 / 75.0; R-Net: 58.6 / 77.8; DocQA: 59.6 / 79.5; BERT: 66.6 / 84.8.

**Validation**: Validation comprised statistical analyses, automatic evaluations using EM and F1 on held-out test partitions, manual annotation for NER evaluation on a 1,000-answer sample, and qualitative manual analysis of 100 questions where all models failed. The authors used the DeepPavlov partition (train/test) for experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Transparency
- Accuracy
- Governance

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Governance**: Lack of data transparency, Lack of system transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
