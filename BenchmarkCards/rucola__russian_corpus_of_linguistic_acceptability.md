# RuCoLA: Russian Corpus of Linguistic Acceptability

## 📊 Benchmark Details

**Name**: RuCoLA: Russian Corpus of Linguistic Acceptability

**Overview**: RuCoLA is the Russian Corpus of Linguistic Acceptability, built from the ground up under the well-established binary linguistic acceptability (LA) approach. RuCoLA consists of 9.8k in-domain sentences from linguistic publications and 3.6k out-of-domain sentences produced by generative models. The out-of-domain set is created to facilitate the practical use of acceptability for improving language generation. The paper releases RuCoLA, the code of experiments, and a public leaderboard to assess the linguistic competence of language models for Russian.

**Data Type**: text (sentences with binary acceptability labels)

**Domains**:
- Natural Language Processing
- Linguistics

**Languages**:
- Russian

**Similar Benchmarks**:
- CoLA
- ItaCoLA

**Resources**:
- [Resource](https://rucola-benchmark.com)
- [GitHub Repository](https://github.com/RussianNLP/RuCoLASource)

## 🎯 Purpose and Intended Users

**Goal**: Provide the first large-scale acceptability classification corpus in Russian (13.4k sentences) to evaluate sentence acceptability and facilitate diagnostic evaluation and improvements of language generation.

**Target Audience**:
- Natural Language Processing Researchers
- Model Developers
- Computational Linguists
- NLP Practitioners

**Tasks**:
- Text Classification (Binary Acceptability Classification)
- Evaluation of Language Generation
- Hallucination Detection

**Limitations**: Explicit limitations stated: reliability and reproducibility concerns of acceptability judgments; potential lack of representativeness because in-domain labels are drawn from linguistic literature (expert bias); time-consuming and resource-intensive data collection; coarse-grained annotation scheme limits the scope of diagnostic evaluation; possible distribution shift between models' pre-training corpora and RuCoLA (word frequency differences) that can introduce bias in evaluation.

## 💾 Data

**Source**: In-domain: sentences and authors' acceptability judgments drawn from linguistic textbooks, academic publications, and methodological materials (examples: rusgram, Testelets (2001), Lutikova (2010), Paducheva (2004/2010/2013), Shavrina et al. (2020)). Out-of-domain: sentences produced by nine open-source machine translation and paraphrase generation models using subsets of Tatoeba, WikiMatrix, TED, and Yandex Parallel Corpus (models include OPUS-MT, M-BART50, M2M-100, ruGPT2-Large, ruT5, mT5 variants).

**Size**: 13,445 sentences (9,837 in-domain; 3,608 out-of-domain); coarse-grained annotation for 3.7k unacceptable sentences.

**Format**: N/A

**Annotation**: Two-stage annotation for machine-generated sentences: Stage 1 — acceptability judgments via Toloka by native Russian speakers with dynamic overlap (3–5 workers per item), majority vote after filtering by response time and control-task performance; Stage 2 — validation and violation-category annotation by 30 undergraduate/graduate students in philology/linguistics (multi-label among Morphology, Syntax, Semantics, Hallucinations, Other). In-domain acceptability labels are drawn from the source linguistic publications.

## 🔬 Methodology

**Methods**:
- Non-neural baselines (majority vote, logistic regression over tf-idf features)
- Acceptability measures from pretrained LMs (PenLP from ruGPT-3 medium)
- Finetuned Transformer models (ruBERT, ruRoBERTa, ruT5, XLM-R, RemBERT)
- Human evaluation (expert students)

**Metrics**:
- Accuracy
- Matthews Correlation Coefficient (MCC)
- Per-category recall (reported in analysis)

**Calculation**: Performance measured by Accuracy and Matthews Correlation Coefficient (MCC). MCC on the validation set is used for hyperparameter tuning and early stopping. Results are reported as averages over ten restarts from different random seeds. For the PenLP acceptability measure, thresholds are selected via 10-fold cross-validation on the train set and evaluated using MCC on the validation set.

**Interpretation**: Higher Accuracy and MCC indicate better acceptability classification. The human baseline achieves MCC 0.63 (Accuracy 84.08) on the test set; the best model (ruRoBERTa) attains MCC 0.54 (Accuracy 80.8), i.e., remains behind humans by approximately 0.09 MCC points.

**Baseline Results**: Selected overall test set results: ruRoBERTa (finetuned) — Accuracy 80.8, MCC 0.54; RemBERT — Accuracy 76.21, MCC 0.44; ruBERT — Accuracy 75.9, MCC 0.42; ruT5 — Accuracy 71.26, MCC 0.27; ruGPT-3 + PenLP — Accuracy 55.79, MCC 0.27; Majority baseline — Accuracy 68.05, MCC ~0.0; Human — Accuracy 84.08, MCC 0.63.

**Validation**: In-domain split: 80/10/10 (train/dev/test ≈ 7.9k/1k/1k). Out-of-domain split: 50/50 (validation and private test ≈ 1.8k/1.8k). Each split is balanced by class, source type, and violation category. MCC on validation used for hyperparameter tuning and early stopping; reported results averaged over ten random seeds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Misuse
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Misuse**: Improper usage
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Detection of hallucinated content in generated text', 'Filtering implausible or ungrammatical generated text to improve language generation quality']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Responses of human annotators are collected and stored anonymously; annotators are warned about potentially sensitive topics. Annotation pay rates are reported and exceed the hourly minimum wage in Russia (stated pay rates: Stage 1 $2.55/hr, Stage 2 $5.42/hr, Human benchmark $6.3/hr).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
