# HypoTermQA

## 📊 Benchmark Details

**Name**: HypoTermQA

**Overview**: HypoTermQA is a benchmarking dataset introduced for evaluating the hallucination tendency of Large Language Models (LLMs). It focuses on generating challenging questions related to hypothetical phenomena to assess how models handle non-existent terms.

**Data Type**: Benchmarking Dataset

**Domains**:
- General
- Law
- Health
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- HaluEval
- PHD
- AutoHall

**Resources**:
- [GitHub Repository](https://github.com/cemuluoglakci/HypoTermQA)

## 🎯 Purpose and Intended Users

**Goal**: To create a framework for benchmarking hallucination tendencies in LLMs and evaluate their performance in handling hypothetical terms.

**Target Audience**:
- Researchers
- Developers
- Academics

**Tasks**:
- Evaluating hallucination tendencies of LLMs
- Generating benchmarking datasets for specific domains

**Limitations**: The dataset is focused exclusively on hypothetical terms and may not cover all aspects of LLM performance or other types of hallucinations.

**Out of Scope Uses**:
- Training language models
- General natural language processing tasks

## 💾 Data

**Source**: OpenAI's GPT-3.5 model output

**Size**: 19,508 questions

**Format**: Text

**Annotation**: Each question is categorized as hypothetical or valid based on the terms used.

## 🔬 Methodology

**Methods**:
- Automated question generation
- LLM performance evaluation
- Hypothetical and valid term creation

**Metrics**:
- HypoTermQA Score
- Error rate

**Calculation**: HypoTermQA Score is calculated as the percentage of valid answers to hypothetical questions.

**Interpretation**: A higher score indicates better performance in resisting hallucination.

**Baseline Results**: Both GPT-3.5 and Llama2-70B models scored around 5.7% for hypothetical questions.

**Validation**: Evaluated using a combination of programmatic checks and LLM responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination tendencies
- Evaluation biases
- Improper generalization

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Misleading information generation', 'Increased reliance on factual inaccuracies']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is publicly available under specified usage policies.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
