# DACTYL (Diverse Adversarial Corpus of Texts Yielded from Language models)

## 📊 Benchmark Details

**Name**: DACTYL (Diverse Adversarial Corpus of Texts Yielded from Language models)

**Overview**: DACTYL is a challenging AIG text detection dataset focusing on one-shot/few-shot generations across six domains, created to improve robustness in AIG text detectors.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Social Media
- E-commerce
- Academic Publishing
- News Media
- Education

**Languages**:
- English

**Similar Benchmarks**:
- MAGE
- RAID

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To address vulnerabilities in existing AIG text detectors and provide a dataset that facilitates better detection performance in real-world scenarios.

**Target Audience**:
- AI Researchers
- Machine Learning Practitioners
- Developers of Text Detection Systems

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Generated using eleven large language models across six vulnerable domains.

**Size**: 458,325 examples

**Format**: text

**Annotation**: Automatically generated and validated using existing human-written texts.

## 🔬 Methodology

**Methods**:
- Deep X-risk Optimization
- Binary Cross-Entropy Optimization

**Metrics**:
- tpAUC (Two-way Partial Area Under the Curve)
- pAUC (Partial Area Under the Curve)
- AUC (Area Under the Curve)
- AP (Average Precision)

**Calculation**: Metrics calculated based on classifier predictions of AIG-generated texts versus human-written texts.

**Interpretation**: Higher scores indicate better classification performance in distinguishing AIG texts from human texts.

**Baseline Results**: DACTYL-trained classifiers performed better than existing detectors, improving generalization on out-of-distribution datasets.

**Validation**: Evaluated on various AIG text detection datasets and through simulated deployment scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
