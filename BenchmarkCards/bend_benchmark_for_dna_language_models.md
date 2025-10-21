# BEND (Benchmark for DNA Language Models)

## 📊 Benchmark Details

**Name**: BEND (Benchmark for DNA Language Models)

**Overview**: BEND is a Benchmark for DNA Language Models, featuring a collection of realistic and biologically meaningful downstream tasks defined on the human genome, aimed at providing a standardized set of tasks that measure the ability of LMs to capture the intricacies of genomic data.

**Data Type**: text

**Domains**:
- Bioinformatics

**Languages**:
- English

**Similar Benchmarks**:
- Genomic Benchmarks
- Genome Understanding Evaluation

**Resources**:
- [GitHub Repository](https://github.com/frederikkemarin/BEND)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark to evaluate the effectiveness of different DNA language models in capturing genomic features relevant for downstream biological tasks.

**Target Audience**:
- ML Researchers
- Bioinformaticians

**Tasks**:
- Gene Finding
- Enhancer Annotation
- Chromatin Accessibility Prediction
- Histone Modification Prediction
- CpG Methylation Prediction
- Noncoding Variant Effects Prediction (Expression)
- Noncoding Variant Effects Prediction (Disease)

**Limitations**: N/A

## 💾 Data

**Source**: Data comes from multiple publicly available genomic datasets including GENCODE, ENCODE, GRASP, ClinVar, and the 1000 Genomes Project.

**Size**: 2,005,617 instances

**Format**: bed

**Annotation**: Annotations are made based on various genomic experiments and public datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Cross-validation

**Metrics**:
- Multiclass Matthews correlation coefficient (MCC)
- Area Under Precision-Recall Curve (AUPRC)
- Area Under Receiver Operating Characteristic Curve (AUROC)

**Calculation**: Metrics are calculated based on standard evaluation procedures for classification tasks.

**Interpretation**: Higher values indicate better performance in capturing genomic features relevant to the tasks.

**Baseline Results**: Comparative results included for existing state-of-the-art methods like AUGUSTUS and Enformer.

**Validation**: The collected tasks and their evaluations are based on established methodologies in bioinformatics, including comprehensive testing across various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of performance across different population groups included due to potential biases in the underlying genomic data.

**Potential Harm**: ['Misleading predictions that may affect genomic research and clinical applications']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The datasets used are governed by their respective licenses as mentioned in the paper, including usage restrictions where applicable.

**Consent Procedures**: The study does not require new data collection and thus does not entail new consent processes.

**Compliance With Regulations**: Not Applicable
