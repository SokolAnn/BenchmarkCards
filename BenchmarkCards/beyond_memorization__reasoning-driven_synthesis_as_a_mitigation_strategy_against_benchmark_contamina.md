# Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination

## 📊 Benchmark Details

**Name**: Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination

**Overview**: The paper presents a contamination-resistant evaluation framework that synthesizes multi-step reasoning questions from arXiv papers to effectively mitigate issues of data contamination in language model evaluations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Mathematics
- Physics

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GPQA
- Frontier-Math

**Resources**:
- [GitHub Repository](https://github.com/TerryJCZhang/BeyondMemorization)

## 🎯 Purpose and Intended Users

**Goal**: To develop an evaluation framework that synthesizes high-quality reasoning-driven questions and addresses the issue of benchmark contamination.

**Target Audience**:
- ML Researchers
- Model Developers
- Academics

**Tasks**:
- Question Answering

**Limitations**: The QA synthesis pipeline may have limitations in question diversity and complexity due to its focus on theorem-based questions.

## 💾 Data

**Source**: Synthesized from 20,277 arXiv papers

**Size**: 1,643 questions

**Format**: JSON

**Annotation**: Automated verification and manual review for quality assurance

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Performance is evaluated based on stability in model capabilities across knowledge cutoffs.

**Interpretation**: Stable performance indicates contamination resistance, implying genuine reasoning capabilities.

**Validation**: Comparative analysis with longitudinal studies reported significant performance decay using retrieval-based benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
