# InjecGuard

## 📊 Benchmark Details

**Name**: InjecGuard

**Overview**: InjecGuard is a novel prompt guard model designed to mitigate the over-defense issue prevalent in existing prompt guard models. It incorporates a training strategy, Mitigating Over-defense for Free (MOF), and has been evaluated on the NotInject dataset to achieve state-of-the-art performance in detecting prompt injection attacks.

**Data Type**: Evaluative

**Domains**:
- Natural Language Processing
- Cybersecurity

**Languages**:
- English
- Chinese
- Russian

**Similar Benchmarks**:
- PINT
- WildGuard
- BIPIA

**Resources**:
- [Resource](Dataset: NotInject)
- [GitHub Repository](GitHub Repository: https://github.com/SaFoLab-WISC/InjecGuard)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust defense mechanism against prompt injection attacks while minimizing false positives.

**Target Audience**:
- Researchers in AI Safety
- Developers of language models
- Cybersecurity professionals

**Tasks**:
- Evaluate performance of prompt guard models
- Identify and mitigate over-defense issues

**Limitations**: None

**Out of Scope Uses**:
- Malicious prompt injections
- Exploiting AI systems

## 💾 Data

**Source**: NotInject dataset

**Size**: 339 samples

**Format**: Benign sentences with trigger words

**Annotation**: Carefully crafted to include trigger words while maintaining benign intent

## 🔬 Methodology

**Methods**:
- Data collection from open-source datasets
- Data-centric augmentation for long-tail problem
- Training using Mitigating Over-defense for Free (MOF)

**Metrics**:
- Overall accuracy
- Malicious accuracy
- Benign accuracy
- Over-defense accuracy

**Calculation**: Accuracy = Number of Correct Predictions / Total Number of Test Cases

**Interpretation**: Higher accuracy indicates better performance in distinguishing between benign and malicious inputs.

**Baseline Results**: InjecGuard achieves an average accuracy of 83.48%, surpassing existing models by 30.8%.

**Validation**: Evaluated against existing prompt guard models and LLM-based guardrails.

## ⚠️ Targeted Risks

**Risk Categories**:
- Over-defense
- False Positives

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in prompt
- **Robustness**: Prompt injection attack

**Potential Harm**: Potential misclassification leading to accessibility issues in interactive systems.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal or sensitive information is utilized, ensuring compliance with ethical standards.

**Data Licensing**: All datasets are either synthetically generated or sourced from publicly available datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with standard ethical guidelines in AI research.
