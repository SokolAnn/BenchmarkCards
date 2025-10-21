# BioMaze

## 📊 Benchmark Details

**Name**: BioMaze

**Overview**: BioMaze is a benchmark designed to evaluate LLMs’ ability to understand and reason about biological pathways, containing 5.1K high-quality, complex biological pathway problems derived from real research.

**Data Type**: question-answering pairs

**Domains**:
- Biological Sciences

**Languages**:
- English

**Similar Benchmarks**:
- BioASQ-QA
- ChatPathway

**Resources**:
- [GitHub Repository](https://github.com/zhao-ht/BioMaze)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning abilities of LLMs in biological tasks through the lens of biological pathways.

**Target Audience**:
- ML Researchers
- Biologists
- Domain Experts

**Tasks**:
- Biological Pathway Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from over 6,000 biological pathway research papers, involving True/False and open-ended questions.

**Size**: 5,100 questions

**Format**: N/A

**Annotation**: Questions reviewed and validated by human experts.

## 🔬 Methodology

**Methods**:
- Chain-of-Thought (CoT)
- Graph-Augmented Reasoning
- P ATHSEEKER

**Metrics**:
- Accuracy

**Calculation**: Accuracy for True/False tasks is averaged across True and False labels; open-ended tasks involve comparing generated answers to ground truth.

**Interpretation**: Higher accuracy indicates better reasoning ability in biological pathways.

**Baseline Results**: CoT and various graph-augmented methods including PATHSEEKER were used for comparison.

**Validation**: Evaluation results across various biological reasoning tasks were validated.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
