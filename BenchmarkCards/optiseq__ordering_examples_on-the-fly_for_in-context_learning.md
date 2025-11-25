# OptiSeq: Ordering Examples On-The-Fly for In-Context Learning

## 📊 Benchmark Details

**Name**: OptiSeq: Ordering Examples On-The-Fly for In-Context Learning

**Overview**: OptiSeq is a novel method that orders in-context examples dynamically at inference time to enhance the performance of large language models on various tasks. It improves accuracy by optimizing the sequence of examples presented to the model, as shown through extensive empirical evaluation across multiple datasets and tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolBench
- RestGPT
- AG News
- SST-5
- TREC

**Resources**:
- [Resource](https://arxiv.org/abs/2501.15030)

## 🎯 Purpose and Intended Users

**Goal**: To optimize the ordering of in-context examples for large language models at inference time to improve task performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- API Sequence Generation
- Text Classification

**Limitations**: OptiSeq requires evaluating k=|E|! permutations, which introduces computational challenges as the number of in-context examples grows.

## 💾 Data

**Source**: The datasets used include ToolBench, RestGPT, AG News, SST-5, and TREC, each containing various instances for evaluation.

**Size**: Multiple datasets with various numbers of instances (e.g., 100 classes in ToolBench, 75 in RestGPT, etc.)

**Format**: N/A

**Annotation**: Data is pre-existing datasets that do not require additional annotation.

## 🔬 Methodology

**Methods**:
- Empirical evaluation across datasets
- Performance comparison against random and Top-K selections

**Metrics**:
- Accuracy
- Precision
- Recall

**Calculation**: Accuracy is based on exact matching of generated API sequences with ground truth; Precision and Recall represent relevancy in predictions.

**Interpretation**: Higher values in Accuracy, Precision, and Recall indicate better performance of the model with respect to the correct API selection.

**Baseline Results**: OptiSeq improves accuracy by 10.5 percentage points over random selection, and 6.5 percentage points over Top-K selection across various tasks.

**Validation**: The benchmarks were validated through empirical evaluation comparing outputs with different ordering strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
