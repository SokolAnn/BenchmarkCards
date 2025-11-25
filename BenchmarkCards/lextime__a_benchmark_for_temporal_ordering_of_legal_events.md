# LEXTIME: A Benchmark for Temporal Ordering of Legal Events

## 📊 Benchmark Details

**Name**: LEXTIME: A Benchmark for Temporal Ordering of Legal Events

**Overview**: LEXTIME is a dataset designed to evaluate LLMs’ event ordering capabilities in legal language, consisting of 512 instances from U.S. Federal Complaints with annotated event pairs and their temporal relations.

**Data Type**: event pairs with temporal relations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TRACIE

**Resources**:
- [GitHub Repository](https://github.com/clairebarale/LexTime)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the temporal reasoning capabilities of large language models (LLMs) specifically in the legal domain.

**Target Audience**:
- Researchers in Legal NLP
- Model Developers
- Practitioners in Legal Technology

**Tasks**:
- Temporal Event Ordering

**Limitations**: The dataset primarily focuses on event ordering which may not capture other temporal reasoning tasks.

## 💾 Data

**Source**: U.S. Federal Complaints

**Size**: 512 examples

**Format**: structured data

**Annotation**: Manually reviewed instances with event pairs and temporal relations labeled.

## 🔬 Methodology

**Methods**:
- Standard prompting
- Chain-of-thought prompting

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated as the proportion of correctly identified temporal relations between event pairs.

**Interpretation**: Higher accuracy indicates better model understanding of temporal relationships in legal contexts.

**Baseline Results**: Accuracy varying across models with GPT-4 Turbo achieving up to 80.8% for explicit-implicit pairs.

**Validation**: Evaluated on split datasets similar to the task design of TRACIE.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: No specific demographic analysis provided.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
