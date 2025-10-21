# CodeQueries

## 📊 Benchmark Details

**Name**: CodeQueries

**Overview**: We contribute a labeled dataset, called CodeQueries, of semantic queries over Python code. In CodeQueries, the queries are about code semantics, the context is file level and the answers are code spans. We curate the dataset based on queries supported by a widely-used static analysis tool, CodeQL, and include both positive and negative examples, and queries requiring single-hop and multi-hop reasoning.

**Data Type**: question-answering pairs (extractive QA) over Python source code with answer spans and supporting-fact spans

**Domains**:
- Software Engineering
- Program Analysis

**Languages**:
- Python

**Similar Benchmarks**:
- CoSQA
- CodeQA
- CS1QA

**Resources**:
- [GitHub Repository](https://github.com/thepurpleowl/codequeries-benchmark)
- [GitHub Repository](https://codeql.github.com/)
- [GitHub Repository](https://codeql.github.com/codeql-query-help/python/py-conflicting-attributes/)
- [GitHub Repository](https://github.com/github/codeql/blob/main/python/ql/src/codeql-suites/python-lgtm.qls)

## 🎯 Purpose and Intended Users

**Goal**: To test the ability of neural models to understand code semantics on the problem of answering semantic queries over code via extractive question-answering, including identification of answer spans and supporting-fact spans.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Question Answering
- Supporting-fact Identification
- Relevance Classification
- Span Extraction (extractive QA)

**Limitations**: The dataset consists of 52 queries. The dataset is created over Python code only. Evaluation in the paper is limited to two model types (GPT3.5-Turbo prompting and CuBERT fine-tuning). The context considered is file-level (not entire repositories).

## 💾 Data

**Source**: 52 public CodeQL queries (from the CodeQL Query Suite) evaluated on the redistributable subset of the ETH Py150 dataset (ETH Py150 Open dataset). English descriptions of the CodeQL queries (from CodeQL documentation) are used as natural-language queries. Positive examples and supporting-fact spans are extracted from CodeQL engine results; negative examples are derived using manually created negated CodeQL queries.

**Size**: 34,662 positive examples and 52,613 negative examples (per-query aggregate count across all queries: 133,456 examples)

**Format**: N/A

**Annotation**: Answer and supporting-fact spans are programmatically extracted from CodeQL analysis results. Negative examples are obtained by manually deriving logical negations of the CodeQL queries and using their results.

## 🔬 Methodology

**Methods**:
- Automated metrics (exact match, pass@k)
- Model-based evaluation: prompting a large language model (GPT3.5-Turbo) in zero-shot and few-shot settings
- Model-based evaluation: fine-tuning a contextual embedding encoder model (CuBERT) with a relevance classifier and span prediction

**Metrics**:
- Exact Match
- Pass@k
- Accuracy
- Precision
- Recall

**Calculation**: Exact match: An exact match occurs when the set of predicted answer spans is same as the set of ground-truth answer spans. When supporting facts are predicted, the exact match also requires that the set of predicted supporting-fact spans is same as the set of ground-truth supporting-fact spans. Pass@k is used for LLM evaluations following (Chen et al., 2021) for k draws from n generations (k ∈ {1,2,5,10}, n = 10). Relevance classification is measured with accuracy, precision, and recall.

**Interpretation**: N/A

**Baseline Results**: GPT3.5-Turbo on sampled test data (pass@10): zero-shot exact match on positive examples 20.84% and on negative examples 26.77%; few-shot (BM25 retrieval) pass@10 exact match on positive 32.66% and negative 70.08%. Few-shot with supporting facts (pass@10) positive exact match 39.08%. CuBERT two-step(all, all) on complete test data: exact match 52.61% (positive) and 96.73% (negative). CuBERT two-step(20,20) (practical small-data setting) on complete test data: exact match 3.74% (positive) and 95.54% (negative).

**Validation**: Queries were selected with at least 50 answer spans in the training split of the ETH Py150 Open dataset. Examples derived from a Python file are placed in the same split as the file. For LLM evaluation, a sampled test set (files with <2000 tokens) was used due to prompt size limits. Positive examples, supporting facts, and relevant code blocks are derived from CodeQL engine outputs; negative examples are derived from negated CodeQL queries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Explainability

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Explainability**: Unexplainable output

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
