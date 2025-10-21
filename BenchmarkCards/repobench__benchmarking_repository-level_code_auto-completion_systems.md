# RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems

## 📊 Benchmark Details

**Name**: RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems

**Overview**: RepoBench is a new benchmark specifically designed for evaluating repository-level code auto-completion systems. RepoBench supports both Python and Java and consists of three interconnected evaluation tasks: RepoBench-R (Retrieval), RepoBench-C (Code Completion), and RepoBench-P (Pipeline). Each task respectively measures the system’s ability to retrieve the most relevant code snippets from other files as cross-file context, predict the next line of code with cross-file and in-file context, and handle complex tasks that require a combination of both retrieval and next-line prediction.

**Data Type**: text (source code files, code snippets, in-file and cross-file context)

**Domains**:
- Software Engineering

**Similar Benchmarks**:
- CoCoMIC
- RepoEval
- CodeXGLUE
- PY150
- Github Java Corpus

**Resources**:
- [GitHub Repository](https://github.com/features/copilot)
- [Resource](https://huggingface.co/datasets/codeparrot/github-code)
- [Resource](https://tree-sitter.github.io/tree-sitter/)
- [Resource](https://platform.openai.com/docs/guides/code)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark tailored for evaluating repository-level code auto-completion systems via three interconnected tasks (RepoBench-R, RepoBench-C, RepoBench-P) spanning Python and Java, enabling more complete comparison of performance in multi-file, real-world programming scenarios.

**Tasks**:
- Code Retrieval
- Code Completion (next-line prediction)
- End-to-End Pipeline Evaluation (retrieval + code completion)

**Limitations**: N/A

## 💾 Data

**Source**: Two sources: (1) github-code dataset (aggregated from file-level code files) used primarily for constructing optional training data; (2) newly crawled non-forked GitHub repositories (Python and Java) created after February 9, 2023 and before August 3, 2023 used exclusively as the test set. Tree-sitter is used to parse files and identify import statements and cross-file lines.

**Size**: Training: 10,345 Python repositories and 14,956 Java repositories. Test: 1,075 Python repositories and 594 Java repositories.

**Format**: N/A

**Annotation**: Automatically parsed and processed: import statements and cross-file lines are parsed using tree-sitter; candidate snippets and 'gold snippet' labels are derived programmatically from parsed import usages.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation
- Baseline comparisons (Random, Lexical, Semantic retrievers; Codex/CodeGen/StarCoder for completion)
- Ablation studies (prompt construction, kept lines for retrieval)
- Fine-tuning experiments

**Metrics**:
- Accuracy@k (acc@1, acc@3, acc@5)
- Exact Match (EM)
- Edit Similarity (ES)

**Calculation**: RepoBench-R uses Accuracy@k to assess retrieval performance (easy subset: acc@1 and acc@3; hard subset: acc@1, acc@3, acc@5). RepoBench-C and RepoBench-P use Exact Match (EM) and Edit Similarity (ES) following prior work.

**Interpretation**: Higher metric values indicate better retrieval or completion performance (e.g., higher acc@k, EM, ES correspond to better performance).

**Baseline Results**: Baseline retrieval (RepoBench-R) shows UniXcoder outperforming other retrievers (e.g., Python UniXcoder Easy XF-F acc@1=25.94, acc@3=59.69 in Table 2). RepoBench-C baseline results compare Codex, CodeGen variants, and StarCoder (see Table 3 for EM/ES values across models and sizes). RepoBench-P baseline shows inclusion of cross-file contexts improves performance and UniXcoder-based retrieval methods outperform random retrieval (see Table 4).

**Validation**: Random retrieval averaged over 100 repeats for stability; fine-tuning validation used a sampled validation set of 200 examples; multiple ablation studies and experiments reported (prompt construction, kept lines for retrieval).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Intellectual Property
- Data Laws

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Intellectual Property**: Data usage rights restrictions
- **Data Laws**: Data usage restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is sourced from GitHub repositories under open-source licenses; newly-crawled repositories are restricted to those 'permitted under their respective licenses' as stated in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
