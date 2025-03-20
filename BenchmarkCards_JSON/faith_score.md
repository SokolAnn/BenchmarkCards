# FAITH SCORE

## 📊 Benchmark Details

**Name**: FAITH SCORE

**Overview**: FAITH SCORE is a reference-free and fine-grained evaluation metric that measures the faithfulness of the generated free-form answers from large vision-language models (LVLMs) by verifying atomic facts against input images.

**Data Type**: Benchmark datasets for evaluating LMS

**Domains**:
- Vision-Language Models

**Languages**:
- N/A

**Similar Benchmarks**:
- CHAIR
- POPE
- NOPE

**Resources**:
- [GitHub Repository](https://github.com/bcdnlp/FAITHSCORE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable metric for evaluating the faithfulness of LVLMs in terms of hallucinations in free-form answers.

**Target Audience**:
- Researchers
- Practitioners in AI and machine learning

**Tasks**:
- Evaluating hallucinations in LVLM outputs
- Fine-grained analysis of generated content

**Limitations**: FAITH SCORE does not address factual recall, focusing instead on factual precision.

**Out of Scope Uses**:
- Broader evaluations beyond LVLMs
- Tasks not involving visual content

## 💾 Data

**Source**: LLaV A-1k and MSCOCO-Cap datasets

**Size**: 2000 images across datasets

**Format**: Images with corresponding answer prompts

**Annotation**: Descriptive sub-sentences and atomic facts extracted and verified manually for evaluation

## 🔬 Methodology

**Methods**:
- Descriptive Sub-sentence Identification
- Atomic Fact Generation
- Fact Verification using a Visual Entailment Model

**Metrics**:
- FAITH SCORE

**Calculation**: The FAITH SCORE is computed by verifying atomic facts against visual input and measuring their consistency.

**Interpretation**: Higher FAITH SCORE indicates better faithfulness of the generated answer to the input image.

**Validation**: The correlation with human judgments of faithfulness was validated through meta-evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination in generated content
- Lack of model interpretability
- Inability to measure factual recall

**Atlas Risks**:
- **Explainability**: Unexplainable output, Inaccessible training data
- **Robustness**: Hallucination, Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misinformation and safety concerns arising from hallucinations in model outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets used have been anonymized and do not contain personal information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adheres to current ethical standards in AI research and evaluation.
