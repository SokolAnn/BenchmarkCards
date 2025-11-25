# UrbanVideo-Bench

## 📊 Benchmark Details

**Name**: UrbanVideo-Bench

**Overview**: UrbanVideo-Bench is a benchmark designed for evaluating embodied motion cognition in urban open-ended spaces through video data. It includes 1.5k video clips and 5.2k multiple-choice questions across various tasks related to recall, perception, reasoning, and navigation.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- LongVideoBench
- MovieChat-1K
- MMBench-Video
- HourVideo
- EgoSchema
- Lingoqa
- VSI-Bench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the UrbanVideo-Bench benchmark is to evaluate the embodied cognitive abilities of video-large language models (Video-LLMs) during navigation and interaction with dynamic urban environments.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Recall
- Perception
- Reasoning
- Navigation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset includes video data collected from real cities in Guangdong Province, China, and two simulated environments, EmbodiedCity and AerialVLN.

**Size**: 1,547 video clips and 5.2k multiple-choice questions

**Format**: N/A

**Annotation**: Manually annotated and generated through a pipeline utilizing LMMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct answers to multiple-choice questions across the tasks.

**Interpretation**: An accuracy score reflects the performance of Video-LLMs in navigating urban environments, with higher scores indicating better performance and understanding of the tasks.

**Baseline Results**: 17 popular Video-LLMs were evaluated with Qwen-VL-Max achieving the highest accuracy at 45.5%.

**Validation**: Results were validated through correlation analysis of task performance among Video-LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
