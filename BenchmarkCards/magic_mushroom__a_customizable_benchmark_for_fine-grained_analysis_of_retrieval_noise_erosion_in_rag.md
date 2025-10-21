# Magic Mushroom: A Customizable Benchmark for Fine-grained Analysis of Retrieval Noise Erosion in RAG Systems

## 📊 Benchmark Details

**Name**: Magic Mushroom: A Customizable Benchmark for Fine-grained Analysis of Retrieval Noise Erosion in RAG Systems

**Overview**: Magic Mushroom is a benchmark designed to evaluate the robustness of Retrieval-Augmented Generation (RAG) systems under complex retrieval noise, enabling flexible configurations of noise types and proportions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RECALL
- RAG-Bench
- NoiserBench
- Robust RALM

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM robustness under complex retrieval noise and facilitate the development of noise-robust RAG systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Built on Natural Questions and HotpotQA datasets.

**Size**: 11,393 question-answer pairs

**Format**: N/A

**Annotation**: Documents were manually verified for factual and structural integrity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Correctness
- Rejection Rate

**Calculation**: Correctness is scored by comparing generated answers to gold answers.

**Interpretation**: Higher correctness scores indicate better model performance in noise conditions.

**Baseline Results**: Various baseline models tested include Llama-3.1 8B and Qwen-2.5 1.5B.

**Validation**: Results averaged over independent runs to ensure statistical reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
