# LBOXOPEN

## 📊 Benchmark Details

**Name**: LBOXOPEN

**Overview**: The first large-scale benchmark of Korean legal AI datasets, LBOXOPEN, that consists of one legal corpus, two classification tasks, two legal judgement prediction tasks, and one summarization task. The legal corpus consists of 147k Korean precedents (259M tokens). The tasks are: CASE NAME, STATUTE, LJP-CRIMINAL, LJP-CIVIL, and SUMMARIZATION. The authors also release extended variants and a Korean legal language model LCUBE trained on the corpus.

**Data Type**: text (legal precedent documents; fact-case name pairs; fact-statute pairs; fact + claim -> claim-acceptance labels; fact -> judgement labels; ruling+reasoning -> summary pairs)

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- Korean

**Similar Benchmarks**:
- ECtHR
- Swiss-Judgment-Prediction
- CAIL
- LexGLUE
- KLUE

**Resources**:
- [GitHub Repository](https://github.com/lbox-kr/lbox-open)
- [Resource](https://huggingface.co/datasets/lbox/lbox_open)
- [Resource](https://huggingface.co/lbox/lcube-base/tree/main)
- [Resource](https://arxiv.org/abs/2206.05224)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale Korean legal language benchmark to stimulate research on legal language understanding and legal judgement prediction and to provide resources (corpus and tasks) for training domain-specific language models.

**Target Audience**:
- Machine Learning Researchers
- Legal AI Researchers
- Model Developers
- Legal Domain Experts / Legal Practitioners

**Tasks**:
- Text Classification
- Legal Judgment Prediction
- Summarization

**Limitations**: Only precedents from first level trials are considered; plaintiff and defendant claims are not used as additional inputs in current datasets; does not currently include legal information retrieval tasks; dataset may not cover all social phenomena.

**Out of Scope Uses**:
- The authors state the datasets should be used for academic purpose only.

## 💾 Data

**Source**: PRECEDENT CORPUS constructed from 82k precedents retrieved from LAW OPEN DATA and an additional 65k precedents from the authors' internal database; datasets (CASE NAME, STATUTE, LJP-CRIMINAL, LJP-CIVIL, SUMMARIZATION) are extracted from this precedent corpus and Supreme Court Decision Report summaries.

**Size**: 147,000 precedents (259M tokens); specific task sizes: CASE NAME 11.3k (CASE NAME + 31k), STATUTE 3.3k (STATUTE + 17.7k), LJP-CRIMINAL 10.5k, LJP-CIVIL 4.7k, SUMMARIZATION 20k (SUMMARIZATION + 51k).

**Format**: JSON (final computer-readable documents saved in JSON format)

**Annotation**: Structured and labeled automatically via a custom data engineering pipeline (layout classifier, layout parser, OCR, post-OCR text corrector) with automatic parsing to extract labels (case names, statutes, fines, imprisonment ranges, claim amounts). Manual processing/verification is performed when ML module confidence is below thresholds; manual corrections and annotation were performed using the LWorks platform with ~100 part-time annotators.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics (string exact match, F1, ROUGE)
- Text-generation formulation for all tasks (models generate targets as text)
- Baseline model fine-tuning and pre-training experiments (domain adaptation and pretraining from scratch)
- Repeated experiments with multiple random seeds to compute error bars

**Metrics**:
- Exact Match (string exact match) for CASE NAME, STATUTE, and LJP-CIVIL
- F1 Score for LJP-CRIMINAL (per-field F1 for fine, imprisonment with labor, imprisonment without labor)
- ROUGE-1, ROUGE-2, ROUGE-Long for SUMMARIZATION

**Calculation**: CASE NAME, STATUTE, and LJP-CIVIL: string exact match between prediction and ground truth. LJP-CRIMINAL: compute F1 for each field using rules: (1) true positive if target exists in both GT and prediction and values equal; (2) false positive otherwise; (3) false negative if target exists only in GT; (4) false positive if field empty in GT but exists in prediction; (5) true negative if field empty in both GT and prediction. Summarization: ROUGE scores computed between generated summary and ground-truth summary.

**Interpretation**: Higher Exact Match, F1, and ROUGE scores indicate better performance. The paper interprets drops in scores at higher difficulty levels (e.g., finer quantization for LJP tasks) as increased task difficulty and uses improvements under domain-specific pretraining as evidence of corpus usefulness.

**Baseline Results**: Baselines reported (examples): KoGPT-2-base: CASE NAME EM 78.5±0.3, STATUTE EM 85.7±0.8, SUMMARIZATION R1 47.2, R2 39.1, RL 45.7. LCUBE-base: CASE NAME EM 81.1±0.3, STATUTE EM 87.6±0.5, SUMMARIZATION R1 46.0, R2 37.7, RL 44.5. mt5-small: CASE NAME EM 81.0±1.3, STATUTE EM 87.2±0.3, SUMMARIZATION R1 56.2, R2 47.8, RL 54.7. mt5-large: CASE NAME EM 82.9±0.2, STATUTE EM 88.1±0.5, SUMMARIZATION R1 59.0, R2 50.1, RL 57.6.

**Validation**: Train/validation/test splits provided per task (see Table 2); experiments repeated three times with different random seeds for error bars (except LJP-CRIMINAL Lv0 where two runs used); an additional test2 set constructed from precedents not included in PRECEDENT CORPUS for fair comparison; manual spot checks were performed for quality assurance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Misuse
- Accuracy
- Data usage restrictions

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Misuse**: Dangerous use
- **Accuracy**: Poor model accuracy
- **Data Laws**: Data usage restrictions

**Demographic Analysis**: The authors performed a case study on gender bias in LJP-CRIMINAL: for the category 'indecent act by compulsion', swapping victim gender on 131 test examples changed the model prediction in 11 examples; in 10 examples (7.6%) the predicted sentence decreased when victim gender was changed from female to male.

**Potential Harm**: ['Biased automatic legal decisions due to dataset bias', 'Potential enabling of illegal acts by making detailed criminal descriptions more accessible (dangerous use)', 'Negative social impacts from misuse of models without understanding dataset biases']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset uses precedents redacted/anonymized by the Korean government following the official redaction protocol; personal information are anonymized except for special cases where the government decides not to anonymize for social benefit.

**Data Licensing**: The authors state LBOXOPEN and LCUBE are released under Attribution-NonCommercial-NoDerivatives 4.0 license.

**Consent Procedures**: No additional consent was obtained from individuals; data are public precedents; individuals were not directly notified and no direct consent from individuals was obtained.

**Compliance With Regulations**: Precedents were obtained from public sources and follow Korean precedent redaction rules; the paper references Civil and Criminal Procedure Act and notes precedent disclosure status; dataset creation used officially anonymized precedents and discusses disclosure and copyright context in Korea.
