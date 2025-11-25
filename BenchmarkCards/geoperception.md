# Geoperception

## 📊 Benchmark Details

**Name**: Geoperception

**Overview**: Geoperception is a benchmark designed to evaluate an MLLM’s ability to accurately transcribe 2D geometric information from an image. It reveals shortcomings in precise geometric perception across leading vision-language MLLMs, both closed and open-source.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://euclid-multimodal.github.io)
- [Resource](https://huggingface.co/euclid-multimodal)
- [GitHub Repository](https://github.com/euclid-multimodal/Euclid)

## 🎯 Purpose and Intended Users

**Goal**: To construct a benchmark focusing solely on the geometric perception ability of MLLMs.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Geometric Perception Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Derived from the Geometry-3K corpus, which compiles problems from high school textbooks.

**Size**: 1,584 images with multiple questions across 7 tasks

**Format**: JSON

**Annotation**: Questions and answers generated directly from logical forms validated by GPT-4.

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: The evaluation score is defined as |P| / |G| if P is a subset of G, otherwise 0.

**Interpretation**: Higher scores indicate better geometric perception capabilities.

**Baseline Results**: Closed-source models, such as Gemini-1.5-Pro, achieved an average score of 56.98%.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
