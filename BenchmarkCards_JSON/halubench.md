# HaluBench

## 📊 Benchmark Details

**Name**: HaluBench

**Overview**: HaluBench is a comprehensive hallucination evaluation benchmark, consisting of 15k samples sourced from various real-world domains.

**Data Type**: benchmark

**Domains**:
- finance
- medicine

**Languages**:
- English

**Similar Benchmarks**:
- Halueval
- RAGTruth

**Resources**:
- [Resource](HuggingFace Model: https://huggingface.co/PatronusAI/Llama-3-Lynx-70B-Instruct)
- [Resource](HaluBench: https://huggingface.co/datasets/PatronusAI/HaluBench)
- [GitHub Repository](GitHub repo: https://github.com/patronus-ai/Lynx-hallucination-detection)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate hallucination detection in LLMs for Retrieval Augmented Generation systems.

**Target Audience**:
- Researchers
- Developers of AI systems
- Machine Learning practitioners

**Tasks**:
- Hallucination detection
- Evaluation of LLM responses
- Assessment of RAG systems

**Limitations**: Focuses solely on hallucination detection; other factors such as factuality not addressed.

**Out of Scope Uses**:
- Applications outside of hallucination detection
- Non-English datasets

## 💾 Data

**Source**: Various question answering datasets

**Size**: 15,000 samples

**Format**: JSON

**Annotation**: Annotated for presence of hallucinations

## 🔬 Methodology

**Methods**:
- Finetuning on various QA datasets
- Generating semantic perturbations of answers
- Human annotation for validation

**Metrics**:
- Accuracy
- Faithfulness to the context

**Calculation**: Comparison against baseline models to evaluate performance on hallucination tasks.

**Interpretation**: Higher accuracy indicates better performance in detecting hallucinations.

**Baseline Results**: LYNX (70B) achieved an overall accuracy of 87.4% on HaluBench against other models.

**Validation**: Compared against human annotated examples for quality assurance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential misinformation in AI-assisted applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open Source

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
