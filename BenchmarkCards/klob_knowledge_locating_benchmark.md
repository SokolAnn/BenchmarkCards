# KLoB (Knowledge Locating Benchmark)

## 📊 Benchmark Details

**Name**: KLoB (Knowledge Locating Benchmark)

**Overview**: KLoB (Knowledge Locating Benchmark) examines three essential properties—Consistency, Relevance, and Unbiasedness—that a reliable knowledge locating method should satisfy. KLoB serves as a benchmark for evaluating existing locating methods in language models and provides a method to reassess the validity of the locality hypothesis of factual knowledge.

**Data Type**: text (sentences containing factual knowledge; sentences composed of random words for non-factual inputs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MQUAKE

**Resources**:
- [GitHub Repository](https://github.com/anon6662/KLoB)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate whether parameters selected by locating methods embed the desired factual knowledge by examining three criteria: Consistency, Relevance, and Unbiasedness; and provide a quantitative method to reassess the locality hypothesis of factual knowledge.

**Tasks**:
- Knowledge Locating Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from Wikidata and MQUAKE; random-word sentences sourced from the English word list of the NLTK library; filtered by querying Llama2-7b with in-context learning to retain only facts the model can correctly predict.

**Size**: KLoB-c: 13,675 examples; KLoB-r: 9,548 examples; KLoB-u: 25,470 examples

**Format**: Raw text (sentence-level examples generated from templates)

**Annotation**: Templates for KLoB-c manually written by human experts; KLoB-c sentences generated from Wikidata triples; KLoB-r sentences generated from MQUAKE two-hop chains and rephrased multi-hop questions; KLoB-u created by replacing words with random words from NLTK; dataset filtered via Llama2-7b in-context evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Relative Similarity (RSim)
- Relative Standard Deviation (RSD)

**Calculation**: RSim = max((Sim_cand - Sim_all) / (1 - Sim_all), 0), where Sim_cand is the intra-similarity among candidate localization results and Sim_all is the average similarity between the candidate localization result and all other localization results in the subtask. RSD = max(1 - SD_nonfactual / SD_factual, 0), where SD_factual is the average standard deviation of parameter scores for sentences with factual knowledge (KLoB-c and KLoB-r) and SD_nonfactual is the average standard deviation for sentences without factual knowledge (KLoB-u).

**Interpretation**: RSim ranges from 0 to 1: RSim = 1 if Sim_cand = 1 (candidate localization results identical); RSim = 0 if Sim_cand <= Sim_all. RSD ranges from 0 to 1: RSD = 1 if SD_nonfactual = 0 (parameter scores for non-factual inputs identical); RSD = 0 if SD_nonfactual > SD_factual.

**Validation**: Filtered factual knowledge by querying Llama2-7b with 8 demonstration examples and retaining only facts the model correctly predicted; templates manually written by human experts; dataset statistics reported in Table 1.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
