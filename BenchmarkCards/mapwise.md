# MAPWise

## 📊 Benchmark Details

**Name**: MAPWise

**Overview**: MAPWise is a novel map-based question-answering benchmark, consisting of maps from three geographical regions (United States, India, China), each containing 1,000 questions designed to test models on their understanding of choropleth maps.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MapQA

**Resources**:
- [Resource](https://arxiv.org/abs/2409.00255)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate and encourage research in the area of visual-language models' question-answering capabilities regarding map data.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Map-based Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from reliable sources including the Reserve Bank of India, Kaiser Family Foundation, and the National Bureau of Statistics of China.

**Size**: 3,000 question-answer pairs

**Format**: N/A

**Annotation**: Manual annotation by expert annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Recall
- Precision

**Calculation**: Metrics were calculated based on exact match criteria for binary and count answers, with recall for single-word answers.

**Interpretation**: Higher accuracy indicates better model performance. Significant performance gaps identified between model outputs and human baselines.

**Baseline Results**: Human evaluation results provided a benchmark for model performance comparison.

**Validation**: Human validation was performed for accuracy verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
