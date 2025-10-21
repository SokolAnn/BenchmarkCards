# TiC-LM (Time-Continual Learning of Language Models)

## 📊 Benchmark Details

**Name**: TiC-LM (Time-Continual Learning of Language Models)

**Overview**: TiC-LM introduces a web-scale benchmark for time-continual pretraining of LLMs using a dataset derived from 114 dumps of Common Crawl, offering time-stratified evaluations across various domains.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Web Data
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- TemporalWiki
- StreamingQA
- EvolvingQA
- TempEL

**Resources**:
- [GitHub Repository](https://github.com/apple/ml-tic-lm)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating continual learning methods in LLMs with a temporal focus.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Continual Learning Evaluation
- Temporal Reasoning

**Limitations**: An important limitation is that the authors could not find a method that outperforms Oracle re-training on all evaluations.

## 💾 Data

**Source**: Common Crawl (CC) web data dumps from May 2013 to July 2024.

**Size**: 2.9T tokens

**Format**: Plain text

**Annotation**: Automatically processed and filtered using standard web scraping and cleanup techniques.

## 🔬 Methodology

**Methods**:
- Cyclic Cosine Learning Rate
- Replay-based Learning
- Regularization Methods (LwF, EWC)

**Metrics**:
- Perplexity
- In-distribution performance (ID)
- Backward transfer
- Forward transfer

**Calculation**: Performance metrics are calculated using a matrix of evaluations based on model training at different timestamps compared against Oracle baseline results.

**Interpretation**: Lower perplexity indicates better model performance, while metrics such as backward and forward transfer evaluate how well a model retains knowledge of past data and adapts to new data, respectively.

**Baseline Results**: Oracle re-training series evaluated every two years.

**Validation**: Assessments conducted across multiple evaluation timesteps and benchmarks against established Oracle models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning, Prompt injection attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Due to the nature of the dataset sourced from the web, concerns related to personally identifiable information exist.

**Data Licensing**: The data is sourced from Common Crawl, which is available under public domain for research.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
