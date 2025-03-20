# CrossCheckGPT: Universal Hallucination Ranking for Multimodal Foundation Models

## 📊 Benchmark Details

**Name**: CrossCheckGPT: Universal Hallucination Ranking for Multimodal Foundation Models

**Overview**: CrossCheckGPT proposes a reference-free universal hallucination ranking approach for multimodal foundation models, designed to assess hallucination robustness. It utilizes cross-system consistency and can be applied to any model or task provided that information consistency can be evaluated through a suitable metric.

**Data Type**: Multimodal (text, image, audio-visual)

**Domains**:
- Multimodal Foundation Models
- Hallucination Detection
- Generative AI

**Similar Benchmarks**:
- MHaluBench
- A VHalluBench

## 🎯 Purpose and Intended Users

**Goal**: To provide a universal evaluation framework for ranking multimodal large language models with respect to their susceptibility to hallucinations.

**Target Audience**:
- Researchers
- AI practitioners
- Developers of AI systems

**Tasks**:
- Hallucination ranking
- Benchmarking multimodal AI models

**Limitations**: None

## 💾 Data

**Source**: A VHalluBench

**Size**: 175 videos

**Format**: Diverse modalities including audio, video, and text descriptions

**Annotation**: Annotated for factual correctness, each video has descriptions generated under specific guidelines to avoid hallucination.

## 🔬 Methodology

**Methods**:
- CrossCheck-explicit
- CrossCheck-implicit

**Metrics**:
- Spearman's Rank Correlation
- Pearson's Correlation Coefficient

**Calculation**: Scores are derived from assessing the consistency of outputs across multiple models, employing a custom weighting based on the historical performance of the evidence models.

**Interpretation**: Metrics indicate the level of hallucination detected across models and tasks, allowing for comparative analysis.

**Baseline Results**: CrossCheckGPT achieves up to 98% correlation with human judgement on MHaluBench and 89% on A VHalluBench.

**Validation**: Validated on established datasets and compared against existing hallucination detection methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination
- Model Misuse

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Compliance with ethical standards for data collection and annotation is maintained, yet specifics are not detailed.

**Data Licensing**: Data used from publicly accessible datasets under appropriate licenses.

**Consent Procedures**: Informed consent processes for data usage were adhered to but not explicitly stated.

**Compliance With Regulations**: Ensures compliance with regulations around AI and data ethics.
