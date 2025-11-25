# MojoBench

## 📊 Benchmark Details

**Name**: MojoBench

**Overview**: MojoBench is the first framework for Mojo code generation, introducing HumanEval-Mojo, a benchmark dataset designed for evaluating code LLMs on Mojo, and Mojo-Coder, an LLM pretrained and finetuned for Mojo code generation.

**Data Type**: code snippets and programming tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- French
- Spanish
- Bangla

**Resources**:
- [GitHub Repository](https://github.com/mraihan-gmu/MojoBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance LLM capabilities specifically in the Mojo programming language.

**Target Audience**:
- ML Researchers
- Developers
- Domain Experts

**Tasks**:
- Code Generation
- Code Completion

**Limitations**: The limited availability of Mojo content on the web significantly constrained dataset sizes.

## 💾 Data

**Source**: Curated from publicly available sources including GitHub repositories, tutorials, and official documentation.

**Size**: 6,583,948 tokens

**Format**: text

**Annotation**: Manual curation and expert verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pass@1

**Calculation**: Performance is measured using the pass@1 metric, which indicates the percentage of correct code generation.

**Interpretation**: Higher pass@1 scores indicate better model performance in generating correct Mojo code.

**Validation**: Models were evaluated against the HumanEval-Mojo benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected strictly from publicly available sources ensuring compliance with ethical guidelines.

**Data Licensing**: Data sources used respect Apache 2.0 licensing.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
