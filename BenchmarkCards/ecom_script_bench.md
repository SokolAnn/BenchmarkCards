# ECOM SCRIPT BENCH

## 📊 Benchmark Details

**Name**: ECOM SCRIPT BENCH

**Overview**: ECOM SCRIPT BENCH is a multi-task benchmark for E-commerce script planning that includes 605,229 product-enriched scripts sourced from 2.4 million products, constructed to evaluate the capabilities of current language models in planning and product retrieval.

**Data Type**: text

**Domains**:
- Natural Language Processing
- E-commerce

**Languages**:
- English

**Similar Benchmarks**:
- IntentioQA

**Resources**:
- [Resource](https://arxiv.org/abs/2505.15196)

## 🎯 Purpose and Intended Users

**Goal**: To advance E-commerce capabilities through improved script planning by evaluating and enhancing LLMs' ability to generate product-enriched scripts.

**Target Audience**:
- ML Researchers
- Model Developers
- E-commerce Practitioners

**Tasks**:
- Script Verification
- Product Discrimination
- Script-Product Verification

**Limitations**: N/A

## 💾 Data

**Source**: Real-world E-commerce data obtained from Amazon product reviews and purchase data.

**Size**: 605,229 scripts with 5,928,271 steps and 2.4 million products.

**Format**: N/A

**Annotation**: Human annotations conducted via Amazon Mechanical Turk for gold label generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- AUC
- Macro-F1

**Calculation**: Metrics are calculated based on the predictions of various language models on test entries related to the tasks.

**Interpretation**: Higher scores indicate better performance in verifying scripts and identifying required products.

**Baseline Results**: Various baseline performance results across different models are presented, showing the challenges faced in E-commerce tasks.

**Validation**: Human verification through expert annotators and crowd-sourced workers on annotated labels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset construction process ensures the absence of offensive content and respects user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
