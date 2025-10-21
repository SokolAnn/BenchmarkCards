# HEAD-QA: A Healthcare Dataset for Complex Reasoning

## 📊 Benchmark Details

**Name**: HEAD-QA: A Healthcare Dataset for Complex Reasoning

**Overview**: HEAD-QA is a multi-choice question answering testbed composed of graduate-level questions from Spanish public healthcare specialization exams, intended to encourage research on complex reasoning in QA. The questions require specialized knowledge and reasoning and are challenging even for highly specialized humans; the dataset is provided in Spanish with an English translation and is evaluated in monolingual and cross-lingual settings.

**Data Type**: question-answering pairs (text) and image references (medical images)

**Domains**:
- Healthcare
- Medicine
- Nursing
- Biology
- Chemistry
- Psychology
- Pharmacology

**Languages**:
- Spanish
- English

**Similar Benchmarks**:
- bAbI
- SQuAD
- RACE
- ARC
- SWAG
- SciTail

**Resources**:
- [Resource](http://aghie.github.io/head-qa/)

## 🎯 Purpose and Intended Users

**Goal**: Encourage research on complex reasoning in question answering by providing a multi-choice dataset of graduate-level healthcare exam questions that combine the need for domain knowledge and reasoning.

**Target Audience**:
- Researchers
- Future work on QA systems

**Tasks**:
- Question Answering (Multi-choice)
- Open-domain Question Answering
- Cross-lingual Question Answering

**Limitations**: HEAD-QA includes images for a small percentage (~14%) of medicine questions but these images are included without being exploited in this work; radiophysics exams were excluded due to difficulty parsing equations from PDFs; the English version is an automatic Google API translation and shows issues with elements such as molecular formulae (translation adequacy and fluency were evaluated).

## 💾 Data

**Source**: Examination questions from the Spanish Ministerio de Sanidad, Consumo y Bienestar Social (public healthcare specialization exams) from 2013 to present, covering medicine (MIR), pharmacology (FIR), psychology (PIR), nursing (EIR), biology (BIR), and chemistry (QIR).

**Size**: 6,765 questions total (unsupervised setting); supervised splits: 2,657 training questions, 1,366 development questions, 2,742 test questions.

**Format**: JSON (fields include: version, language, exams, name, year, category, data; each question: qid, qtext, ra (right answer ID), answers (aid, atext)).

**Annotation**: Original correct answers taken from official exam answer keys (right answer ID provided). English version produced via Google API; translation quality evaluated by human annotators (adequacy and fluency). Invalid questions (if any) were removed; radiophysics exams were excluded.

## 🔬 Methodology

**Methods**:
- Control methods (Random Sampling, Blind option selection, Length-based selection)
- Information Retrieval baseline (DrQA Document Retriever)
- Multi-choice DrQA (document reader + span matching)
- BiDAF adapted for multi-choice
- DGEM (entailment-based)
- DecompAtt (entailment-based)
- Cross-lingual experiments using English translation (HEAD-QA-EN)

**Metrics**:
- Accuracy
- POINTS metric (right answer = +3 points, wrong answer = -1 point)

**Calculation**: Accuracy: proportion of correctly answered questions. POINTS: a right answer counts 3 points and a wrong answer subtracts 1 point (as used in the official exams).

**Interpretation**: HEAD-QA is challenging: model performance is substantially below human performance. Higher Accuracy and POINTS indicate better performance; human and pass mark POINTS are reported for comparison to show the gap between models and humans.

**Baseline Results**: Unsupervised setting: best average Accuracy reported for cross-lingual IR (ENIR) was 34.6% (Table 5) and ENIR average POINTS 87.6 (Table 6). Supervised setting: ENIR average Accuracy 37.2% (Table 7). Human performance (10 best) POINTS averages (Table 9): BIR 627.1, MIR 592.2, EIR 515.2, FIR 575.5, PIR 602.1, QIR 529.1. Pass marks (Table 9): BIR 219.0, MIR 207.0, EIR 180.0, FIR 201.0, PIR 210.0, QIR 185.0.

**Validation**: Official supervised splits defined by exam years (training: 2013-2014 exams; development: 2015; test: remaining years) to allow comparison with official human aggregated results. English translation quality was evaluated on a sample of 60 random questions: adequacy scores by two fluent Spanish-English speakers averaged 4.35 and 4.71 out of 5; fluency scored 4 out of 5 by a native English speaker.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
