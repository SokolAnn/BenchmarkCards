# PECC (Problem Extraction and Coding Challenges)

## 📊 Benchmark Details

**Name**: PECC (Problem Extraction and Coding Challenges)

**Overview**: The PECC dataset assesses the code generation capabilities of large language models across a spectrum of problem complexities, spanning both narrative and neutral contexts, derived from Advent Of Code and Project Euler challenges.

**Data Type**: programming problems with code solutions

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- APPS
- DS-1000

**Resources**:
- [GitHub Repository](https://github.com/HallerPatrick/pecc)
- [Resource](https://huggingface.co/datasets/PatrickHaller/pecc)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of LLMs in extracting problems from narrative descriptions and generating corresponding code solutions.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Code Generation
- Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Advent Of Code challenges and Project Euler problems

**Size**: 2,396 problems

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Qualitative error analysis

**Metrics**:
- Pass@k
- Pass@k-Difficulty

**Calculation**: Metrics are calculated by evaluating if generated code passes predefined unit tests.

**Interpretation**: Higher values in Pass@k and Pass@k-Difficulty indicate better model performance in generating effective code.

**Validation**: Tested against multiple language models including GPT-3.5-turbo and open-source alternatives.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
