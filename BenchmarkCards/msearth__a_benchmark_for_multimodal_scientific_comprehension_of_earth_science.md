# MSEarth: A Benchmark for Multimodal Scientific Comprehension of Earth Science

## 📊 Benchmark Details

**Name**: MSEarth: A Benchmark for Multimodal Scientific Comprehension of Earth Science

**Overview**: MSEarth is a comprehensive benchmark designed for graduate-level Earth science, featuring over 7,000 figures and refined captions sourced from open-access scientific publications. It aims to fill the gap in multimodal evaluation for complex geoscientific tasks.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/MSEarth)
- [GitHub Repository](https://github.com/xiangyu-mm/MSEarth)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous multimodal benchmark for evaluating the capabilities of multimodal large language models in advanced geoscientific reasoning.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Scientific Figure Captioning
- Multiple Choice Questions
- Open-Ended Reasoning

**Limitations**: While MSEarth covers a broad range of topics, niche or highly specialized subfields may not be adequately represented.

## 💾 Data

**Source**: Curated from open-access scientific publications, specifically focused on Earth science topics.

**Size**: 7,195 questions

**Format**: JSON

**Annotation**: Expert-reviewed for accuracy and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Expert validation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the generated responses compared to reference answers or captions, with specific focus on factual accuracy and coherent reasoning.

**Interpretation**: Scores reflect the model's ability to generate logical, accurate, and contextually grounded responses.

**Validation**: Rigorous quality control process combining automated evaluation and expert assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: Analysis is conducted to evaluate the representation of diverse demographic groups in the benchmark.

**Potential Harm**: The benchmark aims to prevent potential harm by ensuring the scientific accuracy and contextual relevance of questions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
