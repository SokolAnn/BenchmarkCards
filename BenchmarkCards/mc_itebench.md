# MC ITEBENCH

## 📊 Benchmark Details

**Name**: MC ITEBENCH

**Overview**: MC ITEBENCH is the first benchmark designed to assess the ability of Multimodal Large Language Models (MLLMs) to generate text with citations in multimodal contexts, featuring diverse information sources and multimodal content.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://caiyuhu.github.io/MCiteBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of MLLMs to generate text with citations from multimodal input.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Generation with Citations

**Limitations**: In MC ITEBENCH, citations are limited to the sentence level, meaning that we do not distinguish between multiple claims within a single sentence.

## 💾 Data

**Source**: Academic papers collected from OpenReview, along with review–rebuttal interactions.

**Size**: 3,000 samples

**Format**: N/A

**Annotation**: Data is annotated through manual verification by human annotators to ensure accuracy and consistency.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Citation F1
- Source F1
- Source Exact Match
- Accuracy

**Calculation**: Metrics are calculated based on the alignment between cited evidence and generated responses.

**Interpretation**: Higher scores indicate better model performance in generating citations accurately and reliably.

**Validation**: The benchmark was validated through extensive experiments with model evaluations and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
