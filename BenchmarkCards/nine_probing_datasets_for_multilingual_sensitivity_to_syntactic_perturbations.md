# Nine Probing Datasets for Multilingual Sensitivity to Syntactic Perturbations

## 📊 Benchmark Details

**Name**: Nine Probing Datasets for Multilingual Sensitivity to Syntactic Perturbations

**Overview**: This paper proposes nine probing datasets organized by the type of controllable text perturbation for three Indo-European languages: English, Swedish, and Russian, aiming to analyze syntactic sensitivity of multilingual Transformer LMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Swedish
- Russian

**Similar Benchmarks**:
- CoLA (Corpus of Linguistic Acceptability)
- BLiMP (Benchmark of Linguistic Minimal Pairs)
- SyntaxGym

**Resources**:
- [GitHub Repository](https://github.com/evtaktasheva/dependency_extraction)

## 🎯 Purpose and Intended Users

**Goal**: To explore the syntactic sensitivity of multilingual LMs through controllable syntactic perturbations in structured datasets.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Syntactic Sensitivity Probing
- Text Perturbation Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Datasets constructed from CoNLL 2017 Shared Task on Multilingual Parsing from Raw Texts to Universal Dependencies.

**Size**: 10,000 pairs for each perturbation type per language

**Format**: CSV

**Annotation**: Manually curated with linguistic expertise.

## 🔬 Methodology

**Methods**:
- Parameter-free Probing
- Self-Attention Probing
- Token Perturbed Masking

**Metrics**:
- Undirected Unlabeled Attachment Score (UUAS)
- Token Identifiability (TI)

**Calculation**: Metrics calculated based on the differences between syntactic trees induced from original and perturbed sentences.

**Interpretation**: Lower UUAS scores indicate better reconstruction of syntactic structures from perturbed sentences.

**Validation**: Probing performances cross-validated using metrics against original sentence embeddings and syntactic trees.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: Sensitivity across different Indo-European languages.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
