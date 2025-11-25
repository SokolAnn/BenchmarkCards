# MedEthicEval

## 📊 Benchmark Details

**Name**: MedEthicEval

**Overview**: MedEthicEval is a novel benchmark designed to systematically evaluate LLMs in the domain of medical ethics. It consists of key components that assess the models' grasp of medical ethics principles and their ability to apply these principles in various scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MedSafetyBench
- MedBench

**Resources**:
- [GitHub Repository](https://github.com/X-LANCE/MedEthicEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework for assessing LLMs’ ability to address complex medical ethics challenges.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Ethics Researchers

**Tasks**:
- Ethical Knowledge Assessment
- Violation Detection
- Priority Dilemma Evaluation
- Equilibrium Dilemma Evaluation

**Limitations**: The relatively small size of the dataset may limit the generalizability of the results.

## 💾 Data

**Source**: Developed through collaboration with medical ethics researchers, utilizing existing open-source datasets for knowledge assessment and newly created datasets for application assessments.

**Size**: 629 questions (Knowledge), 236 questions (Detecting Violation), 100 questions (Priority Dilemma), 100 questions (Equilibrium Dilemma)

**Format**: JSON

**Annotation**: Reviewed and refined by medical experts to ensure accuracy and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Expert review

**Metrics**:
- Accuracy
- Safety Score

**Calculation**: For the knowledge component, accuracy measures the proportion of correctly answered questions. For application components, customized evaluation criteria established by medical ethics experts are used.

**Interpretation**: Higher accuracy indicates better ethical reasoning and knowledge application capabilities of LLMs.

**Baseline Results**: Qwen2.5 achieved the highest performance in both knowledge and ethical reasoning tasks.

**Validation**: Inter-rater reliability assessed and discrepancies resolved through expert judgment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
