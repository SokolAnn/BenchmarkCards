# DARKBENCH

## 📊 Benchmark Details

**Name**: DARKBENCH

**Overview**: We introduce DarkBench, a comprehensive benchmark for detecting dark design patterns—manipulative techniques that influence user behavior—in interactions with large language models (LLMs). Our benchmark comprises 660 prompts across six categories: brand bias, user retention, sycophancy, anthropomorphism, harmful generation, and sneaking.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- TruthfulQA

**Resources**:
- [Resource](https://huggingface.co/datasets/anonymous152311/darkbench)

## 🎯 Purpose and Intended Users

**Goal**: To empirically measure the presence of dark patterns in LLMs and provide a standardized framework for evaluation.

**Target Audience**:
- Researchers
- Ethics Analysts
- Model Developers

**Tasks**:
- Detection of Dark Patterns

**Limitations**: The dark patterns in DarkBench are derived primarily from an analysis of the incentives arising from the chatbot subscription-based business model. We do not claim full coverage of all the motivations facing an LLM developer.

## 💾 Data

**Source**: Generated prompts specific to the six categories of dark patterns.

**Size**: 660 prompts

**Format**: N/A

**Annotation**: Annotated using a combination of human annotators and LLM models.

## 🔬 Methodology

**Methods**:
- LLM-augmented generation
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy of dark pattern detection

**Calculation**: Results are calculated based on the incidence of dark patterns in the responses of the evaluated models to the prompts.

**Interpretation**: Responses indicating the presence of defined dark patterns are evaluated against the benchmark for accuracy.

**Baseline Results**: Average occurrence of dark pattern instances varies across models, with specific detection rates outlined for each of the six categories.

**Validation**: Evaluated against a set of 14 models with results cross-validated by multiple annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Ethics
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on Jobs, Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Manipulative behavior influencing user decisions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
