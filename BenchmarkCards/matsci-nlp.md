# MatSci-NLP

## 📊 Benchmark Details

**Name**: MatSci-NLP

**Overview**: MatSci-NLP is a natural language benchmark for evaluating the performance of natural language processing models on materials science text. It is constructed from publicly available materials science text data and encompasses seven NLP tasks (Named Entity Recognition, Relation Classification, Event Argument Extraction, Paragraph Classification, Synthesis Action Retrieval, Sentence Classification, Slot Filling). The benchmark is provided in a JSON-based format and is intended to enable fine-tuning and evaluation of models on materials science language tasks.

**Data Type**: text (annotated materials science text; JSON records containing text, task definitions, and annotations)

**Domains**:
- Natural Language Processing
- Materials Science

**Similar Benchmarks**:
- QASPER
- BLURB
- PubMedQA
- BioASQ
- BLUE

**Resources**:
- [GitHub Repository](https://github.com/BangLab-UdeM-Mila/NLP4MatSci-ACL23)
- [Resource](https://arxiv.org/abs/2305.08264)

## 🎯 Purpose and Intended Users

**Goal**: To construct the first broad benchmark for NLP in the materials science domain (MatSci-NLP) spanning several NLP tasks to evaluate and analyze how well language models understand materials science text and to enable development of language models applicable to materials discovery and synthesis tasks.

**Target Audience**:
- Materials Science Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Named Entity Recognition
- Relation Classification
- Event Argument Extraction
- Paragraph Classification
- Synthesis Action Retrieval
- Sentence Classification
- Slot Filling

**Limitations**: Limited quantity of available data; evaluations performed in a low-data setting (1% train / 99% test) which may cause memorization rather than generalization; focus limited to BERT-based models (no autoregressive large language models studied); did not study generalization beyond the materials science domain; financial and environmental costs associated with pretraining domain-specific models.

## 💾 Data

**Source**: Unified from publicly available, high-quality, smaller-scale annotated materials science datasets adapted from Weston et al. (2019); Friedrich et al. (2020); Mysore et al. (2019); Yamaguchi et al. (2020); Venugopal et al. (2021); Wang et al. (2022a); MatSciRE (2022).

**Size**: Named Entity Recognition: 112,191 examples; Relation Classification: 25,674 examples; Event Argument Extraction: 6,566 examples; Paragraph Classification: 1,500 examples; Synthesis Action Retrieval: 5,547 examples; Sentence Classification: 9,466 examples; Slot Filling: 8,253 examples.

**Format**: JSON-based format (each sample contains relevant text, task definitions, and annotations).

**Annotation**: High-quality annotated data adapted from the cited source datasets (original annotations come from the respective source datasets cited).

## 🔬 Methodology

**Methods**:
- Text-to-Schema multitask modeling
- Single-task fine-tuning
- Single-task prompting
- MMOE multitask fine-tuning
- Constrained decoding with schema matching
- Low-resource fine-tuning (1% train / 99% test split)

**Metrics**:
- Micro-F1
- Macro-F1
- Cross-Entropy Loss

**Calculation**: Metrics computed as micro-F1 and macro-F1 on the test split (99% of data); experiments repeated 5 times and report mean with a confidence interval of two standard deviations. Models fine-tuned using cross-entropy loss.

**Interpretation**: The authors note dataset class imbalance skews metrics (micro-F1 higher than macro-F1). They state that models with micro-F1 above 0.66 and macro-F1 above 0.5 can be considered to have semantically meaningful understanding of the tasks in this benchmark.

**Baseline Results**: Baseline results are reported in Tables 2-10 (micro-F1 and macro-F1 averaged over 5 runs). The paper reports that MatBERT generally performs best across most tasks, SciBERT often performs second best, and domain-specific pretrained models generally outperform general BERT under the Task-Schema setting.

**Validation**: Experiments repeated five times; report mean and confidence interval of two standard deviations; early stopping used during fine-tuning; low-resource split of 1% training and 99% testing; full hyperparameters to be provided in code release.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Data Laws
- Intellectual Property
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Data Laws**: Data usage restrictions, Data acquisition restrictions
- **Intellectual Property**: Data usage rights restrictions, Copyright infringement
- **Societal Impact**: Impact on the environment

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
