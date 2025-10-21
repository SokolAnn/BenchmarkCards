# Sci2Pol-Bench

## 📊 Benchmark Details

**Name**: Sci2Pol-Bench

**Overview**: The first benchmark and training dataset for evaluating and fine-tuning large language models (LLMs) on policy brief generation from scientific papers, featuring 18 tasks across multiple-choice and open-ended formats.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SciRIFF
- MMLU-Pro

**Resources**:
- [GitHub Repository](https://github.com/WeiminWu2000/Sci2Pol)
- [Resource](https://huggingface.co/datasets/Weimin2000/Sci2Pol-Bench)
- [Resource](https://huggingface.co/datasets/Weimin2000/Sci2Pol-Corpus)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework tailored to scientific-to-policy communication, enhancing the performance of LLMs in generating actionable policy briefs from scientific literature.

**Target Audience**:
- ML Researchers
- Policy Makers
- Model Developers

**Tasks**:
- Policy Problem Generation
- Research Findings Generation
- Scientific Research Study Methods Generation
- Policy Implications Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from 85 expert-written paper-brief pairs sourced from top journals like Nature and the Journal of Health and Social Behavior, and 5.6 million policy records from Overton.io.

**Size**: 639 pairs

**Format**: JSON

**Annotation**: Expert-reviewed for quality and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation metrics

**Metrics**:
- Micro F1
- Reference-free Score
- Reference-based Score

**Calculation**: Metrics are computed based on model outputs compared to expert-written policy briefs and ground-truth comparisons of scientific papers.

**Interpretation**: Higher scores indicate better alignment with expert standards for clarity, accuracy, and comprehensive coverage of the scientific material in policy briefs.

**Baseline Results**: Baseline performance was established using 13 models evaluated across the benchmark tasks.

**Validation**: Validated through evaluation of both open-source and commercial LLMs, ensuring reliability of the benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
