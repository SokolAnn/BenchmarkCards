# FACTBENCH

## 📊 Benchmark Details

**Name**: FACTBENCH

**Overview**: FACTBENCH is designed to be an updatable benchmark grounded in real-world usage of language models, focused on evaluating their factuality and identifying hallucination prompts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- FELM
- ExpertQA
- FactScore

**Resources**:
- [Resource](https://huggingface.co/spaces/launch/factbench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of FACTBENCH is to provide a dynamic benchmark for evaluating the factuality of language models in real-world scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Factuality Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Developed from a dataset of language model interactions (LMSYS-Chat-1M) featuring prompts that elicit hallucinations in language models.

**Size**: 1,000 prompts

**Format**: N/A

**Annotation**: Human-annotated factuality labels on 4,467 content units.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Factual precision
- Hallucination score

**Calculation**: The factual precision is calculated as the proportion of supported units among all extracted units across responses.

**Interpretation**: Higher factual precision indicates better performance in generating factual outputs.

**Baseline Results**: Various LM models evaluated against FACTBENCH, including GPT4-o, Gemini1.5-Pro, and two Llama models.

**Validation**: Prompts categorized into three tiers (Hard, Moderate, Easy) based on their challenge level.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
