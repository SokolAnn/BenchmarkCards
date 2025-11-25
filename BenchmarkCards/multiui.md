# MultiUI

## 📊 Benchmark Details

**Name**: MultiUI

**Overview**: MultiUI is a dataset that synthesizes multimodal instructions from webpage UIs, containing 7.3 million samples from 1 million websites. It covers diverse multimodal tasks and UI layouts, enhancing models' performance in web UI tasks and generalizing to non-web UI tasks such as document understanding and chart interpretation.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VisualWebBench
- Mind2Web

**Resources**:
- [Resource](https://neulab.github.io/MultiUI/)

## 🎯 Purpose and Intended Users

**Goal**: To improve text-rich visual understanding in multimodal large language models by leveraging structured data from webpage UIs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- GUI Understanding
- Document Understanding
- OCR

**Limitations**: N/A

## 💾 Data

**Source**: 1 million websites scraped from the internet, utilizing accessibility trees and screenshots.

**Size**: 7.3 million samples

**Format**: N/A

**Annotation**: Automatically generated multimodal instructions paired with screenshots.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on model performance on various established benchmarks like VisualWebBench and Mind2Web.

**Interpretation**: Higher scores indicate improved model performance in understanding and interacting with text-rich environments.

**Baseline Results**: MultiUI-trained models achieved significant performance improvements over non-MultiUI baselines on various tasks.

**Validation**: Validated through comparison with established benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
