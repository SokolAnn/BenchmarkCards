# HEADLINES (Historical Enormous-Scale Abstractive DupLIcate NewsSummaries)

## 📊 Benchmark Details

**Name**: HEADLINES (Historical Enormous-Scale Abstractive DupLIcate NewsSummaries)

**Overview**: HEADLINES is a massive-scale semantic similarity dataset containing nearly 400 million high quality semantic similarity pairs drawn from 70 years (1920-1989) of off-copyright U.S. local newspapers. Positive pairs are headlines written by different papers that summarize the same underlying wire article; the dataset is intended to facilitate contrastive training and evaluation of models that capture abstractive semantic similarity, and enables study of semantic change across space and time.

**Data Type**: text (headline pairs from historical newspapers)

**Domains**:
- Natural Language Processing
- Historical Text Analysis

**Languages**:
- English

**Similar Benchmarks**:
- Massive Text Embedding Benchmark (MTEB)
- Reddit Comments
- MS COCO
- WikiAnswers
- Quora
- S2ORC

**Resources**:
- [Resource](https://huggingface.co/datasets/dell-research-harvard/headlines-semantic-similarity)
- [Resource](https://arxiv.org/abs/2306.17810)

## 🎯 Purpose and Intended Users

**Goal**: To provide a very large, publicly available semantic similarity dataset spanning 1920-1989 (nearly 400M positive headline pairs) to facilitate contrastive training and evaluation of semantic similarity models, study semantic change across space and time, and support downstream tasks such as clustering, retrieval, semantic search, and topic classification of historical archives.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Researchers working on historical texts / semantic change

**Tasks**:
- Semantic Similarity
- Text Clustering
- Nearest Neighbor Retrieval
- Semantic Search
- Topic Classification
- Publication Year / Region Prediction
- Embedding Training

**Limitations**: HEADLINES contains transcription (OCR) errors and historical language that reflects semantics and cultural biases of the 20th century. The authors do not filter antiquated or potentially offensive terms. The dataset is not intended for training generative models.

**Out of Scope Uses**:
- Training generative models (authors recommend against this use)

## 💾 Data

**Source**: Newly digitized front pages of off-copyright local U.S. newspapers (1920-1989); headlines written by local papers that reproduced wire articles form positive semantic similarity pairs.

**Size**: 34,867,488 headlines; 393,635,650 positive headline pairs

**Format**: JSON (dataset hosted on Hugging Face; each year is a distinct JSON file, e.g., 1952_headlines.json)

**Annotation**: Automatically generated via OCR (Tesseract), document layout recognition (Mask R-CNN), rule-based association to create high-precision silver training data, and neural models (contrastively trained bi-encoder and RoBERTa cross-encoder). Hand-labeled validation and training subsets were used for OCR evaluation and for training/evaluating article association and reproduced-content detection.

## 🔬 Methodology

**Methods**:
- Automated metrics (v-measure, Adjusted Rand Index, F1, Recall, Precision, Character Error Rate)
- Clustering evaluation following MTEB: embed texts with various base models, run k-means with k from ground truth, score with v-measure
- Contrastive training and bi-encoder clustering for reproduced-content detection
- Rule-based and neural (RoBERTa) article association
- OCR evaluation on hand-annotated samples

**Metrics**:
- V-measure
- Adjusted Rand Index (ARI)
- F1 Score
- Recall
- Precision
- Character Error Rate (Levenshtein distance normalized by ground truth length)

**Calculation**: Character error rate is the Levenshtein distance between the transcribed text and the ground truth, normalized by the length of the ground truth. For MTEB-style similarity, random samples (up to 10,000 texts per year) were embedded (all-mpnet-base-v2), pairwise nearest neighbors by cosine similarity computed and averaged to obtain SIM_jk. For clustering benchmarks, texts are embedded, k-means is run with k equal to the ground-truth number of clusters, and v-measure is computed. ARI and clustering comparisons are computed against hand-labeled reproduced-article pairs.

**Interpretation**: Higher v-measure and ARI indicate better clustering performance. Character Error Rate lower values indicate better OCR quality. Authors report that HEADLINES yields substantially higher clustering v-measures (e.g., ST5-XXL ~78 on HEADLINES) compared to many MTEB datasets (e.g., MPNet average v-score 43.69), indicating high-quality clusters; ARI values closer to 100 indicate better reproduced-content detection.

**Baseline Results**: Article association: Full Article Association F1=93.7, Recall=88.3, Precision=99.7 (evaluation on 214 scans / 3,803 labeled bounding boxes). Reproduced-content detection: Bi-encoder ARI=91.5; Re-ranking (bi-encoder + cross-encoder) ARI=93.7; LSH ARI=73.7; N-gram overlap ARI=75.0 (evaluated on sample with 54,996 positive pairs and 100,914,159 negative pairs). Clustering (MTEB-style): best average v-score across MTEB datasets from MPNet = 43.69; best average v-score across decades for HEADLINES from ST5-XXL ≈ 78. OCR character error rates reported per decade in Table 1 (e.g., overall character error rates by decade provided).

**Validation**: Multiple hand-labeled evaluation sets: OCR evaluated on a hand-annotated sample of 300 headlines per decade; article association evaluated on 214 scans (3,803 article bounding boxes, 2,805 headline boxes, 1,851 article-article associations); reproduced-content detection evaluated on a labeled sample (54,996 positive pairs and 100,914,159 negative pairs) drawn from front-page articles in selected days/decades. Hyperparameters and model selection used validation splits as described in supplementary materials.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The dataset includes state metadata and Figure 1 plots geographic distribution by state; the authors note the state field is missing in some cases.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: HEADLINES is built from off-copyright local newspaper headlines that are in the public domain. The authors state the dataset does not contain confidential information. Headlines may mention individuals (names, ages, actions) and thus could identify people appearing in historical news.

**Data Licensing**: Creative Commons CC-BY license (dataset hosted on Hugging Face). DOI: 10.57967/hf/0751.

**Consent Procedures**: Individuals were not notified; data were obtained from publicly available historical newspapers. No institutional review board review was required per the authors.

**Compliance With Regulations**: The authors provide a summary of U.S. copyright law and state that the newspapers included are off-copyright; the dataset is hosted under a CC-BY license. The authors state no export controls or other regulatory restrictions apply.
