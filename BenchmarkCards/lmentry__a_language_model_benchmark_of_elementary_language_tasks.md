# LMentry: A Language Model Benchmark of Elementary Language Tasks

## 📊 Benchmark Details

**Name**: LMentry: A Language Model Benchmark of Elementary Language Tasks

**Overview**: LMentry is a benchmark that requires only very basic language abilities, designed to complement common approaches for evaluating large language models. LMentry consists of 25 tasks which humans are generally expected to perform perfectly, and measures both a model's accuracy and its robustness to a variety of trivial input perturbations. LMentry provides an LMentry score, a single aggregate score combining accuracy and multiple aspects of robustness, and is intended for zero-shot evaluation.

**Data Type**: text (prompt-response / example pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- oLMpics
- bAbI
- HANS
- CheckList

**Resources**:
- [GitHub Repository](https://github.com/aviaefrat/lmentry)
- [Resource](https://arxiv.org/abs/2211.02069)

## 🎯 Purpose and Intended Users

**Goal**: Provide quick and interpretable insights into the capabilities and robustness of large language models using a compact set of trivial tasks; serve as a quick, automatic, and easy-to-run zero-shot "unit test" complementary to large benchmark suites.

**Target Audience**:
- ML Researchers
- Research community
- Labs with fewer resources

**Tasks**:
- Sentence containing word
- Sentence not containing word
- Word containing letter
- Word not containing letter
- Most associated word
- Least associated word
- Any words from category
- All words from category
- First alphabetically
- More letters
- Less letters
- Bigger number
- Smaller number
- Rhyming word
- Homophones
- Word after in sentence
- Word before in sentence
- Sentence starting with word
- Sentence ending with word
- Word starting with letter
- Word ending with letter
- First word of the sentence
- Last word of the sentence
- First letter of the word
- Last letter of the word

**Limitations**: As LMentry tasks are diverse in form, not every robustness aspect can be measured on every task.

## 💾 Data

**Source**: Author-created task templates and instantiated examples; sentence examples for some tasks sourced from the Corpus of Linguistic Acceptability (Warstadt et al., 2019); homophones from the legacy Earlham homophone list (legacy.earlham.edu/~peters/writing/homofone.htm) as curated by the authors; category wordlists based on the A1 and A2 CEFR wordlists of the Cambridge English Profile (https://www.englishprofile.org/american-english).

**Size**: 110,703 examples (3,000 examples per task; 1,000 instantiations per template, with exceptions for the homophones task and some character-level tasks)

**Format**: N/A

**Annotation**: Automatic evaluation using approximately 10 regular-expression patterns per task (an output is scored 1 if it matches any pattern, 0 otherwise). Automatic scoring validated by manual evaluation (Cohen's kappa > 0.99 on sampled predictions). Human performance measured via a small human study (10 random examples per task, 250 examples total) with no incorrect answers under LMentry automatic evaluation.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Automated evaluation via regular-expression scoring
- Human validation / human evaluation (validation studies)

**Metrics**:
- LMentry score
- Accuracy
- Robustness (measured across four aspects: argument order, argument content, template, adjacent tasks)

**Calculation**: Accuracy is calculated as the mean accuracy over the 25 LMentry tasks. Each robustness aspect is calculated as the mean over all tasks to which it applies; for an individual task and robustness aspect, the aspect score is 100 - max_{i != j} |acc(c_i) - acc(c_j)| where c_i are cases the aspect considers. A model's LMentry score is its accuracy multiplied by its robustness, and is always a percentage.

**Interpretation**: The LMentry score can be viewed as a model's accuracy penalized by its brittleness; higher is better. Human performance on LMentry is approximately 100%, and models substantially below 100% indicate accuracy and/or robustness failures on trivial tasks.

**Baseline Results**: Best performing model: TextDavinci002 (175B, instruction-finetuned) with LMentry score 66.1%. InstructGPT 175B scores 48.4%. No other evaluated model scores higher than 41%. Human performance is ~100%.

**Validation**: Automatic evaluation validated by sampling 100 predictions per task from 5 strong baselines (~12,000 examples); Cohen's kappa between automatic and manual evaluation was over 0.99. Additionally, a human study sampled 10 random examples per task (250 examples total) among five untrained annotators; using LMentry's automatic evaluation, no incorrect answers were found.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Transparency**: Uncertain data provenance

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
