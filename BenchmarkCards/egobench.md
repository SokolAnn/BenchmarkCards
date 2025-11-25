# EgoBench

## 📊 Benchmark Details

**Name**: EgoBench

**Overview**: EgoBench is a benchmark designed to comprehensively evaluate the embodied cognitive abilities of existing MLLMs (Multimodal Large Language Models) across eight distinct tasks in egocentric video understanding.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Ego4D
- Charades-Ego
- EgoMCQ

**Resources**:
- [Resource](https://egovisiongroup.github.io/Exo2Ego.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of existing MLLMs on various real-world egocentric tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Reasoning
- Episodic Memory
- Action Recognition
- Multi-Instance Retrieval
- Egocentric Navigation
- Planning
- Video-Text Alignment

**Limitations**: N/A

## 💾 Data

**Source**: Ego-ExoClip dataset

**Size**: 1.1M clip-text pairs

**Format**: N/A

**Annotation**: Annotated by multiple experts for narrative consistency.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Mean Average Precision (MAP)

**Calculation**: Metrics calculated based on the performance of models on the EgoBench tasks including several standardized evaluation datasets.

**Interpretation**: High accuracy indicates effective understanding of egocentric videos and better rule adherence in predictions.

**Baseline Results**: Results benchmarked against state-of-the-art models such as VideoLLaMA2 and VideoChat2.

**Validation**: Extensive experiments validating the effectiveness of the proposed approach across various egocentric tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The dataset analysis includes various scenarios and demographic factors of participating subjects.

**Potential Harm**: The benchmark aims to address inaccuracies in egocentric task understanding.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
