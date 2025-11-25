# CL2GEC (Continual Learning for Chinese Literature Grammatical Error Correction)

## 📊 Benchmark Details

**Name**: CL2GEC (Continual Learning for Chinese Literature Grammatical Error Correction)

**Overview**: CL2GEC is the first Continual Learning benchmark for Chinese Literature Grammatical Error Correction, designed to evaluate adaptive CGEC across multiple academic fields. It includes 10,000 human-annotated sentences spanning 10 disciplines, each exhibiting distinct linguistic styles and error patterns.

**Data Type**: grammatical correction sentences

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- GECToR
- ScholarGEC

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating grammatical error correction systems under continual learning settings in the context of academic writing.

**Target Audience**:
- ML Researchers
- Academic Writers
- Natural Language Processing Practitioners

**Tasks**:
- Grammatical Error Correction

**Limitations**: N/A

## 💾 Data

**Source**: China National Knowledge Infrastructure (CNKI)

**Size**: 10,000 examples

**Format**: JSON

**Annotation**: Human annotation with the assistance of automatic grammatical error detection and language model pre-correction.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Sequential tuning
- Parameter-efficient adaptation

**Metrics**:
- Precision
- Recall
- F0.5 Score
- Backward Transfer (BWT)
- Average Task Performance (AvgPerf)

**Calculation**: Metrics are calculated using standard grammatical error correction scoring alongside continual learning metrics.

**Interpretation**: Average Task Performance shows overall competence, while backward transfer assesses retention of knowledge from previous tasks.

**Baseline Results**: Results benchmarked against naive sequential finetuning and various continual learning strategies like EWC, GEM, LwF, and OGD.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All personal, institutional, and document identifiers are redacted to comply with privacy regulations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
