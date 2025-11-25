# FERMAT (Finding and correcting Errors in handwritten MAThematical content)

## 📊 Benchmark Details

**Name**: FERMAT (Finding and correcting Errors in handwritten MAThematical content)

**Overview**: FERMAT is a benchmark designed to assess Vision-Language Models' ability to detect, localize, and correct errors in handwritten mathematical content. It spans four key error dimensions: computational, conceptual, notational, and presentation.

**Data Type**: handwritten math solutions

**Domains**:
- Education

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/ai4bharat/FERMAT)
- [GitHub Repository](https://github.com/AI4Bharat/FERMAT)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capability of Vision-Language Models in assessing and correcting handwritten mathematical solutions.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Error Detection
- Error Localization
- Error Correction

**Limitations**: While the benchmark includes a comprehensive list of perturbation categories, it may not be exhaustive. It primarily focuses on school-level mathematics questions.

## 💾 Data

**Source**: 609 manually curated math problems from grades 7-12, targeted perturbations were introduced to create erroneous handwritten solutions.

**Size**: 2,244 instances

**Format**: images and LaTeX

**Annotation**: Manually transcribed by over 40 human annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Balanced Accuracy

**Calculation**: Metrics are calculated based on the performance of Vision-Language Models in detecting, localizing, and correcting errors.

**Interpretation**: Higher values indicate better performance in identifying and correcting errors.

**Baseline Results**: GEMINI-1.5-PRO achieved the highest error correction rate of 77%.

**Validation**: Validated through comparative analysis against human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The annotated datasets have no personally identifying information.

**Data Licensing**: The datasets will be made publicly available under permissible licenses.

**Consent Procedures**: Annotators were made aware that the datasets would be publicly released.

**Compliance With Regulations**: Adhering to licensing requirements.
