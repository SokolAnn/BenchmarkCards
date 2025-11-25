# POPVQA

## 📊 Benchmark Details

**Name**: POPVQA

**Overview**: POPVQA is a dataset designed to facilitate the validation of entity identification prior to question answering across visual and textual representations. It highlights the performance gap in entity knowledge extraction and reasoning in Vision Language Models.

**Data Type**: entity-image pairs and question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- PopQA
- infoSeek
- VeQuAE

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the disparity in model performance when answering factual questions about entities presented in text versus those depicted in images, and to provide insights for improving Vision Language Models.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Entity Recognition
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 15,395 entity-image pairs from Wikidata with corresponding questions and answers regarding those entities.

**Size**: 15,395 entity-image pairs

**Format**: N/A

**Annotation**: Questions generated from subject-relation-object triplets using manually designed templates.

## 🔬 Methodology

**Methods**:
- Human Evaluation
- Automated Metrics

**Metrics**:
- Accuracy

**Calculation**: Model performance is calculated as the accuracy of correctly answered questions for identified entities.

**Interpretation**: Lower accuracy drop between visual and textual representations indicates better utilization of visual input by the models.

**Baseline Results**: Detailed performance across various models is provided, with accuracy results showing significant drops for visual inputs.

**Validation**: Further investigation into model performance through various pre-defined layers within the neural network.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was collected with only permissive licenses and complies with institutional IRB approval.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
