# STORM (Stimulating Trustworthy Ordinal Regression Ability of MLLMs for Universal Visual Rating)

## 📊 Benchmark Details

**Name**: STORM (Stimulating Trustworthy Ordinal Regression Ability of MLLMs for Universal Visual Rating)

**Overview**: STORM is a benchmark for evaluating multi-modal large language models on visual rating tasks. It includes 655K image-level pairs and QAs across 14 ordinal regression datasets in five visual rating domains.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://storm-bench.github.io/)
- [GitHub Repository](https://github.com/aTongs1/STORM)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the all-in-one and zero-shot performance of MLLMs in visual rating tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Image Quality Assessment
- Image Aesthetic Assessment
- Facial Age Estimation
- Medical Disease Grading
- Historical Date Estimation

**Limitations**: The definitions of labels for different domain tasks are diverse, impacting performance consistency.

## 💾 Data

**Source**: 14 ordinal regression datasets across five visual rating domains.

**Size**: 655,000 examples

**Format**: JSON

**Annotation**: Annotated via a mixture of expert annotation and automated processes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Mean Absolute Error (MAE)

**Calculation**: Metrics are calculated based on predictions compared to ground truth ratings for visual content.

**Interpretation**: Higher accuracy and lower MAE indicate better visual rating performance.

**Validation**: The benchmark employs official training/testing splits when available and uses random splits otherwise.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was collected for research purposes, ensuring no personally identifiable information is included.

**Data Licensing**: CC BY 4.0 license for data, Apache-2.0 license for code.

**Consent Procedures**: The dataset was created with appropriate consent procedures as described in Appendix H.

**Compliance With Regulations**: Not Applicable
