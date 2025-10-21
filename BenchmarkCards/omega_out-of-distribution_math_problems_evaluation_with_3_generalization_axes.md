# OMEGA (Out-of-distribution Math Problems Evaluation with 3 Generalization Axes)

## 📊 Benchmark Details

**Name**: OMEGA (Out-of-distribution Math Problems Evaluation with 3 Generalization Axes)

**Overview**: OMEGA is a controlled benchmark designed to evaluate three axes of out-of-distribution generalization in mathematical reasoning: exploratory, compositional, and transformative.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Numina-Math
- Omni-Math
- DeepMath
- GSM-Symbolic
- GSM-PLUS

**Resources**:
- [GitHub Repository](https://github.com/sunblaze-ucb/math_ood)

## 🎯 Purpose and Intended Users

**Goal**: To systematically investigate the limitations of LLMs in mathematical reasoning and provide a framework for advancing LLM capabilities in this domain.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Exploratory Generalization
- Compositional Generalization
- Transformative Generalization

**Limitations**: While it reveals capabilities and limitations of LLMs, it may not encompass all potential reasoning strategies.

## 💾 Data

**Source**: Programmatically generated training-test pairs across several mathematical domains.

**Size**: N/A

**Format**: N/A

**Annotation**: Solutions verified using symbolic, numerical, or graphical methods.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Exact-match accuracy

**Calculation**: Metrics measured on held-out sets for various complexity levels.

**Interpretation**: Performance degradation observed with increasing problem complexity.

**Baseline Results**: Performance levels of frontier models evaluated on OMEGA benchmark.

**Validation**: Empirical evaluation across multiple complexity levels and mathematical domains.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
