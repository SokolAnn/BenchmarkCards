# FETA: A Benchmark for Few-Sample Task Transfer in Open-Domain Dialogue

## 📊 Benchmark Details

**Name**: FETA: A Benchmark for Few-Sample Task Transfer in Open-Domain Dialogue

**Overview**: FETA is a benchmark for few-sample task transfer in open-domain dialogue. It contains two underlying conversation sources (DailyDialog and Friends) with 17 total tasks (10 and 7 tasks per source) enabling intra-dataset task transfer studies. The benchmark enables evaluation across 132 source-target task pairs and includes baseline experiments using three pretrained language models and three learning algorithms in single-source and multi-source settings.

**Data Type**: text (multi-turn dialogues with task-specific annotations: utterance-level classification, dialogue-level classification, span extraction, multiple-choice)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- DialoGLUE
- RADDLE
- DailyDialog++

**Resources**:
- [Resource](https://alon-albalak.github.io/feta-website/)
- [GitHub Repository](https://github.com/alon-albalak/TLiDB)
- [Resource](https://arxiv.org/abs/2205.06262v2)

## 🎯 Purpose and Intended Users

**Goal**: To create a benchmark for few-sample task transfer for language understanding in open-domain dialogue and to study intra-dataset task transfer, comparing learning algorithms and model architectures across 132 source-target task pairs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Emotion Recognition
- Dialogue Act Classification
- Topic Classification
- Causal Emotion Span Extraction
- Causal Emotion Entailment
- Dialogue-level Natural Language Inference
- Dialogue Reasoning Span Extraction
- Dialogue Reasoning Multiple Choice
- Commonsense Relation Extraction
- Adversarial Response Selection
- Reading Comprehension
- Character Identification
- Question Answering
- Personality Detection
- Relation Extraction
- Emotion Recognition (MELD)
- Emotion Recognition (EmoryNLP)

**Limitations**: Energy consumption and environmental impact of large-scale experiments; accessibility concerns for researchers with limited resources (benchmark scale may limit who can reasonably compete); differences in model pre-training corpora likely affect results; cannot exhaustively test all language models or learning algorithms; intra-dataset constraint limits the number of pre-annotated tasks that can be accommodated.

## 💾 Data

**Source**: DailyDialog (Li et al., 2017) and Friends (Chen and Choi, 2016) with additional task annotations reused from RECCON, CIDER, DailyDialog++, EmoryNLP, MELD, FriendsQA, DialogRE, and other cited sources.

**Size**: 17 tasks across two dialogue sources; per-task sample counts provided in Table 1 of the paper (FETA uses 7/1.5/15% splits of the original dialogues and down-samples train and development to 10% of original quantities; per-task example counts vary and are listed explicitly in Table 1).

**Format**: N/A

**Annotation**: Reused annotations from the original datasets and referenced works (e.g., RECCON, CIDER, DailyDialog++, EmoryNLP, MELD, FriendsQA, DialogRE); tasks are annotated as described in the paper and original sources.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Aggregate scoring (Average Score and Top-1 Score)
- Single-source transfer experiments
- Multi-source transfer experiments
- Baseline fine-tuning (model trained directly on the target task)

**Metrics**:
- Macro-F1
- micro-F1
- Token-F1
- Weighted-F1
- Exact Match (EM)
- Accuracy
- Average Score (aggregate over source-target pairs)
- Top-1 Score (best source task per target)
- Score Delta (Δ) relative to baseline

**Calculation**: For a given source s, target t, model f, and algorithm A, per-task score is computed by averaging the task-specific metrics Mt (each metric scaled 0-100). Average Score is the mean of score(s,t,f,A) across all source-target pairs. Top-1 Score is the average over target tasks of the maximum source score (excluding scores below the baseline). Score Delta (Δ) = score(s,t,f,A) - baseline_score(s,t,f,AB), where baseline AB is the model trained directly on the target task. Average Δ and Top-1 Δ are computed analogously.

**Interpretation**: Average Score measures aggregate performance of a model and algorithm across all source-target pairs. Top-1 Score measures performance assuming the best source task is known a priori. Positive Score Delta (Δ) indicates improvement over the baseline (model trained only on target). All reported task metrics range from 0 to 100.

**Baseline Results**: Baseline defined as model trained directly on the target task (denoted AB). The paper ran 255 baseline experiments (17 tasks × 3 models × 5 random seeds). Specific baseline scores per task/model/algorithm are reported in the paper (Tables and Appendix).

**Validation**: Validation-based best model selection with hyperparameter sweeps (learning rate values {3e-6, 1e-5, 3e-5, 1e-4}, 3e-5 found to work well). Experiments use 5 random seeds. Models trained for 30 epochs on DailyDialog tasks and 20 epochs on Friends tasks; batch size 60; optimizer: Adam.

## ⚠️ Targeted Risks

**Risk Categories**:
- Environmental impact
- Accessibility
- Testing diversity

**Atlas Risks**:
- **Societal Impact**: Impact on the environment
- **Governance**: Lack of testing diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
