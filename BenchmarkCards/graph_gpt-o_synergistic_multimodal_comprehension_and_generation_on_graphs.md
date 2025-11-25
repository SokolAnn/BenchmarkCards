# GRAPH GPT-O (Synergistic Multimodal Comprehension and Generation on Graphs)

## 📊 Benchmark Details

**Name**: GRAPH GPT-O (Synergistic Multimodal Comprehension and Generation on Graphs)

**Overview**: This paper addresses the task of multimodal content generation on multimodal attributed graphs (MMAGs), formally defines the task, and introduces three real-world benchmark datasets across domains such as art and e-commerce to support this task.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2502.11925)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to define the task of multimodal content generation from multimodal attributed graphs (MMAGs) and provide datasets for evaluation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multimodal Content Generation

**Limitations**: In our current approach, we treat the graph as homogeneous, simplifying all nodes and edges into a single type.

## 💾 Data

**Source**: Datasets include ART500K, Amazon-Baby, and Amazon-Beauty, which consist of multimodal attributed graphs.

**Size**: 40,000 nodes sampled for training; 50 nodes for testing.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- CLIP-I2 Score
- Perplexity
- CLIP-IT Score
- KL Divergence

**Calculation**: Metrics calculate the alignment and quality of synthesized images and texts through various models.

**Interpretation**: Higher scores in CLIP-I2 and lower perplexity indicate better performance.

**Baseline Results**: Performance compared against models like DreamLLM, showing significant improvements.

**Validation**: Evaluations conducted on three datasets from distinct domains.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: The model still depends on the MLLM foundation, making it subject to inherent limitations and ethical concerns.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
