# Adversarial GLUE (AdvGLUE)

## 📊 Benchmark Details

**Name**: Adversarial GLUE (AdvGLUE)

**Overview**: Adversarial GLUE (AdvGLUE) is a new multi-task benchmark to quantitatively and thoroughly explore and evaluate the vulnerabilities of modern large-scale language models under various types of adversarial attacks, constructed by applying 14 textual adversarial attack methods to GLUE tasks.

**Data Type**: adversarial examples for language understanding tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE

**Resources**:
- [Resource](https://adversarialglue.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a cohesive and principled benchmark for evaluating the robustness of language models against adversarial attacks.

**Target Audience**:
- Research community
- ML Researchers
- Corporations developing NLP applications
- Model Developers

**Tasks**:
- Sentiment Analysis
- Question Answering
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: Generated adversarial examples based on GLUE benchmark tasks using multiple adversarial attack methods and human-annotated samples.

**Size**: 5,563 adversarial examples

**Format**: N/A

**Annotation**: Crowdsourced evaluations for verification of adversarial perturbations.

## 🔬 Methodology

**Methods**:
- Manual evaluation
- Adversarial attack simulation

**Metrics**:
- Attack Success Rate (ASR)
- Curated Attack Success Rate (Curated ASR)

**Calculation**: ASR measures the effectiveness of adversarial attacks by assessing how many perturbed examples mislead the models.

**Interpretation**: A lower score indicates a model's robustness against adversarial examples; higher ASR indicates vulnerability.

**Baseline Results**: Models were evaluated against the standard GLUE accuracy and compared to their performance on AdvGLUE.

**Validation**: Human evaluation and automatic filtering process were applied to ensure the quality of adversarial examples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
