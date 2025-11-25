# CliniQ: A Multi-faceted Benchmark for Electronic Health Record Retrieval with Semantic Match Assessment

## 📊 Benchmark Details

**Name**: CliniQ: A Multi-faceted Benchmark for Electronic Health Record Retrieval with Semantic Match Assessment

**Overview**: The paper introduces CliniQ, a novel public benchmark for Electronic Health Record (EHR) retrieval aimed at addressing the scarcity of available benchmarks. It includes two retrieval settings (Single-Patient and Multi-Patient Retrieval), utilizes a dataset of 1,000 discharge summaries from MIMIC-III, and features 1,246 unique queries with 77,206 relevance judgments.

**Data Type**: chunk-level relevance judgments

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zhao-zy15/CliniQ)
- [Resource](https://huggingface.co/datasets/THUMedInfo/CliniQ)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation benchmark for EHR retrieval systems.

**Target Audience**:
- Research community
- Medical informatics professionals

**Tasks**:
- Information Retrieval

**Limitations**: The benchmark currently focuses exclusively on discharge summaries, omitting other types of clinical notes and entities such as symptoms and anatomical structures.

## 💾 Data

**Source**: MIMIC-III Discharge Summaries

**Size**: 1,000 discharge summaries; 16,550 chunks; 1,246 unique queries; 77,206 relevance judgments

**Format**: N/A

**Annotation**: Relevance judgments were generated using GPT-4 annotations and categorized into string match and four types of semantic matches.

## 🔬 Methodology

**Methods**:
- Evaluation of various retrieval methods including BM25 and dense retrievers

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Normalized Discounted Cumulative Gain (NDCG)
- Mean Average Precision (MAP)
- Recall

**Calculation**: Metrics are calculated based on the relevance judgments from Single-Patient and Multi-Patient settings.

**Interpretation**: Higher scores reflect better retrieval performance with relevance integrity maintained through various match types.

**Baseline Results**: BM25 provides a strong baseline in both retrieval settings.

**Validation**: Extensive evaluations through human judgments and comparisons against established models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
