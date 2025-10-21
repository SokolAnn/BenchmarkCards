# IberBench

## 📊 Benchmark Details

**Name**: IberBench

**Overview**: IberBench is a comprehensive benchmark designed to assess LLM performance on both fundamental and industry-relevant NLP tasks in languages spoken across the Iberian Peninsula and Ibero-America, integrating 101 datasets from evaluation campaigns and recent benchmarks, covering 22 task categories.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish
- Portuguese
- Catalan
- Basque
- Galician
- English

**Similar Benchmarks**:
- GLUE
- MMLU
- HELM

**Resources**:
- [Resource](https://huggingface.co/spaces/iberbench/leaderboard)
- [Resource](https://huggingface.co/iberbench)
- [GitHub Repository](https://github.com/IberBench/iberbench-evaluation/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of IberBench is to enable continuous evaluation of LLMs across fundamental and industry-relevant tasks in Iberian languages, addressing the underrepresentation and static nature of existing evaluation benchmarks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Sentiment Analysis
- Emotion Detection
- Toxicity Detection
- Intent Classification
- Question Answering
- Text Summarization
- Author Profiling

**Limitations**: IberBench is constrained to the data that is available from these sources under a permissive license. The benchmark does not cover some language varieties with a large number of speakers.

## 💾 Data

**Source**: IberBench comprises 101 datasets sourced from workshops like IberLEF, IberEval, and TASS, along with recent benchmarks designed to assess LLMs on fundamental and industry-relevant tasks.

**Size**: 333,000 examples

**Format**: N/A

**Annotation**: Datasets were collected and standardized for LLM evaluation, ensuring appropriate labeling and consistency across tasks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Macro F1 Score
- ROUGE-1

**Calculation**: Metrics are calculated based on the predicted outputs compared to reference outputs, with evaluation performed using a comprehensive evaluation suite integrated into IberBench.

**Interpretation**: Performance metrics reflect the model's ability to generate language and perform tasks relative to random baselines and existing shared-task submissions.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Datasets may contain biases, and the evaluation may be influenced by language characteristics and available resources.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Datasets are included with appropriate permissions and are maintained under controlled access to prevent leakage.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
