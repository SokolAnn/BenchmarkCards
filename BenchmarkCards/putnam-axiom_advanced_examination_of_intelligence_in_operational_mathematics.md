# Putnam-AXIOM (Advanced eXamination of Intelligence in Operational Mathematics)

## 📊 Benchmark Details

**Name**: Putnam-AXIOM (Advanced eXamination of Intelligence in Operational Mathematics)

**Overview**: Putnam-AXIOM is a benchmark of 522 university-level competition problems drawn from the William Lowell Putnam Mathematical Competition, designed to assess advanced mathematical reasoning in large language models. Additionally, it includes Putnam-AXIOM Variation, which consists of 100 functional variants generated through perturbation techniques to create contamination-resilient test cases.

**Data Type**: mathematical problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8K

**Resources**:
- [GitHub Repository](https://github.com/brando90/putnam-axiom)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous, contamination-resilient evaluation framework for assessing advanced mathematical reasoning of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: The present release contains only those Putnam items that yield a unique numeric or algebraic answer after the modified boxing procedure, excluding non-modifiable problems.

## 💾 Data

**Source**: William Lowell Putnam Mathematical Competition

**Size**: 522 problems for the Original dataset; 100 problems for the Variation dataset

**Format**: LaTeX

**Annotation**: Manually curated university-level mathematical problems to ensure they require advanced reasoning.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Teacher-Forced Accuracy (TFA) scoring

**Metrics**:
- Teacher-Forced Accuracy (TFA)
- Final answer accuracy

**Calculation**: Examine reasoning traces scored using TFA alongside boxed final answers.

**Interpretation**: Higher TFA scores correlate with better reasoning fidelity, whereas final answer accuracy may reflect memorization.

**Baseline Results**: Initial evaluations showed that the best-performing model, o1-preview, achieved 41.9% accuracy on the Original dataset.

**Validation**: Evaluated using the LM Harness Evaluation framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
