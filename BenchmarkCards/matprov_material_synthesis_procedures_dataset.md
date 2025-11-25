# MatPROV (Material Synthesis Procedures Dataset)

## 📊 Benchmark Details

**Name**: MatPROV (Material Synthesis Procedures Dataset)

**Overview**: MatPROV is a dataset of PROV-DM-compliant synthesis procedures extracted from scientific literature using large language models, which captures structural complexities and causal relationships among materials, operations, and conditions through directed graphs.

**Data Type**: synthesis procedures represented as directed graphs

**Domains**:
- Natural Language Processing
- Materials Science

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/MatPROV-project/MatPROV)
- [GitHub Repository](https://github.com/MatPROV-project/matprov-experiments)
- [Resource](https://matprov-project.github.io/matprov-schema)

## 🎯 Purpose and Intended Users

**Goal**: To provide a flexible framework for representing synthesis procedures that captures real-world complexities and enables automated synthesis planning and optimization.

**Target Audience**:
- ML Researchers
- Materials Scientists
- Industry Practitioners

**Tasks**:
- Graph-based analysis
- Material synthesis optimization

**Limitations**: MatPROV remains relatively small in scale compared with existing datasets and has potential extraction accuracy issues.

**Out of Scope Uses**:
- Direct synthesis implementation without prior validation against original sources.

## 💾 Data

**Source**: Synthesis procedures extracted from 1,568 open-access scientific papers.

**Size**: 2,367 procedures

**Format**: PROV-JSONLD

**Annotation**: Automated extraction using LLMs, followed by expert validation for accuracy.

## 🔬 Methodology

**Methods**:
- Automated extraction using LLMs

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated by comparing LLM outputs with expert-annotated ground truth.

**Interpretation**: Higher scores in precision and F1 indicate better model performance in accurately capturing synthesis procedures.

**Baseline Results**: Demonstrated extraction accuracy metrics through zero-shot prompting evaluation.

**Validation**: Expert validation was performed on a subset of the dataset to ensure extraction quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for incorrect synthesis information leading to failed experiments or safety hazards.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under CC BY 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
