# TCM-SD: A Benchmark for Probing Syndrome Differentiation via Natural Language Processing

## 📊 Benchmark Details

**Name**: TCM-SD: A Benchmark for Probing Syndrome Differentiation via Natural Language Processing

**Overview**: We introduce the first public large-scale benchmark for syndrome differentiation (SD), called TCM-SD. Our benchmark contains 54,152 real-world clinical records covering 148 syndromes to support data-driven AI development in Traditional Chinese Medicine.

**Data Type**: text (clinical notes / electronic medical records)

**Domains**:
- Natural Language Processing
- Healthcare
- Traditional Chinese Medicine
- Medical Diagnosis

**Languages**:
- Chinese

**Similar Benchmarks**:
- MIMIC-III
- emrQA
- ChiMed

**Resources**:
- [GitHub Repository](https://github.com/Borororo/ZY-BERT)
- [Resource](https://arxiv.org/abs/2203.10839)

## 🎯 Purpose and Intended Users

**Goal**: To construct the first high-quality, public large-scale benchmark for syndrome differentiation (SD) in Traditional Chinese Medicine to enable NLP research and development in this domain, and to establish strong baselines.

**Target Audience**:
- Researchers in Natural Language Processing
- Medical and Healthcare researchers
- Researchers interested in Traditional Chinese Medicine and clinical NLP

**Tasks**:
- Text Classification
- Machine Reading Comprehension

**Limitations**: The dataset exhibits an imbalanced (long-tail) distribution of syndromes; some syndrome categories are infrequent and were filtered out (syndromes with fewer than 10 samples). TCM standardization is incomplete, causing inconsistent syndrome naming and requiring normalization (merging and pruning).

## 💾 Data

**Source**: Real-world Chinese clinical records (routine diagnosis and treatment data) collected from clinical sources and additionally a crawled external TCM knowledge corpus.

**Size**: 54,152 examples (processed; originally over 65,000 raw clinical notes)

**Format**: N/A

**Annotation**: Syndrome labels were normalized via a two-stage process (merging and pruning); experts were recruited to conduct syndrome differentiation and validate/merge non-standard names.

## 🔬 Methodology

**Methods**:
- Automated evaluation (model-based)
- Baseline model comparisons (statistical methods, classical NN-based methods, pre-trained language models, domain-specific pre-trained language models)
- Ablation study
- Error analysis

**Metrics**:
- Accuracy
- Macro-F1
- Macro-Precision
- Macro-Recall
- Exact Match (EM) for MRC

**Calculation**: The paper reports Accuracy and Macro-F1 for classification, and Exact Match (EM) and Macro-F1 for MRC. Specific formulaic calculation details are not provided in the text.

**Interpretation**: The authors state that Macro-F1 is a more accurate metric for this imbalanced dataset. The much lower Macro-F1 compared to Accuracy demonstrates challenges from the imbalanced (long-tail) syndrome distribution.

**Baseline Results**: Key results (classification, Dev / Test): ZY-BERT: Accuracy 81.43% / 82.19%, Macro-F1 49.47% / 51.01%. RoBERTa (best general LM): Accuracy 80.81% / 82.26%, Macro-F1 43.18% / 47.55%. (Full table of baseline results provided in the paper, Table 4.)

**Validation**: The processed dataset (148 syndrome categories, 54,152 samples) was split into training, development, and test sets with an 8:1:1 ratio. Syndromes with fewer than 10 samples were filtered out during partitioning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Transparency
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of data transparency
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data used were routine diagnosis and treatment data excluding personal information (such as name, age, and telephone number). All the data have been desensitized.

**Data Licensing**: Not Applicable

**Consent Procedures**: The study did not interfere with medical procedures and did not conduct experiments on patients; the paper states it waives the requirement of individual patient consent.

**Compliance With Regulations**: Not Applicable
