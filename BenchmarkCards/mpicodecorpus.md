# MPICodeCorpus

## 📊 Benchmark Details

**Name**: MPICodeCorpus

**Overview**: MPICodeCorpus, the first publicly-available corpus of MPI-based parallel programs, created by mining more than 15,000 open-source repositories on GitHub to support training and evaluation of MPI-focused code models.

**Data Type**: text (MPI-based C/C++ source code)

**Domains**:
- High-Performance Computing
- Software Engineering

**Similar Benchmarks**:
- Standard Performance Evaluation Corporation (SPEC)
- NAS Parallel Benchmarks (NPB)
- CodeSearchNet

**Resources**:
- [GitHub Repository](https://github.com/Scientific-Computing-Lab-NRCN/MPI-rical)
- [GitHub Repository](https://github.com/Scientific-Computing-Lab-NRCN/MPI-rical/tree/main/BENCHMARKCode)

## 🎯 Purpose and Intended Users

**Goal**: Develop a programming-assistance tool (MPI-RICAL) that assists programmers in writing domain decomposition based distributed memory parallelization code using MPI by suggesting MPI functions and their proper locations in code.

**Target Audience**:
- MPI programmers
- Developers working on distributed memory / High-Performance Computing applications
- Tool developers integrating code-assistants into IDEs

**Tasks**:
- Code Translation
- Code Completion
- Program analysis for function insertion (location prediction)

**Limitations**: Training and evaluation examples were limited to files with 320 tokens (approximately 50 lines) due to hardware limitations, resulting in dropping almost 50% of raw examples. The current work measures generated MPI function names and their locations only — function arguments and structural code changes are not evaluated.

## 💾 Data

**Source**: Created by mining GitHub repositories: extracted 59,446 C programs from approximately 16,500 repositories and filtered to produce the MPICodeCorpus dataset used for training and evaluation.

**Size**: Approximately 25,000 examples in the final dataset (59,446 C programs extracted from ~16,500 repositories; 24,125 examples used for training as reported).

**Format**: Three files per example: (1) MPI-based parallel C code (label), (2) MPI-based parallel C code with MPI functions excluded (input), and (3) X-SBT linearized AST representation (used as input).

**Annotation**: Automatically generated: MPI function calls were programmatically removed from original MPI-based programs to create inputs; original programs serve as labels.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (classification metrics)
- Train/validation/test split (80:10:10)
- Compilation and execution testing of generated programs on a benchmark of 11 numerical computation examples

**Metrics**:
- F1 Score
- Precision
- Recall
- BLEU Score
- Meteor
- ROUGE-L
- Accuracy
- M-F1
- M-Precision
- M-Recall
- MCC-F1
- MCC-Precision
- MCC-Recall
- ACC

**Calculation**: Task framed as classification: RQ1 (MPI function name prediction) as multi-class classification over 456 possible MPI functions; RQ2 (location prediction) as binary classification for each code location. True Positive (TP), False Positive (FP), True Negative (TN), False Negative (FN) defined in paper. Matching uses one-line tolerance: a predicted MPI function matches ground truth if the function name is identical and the predicted location is within one line of the ground-truth location.

**Interpretation**: Higher F1, precision, and recall indicate more accurate suggestions of MPI functions and their insertion locations. Reported M-F1 values (e.g., 0.87–0.91 on datasets and benchmarks) are used to claim effectiveness in suggesting correct MPI functions at appropriate code locations; one-line tolerance applies.

**Validation**: Validated via an 80:10:10 train/validation/test split on the MPICodeCorpus dataset; additionally evaluated on a compiled benchmark of 11 MPI-based numerical computation programs where generated programs were compiled and executed to assess validity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
