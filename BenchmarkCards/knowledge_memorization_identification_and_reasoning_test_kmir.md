# Knowledge Memorization, Identification, and Reasoning test (KMIR)

## 📊 Benchmark Details

**Name**: Knowledge Memorization, Identification, and Reasoning test (KMIR)

**Overview**: We propose a benchmark, named Knowledge Memorization, Identification, and Reasoning test (KMIR). KMIR covers 3 types of knowledge, including general knowledge, domain-specific knowledge, and commonsense, and provides 184,348 well-designed questions to evaluate knowledge memorization, identification, and reasoning abilities of pre-trained language models (PLMs).

**Data Type**: question-answering pairs (cloze-style text)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- LAMA
- KILT

**Resources**:
- [GitHub Repository](https://github.com/KMIR2021/KMIR)
- [Resource](https://query.wikidata.org/)
- [GitHub Repository](https://github.com/commonsense/conceptnet5/wiki/API)
- [Resource](https://arxiv.org/abs/2202.13529)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate knowledge memorization, identification, and reasoning abilities of pre-trained language models (PLMs) and assess their suitability as knowledge sources.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Masked Language Modeling (Cloze completion)
- Entity Distinction
- Statement Checking
- Predicate Reasoning

**Limitations**: The knowledge used in the dataset could have some mistakes or be out-of-date. The dataset is licensed for academic research only and does not support commercial usages.

**Out of Scope Uses**:
- Commercial usages

## 💾 Data

**Source**: Collected knowledge triples from WikiData and ConceptNet; converted into cloze question-answer pairs via a template-based generation method and manual quality control.

**Size**: 192,078 knowledge triples; 184,348 question-answer pairs; 95,532 queried entities

**Format**: N/A

**Annotation**: Manual quality control by annotators: filtered out questions involving violence, pornography, discrimination, and sovereignty disputes; corrected ambiguous questions by refining templates; filtered out triple-completion questions with non-unique answers. Randomly selected 16,000 questions for checking, totaling about 532 hours of annotation.

## 🔬 Methodology

**Methods**:
- Automated metrics (F1 Score)
- Model fine-tuning and evaluation of pre-trained language models (BERT, RoBERTa, ALBERT, ELECTRA, DistilBERT, DistilRoBERTa)
- Baselines including Random Guess
- Co-occurrence analysis via ElasticSearch (ES score) to assess memorization vs. reasoning

**Metrics**:
- F1 Score

**Calculation**: Predictions and correct answers are split into words; token-level F1 measure between prediction and gold answer is computed (following Rajpurkar et al., 2016).

**Interpretation**: F1 measures token overlap between prediction and gold answers. Results across different question types are not directly comparable because some question types are multi-choice-like (smaller answer space) while others are open-ended.

**Baseline Results**: F1 scores (%) on question types (Triple Completion / Statement Checking / Entity Distinction / Predicate Reasoning): Random Guess: 0.00017 / 50.00 / 25.00 / 18.75; BERT (110M): 15.34 / 61.57 / 30.01 / 26.82; ELECTRA (110M): 14.98 / 63.09 / 33.27 / 27.52; DistilBERT (66M): 14.37 / 59.89 / 28.56 / 24.38; ALBERT (11M): 11.79 / 63.42 / 32.46 / 27.16; RoBERTa (125M): 15.50 / 66.13 / 35.92 / 29.19; DistilRoBERTa (82M): 14.64 / 63.02 / 32.67 / 27.02.

**Validation**: Quality control: manual review of generated questions (random sample of 16,000 questions checked), filtering sensitive content, refining templates to remove ambiguity, and removing non-unique-answer triple-completion questions (total ~532 hours).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Intellectual Property
- Misuse
- Data Laws

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Robustness**: Hallucination
- **Intellectual Property**: Data usage rights restrictions
- **Misuse**: Spreading toxicity
- **Data Laws**: Data usage restrictions

**Potential Harm**: ['violence', 'pornography', 'discrimination', 'sovereignty disputes']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Personnel information involved is public information of public figures from WikiData and does not involve personal privacy.

**Data Licensing**: KMIR questions: CC BY-NC-SA 4.0. Wikidata: CC0. ConceptNet: Creative Commons Attribution-ShareAlike 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
