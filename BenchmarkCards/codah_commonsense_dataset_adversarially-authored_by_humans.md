# CODAH (COmmonsense Dataset Adversarially-authored by Humans)

## 📊 Benchmark Details

**Name**: CODAH (COmmonsense Dataset Adversarially-authored by Humans)

**Overview**: We introduce the CODAH dataset, an adversarially-constructed evaluation dataset for testing common sense. CODAH forms a challenging extension to the recently-proposed SWAG dataset, which tests commonsense knowledge using sentence-completion questions that describe situations observed in video.

**Data Type**: multiple-choice question-answering pairs (sentence completion)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- SWAG
- SNLI
- SQuAD
- MultiNLI

**Resources**:
- [GitHub Repository](https://github.com/Websail-NU/CODAH)
- [Resource](https://arxiv.org/abs/1904.04365)

## 🎯 Purpose and Intended Users

**Goal**: An adversarially-constructed evaluation dataset for testing common sense; a challenging extension to the SWAG commonsense question answering benchmark.

**Tasks**:
- Question Answering
- Multiple-choice Sentence Completion

**Limitations**: Smaller than SWAG (2,801 questions); the authors did not explicitly filter questions for annotation artifacts.

## 💾 Data

**Source**: Adversarially-authored multiple-choice sentence completion questions collected via a web-based system from human participants (primarily university students, plus anonymous contributors). Submissions were cleaned by four annotators (the authors) and some questions were categorized/annotated by the authors.

**Size**: 2,801 questions (4,149 raw submissions before cleaning)

**Format**: N/A

**Annotation**: Questions authored by human participants; cleaned and filtered by four annotators (the authors). Category labels assigned manually by four annotators (the authors); human evaluation performed by three annotators on 707 questions.

## 🔬 Methodology

**Methods**:
- 5-fold stratified cross-validation fine-tuning
- Ablation experiments (training set size: 80%, 60%, 40%, 20%)
- SWAG pre-training then fine-tune on CODAH
- Answer-only baseline
- Human evaluation

**Metrics**:
- Accuracy
- Standard deviation
- Feiss' Kappa
- Cohen's Kappa

**Calculation**: Dataset evaluated with 5-fold stratified cross-validation (training on 80% and testing on 20% per fold for the CODAH 80% setting). For most model settings three trials were conducted and mean accuracy with standard deviation is reported. Human accuracy computed as the mean accuracy of three human annotators over 707 questions. Feiss' Kappa reported for annotator agreement on categories; Cohen's Kappa reported for human annotator agreement over 50 questions.

**Interpretation**: Higher Accuracy indicates better commonsense question answering. The paper reports a large gap between human performance (95.3%) and model performance (best reported BERT 69.5% on SWAG+CODAH cross-validation), indicating CODAH is challenging for current models. The authors interpret high human accuracy as evidence that CODAH questions reflect commonsense knowledge.

**Baseline Results**: Key results (accuracy): BERT (CODAH 80%): 67.5% (±1.24). BERT (SWAG+CODAH 80%): 69.5% (±0.34). GPT-1 (SWAG+CODAH 80%): 65.5% (±0.24). SWAG only evaluated on CODAH: BERT 41.3%, GPT-1 38.1%. Answer-only baseline: BERT 52.2% (±1.34), GPT-1 53.4% (±1.14). Human accuracy: 95.3%.

**Validation**: 5-fold stratified cross-validation balancing question categories; BERT hyperparameter grid search run within cross-validation (batch size, learning rate, number of epochs); three trials reported for most settings; re-running with different random seeds if BERT failed to achieve >=30% on a fold.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
