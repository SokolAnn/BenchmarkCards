# PICBench

## 📊 Benchmark Details

**Name**: PICBench

**Overview**: PICBench is the first benchmarking and evaluation framework specifically designed to automate the design generation of Photonic Integrated Circuits (PICs) using LLMs. It includes 24 meticulously crafted PIC design problems, spanning from fundamental device designs to complex circuit-level designs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RTLLM
- VerilogEval
- SPICEPilot
- ChatEDA

**Resources**:
- [GitHub Repository](https://github.com/PICDA/PICBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of PICBench is to provide a comprehensive benchmark and evaluation methodology for automating the generation of PIC designs using LLMs.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Design Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated design problems and expert-written solutions for PIC design.

**Size**: 24 problems

**Format**: JSON

**Annotation**: Each problem is crafted by human experts and includes a ground-truth design for evaluation.

## 🔬 Methodology

**Methods**:
- Automated Evaluation
- Error Feedback Loop
- Simulation-based Testing

**Metrics**:
- Pass@k

**Calculation**: The Pass@k metric is calculated on the generated samples based on their correctness against unit tests.

**Interpretation**: A problem is considered solved if any of the k-generated samples passes the corresponding unit tests.

**Baseline Results**: Various existing LLMs were evaluated including GPT-4, GPT-o1-mini, Gemini 1.5 Pro, and Claude 3.5 Sonnet.

**Validation**: The benchmark uses an open-source simulator (SAX) to validate functionality and syntax of designs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
