# POPQUORN (the Potato-Prolific dataset for Question-Answering, Offensiveness, text Rewriting and politeness rating with demographic Nuance)

## 📊 Benchmark Details

**Name**: POPQUORN (the Potato-Prolific dataset for Question-Answering, Offensiveness, text Rewriting and politeness rating with demographic Nuance)

**Overview**: POPQUORN contains 45,000 annotations from 1,484 annotators, drawn from a representative sample regarding sex, age, and race as the US population. It is a large-scale NLP dataset for four tasks (offensiveness detection, question answering, politeness style transfer/text rewriting, and politeness rating) collected to measure how annotator demographics influence labels and annotator performance.

**Data Type**: question-answering pairs; offensiveness ratings (1-5 Likert); text rewriting pairs (original and rewritten emails); politeness ratings (1-5 Likert) — all text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Ruddit
- SQuAD 2.0
- Enron

**Resources**:
- [GitHub Repository](https://github.com/Jiaxin-Pei/potato-prolific-dataset)
- [GitHub Repository](https://github.com/wujunjie1998/Politenessr)
- [Resource](https://huggingface.co/Seethal/sentiment_analysis_generic_dataset)
- [Resource](https://huggingface.co/s-nlp/roberta-base-formality-ranker)
- [Resource](https://pypi.org/project/certainty-estimator/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a systematic examination of how annotators' demographic background affects perceptions and performance across diverse annotation tasks, and to release a demographically representative annotation dataset (POPQUORN) for research.

**Target Audience**:
- Natural Language Processing researchers
- Machine Learning researchers
- Industry practitioners

**Tasks**:
- Offensiveness detection
- Question Answering
- Text Rewriting / Style Transfer (politeness rewriting)
- Politeness Rating

**Limitations**: The root causes of performance disparities cannot be directly tested from the survey. Demographic categories are based on US Census questions to estimate a balanced US sample, which may limit generalizability outside the US.

## 💾 Data

**Source**: Instances sampled from Ruddit (Reddit comments), SQuAD 2.0 (passage-question pairs), and Enron email dataset; annotations collected via Prolific using a US-population representative sampling procedure; annotation interface built with POTATO.

**Size**: 45,000 annotations; 1,484 annotators; 7,647 instances in total across four tasks (per-task breakdown: Offensiveness: 13,036 annotations for 1,500 instances; Question Answering: 4,576 annotations for 1,000 instances; Text Rewriting: 2,346 annotations for 1,429 instances; Politeness Rating: 25,042 annotations for 3,718 instances).

**Format**: N/A

**Annotation**: Crowdsourced via Prolific with US-population representative sampling. Offensiveness and politeness: 1-5 Likert scale ratings. Question Answering: span identification (annotators highlighted text). Text rewriting: annotators rewrote emails to be more polite (free-text). Demographics collected after study with consent; pilot studies conducted; MACE used to compute annotator competence and filter low-competence annotators; annotators paid $12 per hour.

## 🔬 Methodology

**Methods**:
- Crowdsourced annotation via Prolific with US-representative sampling
- Pilot studies for task validation
- Annotator competence estimation using MACE
- Inter-annotator agreement measurement with Krippendorff's alpha
- Aggregation via majority answer (QA) with shorter-answer tie-breaker
- Automated metric evaluation (SQuAD evaluation script for QA)
- Mixed-effect linear regression analyses to measure demographic effects
- Manual error analysis (sampled instances)

**Metrics**:
- F1 Score
- Precision
- Recall
- Krippendorff's alpha
- Pearson's correlation (r)
- Edit distance
- BERTScore
- BLEU

**Calculation**: For QA: used the SQuAD evaluation script to compute token-level precision, recall, and F1; aggregated answers by majority vote and used the shorter answer in ties as in Rajpurkar et al. Inter-annotator agreement measured with Krippendorff's alpha. Correlations with existing dataset scores computed using Pearson's r. Annotator competence computed using MACE. Text revision similarity measured with edit distance, BERTScore, and BLEU.

**Interpretation**: Differences in aggregated annotations and task performance across demographic groups indicate that annotator background systematically influences labels and reading/comprehension performance. For example, higher education is associated with better QA performance; Black or African American participants rated the same email as more polite and the same comment as more offensive relative to other groups. Moderate-to-low Krippendorff's alpha values are expected for subjective tasks.

**Baseline Results**: QA aggregated answers achieved 0.75 F1, 0.72 precision, and 0.79 recall. Offensiveness: 13,036 annotations, Krippendorff's alpha = 0.29, correlation between averaged annotations and original Ruddit score = 0.67. Politeness rating: 25,042 annotations, Krippendorff's alpha = 0.43. (All numbers reported in the paper.)

**Validation**: Pilot studies conducted per task (e.g., 8 participants for offensiveness and politeness rating pilots, 18 participants for rewriting pilot). Annotator competence assessed with MACE and low-competence annotators removed. Manual examination of QA errors (50 instances) compared crowd annotations to SQuAD ground truth to validate aggregation quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy
- Accuracy
- Societal Impact
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Societal Impact**: Impact on affected communities
- **Governance**: Lack of data transparency

**Demographic Analysis**: Dataset collected from 1,484 annotators sampled to be representative of the US population with respect to sex, age, and race. Analyses show demographic associations with labels and performance: e.g., higher education correlates with higher QA F1; Black annotators rate comments as more offensive and emails as more polite; age and gender effects reported per task.

**Potential Harm**: ['Bias leading to marginalization of populations whose views differ from the majority', 'Underestimation of offensiveness for Black and Asian people when trained on demographically skewed annotations', 'Potential social harm from models reflecting biased annotations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Collecting background information is treated as sensitive: participants were allowed to select 'Prefer not to disclose' and to self-describe identities. Demographic information was collected after the study with an explanation and consent for sharing, following best practices cited (Spiel et al., 2019).

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants were shown consent questions prior to tasks that could contain offensive content. Demographic/background questions were asked after the study with an explanation for their collection and an explicit opt-out ('prefer not to disclose').

**Compliance With Regulations**: Not Applicable
