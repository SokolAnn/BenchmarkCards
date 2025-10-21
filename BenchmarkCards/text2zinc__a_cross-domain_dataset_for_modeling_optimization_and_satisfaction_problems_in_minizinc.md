# TEXT2ZINC: A Cross-Domain Dataset for Modeling Optimization and Satisfaction Problems in MINIZINC

## 📊 Benchmark Details

**Name**: TEXT2ZINC: A Cross-Domain Dataset for Modeling Optimization and Satisfaction Problems in MINIZINC

**Overview**: TEXT2ZINC is a unified, cross-domain dataset that combines both optimization and satisfaction problems expressed in natural language. It aims to bridge the gap between natural language descriptions and formal constraint models using a solver-agnostic modeling language.

**Data Type**: optimization and satisfaction problem instances

**Domains**:
- Operations Research
- Artificial Intelligence
- Mathematics

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/skadio/text2zinc)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for evaluating language-to-model translation in combinatorial optimization and satisfaction problems.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Optimization Experts

**Tasks**:
- Modeling Optimization Problems
- Modeling Satisfaction Problems

**Limitations**: N/A

## 💾 Data

**Source**: Carefully curated from various datasets including NL4OPT, NLP4LP, ComplexOR, CSPLib, and Hakank’s collection.

**Size**: 110 problem instances

**Format**: JSON, DZN, and MZN files

**Annotation**: Manually curated and enriched with metadata for quality and consistency.

## 🔬 Methodology

**Methods**:
- Baseline experiments with LLMs using prompting strategies
- Comparison of different techniques for model generation

**Metrics**:
- Execution Accuracy
- Solution Accuracy

**Calculation**: Execution accuracy is the proportion of generated models that compile and execute successfully. Solution accuracy is the proportion of generated models that achieve the same objective value as the ground truth.

**Interpretation**: Higher execution accuracy indicates better model generation capabilities and successful compilations. Solution accuracy reflects the quality of the generated models against known solutions.

**Validation**: Automated verification of input parameters against DZN files.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
