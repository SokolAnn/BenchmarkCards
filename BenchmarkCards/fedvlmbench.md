# FedVLMBench

## 📊 Benchmark Details

**Name**: FedVLMBench

**Overview**: FedVLMBench is the first systematic benchmark for federated fine-tuning of Vision-Language Models (VLMs). The benchmark integrates two mainstream VLM architectures (encoder-based and encoder-free), four fine-tuning strategies, five federated learning algorithms, and six multimodal datasets, providing a standardized platform for evaluating federated fine-tuning strategies and task generalization.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- FS-LLM
- FedLLM-Bench
- OpenFedLLM
- FedMLLM

**Resources**:
- [Resource](https://arxiv.org/abs/2506.09638)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic benchmark for federated fine-tuning of Vision-Language Models (VLMs) that addresses privacy concerns while offering a comprehensive evaluation framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Visual Question Answering
- Image Classification
- Caption Generation
- Object Detection
- Visual Grounding

**Limitations**: N/A

## 💾 Data

**Source**: Six federated multimodal fine-tuning datasets developed for evaluation.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- CIDER
- ROUGE-L
- IoU

**Calculation**: Metrics are calculated based on evaluation results from the federated fine-tuning experiments.

**Interpretation**: Interpretation includes how different strategies and architectural designs impact performance on various tasks under federated learning settings.

**Baseline Results**: N/A

**Validation**: Extensive experiments to evaluate the performance of federated fine-tuning across various configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Privacy**
- **Accuracy**
- **Fairness**
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
