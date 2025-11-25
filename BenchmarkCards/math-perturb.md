# MATH-Perturb

## 📊 Benchmark Details

**Name**: MATH-Perturb

**Overview**: MATH-Perturb is designed to test the math reasoning abilities of large language models under hard perturbations of existing problems, consisting of MATH-P-Simple and MATH-P-Hard datasets aimed at exploring the generalization capabilities of LLMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- MATH (Hendrycks et al., 2021)

**Resources**:
- [Resource](https://arxiv.org/abs/2502.06453)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the math reasoning abilities of large language models against hard perturbations, evaluating their performance degradation and generalization.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Adapted from level-5 problems in the MATH dataset (Hendrycks et al., 2021)

**Size**: 558 problems (279 for MATH-P-Simple and 279 for MATH-P-Hard)

**Format**: N/A

**Annotation**: Curated by 12 graduate-level experts with a focus on quality control.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Chain-of-thought prompting

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the proportion of correctly solved problems.

**Interpretation**: Higher accuracy indicates better reasoning capabilities of models in response to both simple and hard perturbations.

**Validation**: Performance validated against both the training and test splits of the original MATH dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
