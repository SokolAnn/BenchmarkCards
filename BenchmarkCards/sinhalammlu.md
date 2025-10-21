# SinhalaMMLU

## 📊 Benchmark Details

**Name**: SinhalaMMLU

**Overview**: SinhalaMMLU is the first multiple-choice question answering benchmark designed specifically for Sinhala, a low-resource language. The dataset includes over 7,000 questions spanning secondary to collegiate education levels and is aligned with the Sri Lankan national curriculum. It covers six domains and 30 subjects, including both general academic topics and culturally grounded knowledge.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Sinhala

**Similar Benchmarks**:
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/naist-nlp/SinhalaMMLU)
- [Resource](https://huggingface.co/datasets/naist-nlp/SinhalaMMLU)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language models in the Sinhala language across educational levels, ensuring culturally relevant and educationally aligned benchmarks.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Education Researchers

**Tasks**:
- Question Answering

**Limitations**: SinhalaMMLU is limited to text-based multiple-choice questions and excludes multi-modal and open-ended tasks.

## 💾 Data

**Source**: Collected from various national and provincial exams without relying on translations.

**Size**: 7,044 questions

**Format**: JSON

**Annotation**: Manual annotation by experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the percentage of correct answers across evaluated models.

**Interpretation**: Higher accuracy indicates better performance in understanding the Sinhala language and context.

**Validation**: Evaluated 26 LLMs in zero-shot and few-shot settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Collected data consists of publicly available educational resources.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Compliant with the Sri Lankan Copyright Act for fair use.
