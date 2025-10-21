# HPC Source Code Dataset

## 📊 Benchmark Details

**Name**: HPC Source Code Dataset

**Overview**: Introduce a new dataset of HPC and scientific codes from popular open-source repositories and use it to fine-tune pre-trained language models; compare several pre-trained LLMs on HPC-related tasks and introduce HPC-Coder, fine-tuned on parallel codes, which can auto-complete HPC functions, decorate for loops with OpenMP pragmas, and model performance changes in scientific application repositories and programming competition solutions.

**Data Type**: text (C/C++ source code and code pairs with performance/run-time labels)

**Domains**:
- High Performance Computing
- Scientific Computing
- Software Engineering

**Similar Benchmarks**:
- HumanEval

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To train and evaluate large language models specifically on HPC and scientific code to enable HPC-specific code generation, OpenMP pragma prediction, and relative performance prediction of code changes.

**Target Audience**:
- Computational Scientists
- HPC Developers
- Software Developers

**Tasks**:
- Code Completion
- Program Annotation (OpenMP Pragma Prediction)
- Performance Prediction
- Binary Classification

**Limitations**: Performance depends on numerous variables besides just the code such as input problem, architecture, and current machine load/congestion; these either need to be fixed in the dataset or accounted for within the modeling pipeline.

## 💾 Data

**Source**: Collected from GitHub repositories: repositories with C/C++ marked as the primary language and with 63 stars, filtered by HPC-related GitHub topics; all C/C++ source files pulled by file extension. Additional performance datasets: commits for Kripke and Laghos applications (automated build/run to collect performance for commits) and programming competition solutions aggregated from Aizu, AtCoder, CodeChef, CodeForces, and HackerEarth (code contests dataset).

**Size**: HPC source code dataset after deduplication and removing small/large files: 196,140 files, 50,017,351 lines of code, 1.62 GB. Performance datasets: 830 commits (Kripke + Laghos); ~1.7 million C++ samples (programming competition solutions) used to create paired samples. OpenMP pragma dataset: 13,900 samples.

**Format**: Original data: C/C++ source files. Tokenization: pre-trained GPT-2 Byte-Pair Encoding (BPE) tokenizers used for selected models (tokenized integer sequences).

**Annotation**: Deduplicated by sha256 hash of file contents. OpenMP pragma dataset: extracted every for loop with an OpenMP pragma and included 500 tokens of prior context; pragmas repositioned after the loop with a separating token <begin-omp>. Performance datasets: pairs labeled as 'slower' or 'same/faster' based on measured run times; code pairs separated by tokens <COMMIT> (version control) or <PAIR> (contest pairs).

## 🔬 Methodology

**Methods**:
- Fine-tuning pre-trained autoregressive language models (GPT-2/GPT-Neo/PolyCoder variants) on the collected HPC source code dataset using HuggingFace Trainer with DeepSpeed backend
- Automated evaluation via compilation and functional testing of generated code
- Evaluation of OpenMP pragma generation using syntactic equivalence and functional-correctness comparisons
- Binary classification fine-tuning for relative performance prediction

**Metrics**:
- Perplexity
- pass@k
- Accuracy
- Build success rate (compilation rate)

**Calculation**: Perplexity is calculated as the exponential of the cross-entropy training loss. pass@k is computed as pass@k = 1 - (comb(Np - cp, k) / comb(Np, k)) where cp is number of functionally correct samples out of Np generated samples for a prompt; average pass@k is averaged over prompts. Accuracy = # correct / total for OpenMP pragma prediction and relative performance classification. Build success rate = percentage of generated samples that compile successfully.

**Interpretation**: Lower Perplexity indicates better language modeling (model confidence) and generally correlates with better downstream performance. Higher pass@k, higher Accuracy, and higher build success rate indicate better code generation, pragma prediction, and performance prediction respectively.

**Baseline Results**: Final validation perplexities after fine-tuning on HPC source code dataset: GPT-2: 4.47, GPT-Neo: 2.23, PolyCoder: 2.24. Code generation (PolyCoder+HPC / HPC-Coder) average pass@100 ~71%, pass@1 ~25%. Build success (compilation) rates: PolyCoder+HPC 86%, PolyCoder 84%, GPT-Neo+HPC 74%, GPT-2+HPC 30%. OpenMP pragma functional correctness: PolyCoder+HPC 97% accuracy, PolyCoder 94%; exact textual equivalence: PolyCoder+HPC 67%, PolyCoder 61%. Relative performance classification accuracy: PolyCoder+HPC 88% (proxy applications), 92% (coding competitions); PolyCoder 86% (both datasets reported at 86% in figures).

**Validation**: During fine-tuning: validation dataset is 5% of full dataset (separate from training). For OpenMP pragma fine-tuning: 10% set aside for validation. For relative performance prediction: 90% train / 10% evaluation split. Code generation prompts: Np=100 samples per prompt; nucleus sampling with p=0.93 and multiple temperatures tested (0.1, 0.2, 0.4, 0.6, 0.8).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
