# Visual Network Analysis (VNA) Benchmark

## 📊 Benchmark Details

**Name**: Visual Network Analysis (VNA) Benchmark

**Overview**: We introduce a new benchmark for the evaluation of Vision Language Models (VLMs) on foundational Visual Network Analysis (VNA) tasks, including five tasks related to three core network science concepts: maximum degree, structural balance, and identifying components.

**Data Type**: image

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VisionGraph Benchmark
- GITQA (Graph-Image-Text Question Answering) Dataset

**Resources**:
- [Resource](https://figshare.com/articles/dataset/Multimodal_LLMs_Struggle_with_Basic_Visual_Network_Analysis_a_Visual_Network_Analysis_Benchmark/25938448)
- [GitHub Repository](https://github.com/EvanUp/VNA_Benchmark/blob/main/prompts/prompts.csv)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to evaluate the zero-shot ability of multimodal LLMs to perform Visual Network Analysis tasks on small-scale graphs.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Maximum Degree Identification
- Structural Balance Assessment
- Component Counting

**Limitations**: The tasks designed are not representative of all possible graphs and evaluate mastery of select network science concepts.

## 💾 Data

**Source**: Synthetic graphs generated programmatically using Python libraries NetworkX and netgraph.

**Size**: 200 graph visualizations

**Format**: PNG

**Annotation**: Automatically generated visualizations with corresponding task instructions.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Mean Squared Error (MSE)
- Mean Jaccard Similarity

**Calculation**: Accuracy calculated based on correct identification of graph attributes; MSE computed as the average of squared differences between actual and predicted values.

**Interpretation**: A higher accuracy indicates better performance in identifying graph-related attributes; MSE indicates prediction errors.

**Validation**: Performance was validated by comparing predicted results against ground truth labels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
