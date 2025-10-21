# TRIGO

## 📊 Benchmark Details

**Name**: TRIGO

**Overview**: TRIGO is an ATP benchmark that evaluates the reasoning ability of generative language models on trigonometric expression reduction with manual annotations and generated datasets.

**Data Type**: trigonometric expression reduction problems

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- LeanStep
- IsarStep
- MiniF2F
- FIMO
- Geometry3K

**Resources**:
- [GitHub Repository](https://github.com/menik1126/TRIGO)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the generative language models' reasoning capabilities in formal mathematical theorem proving involving trigonometric expressions.

**Target Audience**:
- ML Researchers
- Model Developers
- Mathematicians

**Tasks**:
- Automated Theorem Proving

**Limitations**: N/A

## 💾 Data

**Source**: Collected from high school exercises and exams, other educational websites, and supplemented by automatic generation methods.

**Size**: 427 problems in TRIGO-real, 459 problems in TRIGO-web, 27,000 generated samples in TRIGO-gen.

**Format**: N/A

**Annotation**: Manual annotation of the simplification process using an interactive software tool.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass rate

**Calculation**: Metrics calculated based on the number of proofs that correctly output a valid solution within given constraints.

**Interpretation**: Higher pass rates indicate better model performance on understanding and manipulating mathematical expressions.

**Validation**: The TRIGO dataset was validated through manual proof verification using the Lean system.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential spread of misinformation if models learn incorrect proofs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from open educational resources; no private personal data was used.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
