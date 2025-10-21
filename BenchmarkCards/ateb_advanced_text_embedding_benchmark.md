# ATEB (Advanced Text Embedding Benchmark)

## 📊 Benchmark Details

**Name**: ATEB (Advanced Text Embedding Benchmark)

**Overview**: ATEB is a new benchmark designed to evaluate text embedding models on advanced NLP tasks such as reasoning, safety, factuality, and instruction-following. It emphasizes the limitations of current embedding models in handling complex text comprehension and processing, providing a comprehensive assessment across diverse real-world scenarios.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MTEB (Massive Text Embedding Benchmark)
- BEIR

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To highlight the limitations of existing embedding models in handling advanced NLP tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Factual Classification
- Safety Classification
- Instruction Following
- Reasoning

**Limitations**: While we included 21 tasks in our benchmark, many other safety, reasoning, and factuality tasks could be incorporated to increase the diversity and complexity of the benchmark.

## 💾 Data

**Source**: Various datasets curated from existing resources, reformulated to align with retrieval tasks.

**Size**: N/A

**Format**: N/A

**Annotation**: Tasks were annotated based on publicly available datasets.

## 🔬 Methodology

**Methods**:
- Contrastive loss
- Retrieval-based fine-tuning

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on task accuracy post-reformulation into retrieval tasks.

**Interpretation**: Higher accuracy indicates better performance of embedding models in advanced NLP tasks.

**Validation**: Evaluation across a range of 21 tasks simulating real-world scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
