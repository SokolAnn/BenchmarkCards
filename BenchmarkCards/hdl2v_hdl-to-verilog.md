# hdl2v (HDL-to-Verilog)

## 📊 Benchmark Details

**Name**: hdl2v (HDL-to-Verilog)

**Overview**: hdl2v is a dataset which seeks to increase the amount of available human-written Verilog data by translating or compiling three other hardware description languages—VHDL, Chisel, and PyMTL3—to Verilog. It consists of 46,549 pairs of translated hardware description languages to enhance LLM Verilog generation.

**Data Type**: code translation pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VerilogEval
- RTLLM

**Resources**:
- [Resource](https://huggingface.co/datasets/hdl2v/vhdl-dataset)
- [Resource](https://huggingface.co/datasets/hdl2v/chisel-dataset)
- [Resource](https://huggingface.co/datasets/hdl2v/pymtl3-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To enhance LLMs' ability to generate correct Verilog code through the use of HDL-to-Verilog translation datasets.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset comprises translations of VHDL, Chisel, and PyMTL3 into Verilog collected from public repositories and through code generation techniques.

**Size**: 46,549 pairs

**Format**: N/A

**Annotation**: Translation pairs created through automated compilation tools.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning
- Automated Metrics
- Evaluation using VerilogEvalV2

**Metrics**:
- Accuracy
- pass@1
- pass@10

**Calculation**: Accuracy is measured using the pass@1 and pass@10 metrics to determine the percentage of functional correctness.

**Interpretation**: Higher pass rates indicate better model performance in generating correct Verilog outputs.

**Baseline Results**: The model improves by up to 23% for pass@10 after fine-tuning with hdl2v.

**Validation**: Model performance is validated using VerilogEvalV2 which tests the correctness of generated Verilog.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
