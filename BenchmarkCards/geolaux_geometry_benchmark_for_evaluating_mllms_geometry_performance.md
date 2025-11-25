# GeoLaux (Geometry Benchmark for Evaluating MLLMs’ Geometry Performance)

## 📊 Benchmark Details

**Name**: GeoLaux (Geometry Benchmark for Evaluating MLLMs’ Geometry Performance)

**Overview**: GeoLaux is a benchmark for evaluating Multimodal Large Language Models (MLLMs) on long-step geometry problems specifically addressing the auxiliary line construction. It contains 2,186 geometry problems with an average of 6.51 reasoning steps, facilitating fine-grained evaluation of MLLM reasoning.

**Data Type**: geometry problems

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- Chinese

**Similar Benchmarks**:
- Geometry3K
- GeoQA+
- UniGeo
- PGDP9K
- GPSM4K
- GeoMath-QA
- GeoEval

**Resources**:
- [GitHub Repository](https://github.com/Candice-yu/GeoLaux)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation benchmark for MLLMs in solving long-step geometry problems requiring auxiliary lines.

**Target Audience**:
- ML Researchers
- Model Developers
- Educational Institutions

**Tasks**:
- Geometry Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Zhongkao mathematics papers across 34 provincial-level regions in China

**Size**: 2,186 problems

**Format**: N/A

**Annotation**: Manually curated solutions and reasoning steps with auxiliary line constructions

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Answer Correctness Score (ACS)
- Process Correctness Score (PCS)
- Process Quality Score (PQS)

**Calculation**: ACS evaluates final answer accuracy, PCS checks correctness of the entire solution process including errors, and PQS assesses the quality of reasoning steps evaluated via a weighted scoring system.

**Interpretation**: Higher scores indicate better performance in answering and reasoning accuracy of MLLMs on complex geometry problems.

**Baseline Results**: Performance results of 13 leading MLLMs were evaluated, with distinct findings based on step lengths and problem types.

**Validation**: The benchmark's effectiveness was validated through extensive testing across various MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
