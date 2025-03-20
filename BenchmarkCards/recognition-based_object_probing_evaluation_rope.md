# Recognition-based Object Probing Evaluation (ROPE)

## 📊 Benchmark Details

**Name**: Recognition-based Object Probing Evaluation (ROPE)

**Overview**: ROPE is an automated evaluation protocol designed to assess multi-object hallucination in large vision language models (LVLMs), focusing on how models misperceive when tasked to recognize multiple objects simultaneously.

**Data Type**: Image and visual prompts

**Domains**:
- Culinary
- Autonomous Driving

**Languages**:
- English

**Similar Benchmarks**:
- CCEval
- GA VIE
- FAITHScore
- HaELM
- M-HalDetect
- MMHal-Bench
- CHAIR
- AMBER

**Resources**:
- [Resource](https://multi-object-hallucination.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To systematically investigate multi-object hallucination in LVLMs and to enable these models to recognize and reason about multiple objects in realistic visual scenes.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Evaluate multi-object recognition
- Analyze factors leading to hallucination

**Limitations**: The dataset has a fixed set of semantic objects, which may introduce bias.

**Out of Scope Uses**:
- Single-object hallucination evaluation
- Non-visual prompt tasks

## 💾 Data

**Source**: MSCOCO-Panoptic and ADE20K datasets

**Size**: 5,000 images

**Format**: Images with bounding boxes and labels

**Annotation**: Instance-level semantic annotations

## 🔬 Methodology

**Methods**:
- Recognition-based Probing
- Visual Prompting

**Metrics**:
- Accuracy
- Hallucination Rate

**Calculation**: Probing models for correct identification of object classes based on visual prompts.

**Interpretation**: Comparative analysis across different model architectures and tasks to identify patterns in hallucination.

**Baseline Results**: Various LVLMs are compared, including LLaVA and QwenVL models.

**Validation**: Empirical validation through extensive experiments and statistical analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Transparency**: Lack of training data transparency
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential for models to generate incorrect or non-existent object identifications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is publicly available; no personal data is used.

**Data Licensing**: All datasets follow respective licensing agreements.

**Consent Procedures**: Not applicable; utilizes existing datasets.

**Compliance With Regulations**: Adheres to licensing and ethical guidelines for dataset use.
