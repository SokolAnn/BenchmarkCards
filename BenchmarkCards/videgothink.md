# VidEgoThink

## 📊 Benchmark Details

**Name**: VidEgoThink

**Overview**: VidEgoThink is a comprehensive benchmark for evaluating egocentric video understanding capabilities in Embodied AI through four interrelated tasks: video question-answering, hierarchy planning, visual grounding, and reward modeling.

**Data Type**: video question-answering pairs, hierarchy planning steps, visual grounding bounding boxes and temporal segments, reward modeling critiques and feedback

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- EgoTaskQA
- EgoPlan
- EgoSchema

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate egocentric video understanding for Multi-modal Large Language Models (MLLMs) in the context of Embodied AI.

**Target Audience**:
- ML Researchers
- AI Developers
- Robotics Researchers

**Tasks**:
- Video Question Answering
- Hierarchy Planning
- Visual Grounding
- Reward Modeling

**Limitations**: VidEgoThink has limited data diversity and immature evaluation methods, particularly in hierarchy planning and reward modeling.

## 💾 Data

**Source**: Generated from the Ego4D dataset using an automatic data generation pipeline leveraging GPT-4o, filtered by human annotators.

**Size**: 4,993 instances

**Format**: N/A

**Annotation**: Automatically generated with human filtering to ensure quality and diversity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- mean Intersection over Union (mIoU)

**Calculation**: Metrics are calculated based on the performance of models against ground truth values across various tasks in the benchmark.

**Interpretation**: Higher scores indicate better performance in egocentric video understanding.

**Baseline Results**: GPT-4o models performed poorly across all tasks, with accuracy around 31.17% in video question-answering tasks.

**Validation**: The benchmark was evaluated via extensive experiments with various models, indicating their capabilities and areas needing improvement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
