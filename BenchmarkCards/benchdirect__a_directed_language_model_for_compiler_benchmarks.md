# BenchDirect: A Directed Language Model for Compiler Benchmarks

## 📊 Benchmark Details

**Name**: BenchDirect: A Directed Language Model for Compiler Benchmarks

**Overview**: We develop BenchPress, the first ML compiler benchmark generator that can be directed within source code feature representations. BenchPress synthesizes executable functions by infilling code that conditions on the program’s left and right context and uses active learning to introduce new benchmarks with unseen features. We further develop BenchDirect, an extension that utilizes a directed language model which infills programs by jointly observing source code context and the compiler features that are targeted.

**Data Type**: text (OpenCL source code kernels)

**Domains**:
- Compiler Optimization
- Programming Languages
- Software Engineering

**Similar Benchmarks**:
- CLgen
- CLSmith
- Rodinia
- AnghaBench

**Resources**:
- [GitHub Repository](https://github.com/fivosts/BenchPress)
- [GitHub Repository](https://github.com/fivosts/BenchPress.git)
- [Resource](https://humanorai.co.uk)
- [GitHub Repository](https://github.com/ChrisLidbury/CLSmith)
- [Resource](http://lava.cs.virginia.edu/Rodinia/download.htm)
- [Resource](https://cloud.google.com/bigquery)
- [GitHub Repository](https://docs.github.com/en/rest)
- [Resource](https://www.khronos.org/registry/OpenCL/specs/3.0-unified/html/OpenCL_C.html)

## 🎯 Purpose and Intended Users

**Goal**: Generate OpenCL compiler benchmarks targeted to desired program feature vectors to improve downstream predictive models and to populate missing regions of the compiler feature space.

**Target Audience**:
- Compiler Engineers
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Program Synthesis
- Benchmark Generation
- Compiler Optimization (heuristic evaluation)

**Limitations**: BenchPress and BenchDirect are restricted by the model sequence length (experiments report a maximum sequence length of 768 tokens in some evaluations and 512 tokens in others), preventing generation of very large benchmarks. BenchDirect can produce syntactic errors and fail to compile when attempting to match very large target feature vectors in a single inference; several targeted Rodinia benchmarks exceed BenchPress's maximum sequence length (6 targets noted).

## 💾 Data

**Source**: OpenCL code mined from BigQuery's GitHub dataset and directly from GitHub via its API; target benchmarks drawn from the Rodinia suite. Features extracted using Grewe et al., LLVM InstCount, and Autophase feature extractors. Execution labels collected via CLDrive.

**Size**: 63,918 OpenCL kernels mined across 12,860 GitHub repositories; 19,637 compiling kernels (31% compilation). Collected 61 Rodinia benchmarks of which 58 compile (used as targets).

**Format**: Tokenized source code sequences using a derived tokenizer (vocabulary of 2,201 unique tokens, including meta-tokens [START],[END],[PAD],[HOLE],[ENDHOLE]); kernels padded or truncated to model sequence length (experiments used max position embeddings 768 and 512).

**Annotation**: Compiler feature vectors extracted per kernel using Grewe et al. features (8 dimensions), InstCount (70 dimensions), and Autophase (56 dimensions); device-performance labels (CPU/GPU) obtained by executing kernels with CLDrive; compilation-status annotations via Clang/LLVM compilation.

## 🔬 Methodology

**Methods**:
- Beam search steering over language model outputs
- Active learning (Query by Committee)
- Directed language modeling (feature-conditioned encoder + BERT-based infilling)
- Automated execution-based evaluation using CLDrive
- Human evaluation (double-blind Turing test)

**Metrics**:
- Compilation rate
- Number of unique benchmarks
- Token length
- LLVM-IR instruction count
- Euclidean distance in feature space (reported as relative proximity)
- Speedup (geometric mean relative to optimal static decision)
- Precision
- Recall
- Specificity
- Time per sample (ms)

**Calculation**: Relative proximity is defined as 1 minus the distance between two kernels in the feature space relative to the distance of the Rodinia benchmark from the axes origin (100% = exact match, 0% = as close as an empty kernel). Speedup is the geometric mean of speedups over all benchmarks relative to the optimal static decision (running on the GPU). Entropy for active learning is computed as H = - sum_{l in L} p(l) * log(p(l)) over committee predicted labels.

**Interpretation**: Higher relative proximity indicates closer match to target features (100% exact match). Higher speedup indicates improved heuristic performance relative to static GPU mapping (maximum observed optimal speedup for task reported as 12%). Compilation rate is proportion of generated kernels that compile.

**Baseline Results**: Throughput comparison (undirected generation): BenchPress generated 190,460 unique benchmarks, 142,607 compiling benchmarks, 86% compilation rate, max tokens 750, max LLVM-IR instructions 161, time per sample 162 ms. CLgen generated 1,564,011 unique benchmarks, 13,035 compiling, 2.33% compilation rate, max tokens 102, max inst 32, time per sample 103 ms. Grewe heuristic results when retrained: training on original human-written benchmarks gives +4% speedup; BenchPress with active learning (BenchPress-AL) improved heuristic speedup to +6% (50% relative improvement from 4% to 6%); BenchPress passive +1%; CLgen -1%; GitHub +1%. Directed model (BenchDirect) produced 1.8× more exact feature matches compared to BenchPress and achieved up to 36% better accuracy and up to 72% reduction in inference time in some configurations.

**Validation**: Validated by (a) comparing generated benchmarks' feature proximity to Rodinia benchmarks across three feature spaces (Grewe et al., InstCount, Autophase), (b) retraining Grewe et al.'s CPU vs GPU heuristic and measuring speedup via CLDrive, (c) compilation checks using Clang/LLVM, and (d) a double-blind human Turing test with 77 participants assessing human-likeness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
