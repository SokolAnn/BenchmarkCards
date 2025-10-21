# SHIELD (Scalable Hardness-Informed Evaluation of LLM Detectors)

## 📊 Benchmark Details

**Name**: SHIELD (Scalable Hardness-Informed Evaluation of LLM Detectors)

**Overview**: SHIELD is a novel benchmark designed for the evaluation of AI text detectors, emphasizing reliability and stability across diverse scenarios while integrating hardness-aware evaluation methods.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BUST
- DetectRL
- ESPERANTO
- MAGE
- M4GT-Bench
- MGTBench
- RAID

**Resources**:
- [GitHub Repository](https://github.com/navid-aub/SHIELD-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To advance the fair evaluation of AI text detectors under realistic deployment scenarios by providing a comprehensive benchmark that measures detector performance and stability.

**Target Audience**:
- ML Researchers
- Detection System Engineers
- Model Developers

**Tasks**:
- Text Detection

**Limitations**: The evaluation was limited to monolingual English text analysis, thereby restricting the generalizability of findings to multilingual contexts.

## 💾 Data

**Source**: The SHIELD dataset contains human-written texts sourced from Medium articles, news articles, Amazon reviews, Reddit answers, arXiv abstracts, pink slime journalism, and Wikipedia, with corresponding LLM-generated texts produced across seven different models.

**Size**: 87.5k human-written texts and 612.5k LLM-generated texts

**Format**: Mixed (text formats)

**Annotation**: Dataset annotated with human-written samples before adversarial manipulation.

## 🔬 Methodology

**Methods**:
- Evaluation of text detectors
- Human evaluation
- Automated metrics

**Metrics**:
- AUROC (Area Under Receiver Operating Characteristic)
- W-AUROC (Weighted AUROC)
- SFD (Stability under False Positive Deviation)
- URSS (Unified Reliability-Stability Score)

**Calculation**: Metrics are calculated using performance measurements in low false positive rate regions and stability assessments across varying threshold conditions.

**Interpretation**: Compares the reliability and stability of detection methods under real-world operational conditions.

**Baseline Results**: Traditional benchmarks for LLM-generated text detection, focusing on AUROC metrics which may overestimate efficacy.

**Validation**: Evaluation is performed through rigorous comparative analysis against contemporary benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Decision bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The benchmark does not currently include demographic breakdowns or fairness assessments across groups as evaluated.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
