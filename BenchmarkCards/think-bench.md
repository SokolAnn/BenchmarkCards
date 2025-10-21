# Think-Bench

## 📊 Benchmark Details

**Name**: Think-Bench

**Overview**: Think-Bench is a benchmark designed to evaluate the reasoning efficiency of large reasoning models (LRMs) and their chain-of-thought quality across mathematics, physics, and chemistry tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GPQA

**Resources**:
- [Resource](https://think-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the reasoning efficiency and quality of chain-of-thought in large reasoning models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Reasoning Efficiency Evaluation
- Chain-of-Thought Quality Evaluation

**Limitations**: The Think-Bench benchmark currently covers only three disciplines: mathematics, physics, and chemistry, which limits its effectiveness in evaluating models’ reasoning abilities across a broader range of subjects.

## 💾 Data

**Source**: Curated from various academic datasets including MMLU, Math500, AGIEval, AIME, GPQA, SciKnowEval, and UGPhysics.

**Size**: 1,375 samples

**Format**: JSON

**Annotation**: Meticulously annotated key reasoning steps for each problem instance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Efficiency
- Recall
- Precision
- Reflection Quality
- Accuracy

**Calculation**: Metrics calculated include the total tokens used, the number of tokens until the first correct answer, and various quality measures comparing generated reasoning steps against a reference.

**Interpretation**: Higher efficiency and quality scores indicate better reasoning capabilities and resource usage.

**Baseline Results**: Various LRMs are evaluated, including Claude 3.7 Sonnet and models from the DeepSeek family.

**Validation**: Benchmarks are validated through comprehensive evaluation across multiple representative LRMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Efficiency
- Quality of Reasoning

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
