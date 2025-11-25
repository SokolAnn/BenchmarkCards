# ChartX

## 📊 Benchmark Details

**Name**: ChartX

**Overview**: ChartX is a comprehensive, high-quality multi-modal evaluation set designed to assess chart understanding and chart-based reasoning of off-the-shelf Multi-modal Large Language Models (MLLMs). It covers 18 chart types, 7 chart tasks, 22 disciplinary topics, and provides multi-modal data (image, CSV, python code, and text description) to evaluate both perception and cognition chart abilities.

**Data Type**: multimodal (image, tabular CSV, python code, text descriptions)

**Domains**:
- Natural Language Processing
- Computer Vision
- Data Visualization

**Similar Benchmarks**:
- PlotQA
- Chart-to-text
- ChartQA
- OpenCQA
- ChartLlama
- ChartBench
- MMC
- ChartAssisstant

**Resources**:
- [GitHub Repository](https://github.com/Alpha-Innovator/ChartVLM)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively and rigorously benchmark the ability of off-the-shelf Multi-modal Large Language Models (MLLMs) in chart understanding and chart-based reasoning across diverse chart types, topics, and tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Chart community
- Industry Practitioners

**Tasks**:
- Structural Extraction
- Chart Type Recognition
- Chart Title Extraction
- Question Answering
- Chart Description
- Chart Summarization
- Chart Redrawing

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated using a two-stage, data-centric generation process driven by GPT-4 with human refinement and manual quality inspection. For each sample the pipeline produces image, CSV, python redrawing code, and text descriptions; redrawing code is used to render images. The paper also consolidates existing open-source chart datasets (ChartQA, Chart-to-text, PlotQA, SimChart9K) for model training (training data exclude ChartX evaluation set).

**Size**: 6,000 chart images; 48,000 multi-task samples (per-image multi-task labels leading to 48K samples); validation: 4,848 samples; test: 1,152 samples.

**Format**: CSV (tabular), image files (PNG rendered from generated code), Python code files (redrawing code), text descriptions

**Annotation**: Data and labels generated via GPT-4 templates then refined and validated through a four-step manual quality inspection: (1) programmatic format validation, (2) human image-CSV-text-code content validation, (3) human + GPT-4 validation of CSV-question-answering pairs, and (4) human + GPT-4 validation and scoring of image-summarization-description pairs (GPT-score).

## 🔬 Methodology

**Methods**:
- Automated metrics (SCRM, EM, AP@tolerance)
- Model-based evaluation using GPT-4 (GPT-acc, GPT-score)
- Human validation during dataset creation

**Metrics**:
- Structuring Chart-oriented Representation Metric (SCRM)
- Exact Match (EM)
- GPT-acc
- GPT-score (0-5 rating by GPT-4)
- Relaxed-acc
- Average Precision (AP) at Strict/Slight/High tolerances (AP@Strict, AP@Slight, AP@High)

**Calculation**: SCRM: linearized CSV tokens are transformed to triplet format for triplet-format matching (tolerance levels: strict/slight/high). GPT-acc: GPT-4 evaluates exact-answer tasks with a 5% margin of error for numerical responses. GPT-score: GPT-4 rates open-ended tasks (description, summarization, redrawing code) on a 0-5 scale based on manually adjudicated scoring criteria. EM: exact match for tasks like chart title and chart type.

**Interpretation**: Higher metric values indicate better performance. GPT-score is 0-5 (higher is better). GPT-acc produces True/False judgments with a 5% numeric tolerance. SCRM uses triplet matching with multiple tolerance levels to assess structural extraction. The paper notes a direct positive correlation between Structural Extraction (SE) accuracy and downstream cognition task performance (e.g., cognition performance peaks when SE attains 100% 'golden table').

**Baseline Results**: Representative results on the ChartX test set (Table 2): ChartVLM-L: Structural Extraction AP@Strict/AP@Slight/AP@High = 23.18 / 30.68 / 38.30; Chart Type (EM) = 96.82; Chart Title (EM) = 97.05; QA (GPT-acc) = 43.84; Chart Description (GPT-score) = 3.68; Chart Summarization (GPT-score) = 3.50; Chart Redrawing (GPT-score) = 3.75. GPT-4V: Structural Extraction AP@Strict/AP@Slight/AP@High = 20.91 / 26.00 / 36.09; Chart Type (EM) = 70.43; Chart Title (EM) = 95.22; QA (GPT-acc) = 33.04; Chart Description (GPT-score) = 3.17; Chart Summarization (GPT-score) = 3.12; Chart Redrawing (GPT-score) = 2.63. (All values reported as presented in the paper's tables.)

**Validation**: Dataset validation comprised a four-step manual quality inspection (programmatic format checks, human content validation across modalities, human+GPT-4 QA validation, human+GPT-4 summarization/description validation). The ChartX benchmark is split into 4,848 validation samples (used during fine-tuning) and 1,152 test samples (reported results).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Governance

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination
- **Governance**: Incorrect risk testing, Lack of testing diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
