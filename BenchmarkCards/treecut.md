# TREECUT

## 📊 Benchmark Details

**Name**: TREECUT

**Overview**: TREECUT is a synthetic dataset that generates infinite unanswerable math word problems and their answerable counterparts to evaluate hallucination in large language models.

**Data Type**: Synthetic

**Domains**:
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH

**Resources**:
- [Resource](Dataset generation code will be released upon publication.)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the hallucination rates of LLMs on systematically generated unanswerable math word problems.

**Target Audience**:
- Researchers
- Developers
- Educational institutions

**Tasks**:
- Evaluate LLM performance
- Identify weaknesses in reasoning
- Generate unanswerable and answerable math problems

**Limitations**: The dataset is limited to the scope of math word problems and does not cover other areas of mathematics.

**Out of Scope Uses**:
- Use in non-mathematical reasoning tasks
- Evaluating datasets outside of the generated structure

## 💾 Data

**Source**: Synthetic generation algorithm described in the paper.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Synthetic problem generation using tree structures.
- Prompting LLMs with zero-shot evaluation templates.

**Metrics**:
- Hallucination rate
- Correct identification of unanswerable problems
- Accuracy on answerable problems

**Calculation**: Hallucination rates are calculated based on model outputs on generated unanswerable problems.

**Interpretation**: Higher hallucination rates indicate challenges LLMs face in identifying unanswerable problems.

**Baseline Results**: GPT-4o showed 61% hallucination on unanswerable problems; o3-mini showed 42%.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination in LLMs
- Misinterpretation of problem requirements

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Explainability**: Inaccessible training data, Unexplainable output
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
