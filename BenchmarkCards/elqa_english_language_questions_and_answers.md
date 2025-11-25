# ELQA (English Language Questions and Answers)

## 📊 Benchmark Details

**Name**: ELQA (English Language Questions and Answers)

**Overview**: A corpus of metalinguistic questions and answers about the English language, collected from two Stack Exchange forums, containing over 70k questions on topics including grammar, meaning, fluency, and etymology; intended to facilitate investigations of metalinguistic capabilities of NLU models and educational applications in language learning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education
- Linguistics

**Languages**:
- English

**Similar Benchmarks**:
- ELI5
- Natural Questions
- GooAQ
- CQADupStack
- DoQA
- MANtIS

**Resources**:
- [GitHub Repository](https://github.com/shabnam-b/ELQAflow)
- [Resource](https://english.stackexchange.com/)
- [Resource](https://ell.stackexchange.com/)
- [GitHub Repository](https://github.com/google-research/t5x)
- [Resource](https://openai.com/blog/gpt-3-apps)
- [Resource](https://archive.org/2)

## 🎯 Purpose and Intended Users

**Goal**: Provide a publicly available metalinguistic QA dataset of English questions and answers to facilitate metalinguistic studies, evaluate models' metalinguistic QA abilities, and support educational applications for language learners.

**Target Audience**:
- ML Researchers
- Model Developers
- Educational NLP researchers
- Language learning practitioners

**Tasks**:
- Question Answering
- Free-form Answer Generation

**Limitations**: Corpus only contains questions in English and about English; models presented are baselines not intended for deployment; potential biases reflecting demographics of authors represented in the training data (native language, level of English proficiency) are noted.

**Out of Scope Uses**:
- Do not deploy a generation system until it is approximately as reliable as existing non-automated alternatives, and present the output with caveats.

## 💾 Data

**Source**: Collected from two Stack Exchange sites: English Language & Usage (ENG) and English Language Learners (ELL), preprocessed from Internet Archive up to 2021-12-06; Stack Exchange data is publicly released under the CC-BY-SA 3.0 license.

**Size**: ELQA-large: 71,052 questions and 201,660 answers; ELQA-small: 20,711 questions and 81,133 answers (counts derived from Table 1).

**Format**: Text provided in HTML and plain text (without HTML tags).

**Annotation**: Human annotation for quality assurance on ELQA-small: two authors annotated 250 Q&A pairs for 'Is the question answerable?' and 'Does the answer fully address the question?' (results: 99.2% of questions answerable, 91.8% of answers acceptable). Additionally, two annotators labeled 100 random questions for the taxonomy with 92% agreement.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (ROUGE, BLEU, BERTScore)
- Human evaluation (two criteria: well-formedness and correctness/completeness, ratings 1-5 by annotators)
- Model-based evaluation (T5 fine-tuning; GPT-3 few-shot and fine-tuning)
- Closed-book question answering setup (no external context at evaluation time)

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BLEU Score
- BERTScore
- Human rating (1-5) for well-formedness (C1) and correctness/completeness (C2); z-scores per annotator

**Calculation**: Checkpoints were selected by interpolating BLEU, BERTScore and ROUGE on the dev set (best checkpoint at 75k updates). Human evaluation: each question evaluated by at least two raters; average score computed per item; z-scores computed per annotator to normalize inter-annotator variation.

**Interpretation**: Automatic metrics are of limited informativeness for this long free-form task; human evaluations show top-rated human answers are best, GPT-3 few-shot is roughly comparable to low-rated human answers; models generally score high on fluency (C1) but lower on correctness/completeness (C2).

**Baseline Results**: Automatic evaluation (overall, percentages): GPT-3 FS: ROUGE-1 31.2, ROUGE-2 8.5, ROUGE-L 20.3, BLEU 10.8, BERTScore 85.7; GPT-3 FT-1000: ROUGE-1 27.1, ROUGE-2 7.0, ROUGE-L 18.7, BLEU 11.8, BERTScore 85.2; T5-xxl: ROUGE-1 28.1, ROUGE-2 8.0, ROUGE-L 19.8, BLEU 4.7, BERTScore 80.3. Human evaluation (average scores out of 5): Top-rated human Avg C1=4.83, Avg C2=4.49; GPT-3 FS Avg C1=4.84, Avg C2=3.70; GPT-3 FT-1000 Avg C1=4.47, Avg C2=2.88; T5-xxl Avg C1=3.89, Avg C2=2.25.

**Validation**: ELQA-small was split into train/dev/test: train 21,175 Q&A pairs, dev 3,107, test 3,107; answers in these splits have score >= 4; if multiple high-rated answers exist they are included for training. Best model checkpoints selected via dev set interpolation of automatic metrics. Human annotation performed for quality assurance on ELQA-small.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Governance**: Unrepresentative risk testing

**Demographic Analysis**: Paper notes potential biases reflecting demographics of authors represented in the training data (native language, level of English proficiency) but does not provide a demographic breakdown.

**Potential Harm**: ['Misleading language learners with plausible but incorrect answers']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset released from public Stack Exchange content under the site license; authors state release is consistent with license terms requiring attribution. No specific anonymization procedures are described.

**Data Licensing**: CC BY-SA 3.0 (Stack Exchange data is publicly released under the CC-BY-SA 3.0 license).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
