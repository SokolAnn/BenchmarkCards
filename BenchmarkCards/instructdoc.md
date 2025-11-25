# InstructDoc

## 📊 Benchmark Details

**Name**: InstructDoc

**Overview**: InstructDoc is the first large-scale collection of 30 publicly available visual document understanding (VDU) datasets, each with diverse instructions in a unified format, covering a wide range of 12 tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LLaV AR
- DocOwl

**Resources**:
- [GitHub Repository](https://github.com/nttmdlab-nlp/InstructDoc)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for training and evaluating models on visual document understanding tasks using instructions.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Key Information Extraction
- Single-page QA
- Multi-page QA
- Document Natural Language Inference
- Dialogue
- Captioning
- Classification
- Document Layout Analysis
- Image-Text Matching

**Limitations**: N/A

## 💾 Data

**Source**: 30 publicly available VDU datasets collected and annotated with diverse instructions.

**Size**: 5,917,602 held-in instances, 30,177 held-out instances

**Format**: Not specified

**Annotation**: Manual annotation of instructions by experts following a unified schema.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- ROUGE-L
- Relaxed Accuracy (RAcc.)
- Entity F1 (eF1)

**Calculation**: Metrics are calculated based on the evaluation protocol of each dataset.

**Interpretation**: Higher scores indicate better performance in zero-shot tasks.

**Baseline Results**: InstructDr outperforms existing MLLMs and ChatGPT in zero-shot evaluations.

**Validation**: The benchmark was validated through testing on held-out datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
