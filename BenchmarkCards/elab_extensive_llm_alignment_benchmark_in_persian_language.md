# ELAB (Extensive LLM Alignment Benchmark in Persian Language)

## 📊 Benchmark Details

**Name**: ELAB (Extensive LLM Alignment Benchmark in Persian Language)

**Overview**: This paper presents a comprehensive evaluation framework for aligning Persian Large Language Models (LLMs) with critical ethical dimensions, including safety, fairness, and social norms by creating three types of Persian-language benchmarks: translated data, new synthetically generated data, and new naturally collected data.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Similar Benchmarks**:
- Ganguli et al. (2022)
- AdvBench
- HarmBench
- DecodingTrust

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To develop a comprehensive framework for evaluating Persian LLMs, focusing on safety, fairness, and social norms.

**Target Audience**:
- ML Researchers
- Ethics Researchers
- AI Practitioners

**Tasks**:
- Safety Evaluation
- Fairness Evaluation
- Social Norms Evaluation

**Limitations**: Evaluations are constrained to open-source models with fewer than 10 billion parameters.

## 💾 Data

**Source**: Translated and generated datasets from existing alignment benchmarks, along with explicitly collected data from social media.

**Size**: 30,000 examples (approx. across various datasets)

**Format**: N/A

**Annotation**: Manual annotation by experts and evaluation using a GPT-based model.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-as-a-Judge evaluation

**Metrics**:
- Accuracy
- Fairness Scores
- Safety Scores

**Calculation**: Scores are derived from human evaluators rating LLM outputs on a scale based on safety, fairness, and social norms.

**Interpretation**: Higher scores indicate better alignment with safety, fairness, and social norms.

**Baseline Results**: Performance across various alignment benchmarks as referenced in the paper.

**Validation**: Uses a systematic evaluation approach involving multiple models and scoring systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: Data includes demographic considerations specific to the Persian language context.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collection was conducted with respect to user privacy and anonymity where feasible.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Attempts to align with local data protection regulations relevant to the Persian context.
