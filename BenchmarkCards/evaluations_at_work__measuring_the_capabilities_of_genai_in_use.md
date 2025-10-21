# Evaluations at Work: Measuring the Capabilities of GenAI in Use

## 📊 Benchmark Details

**Name**: Evaluations at Work: Measuring the Capabilities of GenAI in Use

**Overview**: This paper introduces a novel evaluation framework focused on dyadic, collaborative, and integrated, multi-turn interactions by using task decomposition to assess LLM capabilities in real-world work contexts.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- ROUGE

**Resources**:
- [Resource](https://arxiv.org/abs/2505.10742)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to provide a comprehensive evaluation methodology that accurately assesses the performance of LLMs in real-world collaborative tasks.

**Target Audience**:
- Researchers
- Industry Practitioners

**Tasks**:
- Financial Valuation
- Task Decomposition

**Limitations**: The demonstration is limited to a specific task and participant pool, affecting generalizability.

## 💾 Data

**Source**: Data was collected from participants completing a financial valuation task using GenAI.

**Size**: 34 participants' interactions

**Format**: CSV

**Annotation**: Qualitative coding and analysis of participant transcripts

## 🔬 Methodology

**Methods**:
- Qualitative Coding
- Mixed-Effects Ordinal Logistic Regression
- Semantic Similarity Analysis

**Metrics**:
- Composite Usage Measure
- Structural Coherence
- Diversity
- Average Distance to Frontier

**Calculation**: Metrics are derived from participant responses and analyzed for impacts on output quality.

**Interpretation**: Higher scores in Composite Usage and lower Average Distance to Frontier are associated with better output quality.

**Baseline Results**: Outputs were assessed using a mixed-effects model, revealing significant improvements in quality with effective LLM use.

**Validation**: Validated via qualitative expert assessment of participant outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Societal Impact

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was scrubbed of identifying information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants consented to data usage.

**Compliance With Regulations**: Not Applicable
