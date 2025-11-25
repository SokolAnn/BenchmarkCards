# GDGB (Generative DyTAG Benchmark)

## 📊 Benchmark Details

**Name**: GDGB (Generative DyTAG Benchmark)

**Overview**: GDGB comprises eight meticulously curated DyTAG datasets with high-quality textual features for nodes and edges, enabling rigorous evaluation of DyTAG generation tasks.

**Data Type**: text

**Domains**:
- E-commerce
- Social Network
- Web Interaction
- Celebrity Biography
- Movie Collaboration
- Citation

**Languages**:
- English

**Similar Benchmarks**:
- DTGB (Dynamic Text-Attributed Graph Benchmark)

**Resources**:
- [Resource](https://www.kaggle.com/datasets/f5e51c13e31f34cc84177d121c5902e0076c826d24e40414186024232e62973e)
- [GitHub Repository](https://github.com/Lucas-PJ/GDGB-ALGO)
- [Resource](https://gdgb-algo.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundational resource for advancing generative DyTAG research and evaluating DyTAG generation models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Transductive Dynamic Graph Generation
- Inductive Dynamic Graph Generation

**Limitations**: N/A

## 💾 Data

**Source**: Eight meticulously curated DyTAG datasets from various domains.

**Size**: N/A

**Format**: N/A

**Annotation**: Curated and processed by the authors to ensure high-quality textual attributes.

## 🔬 Methodology

**Methods**:
- Evaluation using multifaceted metrics
- LLM-based multi-agent framework for generative tasks

**Metrics**:
- Degree MMD
- Spectra MMD
- Power-law validity
- Textual Quality metrics based on LLM evaluation

**Calculation**: Metrics calculated according to the definitions provided for graph structural and textual assessments.

**Interpretation**: Lower Degree/Spectra MMD values indicate better preservation of structural fidelity, while higher textual quality scores reflect better attribute generation.

**Baseline Results**: Comparative results against existing models such as VRDAG and DG-Gen.

**Validation**: Experimental results demonstrate the efficacy of GDGB in evaluating DyTAG generation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Exposing personal information
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: Improper use of generated DyTAGs may risk generating misleading information or amplifying biases.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is under various licenses including CC BY 4.0 and CC BY-SA.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
