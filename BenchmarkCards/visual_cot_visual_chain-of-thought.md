# Visual CoT (Visual Chain-of-Thought)

## 📊 Benchmark Details

**Name**: Visual CoT (Visual Chain-of-Thought)

**Overview**: The Visual CoT dataset comprises 438k question-answer pairs, annotated with intermediate bounding boxes highlighting key regions essential for answering the questions, including about 98k pairs with detailed reasoning steps. The benchmark is designed to evaluate Multi-Modal Large Language Models (MLLMs) in scenarios requiring specific local region identification in visual data.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GQA (Grounded Question Answering)
- TextVQA
- DocVQA

**Resources**:
- [GitHub Repository](https://github.com/deepcs233/Visual-CoT)
- [Resource](https://huggingface.co/datasets/deepcs233/Visual-CoT)
- [Resource](https://huggingface.co/collections/deepcs233/viscot-65fe883e2a0cdd3c59fc5d63)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to enhance the reasoning capabilities of Multi-Modal Large Language Models (MLLMs) and improve interpretability and processing of visual inputs in response to questions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: A large-scale collection of visual question-answering data utilizing 12 source datasets across five distinct domains, including annotations with bounding boxes that highlight critical regions in images.

**Size**: 438,000 question-answer pairs

**Format**: JSON

**Annotation**: Annotated with intermediate reasoning steps and bounding boxes highlighting key regions essential for answering the questions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Top-1 Accuracy@0.5

**Calculation**: Metrics are calculated based on the accuracy of predictions in identifying relevant visual regions corresponding to the questions asked.

**Interpretation**: Higher scores indicate better performance in accurately identifying key regions in images for visual question answering tasks and generating correct answers.

**Baseline Results**: N/A

**Validation**: Evaluation is performed against multiple established benchmarks in visual question answering.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
