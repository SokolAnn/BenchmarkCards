# SOCRATIC-PRMB ENCH

## 📊 Benchmark Details

**Name**: SOCRATIC-PRMB ENCH

**Overview**: SOCRATIC-PRMB ENCH is designed to systematically evaluate Process Reward Models (PRMs) under six reasoning patterns: Transformation, Decomposition, Regather, Deduction, Verification, and Integration, comprising a total of 2995 reasoning paths with flaws categorized accordingly.

**Data Type**: reasoning paths

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Xiang-Li-oss/Socratic-PRMBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and fine-grained evaluation framework for Process Reward Models based on systematic reasoning patterns.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Error Detection

**Limitations**: Focus is primarily on reasoning tasks with objectively verifiable answers, such as mathematical problems.

## 💾 Data

**Source**: Constructed from various curated datasets including MATH-Hard and Open-o1, using a specialized Socratic reasoning model for generation.

**Size**: 2995 instances

**Format**: JSON

**Annotation**: Automated generation using LLMs with quality verification by human experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- PRM-Score (combination of F1 scores)

**Calculation**: PRM-Score is defined as a weighted combination of F1 and negative F1 scores.

**Interpretation**: A higher PRM-Score indicates better performance in correctly identifying and correcting reasoning errors.

**Validation**: Extensive experiments conducted on a range of state-of-the-art PRMs and LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
