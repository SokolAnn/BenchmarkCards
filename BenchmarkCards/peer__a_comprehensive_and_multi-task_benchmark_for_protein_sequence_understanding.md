# PEER: A Comprehensive and Multi-Task Benchmark for Protein Sequence Understanding

## 📊 Benchmark Details

**Name**: PEER: A Comprehensive and Multi-Task Benchmark for Protein Sequence Understanding

**Overview**: PEER is a comprehensive and multi-task benchmark for Protein Sequence Understanding that provides a set of diverse protein understanding tasks including protein function prediction, protein localization prediction, protein structure prediction, protein-protein interaction prediction, and protein-ligand interaction prediction. The benchmark evaluates sequence-based methods and studies single-task and multi-task learning settings.

**Data Type**: multimodal (protein sequences and ligand molecular graphs)

**Domains**:
- Bioinformatics
- Computational Biology
- Drug Discovery

**Similar Benchmarks**:
- TAPE
- FLIP
- CASP
- CAFA
- ATOM3D
- ProteinGLUE

**Resources**:
- [GitHub Repository](https://github.com/DeepGraphLearning/PEER_Benchmark)
- [Resource](https://torchprotein.ai/benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive, multi-task benchmark for evaluating and comparing sequence-based protein understanding methods, and to study single-task and multi-task learning across diverse protein tasks.

**Target Audience**:
- Machine Learning Researchers
- Computational Biology Researchers
- Drug Discovery Researchers
- Model Developers

**Tasks**:
- Protein Function Prediction
- Protein Localization Prediction
- Protein Structure Prediction
- Protein-Protein Interaction Prediction
- Protein-Ligand Interaction Prediction
- Multi-task Learning Evaluation

**Limitations**: The current PEER benchmark mainly focuses on sequence-based approaches and could be strengthened by adding more tasks and models and by going beyond sequence-based approaches to structure-based approaches (stated as future work).

## 💾 Data

**Source**: Multiple public datasets as specified per task: Sarkisyan’s fluorescence dataset; Rocklin’s stability dataset; Envision (͏β-lactamase activity); DeepSol (solubility); DeepLoc (subcellular and binary localization); ProteinNet (contact prediction); DeepSF (fold classification); NetSurfP-2.0 / Klausen (secondary structure); Guo’s yeast PPI dataset; Pan’s human PPI dataset; SKEMPI (PPI affinity); PDBbind (protein-ligand affinity); BindingDB (protein-ligand affinity).

**Size**: Varies by task (as reported in Table 1): Fluorescence: 21,446 train, 5,362 validation, 27,217 test (examples); Stability: 53,571 train, 2,512 validation, 12,851 test (examples); β-lactamase activity: 4,158 train, 520 validation, 520 test (examples); Solubility: 62,478 train, 6,942 validation, 1,999 test (examples); Subcellular localization: 8,945 train, 2,248 validation, 2,768 test (examples); Binary localization: 5,161 train, 1,727 validation, 1,746 test (examples); Contact prediction: 25,299 train, 224 validation, 40 test (examples); Fold classification: 12,312 train, 736 validation, 718 test (examples); Secondary structure: 8,678 train, 2,170 validation, 513 test (examples); Yeast PPI: 1,668 train, 131 validation, 373 test (examples); Human PPI: 6,844 train, 277 validation, 227 test (examples); PPI affinity (SKEMPI): 2,127 train, 212 validation, 343 test (examples); PDBbind affinity: 16,436 train, 937 validation, 285 test (examples); BindingDB affinity: 7,900 train, 878 validation, 5,230 test (examples).

**Format**: N/A

**Annotation**: Labels are provided by original data sources and consist of experimental measurements or curated annotations (e.g., experimental fitness scores for fluorescence/stability/β-lactamase, solubility labels, subcellular localization labels, contact labels from structure, fold/secondary structure labels from structural databases, binary PPI labels, binding affinities pKd/pK).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (evaluate baseline models including feature-engineering MLPs, LSTM, Transformer, CNN, ResNet, pre-trained protein language models ProtBert and ESM-1b)
- Single-task learning evaluation
- Multi-task learning evaluation (hard parameter sharing with center and auxiliary tasks)
- Leaderboard tracking

**Metrics**:
- Spearman's rank correlation (Spearman's ρ)
- Accuracy
- Root-mean-square error (RMSE)
- Precision (L/5 precision for contact prediction)
- Weighted F1 (used for class-imbalanced classification tasks in supplement)

**Calculation**: Evaluation follows per-task protocols: regression tasks report Spearman's correlation (e.g., fluorescence, stability, β-lactamase, affinities); classification tasks report Accuracy (e.g., solubility, localization, fold, secondary structure, PPI); contact prediction reports precision of the L/5 most likely medium- and long-range contacts; RMSE is reported for affinity regression tasks. Models trained with cross-entropy or MSE losses as appropriate; ESM-1b truncates sequences longer than 1022 residues by keeping first 1022 residues.

**Interpretation**: Higher values indicate better performance for Spearman's correlation, Accuracy, Precision and Weighted F1; lower values indicate better performance for RMSE. Comparative ranking across baseline models is used to assess model effectiveness per task.

**Baseline Results**: Reported baseline results (Table 3) evaluate 10 baseline models across 14 tasks. Key findings: large pre-trained protein language model ESM-1b achieves the best performance on 10 out of 14 tasks; shallow CNN is the best model among models trained from scratch on multiple tasks. Detailed per-task numbers are provided in Table 3 of the paper.

**Validation**: Each model is trained with three random seeds and mean (std) reported. Validation is performed 10 times uniformly along training; test performance of the best validation-epoch model is reported. Hyperparameter search performed on β-lactamase activity task; training uses Adam optimizer for specified epochs (50 for some tasks, 100 for others).

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse

**Atlas Risks**:
- **Misuse**: Dangerous use

**Potential Harm**: ['Designing harmful drugs']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
