# VidComposition

## 📊 Benchmark Details

**Name**: VidComposition

**Overview**: VidComposition is a new benchmark specifically designed to evaluate the video composition understanding capabilities of MLLMs using carefully curated compiled videos and cinematic-level annotations. It includes 982 videos with 1706 multiple-choice questions covering various compositional aspects such as camera movement, angle, shot size, narrative structure, character actions and emotions.

**Data Type**: video with multiple-choice questions

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Winoground
- MMComposition

**Resources**:
- [Resource](https://yunlong10.github.io/VidComposition/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the VidComposition benchmark is to assess MLLMs' understanding of video composition at a cinematic level.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Cinematography Analysis
- Character Understanding
- Narrative Understanding
- Scene Perception
- Making Analysis

**Limitations**: N/A

## 💾 Data

**Source**: The dataset comprises videos sourced from the Internet, focusing on compiled videos derived from commentary sources, movies, TV series, and animations.

**Size**: 982 videos and 1706 multiple-choice questions

**Format**: N/A

**Annotation**: Human-annotated questions and answers, with QA pairs verified through multiple rounds of review.

## 🔬 Methodology

**Methods**:
- Evaluation of MLLMs on understanding video composition
- Human evaluation for quality control

**Metrics**:
- Accuracy

**Calculation**: Overall accuracy is computed as the ratio of total correct answers to total questions across all sub-tasks.

**Interpretation**: Higher scores indicate better understanding of video compositions compared to human-level comprehension.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through multiple rounds of review of the questions and answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
