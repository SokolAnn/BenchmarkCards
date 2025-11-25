# AstroMLab 2: AstroLLaMA-2-70B Model and Benchmarking Specialised LLMs for Astronomy

## 📊 Benchmark Details

**Name**: AstroMLab 2: AstroLLaMA-2-70B Model and Benchmarking Specialised LLMs for Astronomy

**Overview**: This study aims to quantitatively assess specialized LLMs in astronomy through a new MCQ benchmark dataset designed to evaluate LLMs in the context of astronomical research, providing the first objective metric for evaluating specialized LLMs quantitatively.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science
- Astronomy

**Languages**:
- English

**Similar Benchmarks**:
- AstroLLaMA 1

**Resources**:
- [Resource](https://huggingface.co/AstroMLab)
- [Resource](https://arxiv.org/abs/2409.19750)

## 🎯 Purpose and Intended Users

**Goal**: To establish a robust benchmark that accurately assesses the capabilities of LLMs in astronomical research through the use of a new MCQ dataset.

**Target Audience**:
- ML Researchers
- Domain Experts
- Astronomy Researchers

**Tasks**:
- Question Answering

**Limitations**: The benchmark primarily tests knowledge recall and may not capture nuanced reasoning skills.

## 💾 Data

**Source**: The dataset is derived from the Annual Review of Astronomy and Astrophysics, featuring high-quality MCQs generated from comprehensive reviews.

**Size**: 4,425 questions

**Format**: JSON

**Annotation**: Questions were extracted and processed using LLMs with human input to ensure quality.

## 🔬 Methodology

**Methods**:
- Full Instruct Benchmarking Method
- Base Model Token Benchmarking Method
- Instruct Model Token Benchmarking Method

**Metrics**:
- Fraction of Correctly Answered MCQs

**Calculation**: Scores are calculated based on the fraction of correct answers provided by the specialized LLMs across different benchmarking methodologies.

**Interpretation**: Higher scores indicate better capability in answering astronomy-related multiple-choice questions accurately, with a clear distinction between model performances depending on the dataset used in continual pretraining and supervised fine-tuning.

**Baseline Results**: The AstroLLaMA-2-70B achieved a score of 76.0% in next-token prediction, while the baseline LLaMA-2-70B scored 73.9%.

**Validation**: Reproducibility of results was emphasized through consistent token evaluation and corrections for output variations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['The benchmark raises concerns about potential biases in MCQ generation affecting various demographic groups.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
