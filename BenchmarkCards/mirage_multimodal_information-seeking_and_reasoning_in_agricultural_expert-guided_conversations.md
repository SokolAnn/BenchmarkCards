# MIRAGE (Multimodal Information-seeking and Reasoning in Agricultural Expert-Guided Conversations)

## 📊 Benchmark Details

**Name**: MIRAGE (Multimodal Information-seeking and Reasoning in Agricultural Expert-Guided Conversations)

**Overview**: MIRAGE is a new benchmark for multimodal expert-level reasoning and decision-making in consultative interaction settings, specifically designed for the agriculture domain. It combines natural user queries, expert-authored responses, and image-based context to evaluate models on grounded reasoning, clarification strategies, and long-form generation.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision
- Agriculture

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/MIRAGE-Benchmark)
- [GitHub Repository](https://github.com/MIRAGE-Benchmark/MIRAGE-Benchmark)
- [Resource](https://mirage-benchmark.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate vision-language models on expert-level reasoning and decision-making in agricultural consultations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Named Entity Recognition
- Question Answering
- Conversational Decision-Making

**Limitations**: MIRAGE does not yet simulate interactive dialogue with real users or user simulators, limiting evaluation of adaptation and dialogue flow over time.

## 💾 Data

**Source**: Real user-expert interactions sourced from Ask Extension, reflecting actual agricultural consultation scenarios.

**Size**: 35,000 interactions

**Format**: Dialogues with images

**Annotation**: Curated through a multi-step pipeline involving data cleaning, categorization, and expert validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Identification Accuracy
- Reasoning Score
- Accuracy
- Relevance
- Completeness
- Parsimony

**Calculation**: Metrics are calculated based on comparisons between model outputs and expert responses across multiple dimensions.

**Interpretation**: High scores correspond to better identification accuracy and reasoning quality aligned with expert benchmarks.

**Validation**: Evaluated against an ensemble of reasoning-capable language models to ensure robust and interpretable assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis of performance across different agricultural tasks reveals disparities in model effectiveness for various user needs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User anonymity was preserved during dataset curation, with personal information sanitized.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
