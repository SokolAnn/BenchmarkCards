# Theoretically-Grounded Commonsense Reasoning (TG-CSR)

## 📊 Benchmark Details

**Name**: Theoretically-Grounded Commonsense Reasoning (TG-CSR)

**Overview**: TG-CSR is modeled as a set of question-answering instances, with each instance grounded in a semantic category of commonsense (e.g., time, space, emotions) and is intended to systematically evaluate machine commonsense in a few-shot QA setting. The benchmark is theoretically grounded in the Gordon and Hobbs representational areas and is released in phased splits to preempt overfitting.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Social IQa
- ATOMIC
- Cosmos QA
- CycIC
- SuperGLUE

**Resources**:
- [Resource](https://usc-isi-i2.github.io/TGCSR/)
- [Resource](https://codalab.lisn.upsaclay.fr/competitions/3080)
- [Resource](https://doi.org/10.48550/arXiv.2203.12184)

## 🎯 Purpose and Intended Users

**Goal**: To provide a theoretically-grounded benchmark that enables semantic evaluation of machine commonsense reasoning (CSR) abilities by grounding QA instances in representational categories from the Gordon-Hobbs theory and evaluating models in a few-shot QA setting.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Commonsense Reasoning

**Limitations**: The authors state that they do not claim completeness of the taxonomy and that the initial representation is an initial representation ("While we don’t claim completeness"), and that constructing some QA instances and category assignments can be challenging and subject to annotator disagreement.

## 💾 Data

**Source**: Dataset constructed by the authors/benchmark developers using contexts and themes grounded in the Gordon-Hobbs theory; first phase ("vacationing abroad" context) released as Public Data on the CodaLab competition leaderboard.

**Size**: 331 question-answer pairs total; training set: 81 examples; development set: 77 examples; test set: 173 examples.

**Format**: JSON (Javascript Object Notation) files

**Annotation**: Human annotators rated each answer option per question on a Likert scale of 1-4. Ground truth was derived by averaging annotations across annotators and collapsing 3-4 into 'yes' and 1-2 into 'no'. Annotator correlation/agreement reported as greater than 0.9.

## 🔬 Methodology

**Methods**:
- Human evaluation (annotator ratings averaged; leave-one-out inspired procedure for human performance estimation)
- Automated evaluation via CodaLab leaderboard (submission scoring)
- Generative model evaluation with manual matching to provided answer options

**Metrics**:
- F1 Score

**Calculation**: For human performance: collapse ratings (3-4 -> yes, 1-2 -> no). Use a leave-one-out inspired procedure: treat each annotator in turn as ground truth, take the mode of the remaining annotators as the prediction, compute an F1 score; average F1 scores across annotators. Model submissions are scored on the leaderboard using F1-Score against withheld test labels.

**Interpretation**: Higher F1 indicates better agreement with human-derived ground truth. Human performance on the released phase is reported as 80.5% overall and 79.9% on the test set; random baseline achieves about 35% F1. Authors note models are biased toward predicting 'No', motivating F1 over simple accuracy.

**Baseline Results**: Random baseline: 0.35 F1-Score; T0-small: 0.08 F1-Score; T0: 0.15 F1-Score; T0+: 0.0 F1-Score (as reported in Table 2); T0++: 0.603 F1-Score; Human: 0.799 F1-Score.

**Validation**: Validation via high annotator agreement (correlation > 0.9). Human performance computed using the leave-one-out inspired procedure described above. Test labels withheld on the leaderboard to mitigate observer bias.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination
- **Governance**: Unrepresentative risk testing, Lack of testing diversity

**Demographic Analysis**: Authors report annotator differences likely associated with age, sex, and cultural background and note these differences affected QA construction and annotation.

**Potential Harm**: ['Detecting and preventing overfitting of models to benchmark-specific statistical artifacts', 'Detecting cultural or demographic annotation bias in commonsense datasets']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
