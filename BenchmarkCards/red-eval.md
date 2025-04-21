# RED-EVAL

## 📊 Benchmark Details

**Name**: RED-EVAL

**Overview**: A new safety evaluation benchmark that conducts red-teaming using Chain of Utterances (CoU) prompting, demonstrating the ineffective guardrails in LLMs leading to harmful outputs.

**Data Type**: Conversational Dataset

**Domains**:
- Natural Language Processing
- AI Safety
- Ethical AI

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- MMLU
- HHH

**Resources**:
- [GitHub Repository](https://github.com/declare-lab/red-instruct)
- [Resource](https://huggingface.co/datasets/declare-lab/HarmfulQA)
- [Resource](https://huggingface.co/declare-lab/starling-7B)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety and ethical alignment of large language models and improve their robustness against harmful queries.

**Target Audience**:
- Researchers
- Developers
- AI ethicists

**Tasks**:
- Safety evaluation of LLMs
- Compare effectiveness of LLMs against harmful inputs
- Establish safety benchmarks

**Limitations**: Focused primarily on harmful questions and responses; may not cover all ethical dimensions.

**Out of Scope Uses**:
- General AI assistant tasks
- Non-harmful query evaluations

## 💾 Data

**Source**: HARMFUL QA data collection via Chain of Utterances prompting

**Size**: 1,960 harmful questions, 9,536 safe conversations, and 7,356 harmful conversations

**Format**: Text

**Annotation**: Conversations labeled for safety and harmfulness based on responses

## 🔬 Methodology

**Methods**:
- Chain of Utterances prompting
- Dataset collection from harmful and safe responses
- Safety alignment through fine-tuning

**Metrics**:
- Attack Success Rate (ASR)
- Helpful, Honest, Harmless (HHH) scores

**Calculation**: ASR calculated as the ratio of successful harmful responses to total harmful queries.

**Interpretation**: Higher ASR indicates less effective safety measures in LLMs.

**Baseline Results**: STARLING demonstrates improved safety compared to traditional methods.

**Validation**: Validation performed using the HHH and other safety-related benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety risks in LLMs
- Ethical concerns in AI deployment
- Harmful outputs generation

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Protecting user data and responses during evaluations.

**Data Licensing**: Dataset usage aligns with licensing agreements of Hugging Face datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
