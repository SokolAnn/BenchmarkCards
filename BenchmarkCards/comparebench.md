# CompareBench

## 📊 Benchmark Details

**Name**: CompareBench

**Overview**: CompareBench is a benchmark for evaluating visual comparison reasoning in vision-language models (VLMs), consisting of 1,000 QA pairs across four tasks: quantity, temporal, geometric, and spatial reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- TallyBench
- HistCaps
- MMBench
- MM-Vet
- BLINK

**Resources**:
- [GitHub Repository](https://github.com/caijie0620/CompareBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a controlled and diverse evaluation framework for visual comparison reasoning in vision-language models.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Quantity Comparison
- Temporal Reasoning
- Geometric Property Comparison
- Spatial Relation Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from TallyBench and HistCaps datasets.

**Size**: 1,000 QA pairs

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is measured as the percentage of exact matches between predicted and ground-truth answers.

**Interpretation**: Higher accuracy indicates better performance in visual comparison reasoning tasks.

**Baseline Results**: Human performance is near 100% on most tasks.

**Validation**: Models evaluated include closed-source APIs and open-source models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
