# InfiBench

## 📊 Benchmark Details

**Name**: InfiBench

**Overview**: InfiBench is a systematic benchmark for evaluating the free-form question-answering capabilities of code large language models, comprising 234 carefully selected high-quality Stack Overflow questions that span across 15 programming languages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://infi-coder.github.io/infibench)
- [Resource](https://huggingface.co/datasets/llylly001/InfiBench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the question-answering ability of code LLMs in real-world scenarios, facilitating the development and scientific evaluation of these models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Filtered and selected high-quality questions from the Stack Overflow dataset.

**Size**: 234 questions

**Format**: N/A

**Annotation**: Annotated by domain experts through a multi-step process including selection, paraphrasing, and correctness criteria annotation.

## 🔬 Methodology

**Methods**:
- Model-free automatic evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation scores are calculated based on a point system where correct responses earn points for each correct keyword or answer structure.

**Interpretation**: Higher scores indicate better performance in correctly answering the questions posed in the benchmark.

**Baseline Results**: N/A

**Validation**: Questions and evaluation criteria are cross-validated to ensure correctness and objectivity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Paraphrased questions to remove personal and sensitive information.

**Data Licensing**: Creative Commons Attribution Share Alike 4.0.

**Consent Procedures**: Inferred consent through publicly accessible data and benchmark construction practices.

**Compliance With Regulations**: Not Applicable
