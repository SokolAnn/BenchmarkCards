# OneStopQA

## 📊 Benchmark Details

**Name**: OneStopQA

**Overview**: OneStopQA, a new high-quality dataset for evaluation and analysis of reading comprehension in English that implements the STARC (Structured Annotations for Reading Comprehension) annotation framework, combining a principled four-choice answer structure with manual span annotations for correct answers and distractors.

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- RACE
- SQuAD
- Natural Questions
- MCTest
- MS MARCO
- TriviaQA
- NewsQA

**Resources**:
- [Resource](https://arxiv.org/abs/2004.14797)

## 🎯 Purpose and Intended Users

**Goal**: Provide a principled annotation framework (STARC) and a high-quality multiple-choice reading comprehension dataset (OneStopQA) for robust testing, automated annotation quality probing, and detailed analyses of human and machine reading comprehension behavior.

**Target Audience**:
- Natural Language Processing researchers
- Model developers
- Education assessment researchers

**Tasks**:
- Question Answering
- Reading Comprehension

**Limitations**: OneStopQA is considerably smaller than RACE (30 articles, 162 paragraphs, 486 questions per text-difficulty-level; 1,458 question-paragraph pairs across three difficulty versions).

**Out of Scope Uses**:
- Primary large-scale model training (OneStopQA is intended primarily for testing and analyses and is presented as a complement to larger training datasets such as RACE)

## 💾 Data

**Source**: OneStopEnglish corpus (Guardian News Lessons articles from onestopenglish.com / Macmillan Education)

**Size**: 30 articles; 162 paragraphs; 4-7 paragraphs per article; 486 questions (3 per paragraph per difficulty level); 1,458 question-paragraph pairs across three difficulty versions

**Format**: N/A

**Annotation**: Manual annotation: annotator draft creation followed by first-round review by a second annotator ('reviewer'), iterative piloting on Prolific with targeted edits, and final proofreading and span verification. All spans were annotated manually for each question in all three paragraph versions.

## 🔬 Methodology

**Methods**:
- Automated evaluation of model accuracy
- Ablation experiments (full component ablations and span ablations)
- Crowdsourced human evaluation (Prolific)
- In-lab human experiments

**Metrics**:
- Accuracy
- Choice rate distribution across answer types (A/B/C/D)
- Human consensus percentage (Question Validity)
- Ceiling approximation (derived score based on question validity)
- Readability estimates (Flesch Kincaid, SMOG) as corpus statistics

**Calculation**: Accuracy is reported as percent correct. Ceiling approximation: assign valid questions score 1; assign invalid questions score 1 divided by the average number of answers considered correct across participants (where no correct answer is treated as 4). Choice rates are reported as percent selection for each answer type (A/B/C/D).

**Interpretation**: Higher human ceiling and lower percentage of invalid/guessable questions indicate higher dataset item quality. The authors report approximate ceilings of 88.8% for RACE and 97.9% for OneStopQA; in-lab human ceilings: 84.7% for RACE and 95.3% for OneStopQA. Datasets with ceilings near model performance (e.g., RACE) limit meaningful model improvements.

**Baseline Results**: Key reported baseline accuracies (All splits): RoBERTa Large: 82.9% on RACE (All), 85.6% on OneStopQA (no finetuning, All), 86.0% on OneStopQA (finetuned, All). RoBERTa Base: 68.4% on RACE (All), 68.8% on OneStopQA (All). Stanford Attentive Reader: 42.8% on RACE (All), 34.3% on OneStopQA (All). Random baseline: 25.0%.

**Validation**: Annotation and dataset quality validated via iterative piloting on Prolific with targeted edits, crowdsourced Question Validity Judging (three annotators per item) to identify invalid questions, in-lab human experiments to estimate empirical ceiling, and ablation experiments (span and component ablations) demonstrating tight correspondence between answers and annotated spans and robustness to guessing heuristics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Governance**: Unrepresentative risk testing

**Demographic Analysis**: N/A

**Potential Harm**: Detects guessable questions and low item quality (question validity) that can lead to misleading evaluation of models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Human subject data collected under MIT IRB protocol #1605559077; all subjects provided written consent prior to participation.

**Compliance With Regulations**: Human subject research oversight via MIT IRB protocol #1605559077.
