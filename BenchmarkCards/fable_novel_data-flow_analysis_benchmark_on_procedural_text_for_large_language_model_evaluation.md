# FABLE (Novel Data-Flow Analysis Benchmark on Procedural Text for Large Language Model Evaluation)

## 📊 Benchmark Details

**Name**: FABLE (Novel Data-Flow Analysis Benchmark on Procedural Text for Large Language Model Evaluation)

**Overview**: FABLE is an extensible benchmark designed to assess LLMs’ understanding of data flow using structured, procedural text. It adapts eight classical data-flow analyses from software engineering across domains like cooking recipes, travel routes, and automated plans.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- WIQA
- TORQUE
- CREPE

**Resources**:
- [GitHub Repository](https://github.com/VishalPallagani/FABLE)
- [Resource](https://huggingface.co/datasets/g-nitin/FABLE)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate data-flow reasoning in large language models through procedural texts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Data-Flow Reasoning
- Procedural Understanding

**Limitations**: The dataset's construction over three curated domains introduces specific biases. The approaches and definitions used for data-flow analyses are limited to current interpretations.

## 💾 Data

**Source**: Constructed from three distinct procedural domains: recipes, travel routes, and automated plans.

**Size**: 2,400 question-answer pairs

**Format**: JSON

**Annotation**: Automatically generated via templates based on classical data-flow analyses.

## 🔬 Methodology

**Methods**:
- Majority voting over multiple completions
- Template-based question generation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the proportion of correct predictions compared to ground-truth annotations from the dataset.

**Interpretation**: Higher accuracy indicates better data-flow reasoning capabilities of the models.

**Validation**: Validation is based on empirical tests across the benchmark, comparing different types of LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark analysis does not include demographic breakdowns.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The data is based on publicly available content and complies with open access principles.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
