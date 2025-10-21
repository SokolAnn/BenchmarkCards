# LREBench (Low-resource Relation Extraction Benchmark)

## 📊 Benchmark Details

**Name**: LREBench (Low-resource Relation Extraction Benchmark)

**Overview**: We create a benchmark with 8 relation extraction (RE) datasets covering different languages, domains and contexts to evaluate methods for building relation extraction systems in low-resource settings and perform extensive comparisons over prompt-based methods, balancing methods for long-tailed distributions, and leveraging more instances via data augmentation and self-training.

**Data Type**: Text instances with one entity pair (head and tail) and a relation label (text (entity pair, relation))

**Domains**:
- General
- Encyclopedic
- Scientific
- Biochemical
- Dialogue
- Medical

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- GLUE
- CBLUE

**Resources**:
- [Resource](https://zjunlp.github.io/project/LREBench)
- [GitHub Repository](https://github.com/zjunlp/LREBench)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate methods for low-resource relation extraction and provide an open-sourced testbed (LREBench) of 8 RE datasets for systematic empirical study.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners
- Research Community

**Tasks**:
- Relation Extraction
- Relation Classification

**Limitations**: We cannot compare and evaluate all previous studies due to the settings and non-available open-sourced code. The benchmark will be maintained by adding new datasets.

## 💾 Data

**Source**: Public RE datasets selected: SemEval 2010 Task 8, TACREV, Wiki80 (converted to long-tailed distribution), SciERC, ChemProt, DialogRE, DuIE2.0 (Chinese), CMeIE (Chinese).

**Size**: SemEval: 6,500 train, 2,700 test; TACREV: 68,100 train, 15,500 test; Wiki80: 12,000 train, 5,600 test; SciERC: 3,200 train, 974 test; ChemProt: 19,500 train, 16,900 test; DialogRE: 6,000 train, 1,900 test; DuIE2.0: 153,000 train, 18,000 test; CMeIE: 34,000 train, 8,700 test.

**Format**: JSON (unified json format for evaluation)

**Annotation**: Existing annotations from the public datasets (original dataset annotations)

## 🔬 Methodology

**Methods**:
- PLM fine-tuning (standard fine-tuning)
- Prompt-based tuning (including KnowPrompt and PTR)
- Re-sampling (data re-sampling for balancing)
- Re-weighting losses (DSC, Focal Loss, GHM Loss, LDAM Loss)
- Data Augmentation (token-level substitution via WordNet, TF-IDF, contextual embeddings)
- Self-training (teacher-student with pseudo labels)
- Automated metrics evaluation

**Metrics**:
- Macro F1 Score
- Micro F1 Score

**Calculation**: Macro F1 and Micro F1 computed on test sets. For 8-shot and 10% settings, training datasets are randomly sampled 5 times and reported results are the average over the 5 runs.

**Interpretation**: Macro F1 and Micro F1 are used together because head and tail class performance varies a lot; Macro F1 reflects per-class (including tail) performance while Micro F1 reflects overall instance-level performance.

**Baseline Results**: Baseline results are reported in Table 2: Macro F1 and Micro F1 (%) for PLM fine-tuning, prompt-based tuning (KnowPrompt), balancing methods, data augmentation, and self-training across 8 datasets and three training settings (8-shot, 10%, 100%).

**Validation**: No validation on development sets; models are trained only on training sets to ensure few-shot learning. For 8-shot and 10% settings, experiments are repeated with 5 random training samples and averaged. Training epoch is set to 10.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Uncertain data provenance
- **Accuracy**: Data contamination, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
