# JailFlipBench

## 📊 Benchmark Details

**Name**: JailFlipBench

**Overview**: JailFlipBench is a benchmark specifically designed to capture implicitly harmful scenarios where harmless-looking prompts can lead to dangerous incorrect responses, addressing LLM vulnerabilities related to implicit harm.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- German

**Similar Benchmarks**:
- MMLU
- TruthfulQA
- SorryBench

**Resources**:
- [Resource](https://jailflip.github.io/arXiv:2506.07402v1)

## 🎯 Purpose and Intended Users

**Goal**: To systematically assess the overlooked risk of implicit harm in LLMs by evaluating their performance on benign queries that may yield harmful outputs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed through a multi-stage curation process involving topic filtering, question generation, and fine-grained validation.

**Size**: 6,608 instances

**Format**: N/A

**Annotation**: Manual verification and LLM-assisted filtering

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Factual Accuracy
- Attack Success Rate (ASR)

**Calculation**: Factual Accuracy is calculated based on the correctness of model responses to the yes/no questions.

**Interpretation**: Higher accuracy rates indicate less vulnerability to implicitly harmful prompts.

**Baseline Results**: N/A

**Validation**: Comprehensive evaluation of various LLMs including GPT-4 and Claude models to establish baseline performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential real-world harm from factually incorrect responses']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
