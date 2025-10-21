# XL-AlpacaEval

## 📊 Benchmark Details

**Name**: XL-AlpacaEval

**Overview**: XL-AlpacaEval is a cross-lingual evaluation benchmark built to assess the performance of large language models in the task of cross-lingual open-ended generation. It evaluates whether models can generate coherent responses in a target language different from the one in which the query is posed.

**Data Type**: cross-lingual generation prompts

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- Portuguese
- Hungarian
- Lithuanian
- Irish
- Chinese
- Hindi

**Resources**:
- [Resource](https://huggingface.co/collections/viyer98/xl-suite-68ceb97cb1cc7e8499ffb971)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the current state of cross-lingual open-ended generation capabilities of large language models and to provide a structured benchmark for improvement.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Cross-Lingual Generation
- Open-End Generation

**Limitations**: N/A

## 💾 Data

**Source**: XL-AlpacaEval is adapted from the original AlpacaEval dataset, which consists of multi-domain prompts filtered for suitability in cross-lingual contexts.

**Size**: 797 prompts

**Format**: JSON

**Annotation**: Manually verified and filtered prompts to ensure they are suitable for eliciting cross-lingual responses.

## 🔬 Methodology

**Methods**:
- LLM-as-a-judge evaluation

**Metrics**:
- Win Rate

**Calculation**: Win rates are determined by comparing model outputs against a baseline reference model.

**Interpretation**: Higher win rates indicate better performance in generating responses that humans prefer over baseline responses.

**Baseline Results**: Win rates against GPT-4o-mini across multiple languages.

**Validation**: Live evaluation using multiple reference models and feedback from human evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0 for XL-AlpacaEval; XL-Instruct derived from CulturaX with permissible licenses for commercial use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
