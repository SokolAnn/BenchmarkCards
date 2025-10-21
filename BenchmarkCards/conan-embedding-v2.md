# Conan-Embedding-v2

## 📊 Benchmark Details

**Name**: Conan-Embedding-v2

**Overview**: Conan-Embedding-v2 is a new LLM trained from scratch and fine-tuned as a text embedder to address the data and training gaps between LLMs and embedding models, incorporating a novel cross-lingual retrieval dataset for better multilingual integration.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MTEB (Massive Text Embedding Benchmark)
- Chinese MTEB

**Resources**:
- [Resource](https://arxiv.org/abs/2509.12892)

## 🎯 Purpose and Intended Users

**Goal**: To provide a new text embedding method through a novel LLM that achieves state-of-the-art performance on text embedding benchmarks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Embedding
- Cross-lingual Retrieval
- Classification
- Clustering

**Limitations**: N/A

## 💾 Data

**Source**: Created from a combination of multilingual corpora and various datasets for training and fine-tuning.

**Size**: Approximately 10 million pairs for cross-lingual retrieval dataset.

**Format**: N/A

**Annotation**: Utilizes low-quality filtering methods during data collection and employs human annotations for specific tasks.

## 🔬 Methodology

**Methods**:
- Weakly-supervised training
- Supervised training with dynamic hard negative mining

**Metrics**:
- Accuracy
- V-Meas
- Average Precision (AP)
- Mean Average Precision (MAP)
- nDCG at 10
- Spearman's Rank Correlation Coefficient

**Calculation**: Multiple metrics calculated across various embedding tasks.

**Interpretation**: Higher scores indicate better model performance on the respective embedding tasks.

**Baseline Results**: State-of-the-art performance compared to existing models like Mistral-7B.

**Validation**: Empirical evaluations demonstrate performance improvements through systematic training stages.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Analysis of language performance reveals disparities across language families.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
