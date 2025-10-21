# OMGEval (Open Multilingual Generative Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: OMGEval (Open Multilingual Generative Evaluation Benchmark)

**Overview**: OMGEval is an Open-source Multilingual Generative test set that can assess the capability of LLMs in different languages. For each language OMGEval provides 804 open-ended questions covering capabilities such as general knowledge and logical reasoning. Each question is verified by human annotators and non-English questions are localized for cultural context. The current version includes 5 languages (Chinese, Russian, French, Spanish, Arabic). GPT-4 is employed as the adjudicator to automatically score model outputs.

**Data Type**: open-ended question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- Russian
- French
- Spanish
- Arabic

**Similar Benchmarks**:
- AlpacaEval
- Stanford AlpacaEval
- SuperCLUE
- MT-Bench
- MMLU
- XNLI
- PAWS-X
- XCOPA
- Belebele
- XQA
- TyDi-QA
- Xor-QA
- MLQA
- XQuAD
- MKQA
- M3Exam

**Resources**:
- [GitHub Repository](https://github.com/blcuicall/OMGEval)
- [GitHub Repository](https://github.com/tatsu-lab/alpaca_eval)
- [Resource](https://guanaco-model.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: Provide an open multilingual generative evaluation benchmark to assess LLMs' capabilities across different languages and cultural contexts and to serve as a reference for understanding and improving multilingual capability of LLMs.

**Target Audience**:
- Research community

**Tasks**:
- Question Answering
- Text Generation
- Language Comprehension
- Logical Reasoning
- Code Generation
- Mathematical Problem Solving
- Chit chat / Dialogue
- Harmlessness evaluation

**Limitations**: The proposed dataset only contains five language types in the current version.

**Out of Scope Uses**:
- Use outside research purposes (authors recommend exclusive use for research purposes)

## 💾 Data

**Source**: Derived from AlpacaEval foundational data (805 instructions) and translated, manually localized, and verified into target languages.

**Size**: 804 examples per language (current version includes 5 languages)

**Format**: N/A

**Annotation**: Manual annotation and rigorous verification by human experts: each language team comprises two annotators and one reviewer (annotators/reviewers possess master's degrees in the respective language's linguistics).

## 🔬 Methodology

**Methods**:
- Automated evaluation with GPT-4 adjudicator (following AlpacaEval methodology)
- Human evaluation (annotators) for validation and correlation analysis

**Metrics**:
- Win rate
- Standard error
- Precision
- Recall
- F1 Score
- Pearson correlation coefficient

**Calculation**: Using GPT-4 as an adjudicator to compare the evaluated model's output with a baseline model's output and compute win rate and standard error. For validation, human judges compare outputs from two models and results are compared to GPT-4 judgments to compute Precision, Recall, F1 and Pearson correlation.

**Interpretation**: Higher win rate indicates the evaluated model outperforms the baseline in pairwise comparisons. GPT-4 is reported as the only model surpassing a 50 average win rate (its reported win rate is 55.52), and GPT-4's scores align closely with human annotations according to the authors.

**Baseline Results**: Baseline: GPT-3.5-Turbo (used as baseline after GPT-text-davinci-003 deprecation) with a 50.0 win rate; GPT-4 achieved a reported 55.52 win rate (average) on OMGEval.

**Validation**: Human annotation was conducted for Chinese and Spanish with samples of 100 data points per language (50 localized, 50 other). Table 5 reports Precision, Recall, F1 between human and GPT-4 evaluations: Chinese full testset: Precision 0.81, Recall 0.94, F1 0.88; Chinese localization subset: Precision 0.70, Recall 0.91, F1 0.79; Spanish full testset: Precision 0.92, Recall 0.92, F1 0.91; Spanish localization subset: Precision 0.90, Recall 0.90, F1 0.89. The paper also states a Pearson correlation coefficient of 0.93% between GPT-4 and human-judged results (as reported).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Cultural biases (the benchmark aims to detect/address cultural biases and English-centric bias)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
