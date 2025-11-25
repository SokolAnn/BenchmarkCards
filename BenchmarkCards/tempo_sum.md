# TEMPO SUM

## 📊 Benchmark Details

**Name**: TEMPO SUM

**Overview**: A novel benchmark that contains data samples from 2010 to 2022 to understand the temporal generalization ability of abstractive summarization models. The benchmark consists of two summarization datasets collected from CNN and BBC (2010-2022) and constructs future test sets (post-2019) whose articles contain knowledge conflicts to evaluate robustness and faithfulness on future data.

**Data Type**: news article and summary pairs (text)

**Domains**:
- Natural Language Processing
- Journalism

**Languages**:
- English

**Similar Benchmarks**:
- CNN/DailyMail
- XSum
- Newsroom
- Multi-News
- SumREN

**Resources**:
- [GitHub Repository](https://github.com/NLP2CT/TempoSum)
- [Resource](https://archive.org/)
- [Resource](https://arxiv.org/abs/2305.01951)
- [GitHub Repository](https://github.com/doccano/doccano)

## 🎯 Purpose and Intended Users

**Goal**: Assess the temporal generalization capability of text summarization models, in particular their faithfulness on future data that contain knowledge conflicts with parametric world knowledge.

**Target Audience**:
- Summarization research community
- Machine learning researchers
- Model developers

**Tasks**:
- Text Summarization
- Faithfulness Evaluation
- Factuality Evaluation

**Limitations**: Limited to news domain datasets; analysis of knowledge conflicts mainly focuses on entity relationships with politicians; designed to evaluate PLMs pre-trained on corpora before 2019 (does not evaluate PLMs pre-trained on more recent corpora).

## 💾 Data

**Source**: Crawled news articles from BBC News (2010-2022) and CNN News (2012-2022), filtered to exclude overlap with XSum and CNN/DM training sets; evolving facts identified from Wikidata; archived articles crawled via the Internet Archive.

**Size**: BBC: 6,254 samples in-distribution (2010-2017); 2,260 samples future (2020-2022). CNN: 970 samples in-distribution (2012-2015); 3,250 samples future (2020-2022).

**Format**: N/A

**Annotation**: Manual annotation by the authors (four authors); two annotators per sample; annotation tool: doccano (https://github.com/doccano/doccano).

## 🔬 Methodology

**Methods**:
- Human evaluation (manual annotation by authors)
- Automated metrics evaluation (FactCC, QAFactEval)
- Model-based evaluation comparing PEGASUS, Transformer, CLIFF, and ENT

**Metrics**:
- FactCC
- QAFactEval
- Spearman’s rank correlation

**Calculation**: Spearman’s rank correlation coefficient between human judgments and metric scores; FactCC is entailment-based; QAFactEval is QA-based (as described in their respective original works).

**Interpretation**: Spearman’s correlation coefficients below 0.4 indicate weak correlation with human judgments (the paper reports correlations lower than 0.4 and states this implies weak agreement). Higher FactCC/QAFactEval scores indicate higher estimated faithfulness by those metrics.

**Baseline Results**: FactCC and QAFactEval scores reported in Table 4. Examples: BBC In-distribution - PEGASUS: FactCC 14.44, QAFactEval 27.99; Transformer: FactCC 17.97, QAFactEval 3.99; CLIFF: FactCC 15.40, QAFactEval 30.38; ENT: FactCC 17.99, QAFactEval 20.16. BBC Future - PEGASUS: FactCC 11.24, QAFactEval 24.97; Transformer: FactCC 15.45, QAFactEval 2.28; CLIFF: FactCC 12.04, QAFactEval 29.12; ENT: FactCC 16.86, QAFactEval 18.87. CNN In-distribution - PEGASUS: FactCC 50.57, QAFactEval 73.86; Transformer: FactCC 51.70, QAFactEval 71.69; CLIFF: FactCC 57.11, QAFactEval 78.41; ENT: FactCC 33.02, QAFactEval 61.39. CNN Future - PEGASUS: FactCC 61.64, QAFactEval 77.64; Transformer: FactCC 54.54, QAFactEval 73.44; CLIFF: FactCC 63.42, QAFactEval 80.44; ENT: FactCC 35.83, QAFactEval 65.23.

**Validation**: Human evaluation with two annotators per sample (150 random articles per test split; 600 articles total annotated for BBC and CNN). Reported annotation matching rates: BBC in-distribution 68%, CNN in-distribution 76%, BBC future 72%, CNN future 85%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: ['Generation of outdated hallucinations and unfaithful summaries (misinformation) due to reliance on parametric world knowledge']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The news articles used in the benchmark are publicly available on the internet and therefore the benchmark does not reveal any private information about individuals.

**Data Licensing**: The licenses of the original news sources are applied.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
