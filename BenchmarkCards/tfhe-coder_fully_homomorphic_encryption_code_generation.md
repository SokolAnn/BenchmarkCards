# TFHE-Coder (Fully Homomorphic Encryption Code Generation)

## 📊 Benchmark Details

**Name**: TFHE-Coder (Fully Homomorphic Encryption Code Generation)

**Overview**: This work establishes the first benchmark for TFHE code generation, demonstrating how LLMs, when augmented with domain-specific feedback, can bridge the expertise gap in FHE code generation.

**Data Type**: code generation

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/jinaai/jina-embeddings-v2-base-code)
- [Resource](https://tfhe.github.io/tfhe/gate-bootstrapping-api.html)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM performance in generating TFHE code from natural language specifications.

**Target Audience**:
- ML Researchers
- Cryptography Experts
- Developers

**Tasks**:
- Code Generation

**Limitations**: The most challenging function remains the ReLU, with consistently low performance across all models.

## 💾 Data

**Source**: Experiments conducted on TFHE code generation with various LLMs.

**Size**: N/A

**Format**: Code

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Iterative feedback via compiler diagnostics
- Retrieval-augmented generation (RAG)
- Few-shot prompting

**Metrics**:
- Pass@k (comp)
- Pass@k (func)
- CrystalBLEU

**Calculation**: Metrics are calculated based on the proportion of generated code that compiles and executes correctly, as well as similarity to reference implementations.

**Interpretation**: Higher scores indicate better compilability and functional correctness.

**Baseline Results**: GPT-4o demonstrated the highest performance with near-perfect scores across tasks.

**Validation**: Evaluation conducted using multiple mainstream LLMs under controlled experimental conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Misleading code generation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
