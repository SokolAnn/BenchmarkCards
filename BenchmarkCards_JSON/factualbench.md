# FactualBench

## 📊 Benchmark Details

**Name**: FactualBench

**Overview**: A comprehensive and precise factual QA dataset containing 181k Chinese data spanning 21 domains, designed to facilitate both evaluation and training for reducing factual hallucinations in LLMs.

**Data Type**: QA

**Domains**:
- Film & Entertainment
- Education & Training
- Physics, Chemistry, Mathematics & Biology
- History & Traditional Culture
- Biography
- Politics & Law
- Economics & Management
- Computer Science
- Medical
- Sociology & Humanity
- Agriculture, Forestry, Fisheries & Allied Industries
- Astronomy & Geography
- Sports & Tourism
- Digital & Automotive
- Industrial Engineering
- Military & War
- Slang & Memes
- Work & Life
- High Technology
- Religion & Culture
- Others

**Languages**:
- Chinese

**Similar Benchmarks**:
- CMMLU
- TruthfulQA
- HalluQA
- HaluEval
- AlignBench
- AlpacaEval

**Resources**:
- [Resource](arXiv:2502.19127v1)
- [Resource](https://baike.baidu.com/)

## 🎯 Purpose and Intended Users

**Goal**: To mitigate factual hallucinations and enhance the factual accuracy of language models by providing a dataset specifically designed for factual QA.

**Target Audience**:
- Researchers
- Developers of AI
- Conversational AI systems

**Tasks**:
- Evaluating language models
- Training language models
- Testing against factuality benchmarks

**Limitations**: N/A

**Out of Scope Uses**:
- Non-factual QA tasks
- Open-ended question generation

## 💾 Data

**Source**: Internet encyclopedia (Baidu Baike)

**Size**: 181k

**Format**: QA pairs

**Annotation**: Human annotations for correctness and domain classification.

## 🔬 Methodology

**Methods**:
- Direct Preference Optimization (DPO)
- Self-memory alignment (SMA)

**Metrics**:
- Accuracy
- Factual precision metrics (e.g., FActScore)

**Calculation**: Performance evaluations based on multiple diverse benchmarks focusing on factuality and comprehensiveness.

**Interpretation**: Results are interpreted through comparisons against base models and existing benchmarks.

**Baseline Results**: Performance on benchmarks varied, with SMA achieving improvements across all evaluated tasks.

**Validation**: Models were validated by testing against FactualBench, which includes a testing subset of 3,462 questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data contamination
- Data bias
- Output bias
- Decision bias
- Privacy violations

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Robustness**: Data poisoning, Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sourced from publicly available encyclopedias, estimated privacy concerns with individual data use are addressed during data selection.

**Data Licensing**: Data was collected in compliance with public use policies of the encyclopedias reviewed.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
