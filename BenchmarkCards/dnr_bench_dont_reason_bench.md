# DNR Bench (Don't Reason Bench)

## 📊 Benchmark Details

**Name**: DNR Bench (Don't Reason Bench)

**Overview**: DNR Bench is a novel benchmark designed to evaluate LLMs' ability to robustly understand tricky reasoning triggers and avoid unnecessary generation, consisting of 150 adversarially designed prompts focusing on instruction adherence, hallucination avoidance, redundancy filtering, and unanswerable question recognition.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AIME
- GPQA
- GSM8K
- MATH

**Resources**:
- [Resource](https://arxiv.org/abs/2503.15793)

## 🎯 Purpose and Intended Users

**Goal**: To expose vulnerabilities in current reasoning LLMs related to over-reasoning and their efficiency in generating appropriate responses.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually designed prompts and generated using OpenAI GPT-4o with manual reviews ensuring alignment with evaluation goals.

**Size**: 150 examples

**Format**: N/A

**Annotation**: Manually reviewed to ensure alignment with intended evaluation goals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Token Efficiency

**Calculation**: Accuracy is determined based on the category-specific judgment criteria defined for each prompt, while token efficiency quantifies how many tokens the model generates versus a baseline model (GPT-4o).

**Interpretation**: Higher accuracy with fewer generated tokens indicates a more efficient model performance, while overflow in token generation suggests over-reasoning.

**Baseline Results**: OpenAI-GPT-4o serves as the baseline model.

**Validation**: Responses validated through comparisons with human responses and through structured evaluation by team members.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misleading outputs from LLMs when faced with ambiguous prompts.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
