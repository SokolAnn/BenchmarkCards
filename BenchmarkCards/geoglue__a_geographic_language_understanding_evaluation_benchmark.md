# GeoGLUE: A GeoGraphic Language Understanding Evaluation Benchmark

## 📊 Benchmark Details

**Name**: GeoGLUE: A GeoGraphic Language Understanding Evaluation Benchmark

**Overview**: We propose a GeoGraphic Language Understanding Evaluation benchmark (GeoGLUE). We collect data from open-released geographic resources and introduce six natural language understanding tasks, including geographic textual similarity on recall, geographic textual similarity on rerank, geographic elements tagging, geographic composition analysis, geographic where what cut, and geographic entity alignment. We also provide evaluation experiments and analysis of general baselines.

**Data Type**: text (query-POI pairs, address/room address strings, tokenized geographic text, sentence pairs)

**Domains**:
- Natural Language Processing
- Geographic Information Systems

**Languages**:
- Chinese

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- CLUE
- CBLUE
- TweetEval
- Natural Questions
- LexGLUE
- QuoteR
- KLEJ

**Resources**:
- [Resource](https://modelscope.cn/datasets/damo/GeoGLUE/summary)
- [Resource](https://www.openstreetmap.org)
- [Resource](https://www.lianjia.com/)
- [Resource](https://www.5i5j.com/)
- [Resource](https://www.fang.com/)
- [Resource](https://www.mayanchina.com/)
- [Resource](https://modelscope.cn/models?name=mgeo&page=1)
- [Resource](https://arxiv.org/abs/2305.06545)

## 🎯 Purpose and Intended Users

**Goal**: To promote the development of geographic natural language processing by providing a comprehensive geographic-specific language understanding evaluation benchmark consisting of six tasks.

**Target Audience**:
- Academic researchers
- Industry practitioners
- Model developers

**Tasks**:
- Geographic TExtual Similarity on Recall (GeoTES-recall)
- Geographic TExtual Similarity on Rerank (GeoTES-rerank)
- Geographic Elements TAgging (GeoETA)
- Geographic ComPosition Analysis (GeoCPA)
- Geographic Where What Cut (GeoWWC)
- Geographic Entity AliGnment (GeoEAG)

**Limitations**: GeoGLUE focuses on Chinese geographic usage scenarios. More tasks and various languages / multi-lingual geographic text should be considered in future work.

## 💾 Data

**Source**: All datasets are crawled from online open-released resources, including GIS-based Resources, Secondary-house Trading Resources, Local-information Services Resources, and Query-sessions of Map-related applications.

**Size**: GeoTES-recall: 50,000 train, 20,000 dev, 30,002 test examples; GeoTES-rerank: 50,000 train, 20,000 dev, 30,002 test examples; GeoETA: 8,856 train, 1,970 dev, 50,000 test examples; GeoCPA: 49,784 train, 2,214 dev, 50,001 test examples; GeoWWC: 9,311 train, 1,597 dev, 50,002 test examples; GeoEAG: 96,423 train, 22,974 dev, 35,908 test examples.

**Format**: N/A

**Annotation**: All datasets are annotated by experienced annotators trained with business rules. For Geo-Sequence Tagging tasks, 20 annotators used the BIOES scheme; a sample is considered correctly tagged when at least 70% of grouped annotators agree. For Geo-POI Searching, annotators select POIs within 1km; same POIs labeled as positives, neighboring POIs as hard negatives, others as normal negatives. Geo-Text Classification uses majority labeling (>=70% agreement). Annotated results were evaluated with Fleiss' Kappa scores described as favorable.

## 🔬 Methodology

**Methods**:
- Automated metrics (MRR, Precision, Recall, Micro-F1, Macro-F1)
- Baseline model evaluation (BERT, RoBERTa, ERNIE, Nezha, StructBERT)
- Leaderboard evaluation with held-out test set

**Metrics**:
- Mean Reciprocal Rank (MRR@x)
- Precision
- Recall
- Micro-F1
- Macro-F1

**Calculation**: GeoTES-recall uses MRR@5 (other MRR@k supported); GeoTES-rerank uses MRR@1 (other MRR@k supported). GeoETA, GeoCPA, GeoWWC use Precision, Recall, Micro-F1. GeoEAG uses Macro-F1.

**Interpretation**: Higher MRR, Precision, Recall, and F1 scores indicate better retrieval, tagging, and alignment performance. MRR@5 emphasizes recall accuracy for retrieval; MRR@1 emphasizes top-1 correctness for reranking/geocoding; Micro-F1 evaluates tagging across classes; Macro-F1 evaluates classification balance across labels.

**Baseline Results**: Reported average results (5 runs) in Table 7: BERT - GeoTES-recall MRR@5: 24.59, GeoTES-rerank MRR@1: 81.52, GeoETA Micro-F1: 90.41, GeoCPA Micro-F1: 65.06, GeoWWC Micro-F1: 69.65, GeoEAG Macro-F1: 78.88. RoBERTa - 39.37, 83.20, 90.79, 64.65, 66.44, 78.84. ERNIE - 24.03, 81.82, 90.63, 66.48, 67.73, 79.44. Nezha - 35.31, 81.38, 91.17, 67.70, 70.13, 79.77. StructBERT - 43.10, 83.51, 91.22, 67.47, 68.74, 78.83.

**Validation**: Test sets are held out and not publicly released; the Benchmark provides a Leaderboard. Annotated labels validated by multiple annotators with agreement threshold (>=70%) and Fleiss' Kappa reported as favorable.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state that they 'devote efforts to the data's privacy protections' and 'filter the privacy information and obey the anonymity protection rules' when refining original data. Annotators are paid appropriate compensations; specific amounts are commercial confidentialities.

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
