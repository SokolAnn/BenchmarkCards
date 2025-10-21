# ConceptMath

## 📊 Benchmark Details

**Name**: ConceptMath

**Overview**: ConceptMath is a bilingual (English and Chinese), fine-grained benchmark that evaluates concept-wise mathematical reasoning of Large Language Models (LLMs). It systematically organizes math problems under a hierarchy of math concepts to evaluate mathematical reasoning at different granularity with concept-wise accuracies.

**Data Type**: math word problems

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- GSM8K
- MATH
- Math23K

**Resources**:
- [GitHub Repository](https://github.com/conceptmath/conceptmath)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the mathematical reasoning capabilities of Large Language Models across a diverse set of mathematical concepts in both English and Chinese.

**Target Audience**:
- ML Researchers
- Model Developers
- Educators

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: ConceptMath is created based on a collection of math problems designed for educational use across different concept systems.

**Size**: 4011 problems

**Format**: N/A

**Annotation**: Problems were carefully annotated by education professionals and validated by human experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Concept-wise accuracy
- Overall accuracy

**Calculation**: Metrics are calculated based on the number of correct answers out of total questions in different prompt settings.

**Interpretation**: Higher accuracy scores indicate better mathematical reasoning capabilities of the evaluated models.

**Baseline Results**: Various existing LLMs were evaluated against the ConceptMath benchmark to establish baseline performance.

**Validation**: The benchmark was validated through extensive evaluation across several LLMs using different prompting techniques.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
