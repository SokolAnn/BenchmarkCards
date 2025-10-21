# CRAB (Causal Reasoning Assessment Benchmark)

## 📊 Benchmark Details

**Name**: CRAB (Causal Reasoning Assessment Benchmark)

**Overview**: CRAB is a new Causal Reasoning Assessment Benchmark designed to evaluate causal understanding of events in real-world narratives. It includes fine-grained, contextual causality annotations for approximately 2,700 pairs of real-world events that describe various newsworthy event timelines, allowing evaluation of language models' performance on causal reasoning tasks.

**Data Type**: causality annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/agromanou/CRAB)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate causal reasoning capabilities of large language models on real-world narratives through a structured benchmark.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Causal Inference
- Causal Reasoning

**Limitations**: The benchmark may contain biases due to the media's representations of events.

## 💾 Data

**Source**: Causal events extracted from 173 news articles covering 20 stories from the past ten years.

**Size**: 2,730 event pairs

**Format**: JSON

**Annotation**: Crowdsourced human annotations for causality judgments.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- F1 Score

**Calculation**: Causality scores are calculated on a scale from 0 to 100 based on human annotations.

**Interpretation**: Scores are stratified into four classes reflecting causality strength.

**Baseline Results**: GPT-4 achieved an average F1 score of approximately 54.7 in pairwise causality tasks.

**Validation**: Validated by human experts through an additional annotation phase.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes annotations reflecting potential biases in media representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Data was collected via public news articles; specific consent procedures are not discussed.

**Compliance With Regulations**: Not Applicable
