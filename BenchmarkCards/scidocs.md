# SCIDOCS

## 📊 Benchmark Details

**Name**: SCIDOCS

**Overview**: SCIDOCS is a novel collection of data sets and an evaluation suite for document-level embeddings in the scientiﬁc domain, consisting of seven document-level tasks ranging from citation prediction, to document classification and recommendation.

**Data Type**: text (title and abstract), tabular (anonymized user interaction logs and clickthrough events), graph (citation graph metadata)

**Domains**:
- Natural Language Processing
- Scientific Literature

**Resources**:
- [GitHub Repository](https://github.com/allenai/specter)
- [GitHub Repository](https://github.com/allenai/scidocs)
- [Resource](https://www.nlm.nih.gov/mesh/meshhome.html)

## 🎯 Purpose and Intended Users

**Goal**: Measure the effectiveness of scientiﬁc paper embeddings across diverse document-level tasks including citation prediction, user-activity prediction, document classification, and recommendation.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners
- Researchers working on scientific literature search and recommendation

**Tasks**:
- Document Classification
- Direct Citation Prediction (ranking)
- Co-Citation Prediction (ranking)
- User Activity Prediction (Co-Views ranking)
- User Activity Prediction (Co-Reads ranking)
- Recommendation (ranking with clickthrough data)

**Limitations**: N/A

## 💾 Data

**Source**: Subset of the Semantic Scholar corpus (papers and outgoing citations); MeSH-labelled medical papers (MeSH vocabulary); Microsoft Academic Graph (MAG) topic labels; anonymized user session logs from a major academic search engine; clickthrough dataset from a public scholarly search engine.

**Size**: Training data: about 146,000 query papers (≈26.7M tokens) with outgoing citations; validation: 32,000 papers. Training triples: ~684,000; validation triples: ~145,000. Evaluation datasets: MeSH classification: 23,000 papers; MAG topic classification: 25,000 papers; Direct Citations task: ≈30,000 papers (1,000 query papers); Co-Citations: 30,000 papers; Co-Views: ≈30,000 papers; Co-Reads: ≈30,000 papers; Recommendation clickthrough dataset: 22,000 clickthrough events (train 20,000; validation 1,000; test 1,000).

**Format**: N/A

**Annotation**: MeSH classification labels derived from the MeSH vocabulary and mapped to 11 top-level disease classes; MAG topic labels from level 1 MAG topics; citation links are from Semantic Scholar metadata; user activity datasets are logged/anonymized co-view and co-read signals; clickthrough events are logged and used with propensity scoring.

## 🔬 Methodology

**Methods**:
- Automated metrics (ranking and classification metrics)
- Linear SVM for document classification using embeddings as features
- Ranking by L2 distance between raw embeddings for citation and user-activity tasks
- Feed-forward ranking neural network incorporating embedding similarity and other features for recommendation
- Propensity-adjusted offline evaluation using propensity scores computed via a swap experiment
- Online A/B testing for recommendation (clickthrough rate comparison)

**Metrics**:
- Macro F1
- Mean Average Precision (MAP)
- Normalized Discounted Cumulative Gain (nDCG)
- Precision@1
- Clickthrough Rate (CTR) (used for A/B test reporting)

**Calculation**: For ranking tasks, candidate sets are ranked by L2 distance between raw embeddings and evaluated with MAP and nDCG. For the recommendation task, propensity scores are computed using a swap experiment and used to compute propensity-adjusted Precision@1 and propensity-adjusted nDCG. Classification is evaluated with Macro F1 using a linear SVM on embeddings.

**Interpretation**: Higher Macro F1, MAP, nDCG, and Precision@1 indicate better performance on the respective tasks. The paper reports SPECTER achieved an average of 80.0 across all metrics on SCIDOCS, a 3.1 point absolute improvement over the next-best baseline. Online A/B testing showed a 46.5% improvement in clickthrough rate for the SPECTER-based ranker over a baseline.

**Baseline Results**: SPECTER (reported results on SCIDOCS): MAG F1 82.0; MeSH F1 86.4; Co-View MAP 83.6; Co-View nDCG 91.5; Co-Read MAP 84.5; Co-Read nDCG 92.4; Direct Citation MAP 88.3; Direct Citation nDCG 94.9; Co-Citation MAP 88.1; Co-Citation nDCG 94.8; Recommendation nDCG 53.9; Recommendation Precision@1 20.0; Average across all tasks 80.0.

**Validation**: Held-out validation: 32K papers and 145K validation triples used for hyperparameter tuning. Recommendation clickthrough data partitioned temporally into train (20K), validation (1K), and test (1K). Propensity scores computed via a swap experiment for de-biased evaluation.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The evaluation includes anonymized user signals of document relatedness and an anonymized clickthrough dataset (the paper explicitly states the datasets include anonymized user signals).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
