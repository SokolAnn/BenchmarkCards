# Hal-Eval

## 📊 Benchmark Details

**Name**: Hal-Eval

**Overview**: A universal and fine-grained hallucination evaluation framework for Large Vision Language Models (LVLMs), providing a comprehensive assessment of various hallucination types, including unique categories such as event hallucinations.

**Data Type**: Image-caption pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- POPE
- NOPE
- CIEM
- AMBER

**Resources**:
- [Resource](https://doi.org/10.1145/3664647.3680576)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of hallucinations in LVLMs and refine their outputs.

**Target Audience**:
- Researchers in AI
- Developers of LVLMs
- Academics focused on NLP and CV

**Tasks**:
- Evaluate hallucinations in LVLM outputs
- Analyze model performance based on hallucination types
- Fine-tune models using annotated data

**Limitations**: Only evaluates hallucinations, other evaluation aspects such as accuracy and feasibility of image-text alignment are not covered.

**Out of Scope Uses**:
- General NLP tasks not involving hallucinations
- Processing unrelated visual input

## 💾 Data

**Source**: Hal-Data created from COCO, Conceptual Captions, SBU, and web-sourced images.

**Size**: 130K for Hal-Data 130k; 2M for Hal-Data 2M

**Format**: Image-text pairs with annotated hallucinations

**Annotation**: Annotated using a fine-grained hallucination annotation pipeline with GPT-4.

## 🔬 Methodology

**Methods**:
- Discriminative evaluation with uniform question templates
- Generative evaluation using the Hal-Evaluator

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Calculated metrics based on predictions of hallucinations against ground-truth annotations.

**Interpretation**: Metrics provide insight into the frequency and types of hallucinations present in model outputs.

**Validation**: Validated against human judgments for accuracy of hallucination detection.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Explainability
- Robustness
- Privacy

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential misuse in generating misleading or incorrect captions, adversely affecting the reliability of LVLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Publicly available datasets such as COCO were used; participant consent for data usage was obtained.

**Data Licensing**: Data is sourced from open datasets under typical usage licenses.

**Consent Procedures**: All generated content data used for training was annotated by team members, ensuring compliance.

**Compliance With Regulations**: Not Applicable
