# Reefknot

## 📊 Benchmark Details

**Name**: Reefknot

**Overview**: A comprehensive benchmark targeting relation hallucinations, comprising over 20,000 real-world samples for evaluating the performance of multimodal large language models (MLLMs).

**Data Type**: Multimodal

**Domains**:
- Visual Genome

**Similar Benchmarks**:
- POPE
- HaELM
- MME
- AMBER
- MHaluBench
- R-Bench
- MMRel
- VALOR-EVAL

**Resources**:
- [GitHub Repository](https://github.com/JackChen-seu/Reefknot)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance on relation hallucination in MLLMs and to propose mitigation strategies.

**Target Audience**:
- Researchers
- AI practitioners

**Tasks**:
- Yes/No questions
- Multiple Choice Questions (MCQ)
- Visual Question Answering (VQA)

**Limitations**: None

## 💾 Data

**Source**: Visual Genome dataset

**Size**: 21,880 questions across 11,084 images

**Format**: Triplet-based dataset

**Annotation**: Expert-based validation

## 🔬 Methodology

**Methods**:
- Confidence-based detection
- Detect-then-Calibrate method

**Metrics**:
- Hallucination rates (Halr)
- Response Confidence (Rscore)

**Calculation**: Rscore = Avg[1 - Halr_i] for i = 1 to 3

**Interpretation**: Lower hallucination rate indicates better performance.

**Baseline Results**: 9.75% improvement across three datasets.

**Validation**: Multi-turn manual checking performed by experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
