# KoTox (Korean Toxic instruction dataset)

## 📊 Benchmark Details

**Name**: KoTox (Korean Toxic instruction dataset)

**Overview**: KoTox comprises 39,200 unethical instruction-output pairs designed to improve the ethical robustness of large language models (LLMs) through instruction tuning and is aimed at refining their responses to toxic queries.

**Data Type**: instruction-output pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Similar Benchmarks**:
- SQuARe
- KoSBi

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that can help LLMs mitigate the detrimental consequences of toxic instructions and refine their ethical responses.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated through a systematic process combining derogatory terms, biased expressions, and templates.

**Size**: 39,200 instances

**Format**: N/A

**Annotation**: Human evaluation for quality assurance of generated sentences.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Toxicity scores

**Calculation**: Toxicity is assessed using the Perspective API to evaluate attributes such as Toxicity, Severe toxicity, Insult, and Profanity.

**Interpretation**: Higher scores indicate increased levels of toxicity in the dataset.

**Baseline Results**: N/A

**Validation**: Human-in-the-loop evaluation was used to ensure naturalness and coherence of the auto-generated sentences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
