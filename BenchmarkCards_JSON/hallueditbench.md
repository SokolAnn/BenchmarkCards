# HalluEditBench

## 📊 Benchmark Details

**Name**: HalluEditBench

**Overview**: HalluEditBench is a holistic benchmark to assess knowledge editing methods in correcting real-world hallucinations in Large Language Models (LLMs). It addresses the common gap in existing datasets that fail to verify hallucinations before editing.

**Data Type**: Hallucination dataset

**Domains**:
- art
- business
- entertainment
- event
- geography
- health
- human
- places
- technology

**Resources**:
- [Resource](Project website: https://llm-editing.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark knowledge editing methods for correcting factual inaccuracies in LLMs.

**Target Audience**:
- Researchers in AI and NLP
- Developers working with LLMs
- Academics studying knowledge editing

**Tasks**:
- Assess the efficacy of knowledge editing techniques
- Evaluate the impact of editing on LLM performance across multiple dimensions

**Limitations**: None

## 💾 Data

**Source**: Wikidata

**Size**: More than 6,000 hallucinations from 12,619, 13,210, and 14,366 for Llama2-7B, Llama3-8B, and Mistral-v0.3-7B respectively

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Efficacy
- Generalization
- Portability
- Locality
- Robustness

**Metrics**:
- Efficacy Score (%)
- Generalization Score (%)
- Portability Score (%)
- Locality Score (%)
- Robustness Score (%)

**Calculation**: Scores are defined based on accuracy on evaluation questions generated from a large hallucination dataset.

**Interpretation**: Higher scores indicate better performance of knowledge editing techniques.

**Validation**: Extensive empirical investigations compared knowledge editing methods across 9 domains and 26 topics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Explainability
- Misuse

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack
- **Explainability**: Unexplainable output
- **Misuse**: Spreading disinformation

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
