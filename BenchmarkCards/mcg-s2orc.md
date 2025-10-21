# MCG-S2ORC

## 📊 Benchmark Details

**Name**: MCG-S2ORC

**Overview**: MCG-S2ORC is a curated dataset composed of English-language academic research papers in Computer Science, showcasing multiple citation instances for the task of multi-citation text generation.

**Data Type**: citation texts

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- S2ORC

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to facilitate research in citation text generation, particularly focusing on generating coherent multi-sentence citations.

**Target Audience**:
- ML Researchers
- Academic Researchers
- Data Scientists

**Tasks**:
- Citation Text Generation

**Limitations**: The maximum token length restriction of the LLMs used limits the number of relations incorporated into the prompts.

## 💾 Data

**Source**: Curated dataset created from the S2ORC dataset focused on multi-reference citation texts.

**Size**: 17,210 samples

**Format**: JSON

**Annotation**: Manually curated and constructed from extracted citation information.

## 🔬 Methodology

**Methods**:
- Fine-tuning of LLaMA, Alpaca, and Vicuna models

**Metrics**:
- METEOR
- ROUGE-1
- ROUGE-2
- ROUGE-L

**Calculation**: Metrics are calculated based on the degree of similarity between generated citation texts and actual reference citation texts.

**Interpretation**: Higher METEOR and ROUGE scores indicate better performance in generating coherent citation text.

**Validation**: Results compared against baseline models to assess performance improvement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
