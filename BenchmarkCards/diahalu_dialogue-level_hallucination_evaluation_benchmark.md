# DiaHalu (Dialogue-level Hallucination Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: DiaHalu (Dialogue-level Hallucination Evaluation Benchmark)

**Overview**: DiaHalu is the first dedicated dialogue-level hallucination evaluation benchmark for large language models, covering four common multi-turn dialogue domains and encompassing five hallucination subtypes, namely, factuality and faithfulness hallucinations.

**Data Type**: multi-turn dialogue

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FactCollect
- HADES
- BEGIN
- FactCHD
- HaluEval
- WikiBio+

**Resources**:
- [GitHub Repository](https://github.com/ECNU-ICALK/DiaHalu)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark and assess the effectiveness of hallucination detection in large language models during multi-turn dialogues.

**Target Audience**:
- ML Researchers
- Model Developers
- Academia
- Industry Practitioners

**Tasks**:
- Hallucination Detection

**Limitations**: N/A

## 💾 Data

**Source**: Generated dialogues combining topics from multiple datasets, e.g., TruthfulQA, MultiWOZ, and mathematical problem datasets.

**Size**: 1,103 dialogue samples

**Format**: JSON

**Annotation**: Manually annotated by expert scholars

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Binary classification for hallucination detection, detailed classification for hallucination types using micro-F1 score.

**Interpretation**: Higher F1 scores represent better accuracy in detecting hallucination types.

**Baseline Results**: Existing LLMs showed varying levels of success in hallucination detection; none exceeded 50% F1 score on average.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
