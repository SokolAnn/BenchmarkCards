# ReliableMath

## 📊 Benchmark Details

**Name**: ReliableMath

**Overview**: ReliableMath is a benchmark designed to systematically investigate the reliability of Large Language Models (LLMs) on reasoning tasks in mathematics by evaluating their performance on both solvable and unsolvable mathematical problems.

**Data Type**: mathematical problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- AIME
- AMC
- Minerva

**Resources**:
- [Resource](https://huggingface.co/datasets/aimo/aimo-validation-aime)
- [Resource](https://huggingface.co/datasets/AI-MO/aimo-validation-amc)
- [Resource](https://huggingface.co/datasets/math-ai/minervamath)
- [GitHub Repository](https://github.com/hendrycks/math/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the reliability of LLMs in solving mathematical reasoning tasks, including both solvable and unsolvable problems.

**Target Audience**:
- ML Researchers
- Model Developers
- Educators

**Tasks**:
- Mathematical Reasoning

**Limitations**: The investigation of ReliableMath is solely limited to mathematical reasoning, while other reasoning tasks have not been explored.

## 💾 Data

**Source**: Open-source solvable and human-evaluated unsolvable mathematical problems

**Size**: 1,375 problems (both solvable and unsolvable)

**Format**: structured data format containing questions and answers

**Annotation**: Human evaluations and synthesis from existing datasets

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Prudence

**Calculation**: Precision is calculated as the ratio of successful answers to the total number of solvable questions, while Prudence evaluates the ratio of refused responses.

**Interpretation**: Higher precision indicates more reliable answers, while prudence evaluates the reliability of refusal responses.

**Baseline Results**: Baseline models evaluated include reasoning and instruction LLMs like DeepSeek-R1 and GPT-4.

**Validation**: The dataset and results were validated through extensive human evaluations and automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data was collected under ethical guidelines, ensuring participant privacy and informed consent were prioritized.

**Data Licensing**: The datasets used are open-source and publicly available.

**Consent Procedures**: Informed consent was obtained from contributors involved in data annotation.

**Compliance With Regulations**: Not Applicable
