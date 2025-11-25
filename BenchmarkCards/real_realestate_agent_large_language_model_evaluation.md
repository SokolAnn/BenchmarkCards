# REAL (RealEstate Agent Large Language Model Evaluation)

## 📊 Benchmark Details

**Name**: REAL (RealEstate Agent Large Language Model Evaluation)

**Overview**: REAL is the first evaluation suite designed to assess the abilities of large language models in the field of housing transactions and services. It includes 5,316 high-quality evaluation entries organized across 4 topics: memory, comprehension, reasoning, and hallucination.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- C-Eval
- CMMLU
- OpenbookQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models in the context of housing transactions and services.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Memory Evaluation
- Comprehension Evaluation
- Reasoning Evaluation
- Hallucination Evaluation

**Limitations**: The current scope of REAL is limited to Beijing and does not involve other cities.

## 💾 Data

**Source**: Real estate-related data collected from Beike corporation and client queries about residential issues from the Internet.

**Size**: 5,316 questions

**Format**: JSON

**Annotation**: All questions and corresponding answers were verified and checked by annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the percentage of correct answers across the evaluation categories.

**Interpretation**: Higher accuracy indicates better performance of LLMs in residential field tasks.

**Baseline Results**: All models evaluated and their performance metrics are documented in the paper.

**Validation**: All entries are verified manually before being included in the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data manipulation was performed to filter out personal information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
