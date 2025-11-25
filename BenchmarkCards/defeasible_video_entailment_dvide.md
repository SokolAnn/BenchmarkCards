# Defeasible Video Entailment (DVidE)

## 📊 Benchmark Details

**Name**: Defeasible Video Entailment (DVidE)

**Overview**: The DVidE benchmark introduces a new task that challenges models to dynamically revise inferences about video content based on textual updates, with annotations for strengthener and weakener relationships.

**Data Type**: video and text

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VIOLIN

**Resources**:
- [Resource](https://doi.org/10.48550/arXiv.2412.16232)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of models to perform defeasible inference in video understanding tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Defeasible Video Entailment Classification
- Defeasible Video Entailment Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is derived from the VIOLIN dataset, which consists of video-and-language inference pairs.

**Size**: 986 examples

**Format**: N/A

**Annotation**: Annotations were done by multiple annotators to classify updates as strengtheners or weakeners.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Generated update evaluation with LLM

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall
- ROUGE-L
- BLEU-4

**Calculation**: Metrics are calculated based on the standard evaluation frameworks for classification and generation tasks.

**Interpretation**: Higher metrics signify better model performance in classifying and generating accurate updates.

**Validation**: Seen through experimental results demonstrating significant improvements in classification and generation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
