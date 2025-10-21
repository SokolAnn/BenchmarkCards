# A Benchmark Evaluation of Clinical Named Entity Recognition in French

## 📊 Benchmark Details

**Name**: A Benchmark Evaluation of Clinical Named Entity Recognition in French

**Overview**: This paper presents the first benchmark evaluation of masked language models for the biomedical domain on the clinical French Named Entity Recognition (NER) task, using three publicly available clinical French corpora. The evaluation is based on released gold standard annotations, including nested entities.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- French

**Resources**:
- [Resource](https://deft.limsi.fr/2020/index-en.html)
- [GitHub Repository](https://github.com/percevalw/nlstruct)
- [Resource](https://brat.nlplab.org/standoff.html)
- [GitHub Repository](https://github.com/grouin/propa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of masked language models for clinical named entity recognition in the biomedical domain in French.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: While a full evaluation could cover more models, it would incur a higher carbon footprint and we decided to select representative models of the categories that we aimed to cover: general and domain-specific models that had been recently evaluated on similar corpora without direct comparability.

## 💾 Data

**Source**: Three publically available corpora for clinical named entity recognition in French: DEFT, E3C, and QUAERO French Med.

**Size**: 1,615 clinical cases from E3C, 167 clinical cases from DEFT, 2,500 titles from MEDLINE.

**Format**: N/A

**Annotation**: Gold-standard annotations including nested entities.

## 🔬 Methodology

**Methods**:
- Entity-level evaluation
- Micro Precision
- Recall
- F-measure

**Metrics**:
- Precision
- Recall
- F-measure

**Calculation**: Confidence intervals at 95% confidence level were computed using the empirical bootstrap method from 1,000 samples.

**Interpretation**: Models with higher F-measure indicate better performance in the NER task.

**Baseline Results**: Baseline scores were computed using a symbolic method that builds a dictionary of entities found in the training and development splits of a corpus.

**Validation**: Systematic evaluation providing comparability across systems as well as with literature introducing the reference corpora.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Environmental Impact

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
