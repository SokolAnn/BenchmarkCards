# ORSUM dataset

## 📊 Benchmark Details

**Name**: ORSUM dataset

**Overview**: We introduce the task of Scientific Opinion Summarization, where research paper reviews are synthesized into meta-reviews, and construct the ORSUM dataset covering 15,062 paper meta-reviews and 57,536 paper reviews from 47 conferences to facilitate supervised abstractive meta-review generation and related analyses.

**Data Type**: text (paper reviews and meta-reviews)

**Domains**:
- Machine Learning

**Similar Benchmarks**:
- The Rotten Tomatoes (RT)
- Copycat
- OPOSUM
- Yelp
- DENOISESUM
- PLANSUM
- SPACE
- MReD

**Resources**:
- [GitHub Repository](https://github.com/Mankeerat/orsum-meta-review-generation)
- [Resource](https://openreview.net/)

## 🎯 Purpose and Intended Users

**Goal**: Given a research paper’s title, abstract, and set of reviews, generate a meta-review summarizing the reviews' opinions to make a decision recommendation for acceptance or rejection (Scientific Opinion Summarization).

**Tasks**:
- Opinion Summarization
- Abstractive Summarization
- Meta-review Generation

**Limitations**: The dataset is collected from OpenReview and the majority of meta-reviews are in Machine Learning. Author rebuttals are not included as input.

## 💾 Data

**Source**: Human-written meta-reviews and individual reviewer comments crawled from OpenReview; each instance contains paper URL, title, abstract, decision, area-chair meta-review, and individual reviewer reviews from 47 conference venues.

**Size**: 15,062 meta-reviews and 57,536 individual reviews from 47 conference venues; train/validation/test splits: 9,890/549/550 samples.

**Format**: Data format is unified across venues; train/validation/test splits provided (no specific file format stated).

**Annotation**: Meta-reviews are human-written meta-reviews from area chairs; no additional annotation scheme for dataset collection beyond filtering (papers with meta-reviews shorter than 20 tokens and comments by non-official reviewers excluded).

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based evaluation
- Human evaluation

**Metrics**:
- ROUGE-L
- BERTScore
- FactCC
- SummaC
- DiscoScore
- G-EVAL
- GPTLikert

**Calculation**: ROUGE-L computes longest common subsequence overlap. BERTScore uses contextualized embeddings to measure similarity. FACTCC checks claim-level factual consistency. SummaC uses sentence-level natural language inference models for inconsistency detection. DiscoScore averages scores from six BERT-based model variants as a coherence indicator. G-EVAL and GPTLikert are LLM-based evaluation methods that use constructed prompts/chain-of-thought or Likert scoring to rate aspects such as discussion involvement, opinion faithfulness, and decision consistency.

**Interpretation**: Higher standard metric scores indicate better summarization relevance/factuality/coherence but do not necessarily imply better opinion summarization (discussion involvement and decision consistency require additional evaluation). LLM-based metrics (G-EVAL, GPTLikert) are used to assess discussion involvement, opinion faithfulness, and decision consistency and are presented as complementary to reference-based metrics.

**Baseline Results**: Selected results from Table 3 (ROUGE-L, BERTScore, FactCC, SummaC, DiscoScore, G-EVAL, GPTLikert): Human: - , - , 0.538, 0.368, 0.740, 0.731, 0.607. LED-finetuned: 0.221, 0.853, 0.634, 0.795, 0.961, 0.751, 0.649. LexRank: 0.433, 0.881, 0.729, 0.937, 1.256, 0.726, 0.656. CGI2 (ours): 0.199, 0.836, 0.559, 0.320, 0.906, 0.770, 0.687.

**Validation**: Provided train/validation/test splits (9,890/549/550). Human evaluation: composition analysis with three annotators for discussion involvement; additional human annotation on 50 challenging test papers with three annotators providing binary labels for informativeness, soundness, self-consistency, and faithfulness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Transparency
- Fairness

**Atlas Risks**:
- **Robustness**: Hallucination
- **Governance**: Lack of system transparency
- **Fairness**: Data bias

**Potential Harm**: The paper states that LLM-generated meta-reviews may contain hallucinations which may lead to misunderstandings of the original research paper or reviewers' opinions. The dataset's concentration in Machine Learning could introduce biases to recommendation decisions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
