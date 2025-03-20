# HuDEx

## 📊 Benchmark Details

**Name**: HuDEx

**Overview**: HuDEx is a model designed to enhance the reliability of LLM-generated responses by detecting hallucinations and providing detailed explanations.

**Data Type**: N/A

**Domains**:
- Natural Language Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- FELM
- TruthfulQA
- QAFactEval

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To detect hallucinations in large language models and provide explanations for them, improving user understanding and model reliability.

**Target Audience**:
- Researchers
- Practitioners in NLP

**Tasks**:
- Hallucination detection
- Explanation generation

**Limitations**: None

**Out of Scope Uses**:
- General purpose LLM tasks

## 💾 Data

**Source**: HaluEval, FactCHD, FaithDial datasets

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Low-rank adaptation (LoRA)
- Binary classification for hallucination detection

**Metrics**:
- Accuracy
- Factuality
- Clarity

**Calculation**: Accuracy was primarily calculated through binary classification.

**Interpretation**: Higher accuracy indicates better hallucination detection performance.

**Validation**: Human evaluation was used to validate the generated explanations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination risks
- Factual inaccuracies

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Explainability**: Unexplainable output

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
