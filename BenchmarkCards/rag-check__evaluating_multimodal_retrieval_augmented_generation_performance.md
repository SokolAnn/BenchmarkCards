# RAG-Check: Evaluating Multimodal Retrieval Augmented Generation Performance

## 📊 Benchmark Details

**Name**: RAG-Check: Evaluating Multimodal Retrieval Augmented Generation Performance

**Overview**: RAG-Check is a novel framework designed to evaluate the reliability of multi-modal retrieval-augmented generation systems. It includes two performance measures: the relevancy score (RS) for assessing the relevance of retrieved entries to the query and the correctness score (CS) for evaluating the accuracy of the generated response.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2501.03995)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of multi-modal RAG systems by quantifying the relevance and correctness of their generated outputs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Generation
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 5000-sample human-annotated database evaluating the relevancy of retrieved pieces and the correctness of response statements.

**Size**: 5,000 samples

**Format**: N/A

**Annotation**: Human annotation for evaluating the relevancy and correctness.

## 🔬 Methodology

**Methods**:
- Neural network structure for RS and CS
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Relevancy Score
- Correctness Score

**Calculation**: RS is calculated based on the relevance of retrieved entries and CS is determined by the correctness of generated spans based on raw context.

**Interpretation**: A higher RS indicates better relevance of retrieved pieces to the query, while a higher CS signifies that the generated responses are accurate relative to the retrieved raw context.

**Baseline Results**: N/A

**Validation**: Trained on a dataset comprising human evaluator samples and a ChatGPT-derived database.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
