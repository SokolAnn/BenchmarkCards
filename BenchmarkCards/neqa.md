# NeQA

## 📊 Benchmark Details

**Name**: NeQA

**Overview**: NeQA: a question answering dataset consisting of questions with negation, designed to evaluate the ability of language models to process negation and which yields different scaling trends (inverse, U-shaped, or positive) depending on prompting methods and model families.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NegatedLAMA
- OBQA
- TruthfulQA

**Resources**:
- [GitHub Repository](https://github.com/yuhui-zh15/NeQA)
- [Resource](https://arxiv.org/abs/2305.17311)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of language models to process negation in natural language by providing a multiple-choice question answering dataset containing negated questions.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering
- Negation Understanding

**Limitations**: The dataset may miss some types of negation or domains of text; NeQA is an English-only dataset; evaluation results may be sensitive to specific prompts (prompt sensitivity).

## 💾 Data

**Source**: Constructed by transforming questions from NegatedLAMA (including ConceptNet, GoogleRE, SQuAD, TREx) and OBQA, plus additional rule-based negation transformations on OBQA to create diverse negation types.

**Size**: 1,718 questions (ConceptNet: 150 questions; GoogleRE: 374 questions; SQuAD: 100 questions; TREx: 594 questions; OBQA: 500 questions)

**Format**: N/A

**Annotation**: Created via rule-based transformations with manual examination and editing; labels redistributed/balanced between options A and B; wrong answer sampled from original incorrect choices for some transformations; validity checked manually and via crowdsourced validation (see paper).

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Zero-shot with hint prompting
- Few-shot chain-of-thought prompting
- Automated metric evaluation (probability ranking of choices)
- Model evaluation across multiple language model families

**Metrics**:
- Accuracy

**Calculation**: For zero-shot and zero-shot with hint: generate one token and rank the probability of selecting option A or B; for few-shot with chain-of-thought: generate full reasoning and parse final answer using regular expressions. Report accuracy of model predictions (dataset is balanced, chance = 50%).

**Interpretation**: Higher accuracy indicates better ability to answer negated questions. Scaling trends are interpreted as: positive scaling = performance improves with model scale; inverse scaling = performance degrades with model scale; U-shaped = performance degrades then improves with scale. Chance accuracy is 50% for the balanced two-choice dataset.

**Baseline Results**: Example results from paper (NeQA accuracy): GPT-3 zero-shot: ada 0.54, babbage 0.54, curie 0.36, davinci 0.33. GPT-3 Text Series few-shot w/ CoT: davinci-v2 0.98, davinci-v3 0.98. Full tables of model-by-prompt results are provided in the paper (Table 1 and Table 2).

**Validation**: Dataset validity ensured through manual examination and editing. As part of the inverse scaling prize submission, organizers crowdsourced validation on 50 random NeQA examples and reported average agreement between workers and gold labels of 100%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety
- Societal Impact
- Governance

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Value Alignment**: Harmful output
- **Societal Impact**: Impact on affected communities
- **Governance**: Lack of testing diversity

**Demographic Analysis**: N/A

**Potential Harm**: Incorrect handling of negation leading to wrong outputs that could cause harmful decisions in high-stakes domains (e.g., finance, healthcare, law) as stated in the Ethics Statement.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
