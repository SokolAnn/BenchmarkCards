# Dialogue Summarization with LLMs: Circumstantial Inference Trends

## 📊 Benchmark Details

**Name**: Dialogue Summarization with LLMs: Circumstantial Inference Trends

**Overview**: This benchmark evaluates the faithfulness of LLMs (GPT-4 and Alpaca-13B) in dialogue summarization, focusing on identifying and categorizing circumstantial inconsistencies.

**Data Type**: Dialogue Summarization

**Domains**:
- Dialogue

**Languages**:
- English

**Similar Benchmarks**:
- RefMatters
- FacEval

**Resources**:
- [GitHub Repository](https://github.com/sanjanaramprasad/circumstantial_inference.git)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the effectiveness of large language models in dialogue summarization and identify specific types of errors resulting from their generation.

**Target Audience**:
- Research community
- AI practitioners

**Tasks**:
- Error categorization
- Model evaluation

**Limitations**: Limited to two LLMs, which may not represent all LLM behaviors.

**Out of Scope Uses**:
- Real-time applications
- Non-dialogue summarization tasks

## 💾 Data

**Source**: SAMSum and DialogSum datasets

**Size**: N/A

**Format**: Text

**Annotation**: Human annotations identifying inconsistent spans based on dialogue summaries.

## 🔬 Methodology

**Methods**:
- Human annotations
- Error categorization taxonomy

**Metrics**:
- Factual consistency
- Error rate analysis

**Calculation**: Comparison of human annotations against model-generated summaries to identify inconsistencies.

**Interpretation**: LLMs exhibit unique error patterns compared to fine-tuned models, particularly with circumstantial inferences.

**Baseline Results**: 23% inconsistency in GPT-4 summaries, 38% errors classified as circumstantial inference.

**Validation**: Inter-annotator agreement was 66.94% using F-1 metric.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential introduction of misinformation through circumstantial inferences.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
