# SEED-Bench

## 📊 Benchmark Details

**Name**: SEED-Bench

**Overview**: SEED-Bench consists of 19K multiple choice questions with accurate human annotations spanning 12 evaluation dimensions including both image and video modalities, designed to evaluate the generative comprehension capability of Multimodal Large Language Models (MLLMs). The benchmark uses multiple-choice questions with groundtruth options derived from human annotation to enable objective and efficient assessment.

**Data Type**: multimodal (image and video) multiple-choice question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Similar Benchmarks**:
- MME
- MMBench
- LVLM-eHub
- LAMM

**Resources**:
- [GitHub Repository](https://github.com/AILab-CVC/SEED-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the generative comprehension capability of Multimodal Large Language Models (MLLMs) via a large-scale, objective multiple-choice benchmark covering 12 evaluation dimensions across spatial and temporal understanding.

**Target Audience**:
- the community

**Tasks**:
- Scene Understanding
- Instance Identity
- Instance Attributes
- Instance Location
- Instance Counting
- Spatial Relation
- Instance Interaction
- Visual Reasoning
- Text Recognition
- Action Recognition
- Action Prediction
- Procedure Understanding

**Limitations**: Extracting reliable temporal information from videos using existing foundation models is extremely difficult; therefore video questions are constructed using ground-truth video annotations rather than fully automated visual extraction.

## 💾 Data

**Source**: Images: CC3M (filtered and captioned with Tag2Text and BLIP2); Videos: Something-Something-v2 (SSV2) validation set (1,740 videos), Epic-Kitchen 100 (138 long videos), Breakfast (videos with fine-grained action segmentation annotations).

**Size**: 19,242 multiple-choice questions

**Format**: N/A

**Annotation**: Human annotation: human annotators verified generated question/answer pairs, selected the correct option for each multiple-choice question, and classified each question into one evaluation dimension. Questions that could not be answered from the visual input, had no correct choice, or had multiple correct choices were discarded.

## 🔬 Methodology

**Methods**:
- Automated metrics (accuracy)
- Answer ranking via log-likelihood for each candidate option
- Automatic filtering using multiple LLMs to remove questions answerable without visual input
- Human annotation verification and classification

**Metrics**:
- Accuracy

**Calculation**: For each candidate choice, compute the likelihood that an MLLM generates the content of that choice given the question (log-likelihood); select the choice with the highest likelihood as the model's prediction. Accuracy is the proportion of correctly answered multiple-choice questions relative to the total number of questions.

**Interpretation**: Higher Accuracy indicates better generative comprehension on the evaluated dimension(s). Accuracy is interpreted as the proportion of correctly answered multiple-choice questions; per-dimension and averaged spatial/temporal accuracies are reported.

**Baseline Results**: Evaluation of 18 models provided. Examples of reported overall accuracies include: InstructBLIP Vicuna 53.37% overall, InstructBLIP 52.73% overall, BLIP2 46.35% overall, MiniGPT-4 42.84% overall (see paper tables and leaderboards for full results).

**Validation**: Automatic filtering: generated questions (without images) were fed to Vicuna-7B, Flan-T5-XXL and LLaMA-7B and questions answerable by all three were removed (5.52% filtered). Human annotators then verified correctness, discarded ambiguous or unanswerable questions, and classified each question into evaluation dimensions, resulting in a clean benchmark of 19K multiple-choice questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Governance

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Governance**: Incorrect risk testing

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
