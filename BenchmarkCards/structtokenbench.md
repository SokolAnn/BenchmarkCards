# StructTokenBench

## 📊 Benchmark Details

**Name**: StructTokenBench

**Overview**: StructTokenBench is a comprehensive evaluation framework designed to assess the quality and efficiency of protein structure tokenization methods, using four key perspectives: downstream effectiveness, sensitivity, distinctiveness, and codebook utilization efficiency.

**Data Type**: protein structure data

**Domains**:
- Healthcare

**Languages**:
- N/A

**Similar Benchmarks**:
- TAPE
- ProteinGLUE
- ATOM3D
- FLIP
- PEER

**Resources**:
- [GitHub Repository](https://github.com/KatarinaYuan/StructTokenBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified benchmark for evaluating protein structure tokenization methods across various tasks and perspectives.

**Target Audience**:
- ML Researchers
- Bioinformaticians

**Tasks**:
- Functional Site Prediction
- Catalytic Site Prediction
- Conserved Site Prediction
- Binding Site Prediction
- Structural Flexibility Prediction
- Remote Homology Detection
- Epitope Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Datasets collected from ATLAS, InterPro, BioLIP2, ProteinShake, ProteinGLUE, TAPE, CAMEO, and CASP14.

**Size**: Various - ranging from tens to tens of thousands of examples across 10 datasets.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- AUROC
- Spearman's ρ
- Macro F1
- PCC
- Cosine Similarity
- Utilization Rate (UR)
- Perplexity
- Marginal Utility of Vocabulary (MUV)

**Calculation**: Metrics are calculated based on the structural representations extracted from protein structures using PST.

**Interpretation**: Higher metrics indicate better performance in evaluating structural representations.

**Baseline Results**: VQ-V AE-based and IF-based PST methods evaluated across various tasks.

**Validation**: Validation procedures included various datasets split methods to ensure effective performance evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
