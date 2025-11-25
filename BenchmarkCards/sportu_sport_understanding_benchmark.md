# SPORTU (SPORT Understanding Benchmark)

## 📊 Benchmark Details

**Name**: SPORTU (SPORT Understanding Benchmark)

**Overview**: SPORTU is a comprehensive benchmark designed to assess Multimodal Large Language Models (MLLMs) across multi-level sports reasoning tasks, comprising two components: SPORTU-text for text-based question answering and SPORTU-video for video-based question answering.

**Data Type**: question-answering pairs, video clips

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SportsQA
- SoccerNet-XFoul

**Resources**:
- [GitHub Repository](https://github.com/chili-lab/SPORTU)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the sports understanding capabilities of MLLMs across text and video-based tasks, focusing on deep reasoning and rule-based understanding in sports.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: The models showed significant challenges in handling complex reasoning and rule comprehension, particularly in tasks requiring deep sports knowledge.

## 💾 Data

**Source**: SPORTU-text and SPORTU-video datasets generated and annotated by sports experts.

**Size**: 900 multiple-choice questions, 1,701 slow-motion video clips, 12,048 QA pairs

**Format**: JSON

**Annotation**: Human-annotated explanations by sports experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ROUGE-L
- BERTScore
- BLEURT
- G-Eval Score

**Calculation**: Accuracy metrics are based on the comparison of model predictions against ground truth labels.

**Interpretation**: The evaluation metrics help assess model performance in terms of accuracy and reasoning quality for sports understanding.

**Baseline Results**: GPT-4o achieved the highest accuracy at 71% on SPORTU-text.

**Validation**: A rigorous quality verification process ensured accuracy and consistency of annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
