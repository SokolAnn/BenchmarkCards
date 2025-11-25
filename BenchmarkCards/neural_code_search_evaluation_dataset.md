# Neural Code Search Evaluation Dataset

## 📊 Benchmark Details

**Name**: Neural Code Search Evaluation Dataset

**Overview**: An evaluation dataset consisting of natural language query and code snippet pairs (from Stack Overflow) together with matching code snippet examples from a search corpus (method bodies from GitHub). The dataset is intended to serve as a common benchmark to evaluate code search models.

**Data Type**: question-answering pairs (natural language queries and code snippet answers); code method bodies

**Domains**:
- Software Engineering
- Natural Language Processing

**Resources**:
- [Resource](https://arxiv.org/abs/1908.09804)
- [Resource](https://archive.org/details/stackexchange)
- [GitHub Repository](https://developer.github.com/v3/search/)
- [GitHub Repository](https://github.com/00-00-00/ably-chat/archive/9bb2e36acc24f1cd684ef5d1b98d837055ba9cc8.zip)
- [GitHub Repository](https://github.com/Mindgames/VideoStreamServer/blob/b7c73d2bcd296b3a24f83cf67d6a5998c7a1af6b/playersdk/src/main/java/com/kaltura/playersdk/PlayerViewController.java#L506-L566)

## 🎯 Purpose and Intended Users

**Goal**: To construct and release an evaluation dataset of natural language queries and relevant code snippet answers (from Stack Overflow) with matching examples from a GitHub-derived search corpus, so that future work on code search can use this dataset as a common benchmark.

**Target Audience**:
- Researchers in code search
- Model developers

**Tasks**:
- Code Search
- Question Answering (retrieval of code snippets)
- Information Retrieval

**Limitations**: Final dataset contains 287 Stack Overflow question-answer pairs; dataset is constructed from Stack Overflow questions filtered by heuristics and manually filtered for vagueness; not all GitHub links in the dataset may remain available in the future.

## 💾 Data

**Source**: Stack Exchange Network (Stack Overflow) question-answer pairs (extracted from StackExchange data dump) and method bodies parsed from 24,549 popular Android GitHub repositories (commit-specific links).

**Size**: 287 Stack Overflow question-answer pairs (evaluation dataset); 24,549 GitHub repositories indexed for the search corpus; 4,716,814 method bodies in the search corpus.

**Format**: Per-method and per-evaluation-entry metadata provided as JSON-like records (examples shown in paper); GitHub download links in a text file; score sheet saved as comma-delimited CSV.

**Annotation**: Questions were heuristics-filtered and manually filtered to remove vague queries. Correctness of search results is determined automatically using the Aroma code-to-code similarity tool with a similarity threshold of 0.25 to count a result as correct.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Automatic matching via code-to-code similarity (Aroma)
- Rank-based evaluation (first-correct-rank and top-k evaluation)

**Metrics**:
- FRank (first correct answer rank)
- Answered@1
- Answered@5
- Answered@10
- Mean Reciprocal Rank (MRR)

**Calculation**: For each query, the model returns ranked code snippets from the search corpus. A returned method is counted as correct if the code-to-code similarity score from Aroma between the returned method and the Stack Overflow ground-truth answer exceeds 0.25. FRank is the rank of the first returned method counted as correct. Answered@k counts queries with a correct result in the top k. MRR is computed across queries using reciprocal ranks.

**Interpretation**: Higher Answered@k counts and higher MRR indicate better retrieval performance; lower FRank indicates better performance (earlier correct results).

**Baseline Results**: Table 1 in the paper reports: NCS — Answered@1: 33, Answered@5: 74, Answered@10: 98, MRR: 0.189. NCSpostrank — Answered@1: 85, Answered@5: 151, Answered@10: 180, MRR: 0.4. UNIF_android — Answered@1: 25, Answered@5: 74, Answered@10: 110, MRR: 0.178. UNIF_stackoverflow — Answered@1: 104, Answered@5: 164, Answered@10: 188, MRR: 0.465.

**Validation**: Correctness judgment uses Aroma similarity with threshold 0.25 (threshold choice referenced to prior work [1]). The dataset was filtered via heuristics and manual inspection to ensure upvoted code answers and presence of at least one matching method in the search corpus.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Stack Exchange data dump referenced as CC-BY-SA 3.0 (per paper). GitHub repositories used via publicly available links; specific repository licenses not enumerated in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
