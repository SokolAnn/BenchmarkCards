# ELABORATION

## 📊 Benchmark Details

**Name**: ELABORATION

**Overview**: ELABORATION is a novel benchmark for human-LLM competitive programming, featuring a comprehensive evaluation protocol and a human-LLM programming dataset that enables fine-grained assessment of collaborative effectiveness and identifies strengths and weaknesses of existing methods.

**Data Type**: programming problems

**Domains**:
- Computer Science Education

**Languages**:
- English

**Similar Benchmarks**:
- APPS
- CODE-CONTESTS
- XCODEEVAL
- CODESCOPE
- KareCoder

**Resources**:
- [GitHub Repository](https://github.com/SCUNLP/ELABORATION)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate a thorough assessment of human-LLM collaboration in competitive programming tasks using a structured evaluation protocol and dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Computer Science Educators

**Tasks**:
- Code Generation
- Code Debugging
- Human-LLM Interaction

**Limitations**: N/A

## 💾 Data

**Source**: The dataset comprises 8,320 problems from Codeforces and AtCoder.

**Size**: 8,320 problems

**Format**: N/A

**Annotation**: Problems are meticulously annotated for human interaction, generating feedback and facilitating efficient assessment of interactive tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pass@1
- Pass@3
- Pass@5

**Calculation**: Metrics are calculated based on the performance of human-LLM collaboration throughout the competitive programming task.

**Interpretation**: Higher Pass@k scores indicate better performance of human-LLM collaboration in solving programming challenges.

**Baseline Results**: N/A

**Validation**: The benchmark was validated via extensive human evaluations and performance tests against multiple LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sourced from publicly available competitive programming sites, ensuring no personal identifiable information is included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants were informed of the study's purpose and usage of data.

**Compliance With Regulations**: Not Applicable
