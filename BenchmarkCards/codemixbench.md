# CodeMixBench

## 📊 Benchmark Details

**Name**: CodeMixBench

**Overview**: CodeMixBench is a novel benchmark designed to evaluate the robustness of large language models on code generation from code-mixed prompts, supporting Hinglish, Spanish-English, and Chinese Pinyin-English.

**Data Type**: code generation tasks with code-mixed prompts

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi
- Spanish
- Chinese
- English

**Similar Benchmarks**:
- BigCodeBench
- HumanEval
- MBPP

**Resources**:
- [Resource](https://huggingface.co/datasets/codemixbench)
- [GitHub Repository](https://github.com/user/codemixbench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for studying multilingual code generation and evaluate model robustness in code-mixed scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation
- Code Completion

**Limitations**: N/A

## 💾 Data

**Source**: Augmentation of BigCodeBench with controlled code-mixing for multilingual prompts.

**Size**: 6,840 total prompts

**Format**: N/A

**Annotation**: Automatically generated using LLM-driven augmentation pipeline.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass@1
- GAME score

**Calculation**: Pass@1 checks if the top-1 generated solution passes all associated test cases.

**Interpretation**: Higher Pass@1 indicates better performance in generating valid code under varying code-mixing conditions.

**Baseline Results**: Performance comparisons between code-mixed prompts and English-only prompts.

**Validation**: Results validated by executing generated code within isolated environments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark focuses on code-mixing in multilingual communities but lacks demographic breakdowns.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
