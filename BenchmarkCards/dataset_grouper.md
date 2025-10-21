# Dataset Grouper

## 📊 Benchmark Details

**Name**: Dataset Grouper

**Overview**: Dataset Grouper, a library to create large-scale group-structured (e.g., federated) datasets, enabling federated learning simulation at the scale of foundation models. The library facilitates creation of group-structured versions of existing datasets based on user-specified partitions, is engineered for efficiency and scalability, and is framework-agnostic.

**Data Type**: text (group-structured language modeling sequences)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TensorFlow Federated
- LEAF
- FedNLP
- FedScale
- FedML
- FedJAX
- WILDS
- FLAIR
- FLamby
- Motley
- pFL-bench

**Resources**:
- [GitHub Repository](https://github.com/google-research/dataset_grouper)
- [GitHub Repository](https://github.com/google-research/dataset_grouper/tree/main/dataset_grouper/examples/datasets)
- [Resource](https://pypi.org/project/dataset-grouper/)
- [Resource](https://arxiv.org/abs/2307.09619)

## 🎯 Purpose and Intended Users

**Goal**: Enable creation of large-scale group-structured (federated) datasets and provide scalable, efficient dataset pipelines suitable for foundation-model-scale federated learning simulation, pre-training, fine-tuning, and downstream personalization experiments.

**Target Audience**:
- Federated Learning Researchers
- Machine Learning Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Language Modeling
- Pre-training
- Fine-tuning
- Federated Learning simulation
- Personalization
- Evaluation (group-level evaluation)

**Limitations**: Dataset Grouper does not host datasets and instead creates partitioned versions of existing datasets; users must ensure that their use falls under the license of the base dataset and abide by associated terms. The library requires partition functions to be embarrassingly parallel for scalability.

**Out of Scope Uses**:
- Creating partition methods that require sequential or non-embarrassingly-parallel operations (Dataset Grouper supports only embarrassingly parallel partition methods).
- Guaranteeing hosting of partitioned datasets in perpetuity (Dataset Grouper does not host datasets).

## 💾 Data

**Source**: Group-structured versions of existing datasets created via partitioning: Colossal Clean Crawled Corpus (C4) -> FedC4 (partitioned by web domain), Wikipedia (English) -> FedWiki (one full English article per client), BookCorpusOpen -> FedBookCO (one book per client), CC-News -> FedCCnews (partitioned by web domain). Base datasets accessed via TensorFlow Datasets and HuggingFace Datasets.

**Size**: FedC4: 15.6M clients; 132B words; 0.36B examples. FedWiki: 6.5M clients; 3B words; 6.5M examples. FedBookCO: 18K clients; 1.2B words; 18K examples. FedCCnews: 8.8K clients; 0.3B words; 0.7M examples. (Numbers from Tables 6 and 7 in the paper.)

**Format**: TFRecord (streaming TFRecord files; datasets exposed via tf.data and nested iterators of tensors compatible with TensorFlow and NumPy).

**Annotation**: Not annotated (raw text for language modeling); N/A for supervised labels.

## 🔬 Methodology

**Methods**:
- Federated training experiments (FedAvg, FedSGD)
- Automated metrics evaluation (causal language modeling loss / cross-entropy)
- Per-group evaluation (histograms and percentile summaries across clients)
- Iteration/time profiling of dataset pipelines

**Metrics**:
- Causal language modeling loss (cross-entropy; equals logarithm of perplexity)
- Per-client validation loss percentiles (10th percentile, median, 90th percentile)
- Iteration time (seconds) to iterate over dataset and percentage of training time spent on data iteration
- Pre-personalization loss and Post-personalization loss (average causal language modeling loss before and after client fine-tuning)

**Calculation**: Per-round training loss: average the loss over all batches seen by a given client within the round, then average that quantity across participating clients. Pre-personalization loss: average causal language modeling loss of the model on all examples held by a client before personalization. Post-personalization loss: average causal language modeling loss after fine-tuning the model for a single epoch on the client's dataset. Iteration time: time to iterate over all examples in all group datasets in serial on a single CPU (average and standard deviation over trials).

**Interpretation**: Lower causal language modeling loss (log perplexity) indicates better model performance. The paper interprets that FedAvg behaves more like a meta-learning algorithm (leading to much lower post-personalization loss) while FedSGD behaves more like empirical risk minimization (better pre-personalization loss). Dataset iteration taking under ~10% of runtime indicates efficient streaming format.

**Baseline Results**: Table 5 (FedC4 validation): FedAvg pre-personalization loss percentiles (10th: 5.13, median: 5.64, 90th: 6.27); FedAvg post-personalization (10th: 0.002, median: 0.012, 90th: 0.934). FedSGD pre-personalization (10th: 4.38, median: 4.93, 90th: 5.40); FedSGD post-personalization (10th: 1.25, median: 3.38, 90th: 4.53). (Additional experimental results and ablations reported in paper figures and tables.)

**Validation**: Validation uses the held-out validation split of the base datasets (e.g., C4 validation split) partitioned with the same group structure. Per-client histograms and percentile statistics are computed across all validation clients (FedWiki personalization samples 20K clients due to size). Iteration time and memory usage are measured on a single CPU; training experiments run on TPU Pod slice (16 TPU v3 chips).

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Legal Compliance
- Governance
- Accuracy
- Intellectual Property

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions
- **Governance**: Incomplete usage definition
- **Accuracy**: Data contamination
- **Intellectual Property**: Copyright infringement, Data usage rights restrictions

**Demographic Analysis**: N/A

**Potential Harm**: ['Privacy and memorization concerns of training data (discussion of user-level differential privacy and memorization)', "Enshrinement of datasets as 'sole benchmarks' and misuse beyond intended tasks", 'Possible copyright issues and dataset licensing concerns (noted for BookCorpusOpen and base datasets)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper discusses privacy and memorization concerns and the need for user-level differential privacy; no specific anonymization procedures for the provided partitioned datasets are detailed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
