# SCBench: A Sports Commentary Benchmark for Video LLMs

## 📊 Benchmark Details

**Name**: SCBench: A Sports Commentary Benchmark for Video LLMs

**Overview**: SCBench is a novel benchmarking task developed for sports video commentary generation, featuring a dataset called CommentarySet that includes 5,775 annotated video clips across six sports categories, evaluated using a new six-dimensional metric SCORES.

**Data Type**: video clips with commentary annotations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SoccerNet
- FineGym
- TenniSet

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of Video Large Language Models (Video LLMs) on generating detailed sports commentary and to advance research in sports video understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Sports Video Commentary Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected high-definition sports videos with professional English commentary from various sporting events.

**Size**: 5,775 clips

**Format**: JSON and video files

**Annotation**: Annotations are made by humans, marking the commentary and timestamps for video clips.

## 🔬 Methodology

**Methods**:
- Model Inference
- GPT-based Evaluation

**Metrics**:
- SCORES

**Calculation**: Performance evaluated by a combination of model-generated commentary and ground-truth commentary through the SCORES metric.

**Interpretation**: Scores range from 0 to 10 based on the quality of generated commentary compared to ground truth.

**Baseline Results**: InternVL-Chat-2 achieved the best performance with a score of 5.44.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
