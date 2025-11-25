# HistNERo (Historical Named Entity Recognition for the Romanian Language)

## 📊 Benchmark Details

**Name**: HistNERo (Historical Named Entity Recognition for the Romanian Language)

**Overview**: This work introduces HistNERo, the first Romanian corpus for Named Entity Recognition (NER) in historical newspapers. The dataset contains 323k tokens of text, covering more than half of the 19th century until the late part of the 20th century, annotated with five named entities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Romanian

**Similar Benchmarks**:
- RONECv1
- RONECv2
- LegalNERo
- MicroBloggingNERo

**Resources**:
- [Resource](https://huggingface.co/datasets/avramandrei/histnero)

## 🎯 Purpose and Intended Users

**Goal**: To provide a valuable resource that advances the state of the art in historical NER, facilitating a more accurate and nuanced analysis of Romanian historical documents.

**Target Audience**:
- ML Researchers
- Historicians
- Natural Language Processing Practitioners

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The ROmanian DIachronic Corpus with Annotations (RODICA) corpus.

**Size**: 323,865 tokens

**Format**: BRAT format

**Annotation**: Annotated by eight native Romanian speakers with five named entities.

## 🔬 Methodology

**Methods**:
- Evaluation of several Romanian pre-trained language models

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: The strict F1-score was calculated based on the predicted and true entities.

**Interpretation**: Higher F1 scores indicate better model performance in identifying and classifying the named entities.

**Baseline Results**: RoBERT-large achieved a strict F1-score of 66.80%.

**Validation**: Validation was performed using an 80%, 10%, and 10% train-validation-test split of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
