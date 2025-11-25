# EducationQ

## 📊 Benchmark Details

**Name**: EducationQ

**Overview**: EducationQ introduces a multi-agent dialogue framework to assess the teaching capabilities of Large Language Models (LLMs) through simulated dynamic educational scenarios, enabling efficient evaluation of LLMs-as-Teachers across various disciplines.

**Data Type**: question-answering pairs

**Domains**:
- Education

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- GPQA (Graduate Proofreading Question Answering)

**Resources**:
- [GitHub Repository](https://github.com/SunriserFuture/EducationQ)
- [Resource](https://arxiv.org/abs/2504.14928v3)

## 🎯 Purpose and Intended Users

**Goal**: To efficiently evaluate the teaching capabilities of LLMs within dynamic educational scenarios, examining their effectiveness in simulated teacher-student interactions.

**Target Audience**:
- Education Researchers
- AI Developers
- Educational Institutions

**Tasks**:
- Teaching Effectiveness Evaluation
- Question-Answering
- Pedagogical Strategy Analysis

**Limitations**: The evaluation framework cannot fully capture the complexity of teaching roles and capabilities in practice, particularly regarding classroom dynamics and diverse student profiles.

## 💾 Data

**Source**: Curated from established benchmarks GPQA and MMLU-Pro, featuring questions across various disciplines and difficulty levels.

**Size**: 1,498 questions

**Format**: JSON

**Annotation**: Questions were standardized and validated by educational experts.

## 🔬 Methodology

**Methods**:
- Automated qualitative analysis
- Human evaluation

**Metrics**:
- Absolute Learning Gain (ALG)
- Positive-Negative Impact Ratio (PNIR)
- Cross-Subject Stability (CSS)

**Calculation**: Metrics calculated based on pre-test and post-test results from student interactions with LLMs.

**Interpretation**: Higher ALG indicates better teaching effectiveness. Lower PNIR and CSS values suggest more stable and consistent teaching performance across subjects.

**Baseline Results**: Llama 3.1 70B Instruct achieved 12.63% learning gain on evaluated questions.

**Validation**: Validation achieved through high agreement (78%) between automated qualitative analyses and human expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias

**Demographic Analysis**: Limited demographic factors were analyzed due to a focus on educational effectiveness across diverse LLM outputs.

**Potential Harm**: Potential biases in LLM interactions affecting educational outcomes.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Utilizes publicly available datasets (GPQA, MMLU-Pro) following their terms of use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
