# KFinEval-Pilot: A Comprehensive Benchmark Suite for Korean Financial Language Understanding

## 📊 Benchmark Details

**Name**: KFinEval-Pilot: A Comprehensive Benchmark Suite for Korean Financial Language Understanding

**Overview**: KFinEval-Pilot is designed to evaluate large language models in the Korean financial domain. It includes over 1,000 questions curated across three areas: financial knowledge, legal reasoning, and financial toxicity, constructed through a semi-automated pipeline.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- Korean

**Similar Benchmarks**:
- PIXIU
- FinBen

**Resources**:
- [Resource](https://www.datop.or.kr/cmm/mainView.do)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models in the Korean financial domain and provide a standard framework for assessing financial AI applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Legal Reasoning
- Toxicity Detection

**Limitations**: The current version of KFinEval-Pilot does not comprehensively cover all sub-domains of finance and remains relatively modest in scope.

## 💾 Data

**Source**: Constructed from curated questions derived from financial knowledge resources, legal materials, and toxicity scenarios applicable to the Korean financial context.

**Size**: 1,145 questions

**Format**: JSON

**Annotation**: Semi-automated generation using GPT-4 prompts with human expert validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Scores calculated based on the correctness of model responses against expert-validated answers and the coherence of reasoning processes.

**Interpretation**: Higher scores indicate better reasoning and knowledge performance, with specific thresholds defined for accuracy and response quality.

**Validation**: Utilized a multi-step validation involving both initial checks and expert reviews to enhance reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data

**Demographic Analysis**: Included demographic considerations for fair evaluation across different user groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data privacy measures and anonymization procedures include the careful curation of financial scenarios to avoid personal identification.

**Data Licensing**: Data is collected from publicly available sources under permissive licenses. All uses are compliant with Korean financial regulations.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The benchmark has been designed to adhere to the regulatory frameworks of the Korean financial environment.
