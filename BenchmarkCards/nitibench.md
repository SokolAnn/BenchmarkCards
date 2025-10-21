# NitiBench

## 📊 Benchmark Details

**Name**: NitiBench

**Overview**: NitiBench is a benchmark dataset specifically designed for evaluating Thai legal question answering systems, consisting of two datasets: NitiBench-CCL covering general Thai financial law and NitiBench-Tax focusing on real-world tax law cases. The benchmark measures retrieval and end-to-end performance with customized metrics suited for legal queries.

**Data Type**: question-answering pairs

**Domains**:
- Legal

**Languages**:
- Thai

**Similar Benchmarks**:
- LexGLUE
- LegalBench

**Resources**:
- [Resource](https://huggingface.co/datasets/VISAI-AI/nitibench)
- [GitHub Repository](https://github.com/vistec-ai/nitibench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation framework for Thai legal question answering systems, addressing the lack of benchmarks in this domain.

**Target Audience**:
- Legal AI Researchers
- Legal Practitioners
- NLP Researchers

**Tasks**:
- Legal Question Answering

**Limitations**: The dataset may exhibit ambiguous queries due to its construction process, impacting model evaluation.

## 💾 Data

**Source**: Constructed from Thai financial law codes and real-world tax law cases, with annotations by legal experts.

**Size**: 3,730 entries (NitiBench-CCL); 50 cases (NitiBench-Tax)

**Format**: JSON

**Annotation**: Curated by legal experts with a combination of manual and semi-automated methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Multi-Hit Rate
- Mean Reciprocal Rank (MRR)
- E2E Recall
- Coverage
- Contradiction

**Calculation**: Metrics are computed based on the performance of the QA systems in retrieving and generating correct legal responses.

**Interpretation**: High scores indicate better retrieval performance and greater alignment between generated answers and ground truth.

**Baseline Results**: Human-Finetuned BGE-M3 shows the best performance compared to other models evaluated.

**Validation**: Results validated against benchmarks and peer-reviewed metrics for legal question answering.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias

**Demographic Analysis**: Future evaluations may consider demographic factors in query construction and performance metrics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensure that personally identifiable information from tax cases is anonymized.

**Data Licensing**: Open-sourced under a standard dataset license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
