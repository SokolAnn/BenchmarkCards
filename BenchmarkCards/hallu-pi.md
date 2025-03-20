# Hallu-PI

## 📊 Benchmark Details

**Name**: Hallu-PI

**Overview**: Hallu-PI is the first benchmark designed to evaluate hallucination in Multi-modal Large Language Models (MLLMs) within perturbed inputs, consisting of seven perturbed scenarios with 1,260 images across 11 object categories.

**Data Type**: Images

**Domains**:
- Visual-language understanding
- Visual-language generation

**Languages**:
- N/A

**Similar Benchmarks**:
- POPE
- M-HalDetect
- HaELM
- Halle-Switch
- AMBER

**Resources**:
- [GitHub Repository](https://github.com/NJUNLP/Hallu-PI)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of hallucinations in MLLMs when exposed to perturbed inputs.

**Target Audience**:
- Researchers
- Developers of MLLMs
- AI practitioners

**Tasks**:
- Evaluate hallucination performance
- Assess performance across different perturbation types

**Limitations**: None

**Out of Scope Uses**:
- Evaluation of MLLMs without perturbed inputs

## 💾 Data

**Source**: Collected from various internet sources focusing on high-quality images.

**Size**: 1,260 images

**Format**: N/A

**Annotation**: Includes detailed annotations for hallucination types such as existence, attribute, and relation.

## 🔬 Methodology

**Methods**:
- Manual annotation of images
- Evaluation of 12 MLLMs under perturbed input conditions

**Metrics**:
- CHAIR
- Cover
- Hal
- Cog
- Accuracy+
- PI-Score

**Calculation**: PI-Score = Avg(α(1−Hal),(1−α)Accuracy+)

**Interpretation**: Lower metrics indicate higher hallucination occurrences.

**Validation**: Extensive experiments conducted on multiple MLLMs like GPT-4V and Gemini-Pro Vision.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination due to perturbed inputs
- Ability to handle different types of hallucinations

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Potential Harm**: ['Incorrect information generation', 'Potential risks in high-stakes applications (e.g. medical diagnosis)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
