# DORE

## 📊 Benchmark Details

**Name**: DORE

**Overview**: DORE is a dataset for Definition Modelling in Portuguese, comprising more than 100,000 definitions, filling the gap for DM datasets in mid/high-resource languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Portuguese

**Resources**:
- [Resource](https://huggingface.co/datasets/multidefmod/dore)

## 🎯 Purpose and Intended Users

**Goal**: To fill the gap in available datasets for Definition Modelling for the Portuguese language and to facilitate research and applications in this area.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Definition Modelling

**Limitations**: N/A

## 💾 Data

**Source**: Data was collected from Dicio and Portuguese Wiktionary, both being publicly available resources.

**Size**: 103,019 definitions

**Format**: N/A

**Annotation**: Definitions were scraped from publicly available online dictionaries.

## 🔬 Methodology

**Methods**:
- Deep Learning Models
- Prompting with LLMs

**Metrics**:
- BLEU
- TER
- BERTScore
- BLEURT

**Calculation**: Evaluation metrics were calculated based on the performance of the models on the test set.

**Interpretation**: Higher scores indicate better generation quality of definitions.

**Baseline Results**: N/A

**Validation**: The dataset was validated by splitting into training and test sets and experimenting with various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-Non Commercial-ShareAlike (CC-BY-NC-SA) 4.0 International Public License

**Consent Procedures**: Permission was sought from Dicio to use definitions for research.

**Compliance With Regulations**: Not Applicable
