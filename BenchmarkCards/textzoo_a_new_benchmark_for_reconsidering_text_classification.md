# TextZoo, a New Benchmark for Reconsidering Text Classification

## 📊 Benchmark Details

**Name**: TextZoo, a New Benchmark for Reconsidering Text Classification

**Overview**: An open-source benchmark that re-implements more than 20 popular text representation models for classification and evaluates them on more than 10 datasets to provide a unified comparison for text classification.

**Data Type**: text (labeled text classification examples)

**Domains**:
- Natural Language Processing

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified open-source benchmark for systematically comparing text representation models for text classification by re-implementing over 20 models across more than 10 datasets.

**Target Audience**:
- Natural Language Processing researchers

**Tasks**:
- Text Classification

**Limitations**: Authors state further work remains to be done: Performance analysis, Significance test, Effectiveness-efficiency discussion, Case study, comparison between RNN and CNN, and embedding sensitivity analysis.

## 💾 Data

**Source**: Datasets listed in the paper/table: 20Newsgroups; SST-1; SST-2; Trec; IMDB; SUBJ (as shown in Table 1).

**Size**: IMDB: 25,000 train, 25,000 test examples; SST-1: 8,544 train, 2,210 test examples; SST-2: 6,920 train, 1,821 test examples; SUBJ: 9,000 train, 1,000 test examples. (Other dataset sizes not specified in the provided text.)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Model re-implementation and empirical evaluation (re-implementing >20 models)
- Automated evaluation using Precision
- Significance testing (authors state the need for rigorous significance tests)

**Metrics**:
- Precision

**Calculation**: The paper states: 'We adopt the Precision as the final evaluation metrics, which is widely used in the classification task.'

**Interpretation**: N/A

**Validation**: Authors state the importance of robust comparison with significance testing but do not provide detailed validation procedures in the provided text.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
