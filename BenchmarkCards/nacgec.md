# NaCGEC

## 📊 Benchmark Details

**Name**: NaCGEC

**Overview**: We present a challenging CGEC benchmark derived entirely from errors made by native Chinese speakers in real-world scenarios.

**Data Type**: sentence pairs (incorrect-correct)

**Domains**:
- Natural Language Processing
- Education
- Government
- Journalism

**Languages**:
- Chinese

**Similar Benchmarks**:
- NLPCC
- CGED
- YACLC
- MuCGEC
- Lang-8
- HSK

**Resources**:
- [GitHub Repository](https://github.com/masr2000/CLG-CGEC)
- [Resource](https://arxiv.org/abs/2210.10442)

## 🎯 Purpose and Intended Users

**Goal**: To automatically construct large-scale CGEC training corpora using linguistic rules (CLG) and to provide a challenging human-annotated test benchmark (NaCGEC) containing grammatical errors made by native Chinese speakers to better evaluate and improve CGEC models.

**Target Audience**:
- CGEC researchers
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Grammatical Error Correction

**Limitations**: This work focuses on Chinese; the CLG rules and generation approach are based on Chinese linguistic rules and cannot be directly extended to other languages. Experiments are limited by hardware resources (models used have ~54M and ~108M parameters) and do not explore larger models or ensembles.

## 💾 Data

**Source**: Training data: automatically generated from large public Chinese corpora (e.g., Chinese People's Daily corpus, Chinese machine translation datasets, Chinese wiki corpus) using the CLG linguistic-rules-based generation method. Test data (NaCGEC): collected from entrance examinations (secondary school and university grammar questions), recruitment examinations for government departments, and various Chinese news sites; annotated by highly educated university students majoring in Chinese linguistics with adjudication by a senior referee.

**Size**: CLG-Train: 591,404 sentences; NaCGEC (test): 6,767 sentences (6,496 erroneous sentences); Number of references: CLG-Train 591,404 references; NaCGEC 7,793 references.

**Format**: N/A

**Annotation**: Training data: automatically generated with labeled error types by CLG. NaCGEC test data: human annotation workflow with 5 annotators and 1 senior annotation referee; each sample labeled by 5 annotators, majority selected as final label, senior referee resolves ties; annotators also provided rewrites and references selected if appearing at least twice. Fleiss' kappa for annotation agreement: 0.823.

## 🔬 Methodology

**Methods**:
- Automated metrics (word-level MaxMatch M^2 scorer)
- Human evaluation (annotators distinguishing whether sentences contain grammatical errors and scoring language-style match to native speakers)

**Metrics**:
- Precision
- Recall
- F0.5
- F1 Score

**Calculation**: Evaluation uses the word-level MaxMatch (M^2) Scorer to compute Precision, Recall and F0.5 between the gold edit set and the system edit set. Human evaluation computes Precision, Recall and F1 for annotators distinguishing whether sentences contain grammatical errors; native-likeness scored 0/1/2 and averaged.

**Interpretation**: Lower F0.5 scores (reported below 25 for existing models on NaCGEC) indicate that NaCGEC is a challenging benchmark. Improvements in Precision/Recall/F0.5 when training with CLG-generated data indicate that CLG-generated training data effectively improves model performance on native-speaker errors.

**Baseline Results**: Transformer trained on CLG (591K) on NaCGEC: Precision 17.19, Recall 6.20, F0.5 12.69. Transformer Lang8+CLG (1811K): Precision 26.75, Recall 5.89, F0.5 15.66. GECToR-Chinese trained on CLG (591K): Precision 23.25, Recall 11.03, F0.5 19.04. GECToR-Chinese Lang8+CLG (1811K): Precision 27.71, Recall 12.19, F0.5 22.09.

**Validation**: Benchmark validated via human evaluation comparing NaCGEC with NLPCC and CGED (3 annotators for that evaluation). Annotation reliability for NaCGEC measured with Fleiss' kappa = 0.823 (interpreted as almost perfect agreement).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state that all original corpora used are from publicly available datasets or resources on legitimate websites and that no sensitive data is involved.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
