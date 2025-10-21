# P-FOLIO

## 📊 Benchmark Details

**Name**: P-FOLIO

**Overview**: P-FOLIO is a human-annotated dataset consisting of diverse and complex reasoning chains for a set of realistic logical reasoning stories, written by humans, collected using a structured annotation protocol.

**Data Type**: natural language proofs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FOLIO

**Resources**:
- [Resource](https://arxiv.org/abs/2410.09207)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve large-language-model (LLM) reasoning capabilities using expert-written proof chains.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Single-step Inference Rule Classification
- Single-step Derivation Reasoning
- Proof Generation

**Limitations**: N/A

## 💾 Data

**Source**: Expert-written logical reasoning for an existing dataset of logical reasoning, FOLIO.

**Size**: 1,430 proofs

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Pass@k

**Calculation**: Metrics calculated using various evaluations including overlap and quality of model-generated reasoning chains compared to human-annotated chains.

**Interpretation**: Higher pass@k values indicate better alignment with human reasoning chains.

**Baseline Results**: N/A

**Validation**: Cross-checking of annotated proofs by multiple annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
