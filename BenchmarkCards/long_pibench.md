# LONG PIBENCH

## 📊 Benchmark Details

**Name**: LONG PIBENCH

**Overview**: LONG PIBENCH is a benchmark designed to evaluate positional bias with multiple relevant information pieces in long-context large language models (LLMs). It assesses positional bias in both absolute and relative positions, including diverse tasks across different complexities and input lengths.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Long Range Arena
- Scrolls
- ZeroScrolls
- Longbench
- L-Eval
- LV-Eval
- Counting-Stars
- ∞Bench

**Resources**:
- [Resource](https://arxiv.org/abs/2410.14641)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate positional bias in long-context large language models (LLMs) involving multiple relevant pieces of information.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Table SQL
- Code Completion
- Wiki Retrieval

**Limitations**: The findings are limited to the nine popular models evaluated and do not account for the performance of other emerging or less popular models.

## 💾 Data

**Source**: Manually annotated seed data and augmented by varying the positions of relevant information.

**Size**: 7,040 instances

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Recall rate
- Pass rate

**Calculation**: The recall rate is measured as the proportion of relevant items included in the output. The pass rate is computed based on successful completion of coding tasks across multiple test cases.

**Interpretation**: Performance ranges from 0.0 (complete failure) to 1.0 (perfect performance).

**Baseline Results**: Comparison to nine popular LLMs including Gemini-1.5-Flash, Claude-3.5-Haiku, and multiple variants from the Qwen family.

**Validation**: Performance evaluated using standardized inference parameters across all models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection protocol was approved, and human annotation was carried out by authors with substantial knowledge in LLM evaluation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent was obtained from individuals whose data is being used or curated.

**Compliance With Regulations**: Not Applicable
