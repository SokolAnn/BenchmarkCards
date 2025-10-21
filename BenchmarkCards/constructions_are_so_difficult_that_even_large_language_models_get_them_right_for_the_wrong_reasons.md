# Constructions Are So Difficult That Even Large Language Models Get Them Right for the Wrong Reasons

## 📊 Benchmark Details

**Name**: Constructions Are So Difficult That Even Large Language Models Get Them Right for the Wrong Reasons

**Overview**: This paper introduces a small challenge dataset for Natural Language Inference (NLI) with large lexical overlap, which minimizes the possibility of models discerning entailment solely based on token distinctions, and shows that GPT-4 and Llama 2 fail it with strong bias.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/shijiazh/Constructions-Are-So-Difficult)

## 🎯 Purpose and Intended Users

**Goal**: To test the ability of large language models (LLMs) to identify different meanings in sentences that are superficially similar.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: Dataset was collected using Universal Dependency annotations from a parsed Wikipedia corpus and a parsed Amazon Reviews corpus, manually annotated.

**Size**: 323 sentences

**Format**: N/A

**Annotation**: Manual annotation of sentence pairs based on semantic constructions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on model performance on identifying entailment.

**Interpretation**: A model is considered to perform well if it can accurately identify the semantic properties and causality of constructions.

**Baseline Results**: N/A

**Validation**: Using probing classifiers to assess model representations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

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
