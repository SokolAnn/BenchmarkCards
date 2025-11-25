# TransportationGames

## 📊 Benchmark Details

**Name**: TransportationGames

**Overview**: TransportationGames is a carefully designed and thorough evaluation benchmark for assessing (M)LLMs in the transportation domain, focusing on their capabilities in memorizing, understanding, and applying transportation knowledge through various tasks.

**Data Type**: multimodal

**Domains**:
- Transportation

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- CMMLU
- BIG-bench
- MMBench
- LegalBench
- LawBench
- MIR-based benchmark
- ChemLLM-Bench

**Resources**:
- [Resource](http://transportation.games)

## 🎯 Purpose and Intended Users

**Goal**: To accurately evaluate the capabilities of (M)LLMs in executing transportation-related tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Traffic Concepts Question Answering
- Traffic Regulations Question Answering
- Traffic Signs Question Answering
- Traffic Accidents Analysis
- Traffic Public Sentiment Analysis
- Traffic Safety Recommendation
- Traffic Sign Error Detection
- Traffic Road Occupation Detection
- Traffic Emergency Plan Generation
- Traffic Safety Education Copy Generation

**Limitations**: Data leakage due to the use of data from the internet. Evaluation of long text generation is challenging owing to non-uniqueness of answers.

## 💾 Data

**Source**: Data for TransportationGames is primarily sourced from internet examination papers, accident reports, public sentiment from news websites, and institutional articles.

**Size**: N/A

**Format**: N/A

**Annotation**: Data has been processed with manual verification to ensure accuracy and coherence.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- ROUGE

**Calculation**: Metrics are calculated based on golden answers, with accuracy for multiple-choice and True/False tasks, and ROUGE for generation tasks.

**Interpretation**: The higher the metric score, the better the performance of the model.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through extensive testing on various (M)LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive information was removed during data processing to safeguard privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
