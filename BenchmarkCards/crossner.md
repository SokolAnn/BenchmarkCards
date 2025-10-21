# CrossNER

## 📊 Benchmark Details

**Name**: CrossNER

**Overview**: CrossNER is a human-annotated NER dataset spanning over five diverse domains with specialized entity categories for each domain, aimed at evaluating cross-domain named entity recognition models.

**Data Type**: named entity recognition samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zliucr/CrossNER)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset and facilitate research in the NER domain adaptation area.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Cross-domain NER dataset created from Wikipedia and pre-annotated using DBpedia Ontology.

**Size**: 5,000 examples (1,000 examples across 5 domains for development and test sets, with smaller training examples in low-resource scenarios)

**Format**: JSON

**Annotation**: Manual annotation by experts after pre-annotating with DBpedia Ontology.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 Score calculated on the NER task to evaluate model performance.

**Interpretation**: Higher F1 Scores indicate better performance in recognizing and classifying named entities.

**Validation**: Models were validated based on performance metrics observed in the development set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
