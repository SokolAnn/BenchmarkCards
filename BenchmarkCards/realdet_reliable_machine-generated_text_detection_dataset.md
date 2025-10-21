# RealDet (Reliable Machine-Generated Text Detection Dataset)

## 📊 Benchmark Details

**Name**: RealDet (Reliable Machine-Generated Text Detection Dataset)

**Overview**: RealDet is a high-quality benchmark dataset designed for machine-generated text detection, covering 15 diverse domains and constructed using 22 powerful language models. It provides extensive data for calibrating detection systems and evaluating their robustness against adversarial attacks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- TuringBench
- HC3
- RAID
- M4
- MAGE

**Resources**:
- [Resource](https://arxiv.org/abs/2505.05084)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for machine-generated text detection research that ensures realistic calibration and enhances the performance of detection frameworks.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Text Classification

**Limitations**: RealDet dataset may still exhibit some inherent biases due to the nature of the sources it encompasses.

## 💾 Data

**Source**: Constructed from 15 representative data sources across various writing tasks including question answering, news writing, and academic writing.

**Size**: 847,909 texts

**Format**: Raw text files

**Annotation**: Generated from a mix of human-written and machine-generated sources, ensuring diversity and domain coverage.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- False Positive Rate (FPR)
- True Positive Rate (TPR)
- F1 Score

**Calculation**: Metrics are calculated by comparing the predictions of detectors on the test datasets against the known labels of the texts.

**Interpretation**: High TPR and low FPR are desired to indicate effective detection performance.

**Validation**: Extensive empirical evaluations demonstrate that the MCP framework effectively constrains FPRs and improves detection performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: Data includes diverse age groups, but specifics depend on sampling methods.

**Potential Harm**: ['Potential risks of misclassification leading to societal harm.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
