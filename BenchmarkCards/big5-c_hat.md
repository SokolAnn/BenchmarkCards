# BIG5-C HAT

## 📊 Benchmark Details

**Name**: BIG5-C HAT

**Overview**: BIG5-C HAT is a large-scale dataset containing 100,000 dialogues designed to ground models in how humans express their personality in language, addressing realism and validity issues in prior methods.

**Data Type**: dialogue pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/wenkai-li/Big5-Chat.git)
- [Resource](https://huggingface.co/datasets/wenkai-li/big5_chat)

## 🎯 Purpose and Intended Users

**Goal**: To investigate how training-based methods grounded in real human data compare to traditional prompting techniques for inducing personality traits in LLMs.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Text Generation
- Social Interaction Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Combination of PsychGenerator and SODA datasets.

**Size**: 100,000 dialogues

**Format**: JSON

**Annotation**: Generated text based on personality traits using fine-tuned models.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Direct Preference Optimization

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on personality assessments using BFI and IPIP-NEO.

**Interpretation**: Higher scores indicate better alignment with human-like personality traits.

**Baseline Results**: N/A

**Validation**: Human evaluations were conducted comparing generated outputs with baseline methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Reinforcing undesirable behaviors or stereotypes', 'Exaggerated outputs leading to hallucination']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
