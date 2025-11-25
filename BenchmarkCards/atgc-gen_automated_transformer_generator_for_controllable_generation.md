# ATGC-Gen (Automated Transformer Generator for Controllable Generation)

## 📊 Benchmark Details

**Name**: ATGC-Gen (Automated Transformer Generator for Controllable Generation)

**Overview**: ATGC-Gen is a language model framework for controllable DNA sequence generation that supports flexible conditioning on diverse biological modalities, enabling biologically meaningful sequence design under complex control constraints. The benchmark includes evaluation metrics to assess functionality, fluency, and diversity, introduced via a new dataset derived from ChIP-Seq experiments.

**Data Type**: DNA sequences

**Domains**:
- Biological Sciences
- Genomics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/divelab/AIRS/blob/main/OpenBio/ATGC_Gen)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the effectiveness of controllable DNA sequence generation models against established biological properties.

**Target Audience**:
- ML Researchers
- Biologists
- Genomic Researchers

**Tasks**:
- Controllable DNA Sequence Generation
- DNA-Protein Binding Sequence Generation

**Limitations**: Despite promising results, the work is constrained by limited computational resources, preventing the training of larger models.

## 💾 Data

**Source**: ChIP-Seq experiments data derived from the ENCODE project

**Size**: approximately 10 million rows

**Format**: N/A

**Annotation**: Annotated protein-DNA binding relationships based on ChIP-Seq experiments

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Functionality
- Fluency
- Diversity

**Calculation**: Metrics are calculated based on predictive modeling using the SEI framework for chromatin profiles and fluency measures via perplexity in a pretrained model.

**Interpretation**: Lower scores in functionality and fluency indicate better performance in generating biologically relevant sequences.

**Baseline Results**: ATGC-Gen outperforms strong baselines in generating accurate, coherent, and diverse sequences under various biological conditions.

**Validation**: Extensive performance evaluations across multiple generations tasks, including promoter and enhancer sequences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Societal Impact**: Impact on affected communities
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential risks associated with unintended synthesis of harmful sequences.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: N/A - Data from ENCODE project; no license required.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
