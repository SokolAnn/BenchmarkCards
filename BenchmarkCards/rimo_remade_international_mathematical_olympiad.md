# RIMO (Remade International Mathematical Olympiad)

## 📊 Benchmark Details

**Name**: RIMO (Remade International Mathematical Olympiad)

**Overview**: RIMO is a two-track benchmark designed to evaluate mathematical reasoning by reformulating International Mathematical Olympiad problems into a deterministic format. It consists of RIMO-N, with 335 problems that allow for exact answer checking, and RIMO-P, featuring 456 proof problems with guided sub-problems for step-by-step reasoning evaluation.

**Data Type**: mathematical problems

**Domains**:
- Education

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- AIMO
- OLYMMATH
- OMNI-MATH

**Resources**:
- [GitHub Repository](https://github.com/username/repo)
- [Resource](https://huggingface.co/datasets/RIMO)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-resolution benchmark for evaluating advanced mathematical reasoning capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: International Mathematical Olympiad materials from 1959 to 2023

**Size**: 791 problems

**Format**: N/A

**Annotation**: Problems curated and transformed by experts

## 🔬 Methodology

**Methods**:
- Automated grading
- Expert grading

**Metrics**:
- Pass@1 accuracy

**Calculation**: Deterministic grading for RIMO-N based on a constant-time string match, and multi-step evaluation for RIMO-P.

**Interpretation**: Higher accuracy indicates better mathematical reasoning capabilities.

**Baseline Results**: Scores of ten models, with the highest being 62.96% on RIMO-N.

**Validation**: Results benchmarked against GSM8K and MATH datasets

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
