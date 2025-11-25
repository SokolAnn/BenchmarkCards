# arXivBench

## 📊 Benchmark Details

**Name**: arXivBench

**Overview**: arXivBench is a benchmark specifically designed to assess LLM performance across eight major subject categories on arXiv and five subfields within computer science. It provides a standardized tool for evaluating LLM reliability in scientific contexts, promoting more dependable academic use in research environments.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- REASONS

**Resources**:
- [GitHub Repository](https://github.com/liningresearch/arXivBench)
- [Resource](https://huggingface.co/datasets/arXivBenchLLM/arXivBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of arXivBench is to evaluate the accuracy of large language models in generating relevant research papers and their associated arXiv links.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: One limitation is the coverage of only major subjects on arXiv, potentially missing areas such as social sciences and humanities.

## 💾 Data

**Source**: The dataset is composed of 6,500 prompts from various academic fields, primarily from arXiv, and includes prompts generated using a large language model.

**Size**: 6,500 prompts

**Format**: N/A

**Annotation**: Prompts generated using a language model and processed to assess model outputs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is determined by evaluating the model outputs against valid arXiv links.

**Interpretation**: Higher accuracy rates indicate better model performance in generating relevant and accurate papers.

**Validation**: The evaluation utilized a cross-reference approach with updated Kaggle arXiv dataset to ensure current information.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
