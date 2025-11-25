# Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs

## 📊 Benchmark Details

**Name**: Quality Matters: Evaluating Synthetic Data for Tool-Using LLMs

**Overview**: This paper proposes two approaches for assessing the reliability of data for training LLMs to use external tools, including intrinsic quality evaluation criteria and in-context evaluation metrics (ICE). The findings indicate that models trained on high-quality data significantly outperform those trained on unvalidated data, highlighting the importance of data quality in model performance for tool-using LLMs.

**Data Type**: instruction and API call sequences

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolBench
- ToolAlpaca

**Resources**:
- [Resource](https://arxiv.org/abs/2409.16341)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the quality of synthetic data for tool-using LLMs and demonstrate its impact on model performance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Tool Usage Evaluation
- Data Quality Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Datasets synthesized for training tool-using LLMs, specifically ToolBench and ToolAlpaca.

**Size**: 125,000 examples for ToolBench, 4,200 examples for ToolAlpaca

**Format**: JSON

**Annotation**: Manually annotated by researchers according to intrinsic quality criteria.

## 🔬 Methodology

**Methods**:
- Intrinsically Evaluated Data Quality
- In-Context Evaluation

**Metrics**:
- Pass Rate
- ICE Score

**Calculation**: Metrics are calculated based on the proportion of instances that the model successfully addressed according to the intrinsic evaluation criteria.

**Interpretation**: A higher pass rate and ICE score indicate better data quality and improved model performance.

**Baseline Results**: Models trained on high-quality subsets consistently performed better than those trained on full datasets with low-quality data.

**Validation**: Evaluation results validate the effectiveness of the proposed data quality metrics against human annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Quality
- Model Performance

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
