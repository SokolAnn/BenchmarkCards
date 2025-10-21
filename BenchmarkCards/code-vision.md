# CODE-VISION

## 📊 Benchmark Details

**Name**: CODE-VISION

**Overview**: CODE-VISION is a benchmark designed to evaluate the logical understanding and code generation capabilities of Multimodal Large Language Models (MLLMs) by challenging them to generate correct programs based on given flowcharts.

**Data Type**: code generation problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMCode
- MathVista

**Resources**:
- [GitHub Repository](https://github.com/wanghanbinpanda/CodeVision)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multimodal large language models' logical understanding and code generation capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Code Generation
- Algorithmic Problem Solving
- Mathematical Problem Solving

**Limitations**: The dataset size of CODE-VISION is relatively limited, especially in the Hard category of the Algorithm and MATH subsets.

## 💾 Data

**Source**: Collected from LeetCode and HumanEval.

**Size**: 438 total problems

**Format**: N/A

**Annotation**: Manually curated from various programming sources.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Error analysis

**Metrics**:
- Pass@1

**Calculation**: Pass@1 represents the probability that at least one correct solution appears among the top k generated solutions for each problem.

**Interpretation**: Higher Pass@1 implies better model performance in generating correct code from flowcharts.

**Baseline Results**: Proprietary models like GPT-4o achieved a top score of 79.3% on hard problems.

**Validation**: No explicit detailed validation procedures mentioned.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
