# SCIGYM

## 📊 Benchmark Details

**Name**: SCIGYM

**Overview**: SCIGYM is a benchmark that assesses LLMs’ iterative experiment design and analysis abilities in open-ended scientific discovery tasks using a dry lab setup.

**Data Type**: SBML models for biological systems

**Domains**:
- Natural Language Processing
- Biology

**Languages**:
- English

**Similar Benchmarks**:
- BioDiscoveryAgent
- DiscoveryWorld

**Resources**:
- [Resource](https://h4duan.github.io/scigym-benchmark/)
- [GitHub Repository](https://github.com/h4duan/SciGym)
- [Resource](https://huggingface.co/datasets/h4duan/scigym-sbml)
- [Resource](https://huggingface.co/datasets/h4duan/scigym-eval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models' capabilities in conducting scientific experiments and analysis in a simulated biological context.

**Target Audience**:
- ML Researchers
- Biologists
- AI Practitioners

**Tasks**:
- Experiment Design
- Data Analysis

**Limitations**: Performance of models declines significantly with increasing system complexity.

## 💾 Data

**Source**: 350 SBML models curated from BioModels database

**Size**: 350 models

**Format**: SBML

**Annotation**: Curated and filtered to remove unusable models

## 🔬 Methodology

**Methods**:
- Evaluation of LLMs through simulated experiments
- Performance comparison among models

**Metrics**:
- Simulation Trajectory Error (STE)
- Reaction Matching Score (RMS)
- Network Topology Score (NTS)

**Calculation**: Metrics are calculated based on the similarity between predicted and actual biological models.

**Interpretation**: Lower STE and higher RMS/NTS indicate better performance in recovering the underlying biological mechanisms.

**Baseline Results**: Performance comparisons were made against zero-shot prompting results of the models.

**Validation**: Validated through experimental simulations and comprehensive performance metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Scientific Misconduct
- Overfitting
- Methodological Limitations

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
