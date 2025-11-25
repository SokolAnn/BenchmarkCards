# MME-SCI (Multimodal Evaluation for Science)

## 📊 Benchmark Details

**Name**: MME-SCI (Multimodal Evaluation for Science)

**Overview**: MME-SCI is a comprehensive multimodal benchmark for assessing the reasoning capabilities of multimodal large language models (MLLMs) across various scientific domains, including mathematics, physics, chemistry, and biology. It contains 1,019 meticulously curated question-answer pairs across three modalities: text-only, image-only, and image-text hybrid, and supports five languages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Science

**Languages**:
- Chinese
- English
- French
- Spanish
- Japanese

**Similar Benchmarks**:
- MMMU
- GAOKAO-Bench
- MathVerse
- MATH-Vision
- EMMA

**Resources**:
- [GitHub Repository](https://github.com/JCruan519/MME-SCI)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging and comprehensive evaluation benchmark for multimodal large language models in scientific reasoning, enhancing their evaluation across diverse linguistic and modal contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 1,019 high-quality question-answer pairs collected from mock exam papers and digitized for multiple modalities.

**Size**: 1,019 examples

**Format**: JSON

**Annotation**: Manually curated and annotated with fine-grained knowledge points across various scientific topics.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correctly answered questions across different modalities and subjects.

**Interpretation**: Higher accuracy indicates better reasoning and understanding of scientific concepts by the MLLMs.

**Baseline Results**: Evaluation results indicate that advanced closed-source models outperform open-source ones on average by approximately 13.94%.

**Validation**: Extensive experimentation involving 16 open-source and 4 closed-source models was conducted to assess benchmark performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
