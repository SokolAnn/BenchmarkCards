# MedNLI

## 📊 Benchmark Details

**Name**: MedNLI

**Overview**: Introduce MedNLI - a dataset annotated by doctors, performing a natural language inference task (NLI), grounded in the medical history of patients. The paper presents strategies to leverage transfer learning from open-domain NLI datasets (e.g., SNLI) and to incorporate domain knowledge from external data and lexical sources (e.g., medical terminologies).

**Data Type**: text (premise-hypothesis sentence pairs)

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- SNLI
- MultiNLI

**Resources**:
- [Resource](https://jgc128.github.io/mednli/)
- [Resource](http://www.i2b2.org/NLP)
- [Resource](https://metamap.nlm.nih.gov/)
- [Resource](https://pytorch.org/)
- [Resource](http://commoncrawl.org/)
- [Resource](http://clinicaltrials.gov)

## 🎯 Purpose and Intended Users

**Goal**: Provide a publicly available, expert-annotated dataset for natural language inference in the clinical domain to enable research and evaluation of NLI systems grounded in patient medical history.

**Target Audience**:
- Machine Learning Researchers
- Clinical NLP Researchers
- Model Developers

**Tasks**:
- Natural Language Inference (Recognizing Textual Entailment)

**Limitations**: Each example in MedNLI was single annotated (no multiple annotations per pair). The dataset contains annotation artifacts similar to other NLI datasets. Some premises were discarded due to de-identification artifacts. Dataset size is modest compared to large open-domain NLI corpora.

## 💾 Data

**Source**: Premises sampled from MIMIC-III v1.3 clinical notes (de-identified records of 38,597 patients; 2,078,705 clinical notes). Hypotheses generated and annotated by clinicians.

**Size**: 14,049 unique sentence pairs (Training: 11,232 pairs; Development: 1,395 pairs; Test: 1,422 pairs).

**Format**: N/A

**Annotation**: Expert annotation by clinicians (two board-certified radiologists in pilot; two additional clinicians / board-certified medical students for final dataset). Single annotation per sentence pair. Labels: "Definitely true" (entailment), "Maybe true" (neutral), "Definitely false" (contradiction). Inter-annotator agreement (pilot) Cohen's kappa = 0.78.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (baseline and neural models)
- Automated metrics

**Metrics**:
- Accuracy
- Cohen's kappa (for annotator agreement)

**Calculation**: Accuracy computed on development and test sets. Model results reported as the average over 6 runs with different random seeds. The epoch with the lowest validation loss was selected for testing. Cohen's kappa computed for pilot inter-annotator agreement.

**Interpretation**: Higher Accuracy indicates better NLI performance on MedNLI. Direct transfer from open-domain datasets is worse than in-domain baseline but may be better than random baseline (33.3%). Sequential and multi-target transfer can yield improvements. The neutral class is the hardest to recognize; annotation artifacts affect dataset behavior.

**Baseline Results**: Feature-based system: Dev 51.9%, Test 51.9%. BOW: Dev 71.9%, Test 70.2%. InferSent: Dev 76.0%, Test 73.5%. ESIM: Dev 74.4%, Test 73.1%.

**Validation**: Dataset split into training, development, and test with no premise overlap between splits. Models trained with early stopping based on validation loss; best epoch selected by lowest validation loss. Results averaged over 6 runs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Data Laws

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Data contamination, Unrepresentative data
- **Data Laws**: Data usage restrictions

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset premises sourced from de-identified MIMIC-III records. Access to MedNLI is provided through the MIMIC-III derived data repository and requires certification to access MIMIC-III.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
