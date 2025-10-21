# TreeEval: Benchmark-Free Evaluation of Large Language Models through Tree Planning

## 📊 Benchmark Details

**Name**: TreeEval: Benchmark-Free Evaluation of Large Language Models through Tree Planning

**Overview**: We introduce TreeEval, a benchmark-free evaluation method for large language models (LLMs) that lets a high-performance LLM host an irreproducible evaluation session to avoid data leakage. The examiner LLM generates a series of questions under a topic using a tree planning strategy that considers the current evaluation status to decide the next question generation, ensuring completeness and efficiency of the evaluation process.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- MMLU
- Big-Bench Hard (BBH)
- AlpacaEval
- AlpacaEval2.0
- MT-Bench

**Resources**:
- [GitHub Repository](https://github.com/Ashura5/TreeEval)
- [Resource](https://arxiv.org/abs/2402.13125)

## 🎯 Purpose and Intended Users

**Goal**: Benchmark-free evaluation of the knowledge implication and question-answering capabilities of LLMs through tree planning.

**Tasks**:
- Question Answering

**Limitations**: Using LLMs like GPT-4 as judges introduces potential data leakage risks due to biases in their pre-training data. GPT-4 has limitations, particularly in areas outside its expertise, which can be mitigated by providing more contextual guidance or training specialized evaluators for domain-specific evaluations.

## 💾 Data

**Source**: Automatically generated questions by an examiner LLM (GPT-4-0613) based on a predefined topic set (FC_pre-define) and responses from the evaluated LLMs collected during the evaluation sessions.

**Size**: Average 45.1 questions per evaluation session; main experiments evaluated 6 models (two 7B, two 13B, two 33B).

**Format**: JSON (examiner prompt requires JSON output for questions; judge returns evaluation decisions in JSON format as specified in prompts).

**Annotation**: Automatically annotated by an LLM judge via pairwise comparison with exchange evaluation (judge compares two responses, may output winner/tie and scores); no human annotation reported.

## 🔬 Methodology

**Methods**:
- LLM-based Examiner (automated question generation)
- LLM-based Judge (automated pairwise comparison with exchange evaluation)
- Tree planning with breadth-first search for question generation and evaluation control
- Score aggregation using weighted node importance (distance, topic origin, sibling variance)
- Ablation studies (BFS vs DFS, component removals) and repeated runs to measure stability

**Metrics**:
- Spearman correlation coefficient (ρ)
- Kendall correlation coefficient (τ)
- Win-Rate
- Accuracy
- Number of Questions (#Q)
- Aggregated score (weighted win-rate)

**Calculation**: Final score S is computed by weighting node win-rates: wt = w_root_t^α · w_topic_t^β · w_sibling_t^γ where w_root_t = 1/d (d is distance to root), w_topic_t is 1 if topic originated from loser else 0.5, and w_sibling_t = 1/(σ^2 + 1). The aggregated score S = (1/N) * sum_i(sum_t wt · St) normalized over nodes and questions; hyperparameters α, β, γ are set (authors used α=1, β=1, γ=0.4).

**Interpretation**: Higher Spearman ρ and Kendall τ correlation with AlpacaEval2.0 indicate reliability of TreeEval ranking. Fewer average number of questions (#Q) indicates evaluation efficiency. Deeper trees indicate more similar abilities between evaluated LLMs and thus more intensive competition for discrimination.

**Baseline Results**: TreeEval achieves highest correlation with AlpacaEval2.0 among compared methods: Spearman ρ = 0.83 and Kendall τ = 0.73, with average #Q = 45.1 (reported in Table 1).

**Validation**: Experiments repeated three times with averaged scores and reported variance to reduce randomness; ablation studies (e.g., BFS→DFS, removing topic generation, removing aggregator components); comparisons against existing evaluation methods and leaderboards (MMLU, BBH, AlpacaEval, AlpacaEval2.0, MT-Bench).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Value Alignment

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Fairness**: Output bias, Data bias
- **Value Alignment**: Toxic output, Harmful output

**Potential Harm**: ['Biases', 'Discrimination', 'Harmful content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
