# CRITIC EVAL

## 📊 Benchmark Details

**Name**: CRITIC EVAL

**Overview**: CRITIC EVAL is a novel benchmark designed to comprehensively and reliably evaluate the critique ability of Large Language Models (LLMs) across four dimensions and nine diverse task scenarios, involving both scalar-valued and textual critiques.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CRITIC BENCH
- MetaCritique
- UltraFeedback
- Auto-J

**Resources**:
- [GitHub Repository](https://github.com/open-compass/CriticEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and reliable benchmark for evaluating the critique abilities of LLMs, ensuring effective analysis and correction of flaws in their responses.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Critique Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Annotated critiques generated through a human-in-the-loop process, utilizing metrics from various LLMs across different tasks and scenarios.

**Size**: 3,608 critiques

**Format**: text

**Annotation**: Generated critiques are annotated and reviewed by human experts using a rigorous human-in-the-loop data construction pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Spearman correlation

**Calculation**: Spearman correlation coefficients are computed for critiques based on the consistency with human judgments, ranging from -1 to 1, and normalized to a scale of 0 to 100 for reporting.

**Interpretation**: Higher Spearman correlation scores indicate greater consistency with human judgments, reflecting better performance in critique evaluation.

**Baseline Results**: Baseline results include evaluations from 35 widely used open-source and closed-source LLMs mentioned in the paper.

**Validation**: The benchmark is validated through extensive evaluations of multiple LLMs, demonstrating its reliability in evaluating critique ability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures include securing privacy and confidentiality of participants, with no personal identification information involved.

**Data Licensing**: Apache 2.0 License for the CRITIC EVAL dataset; specific licenses for datasets used are discussed in Appendix D.

**Consent Procedures**: Human annotators are compensated adequately, ensuring ethical compliance in data collection.

**Compliance With Regulations**: Not Applicable
