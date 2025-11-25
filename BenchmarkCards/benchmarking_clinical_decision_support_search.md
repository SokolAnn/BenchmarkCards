# Benchmarking Clinical Decision Support Search

## 📊 Benchmark Details

**Name**: Benchmarking Clinical Decision Support Search

**Overview**: A platform to compare document and query processing techniques on the TREC Clinical Decision Support 2016 corpus. The system benchmarks indexing and search techniques (e.g., negation detection, normalization, query expansion, use of knowledge bases, learning-to-rank) and reproduces leading teams' runs to enable statistical testing of hypotheses and provide a common baseline for future research.

**Data Type**: text (full-text biomedical articles and clinical note queries)

**Domains**:
- Natural Language Processing
- Healthcare

**Similar Benchmarks**:
- EvaluatIR
- EvALL

**Resources**:
- [Resource](https://arxiv.org/abs/1801.09322)
- [Resource](http://lucene.apache.org/solr/)
- [Resource](https://www.ncbi.nlm.nih.gov/pubmed/)
- [Resource](https://www.evaluatIR.org)

## 🎯 Purpose and Intended Users

**Goal**: To provide a stable platform to formally specify methods, re-run past TREC CDS experiments, compare document and query processing techniques on the CDS'16 corpus, and produce benchmark results to evaluate and rank retrieval methods.

**Target Audience**:
- Biomedical Information Retrieval Researchers
- Information Retrieval Researchers
- TREC participants

**Tasks**:
- Document Retrieval
- Information Retrieval
- Ranking

**Limitations**: Results could not be reproduced exactly due to lack of sufficient details on preprocessing steps, implementation details, and unavailability of older versions of public search engines.

## 💾 Data

**Source**: CDS'2016 corpus: a snapshot of PubMed Central taken on 28 March 2016 (provided by TREC CDS 2016). Topics were nursing admission notes with three fields: Note, Description, and Summary.

**Size**: 1.25 million full-text journal articles

**Format**: NXML (re-encoded to ASCII text) indexed using Solr

**Annotation**: MeSH keywords appended from corresponding Medline abstracts; Metamap concepts (UMLS) automatically generated for each article

## 🔬 Methodology

**Methods**:
- Baseline BM25 retrieval (Solr)
- Query expansion using Pseudo-Relevance Feedback (PRF)
- Query expansion using word embeddings
- Concept extraction via MetaMap/UMLS
- Negation detection/removal using MetaMap Lite's NegEx
- Faceted search with hill-climbing weighting
- Learning to Rank (LambdaRank)
- Automated evaluation using retrieval metrics
- Paired two-sample t-test for significance testing

**Metrics**:
- inferred NDCG (infNDCG)
- inferred average precision (infAP)
- R-Precision (R-Prec)
- Precision at 10 (P@10)

**Calculation**: Evaluations use the four CDS track metrics (infNDCG as the main metric, infAP, R-Prec, P@10). Statistical significance of improvements over baseline is tested using a paired two-sample t-test reported at 95% and 98% confidence levels.

**Interpretation**: infNDCG is treated as the primary effectiveness measure; statistically significant increases in these metrics (per paired t-test at 95%/98% confidence) indicate improvement over baseline methods.

**Baseline Results**: Baseline BM25 (no query expansion or preprocessing): Note infNDCG 0.1074, Desc infNDCG 0.1067, Sum infNDCG 0.1721; P@10 Note 0.1400, Desc 0.1200, Sum 0.2067 (see Table 2).

**Validation**: Evaluated against TREC CDS relevance judgments (qrels). Learning-to-rank used topics and relevance judgments from TREC CDS 2014 and 2015 as training data. Significance testing via paired two-sample t-test.

## ⚠️ Targeted Risks

**Risk Categories**:
- Governance
- Transparency

**Atlas Risks**:
- **Governance**: Lack of system transparency, Lack of data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
