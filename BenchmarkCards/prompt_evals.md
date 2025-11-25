# PROMPT EVALS

## 📊 Benchmark Details

**Name**: PROMPT EVALS

**Overview**: PROMPT EVALS is a dataset of 2087 human-contributed prompt templates and 12623 assertion criteria, designed to improve the reliability of large language model (LLM) outputs in production environments.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance
- Marketing
- E-commerce
- Education
- Healthcare
- IT and Programming

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://huggingface.co/datasets/reyavir/PromptEvals)
- [Resource](https://huggingface.co/reyavir/promptevals_mistral)
- [Resource](https://huggingface.co/reyavir/promptevals_llama)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating LLM-generated assertion criteria in various application contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Assertion Generation
- Prompt Engineering
- Evaluation of LLM Outputs

**Limitations**: N/A

## 💾 Data

**Source**: Human-contributed LLM prompt templates and their assertion criteria derived from an open-source LLM pipeline.

**Size**: 2,087 prompt templates, 12,623 assertion criteria

**Format**: JSON

**Annotation**: Generated through a three-step process involving initial criteria generation using LLMs, manual review for missed criteria, and final refinement.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Semantic F1
- Number of criteria

**Calculation**: Calculating Semantic F1 involves comparing the semantic similarity between predicted and ground truth criteria using cosine similarity over vector representations.

**Interpretation**: A higher Semantic F1 indicates better performance in generating relevant assertion criteria.

**Baseline Results**: GTP-4o scores considered as baseline; fine-tuned models outperform it by significant percentages.

**Validation**: Validating generated assertion criteria against ground truth using metrics defined in the evaluation section.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Developers contributing prompts were not required to provide personally identifiable information (PII).

**Data Licensing**: Open-source; licensed under terms as specified in Hugging Face model card.

**Consent Procedures**: Developers consented to share their prompts and can request deletion.

**Compliance With Regulations**: Not Applicable
