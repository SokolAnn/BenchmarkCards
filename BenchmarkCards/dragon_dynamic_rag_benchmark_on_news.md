# DRAGON (Dynamic RAG Benchmark On News)

## 📊 Benchmark Details

**Name**: DRAGON (Dynamic RAG Benchmark On News)

**Overview**: DRAGON is the first dynamic benchmark for evaluating RAG (Retrieval-Augmented Generation) systems in Russian on a changing news corpora, addressing the need for standardized evaluation tools for RAG systems in the Russian language.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Russian

**Similar Benchmarks**:
- KILT
- NoMIRACL
- RusBEIR

**Resources**:
- [GitHub Repository](https://github.com/RussianNLP/DRAGON)
- [Resource](https://huggingface.co/spaces/ai-forever/rag-leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and dynamic benchmark for evaluating retrieval-augmented generation systems in Russian and support reproducible and community-driven research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: While the proposed benchmark provides a valuable framework for evaluating RAG systems, it relies on a specific domain (news) and currently only supports Russian language documents.

## 💾 Data

**Source**: Regularly updated corpus of Russian news and public documents.

**Size**: N/A

**Format**: N/A

**Annotation**: Automatically generated questions using a Knowledge Graph constructed from the corpus.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE-L
- Hit Rate
- Recall
- NDCG

**Calculation**: Metrics are calculated based on the performance of retrieval and generation components against the ground truth.

**Interpretation**: High scores indicate better retrieval and generation capabilities of the RAG systems.

**Baseline Results**: N/A

**Validation**: The benchmark includes a validation portal for assessing submissions against private datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark addresses potential biases in retrieval and generation processes.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Datasets included in the benchmark are sourced following strict privacy regulations and guidelines.

**Data Licensing**: The framework is released under the MIT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
