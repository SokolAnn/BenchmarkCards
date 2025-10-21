# ONEBench (OpeN-Ended Benchmarking)

## 📊 Benchmark Details

**Name**: ONEBench (OpeN-Ended Benchmarking)

**Overview**: ONEBench is a new paradigm that consolidates individual evaluation datasets into a unified, ever-expanding sample pool. It enables custom benchmarks for specific capabilities while reusing and aggregating samples, mitigating overfitting and dataset bias for broader capability assessment.

**Data Type**: sample-level evaluations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- BigBench
- HELM
- VHELM

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate models using a continuously expanding pool of test data samples drawn from multiple benchmarks and to provide a democratized, customizable evaluation framework.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Model Evaluation
- Dynamic Capability Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Data sourced from multiple evaluation datasets including HELM, LMMs-Eval, and open source contributions.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Sample-level aggregation
- Dynamic querying
- Ordinal rankings

**Metrics**:
- Kendall's Tau

**Calculation**: Rankings are obtained through Plackett-Luce model aggregation.

**Interpretation**: Higher rankings indicate better model performance on retrieval tasks.

**Baseline Results**: N/A

**Validation**: Empirical validation shows high correlation with ground-truth rankings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Transparency

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
