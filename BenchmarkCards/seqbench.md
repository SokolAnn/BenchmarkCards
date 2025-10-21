# seqBench

## 📊 Benchmark Details

**Name**: seqBench

**Overview**: seqBench is a parametrized benchmark for probing sequential reasoning limits in Large Language Models (LLMs) through precise control over logical depth, backtracking steps, and noise ratio.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ZebraLogic
- GridPuzzle
- BABILong
- MuSR
- Dyna-bAbI
- GRASP
- SPARTQA
- SpaRTUN
- StepGame

**Resources**:
- [Resource](https://huggingface.co/datasets/emnlp-submission/seqBench)

## 🎯 Purpose and Intended Users

**Goal**: To probe and analyze sequential reasoning capabilities in language models by systematically controlling key complexity factors.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Sequential Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated from a controlled algorithmic pathfinding process.

**Size**: 7,079 instances

**Format**: Various structured task configurations in natural language.

**Annotation**: Automatically annotated with logical depth, backtracking count, and noise ratio.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Pass@1 Success Rate
- Progress Ratio
- Precision
- Recall

**Calculation**: Success Rate measures the proportion of runs with correct action sequences, Progress Ratio is k/n where n is total actions and k is correctly executed actions.

**Interpretation**: Pass@1 Success Rate indicates exact matches to ground truth, and Progress Ratio assesses how far models progress before errors occur.

**Validation**: 5 independent runs per problem to establish robust performance statistics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
