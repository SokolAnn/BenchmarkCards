# ParaAMR: A Large-Scale Syntactically Diverse Paraphrase Dataset by AMR Back-Translation

## 📊 Benchmark Details

**Name**: ParaAMR: A Large-Scale Syntactically Diverse Paraphrase Dataset by AMR Back-Translation

**Overview**: PARAAMR, a large-scale syntactically diverse paraphrase dataset created by abstract meaning representation (AMR) back-translation. The dataset's paraphrases are syntactically more diverse compared to existing large-scale paraphrase datasets while preserving good semantic similarity. PARAAMR is demonstrated to improve three NLP tasks: learning sentence embeddings, syntactically controlled paraphrase generation, and data augmentation for few-shot learning.

**Data Type**: text (paraphrase pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PARANMT
- PARABANK 1
- PARABANK 2

**Resources**:
- [GitHub Repository](https://github.com/uclanlp/ParaAMR)
- [Resource](https://catalog.ldc.upenn.edu/LDC2020T02)
- [GitHub Repository](https://github.com/bjascob/amrlib)
- [GitHub Repository](https://github.com/goodmami/penman)

## 🎯 Purpose and Intended Users

**Goal**: To construct a large-scale paraphrase corpus that is syntactically diverse using AMR back-translation, and to demonstrate its usefulness for improving sentence embeddings, syntactically controlled paraphrase generation, and data augmentation for few-shot learning.

**Tasks**:
- Paraphrase Generation
- Sentence Embedding (Semantic Textual Similarity)
- Data Augmentation for Few-Shot Learning

**Limitations**: Dependence on the quality of pre-trained text-to-AMR parsers and AMR-to-text generators; not all AMR nodes are appropriate as root nodes for re-focusing which can produce ungrammatical or unnatural paraphrases; some imperfect paraphrases may remain after perplexity filtering.

## 💾 Data

**Source**: English source sentences from the Czech–English dataset (Bojar et al., 2016); specifically the same source sentences used by PARABANK 2 (Hu et al., 2019b).

**Size**: 15,543,606 paraphrase instances

**Format**: N/A

**Annotation**: Automatically generated via AMR back-translation: parse source sentences to AMR graphs using a pre-trained AMR parser (SPRING), modify AMR focus, linearize the graph, decode with a pre-trained AMR-to-text generator (T5-based), and filter candidates by GPT-2 perplexity threshold.

## 🔬 Methodology

**Methods**:
- Automated metrics-based quantitative analysis
- Human evaluation (Amazon Mechanical Turk)
- Downstream task evaluations (sentence embedding learning, syntactically controlled paraphrase generation, few-shot data augmentation)

**Metrics**:
- Cosine similarity (SimCSE embeddings)
- 1 - BLEU Score (lexical diversity)
- 1 - ∩/∪ (token overlap-based lexical diversity)
- Tree Edit Distance (top-3 layers) (TED-3)
- Tree Edit Distance (full tree) (TED-F)
- BLEU Score (for paraphrase generation evaluation)
- Pearson correlation coefficient (STS evaluation)
- Spearman correlation coefficient (STS evaluation)
- Perplexity (GPT-2) for filtering
- 3-point human evaluation scores for semantic similarity and syntactic diversity

**Calculation**: Semantic similarity: obtain sentence embeddings using the supervised SimCSE model and compute cosine similarity. Lexical diversity: compute 1 - BLEU and 1 - (intersection/union) of tokens. Syntactic diversity: obtain constituency parse trees via Stanford CoreNLP and compute tree edit distance (TED-3 uses top-3 layers; TED-F uses the whole tree). STS evaluation: use SentEval scripts to compute Pearson's r and Spearman's rho over STS 2012-2016. Perplexity: compute with GPT-2 to filter paraphrases above threshold.

**Interpretation**: Higher semantic similarity (cosine similarity, STS correlations, human semantic scores) indicates better preservation of meaning. Higher values of diversity metrics (1 - BLEU, 1 - ∩/∪, TED-3, TED-F, human syntactic diversity scores) indicate greater lexical or syntactic diversity. Lower perplexity indicates more fluent candidate paraphrases.

**Baseline Results**: Key reported comparisons: PARAAMR contains 15,543,606 instances (avg. 6.91 paraphrases per source). STS (STS2012-2016) Pearson / Spearman: PARANMT 74.38 / 73.80, PARABANK 1 74.80 / 74.56, PARABANK 2 75.39 / 75.17, PARAAMR 77.70 / 75.72. Syntactically controlled paraphrase generation (BLEU on Quora / MRPC / PAN): PARAAMR 48.50 / 47.38 / 40.30 (5-run averages), outperforming PARANMT, PARABANK 1, and PARABANK 2. Few-shot data augmentation (example: 15-shot MRPC/QQP/RTE and 30-shot results reported in Table 7) show improved task performance when using PARAAMR for augmentation compared to other paraphrase corpora.

**Validation**: Quantitative evaluation conducted on 193,869 examples that appear in all compared datasets. Human evaluation via Amazon Mechanical Turk: sampled 300 paraphrases per dataset, three annotators per item, 3-point scales for semantic similarity and syntactic diversity. Downstream task experiments (5 runs) used as extrinsic validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

**Potential Harm**: ['Offensive or biased content learned from training data']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Human evaluation via Amazon Mechanical Turk: pay rate $0.1 per paraphrase pair; filtered MTurk workers by approval rate and number of approvals; the authors state they did not collect any personal information of MTurk workers.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
