# OR-Bench

## 📊 Benchmark Details

**Name**: OR-Bench

**Overview**: OR-Bench is the first large-scale over-refusal benchmark designed to evaluate the performance of large language models (LLMs) in rejecting innocuous prompts that seem toxic.

**Data Type**: Text

**Domains**:
- Text Generation
- Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToxicChat
- PromptBench
- AdvBench

**Resources**:
- [Resource](https://huggingface.co/datasets/bench-llm/or-bench)
- [Resource](https://huggingface.co/spaces/bench-llm/or-bench)

## 🎯 Purpose and Intended Users

**Goal**: To develop better safety-aligned large language models by assessing their over-refusal rates.

**Target Audience**:
- Researchers
- AI Safety Engineers
- Developers of Large Language Models

**Tasks**:
- Evaluate model performance on seemingly toxic prompts
- Analyze safety alignment of LLMs
- Identify over-refusal trends in LLM outputs

**Limitations**: The dataset may include toxic prompts that were not identified correctly by moderators.

**Out of Scope Uses**:
- General usage without safety evaluation
- Applications in non-LLM models

## 💾 Data

**Source**: Generated and curated using a systematic framework for prompt generation

**Size**: 80,000 seemingly toxic prompts alongside 1,000 hard prompts and 600 toxic prompts

**Format**: Text

**Annotation**: Prompts are moderated by ensembles of large language models to classify toxicity.

## 🔬 Methodology

**Methods**:
- Automated prompt generation
- LLM moderation for toxicity assessment
- Collection of rejection data across multiple model families

**Metrics**:
- Rejection Rate of seemingly toxic prompts
- Safety and helpfulness balance metrics

**Calculation**: Rejection rates calculated based on model responses to the benchmark prompts.

**Interpretation**: Higher rejection rates indicate more over-refusal behavior in LLMs.

**Baseline Results**: N/A

**Validation**: Evaluation results of 25 LLMs showed significant insights into over-refusal rates and safety alignment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Model safety
- Over-refusal
- Rejection of non-harmful prompts

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: The over-refusal of innocuous prompts can lead to reduced model utility in practical applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
