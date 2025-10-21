# The Elicitation Game: Evaluating Capability Elicitation Techniques

## 📊 Benchmark Details

**Name**: The Elicitation Game: Evaluating Capability Elicitation Techniques

**Overview**: This paper evaluates the effectiveness of capability elicitation techniques by training model organisms based on circuit-breaking and password-locking methods to reveal hidden capabilities. It emphasizes the need for trustworthy capability evaluations in AI systems.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WMDP (Weapons of Mass Destruction Proxy)
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [GitHub Repository](https://github.com/Felhof/sandbagging-elicitation)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate elicitation techniques for AI systems to improve the trustworthiness of capability evaluations.

**Target Audience**:
- AI Researchers
- AI Safety Practitioners

**Tasks**:
- Multiple-Choice Question Answering
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Training data comes from the WMDP and MMLU benchmarks, and the code-generation task APPS.

**Size**: 3668 examples (WMDP), 1402 examples (MMLU), 3000 examples (APPS)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Supervised fine-tuning
- Prompting techniques
- Steering techniques

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the performance of model organisms on the specified tasks.

**Interpretation**: Performance metrics indicate the ability of elicitation techniques to recover hidden capabilities of AI models.

**Baseline Results**: Supervised fine-tuning results in the most reliable elicitation of hidden capabilities.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Trustworthiness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
