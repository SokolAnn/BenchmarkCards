# AURA (Audio-visual Understanding and Reasoning Assessment)

## 📊 Benchmark Details

**Name**: AURA (Audio-visual Understanding and Reasoning Assessment)

**Overview**: AURA is the first question-answering benchmark designed to evaluate the reasoning capabilities of Audio-Visual Large Language Models (AV-LLMs) and Omni-Modal Language Models (OLMs) on fine-grained cognitive tasks, including Cross-Modal Causal Reasoning, Timbre/Pitch Reasoning, Tempo/AV Synchronization Analysis, Unanswerability, Implicit Distractions, and Performer Skill Profiling.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Music

**Languages**:
- English

**Similar Benchmarks**:
- A VQA
- Music-A VQA

**Resources**:
- [Resource](https://rishieraj.github.io/aura-project-page/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cross-modal, audio-visual reasoning performance of state-of-the-art models on six fine-grained cognitive tasks.

**Target Audience**:
- A I Researchers
- Model Developers
- Educators

**Tasks**:
- Cross-Modal Causal Reasoning
- Timbre/Pitch Reasoning
- Tempo/AV Synchronization Analysis
- Unanswerability
- Implicit Distractions
- Performer Skill Profiling

**Limitations**: N/A

## 💾 Data

**Source**: Multiple sources including FineVideo dataset, MUSIC-A VQA dataset, and custom YouTube videos.

**Size**: 1,600 question-answering pairs

**Format**: JSONL

**Annotation**: Automatically generated via a modular QA generation pipeline utilizing large language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Answer Accuracy
- Factual Consistency Score (FCS)
- Core Inference Score (CIS)

**Calculation**: FCS evaluates if reasoning is factually grounded, while CIS assesses logical validity of reasoning.

**Interpretation**: Higher FCS and CIS scores indicate better reasoning quality in audio-visual context.

**Baseline Results**: Various state-of-the-art models evaluated with varying performance across AURA tasks.

**Validation**: Evaluation includes comparison against ground-truth reasoning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
