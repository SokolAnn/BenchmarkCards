# vTikZ

## 📊 Benchmark Details

**Name**: vTikZ

**Overview**: The vTikZ benchmark is designed to evaluate the ability of Large Language Models (LLMs) to customize code while preserving coherent visual outcomes. It consists of carefully curated TikZ editing scenarios and a reviewing tool that assesses correctness based on visual feedback.

**Data Type**: code customization tasks

**Domains**:
- Software Engineering
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/CharlyR/vtikz)
- [GitHub Repository](https://github.com/IV2C/VTikZ)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs in customizing TikZ code with visual results.

**Target Audience**:
- Software Engineers
- AI Researchers

**Tasks**:
- Code Customization

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of 100 manually curated TikZ code customization tasks derived from various TikZ code sources.

**Size**: 100 examples

**Format**: JSON

**Annotation**: Annotations were created based on human evaluation of LLM-generated variants.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Compile Metric
- Location Metric
- Success Customization Metric
- Line Metric
- Similarity Metric

**Calculation**: Metrics are calculated based on evaluations comparing LLM outputs with reference solutions.

**Interpretation**: Metrics provide a way to assess the success of code modifications based on visual and textual criteria.

**Validation**: The benchmark was validated through human feedback and systematic evaluation of generated outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Potential Harm**: ['Incorrect visual outputs may mislead users.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
