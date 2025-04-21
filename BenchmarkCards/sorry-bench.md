# SORRY-Bench

## 📊 Benchmark Details

**Name**: SORRY-Bench

**Overview**: SORRY-Bench is designed to systematically evaluate large language models' (LLMs) safety refusal capabilities in response to unsafe user requests. It addresses limitations in previous benchmarks by employing a fine-grained taxonomy of potentially unsafe topics.

**Data Type**: Unsafe instructions

**Domains**:
- Hate Speech Generation
- Assistance with Crimes or Torts
- Potentially Inappropriate Topics
- Potentially Unqualified Advice

**Languages**:
- English
- French
- Tamil
- Malayalam
- Marathi
- Chinese (Simplified)

**Similar Benchmarks**:
- HarmBench
- SALAD-Bench
- StrongREJECT

**Resources**:
- [Resource](https://sorry-bench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety refusal capabilities of aligned large language models in a balanced and comprehensive manner.

**Target Audience**:
- Researchers
- Developers of AI models

**Tasks**:
- Evaluate model responses to potentially unsafe instructions
- Analyze safety refusal behaviors across different models

**Limitations**: Focused exclusively on refusal safety evaluation and does not capture all dimensions of model safety.

**Out of Scope Uses**:
- Evaluation of non-unsafe instructions
- Detection of neutral prompts

## 💾 Data

**Source**: SORRY-Bench dataset

**Size**: 440 unsafe instructions with an additional 8.8K augmented unsafe instructions

**Format**: Textual instructions categorized into 44 safety topics

**Annotation**: Human-annotated with over 7K labels for model responses

## 🔬 Methodology

**Methods**:
- Meta-evaluation of LLMs as judges
- Human judgment comparisons

**Metrics**:
- Fulfillment rate
- Safety refusal agreement with human judges

**Calculation**: Fulfillment rate calculated as the ratio of model responses fulfilling unsafe instructions over total responses.

**Interpretation**: High fulfillment rates indicate lower safety refusal; low fulfillment rates indicate higher safety refusal.

**Baseline Results**: 27 out of 56 LLMs show medium fulfillment rate of 20% to 50%.

**Validation**: Meta-evaluated numerous LLMs and collected extensive human annotations to validate the benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety refusal behaviors
- Potential misuse of safety evaluation results

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Transparency**: Lack of training data transparency
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential risk of misuse in deploying LLMs evaluated in the benchmark.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Collected data contains sensitive information and requires handling to mitigate privacy risks.

**Data Licensing**: The dataset and models are available under appropriate licenses on specified hosting platforms.

**Consent Procedures**: Informed consent obtained for all human annotations.

**Compliance With Regulations**: Ensures adherence to applicable data protection laws.
