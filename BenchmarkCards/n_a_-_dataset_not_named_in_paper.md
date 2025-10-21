# N/A - Dataset not named in paper

## 📊 Benchmark Details

**Name**: N/A - Dataset not named in paper

**Overview**: The paper introduces a new dataset of Bulgarian multiple-choice reading-comprehension questions (2,633 questions) collected from 12th grade matriculation exams and online history quizzes, and studies zero-shot transfer from English (models fine-tuned on RACE) to Bulgarian using Multilingual and Slavic BERT. The paper also proposes a pipeline to extract relevant contexts from Wikipedia using information retrieval and evaluates various indexing and pre-training strategies.

**Data Type**: text (multiple-choice question-answer pairs)

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Bulgarian

**Similar Benchmarks**:
- SQuAD
- CoQA
- MS Macro
- RACE
- MCTest
- MS MARCO
- ARC

**Resources**:
- [GitHub Repository](http://github.com/mhardalov/bg-reason-BERT)
- [GitHub Repository](http://github.com/deepmipt/Slavic-BERT-NER)
- [Resource](http://www.elastic.co/)
- [Resource](http://dumps.wikimedia.org/)

## 🎯 Purpose and Intended Users

**Goal**: To build a task and dataset for a low-resource language (Bulgarian) to evaluate zero-shot multilingual transfer for multiple-choice reading comprehension, and to provide a pipeline for extracting relevant contexts from Wikipedia.

**Tasks**:
- Multiple-Choice Reading Comprehension

**Limitations**: The dataset contains multiple-choice questions without explanatory contexts; resource scarceness in low-resource languages is noted as a challenge.

## 💾 Data

**Source**: Twelfth grade matriculation exams created by the Ministry of Education of Bulgaria (2008–2019) and online history quizzes; Wikipedia (Bulgarian dump) was used as external corpus for context retrieval.

**Size**: 2,633 multiple-choice questions

**Format**: N/A

**Annotation**: Correct answers as provided in the original matriculation exams and online quizzes.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (fine-tuned Multilingual BERT and Slavic BERT)
- Automated metrics (Accuracy)
- Information retrieval for context retrieval
- Ablation study and per-category analysis

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the proportion of correctly answered multiple-choice questions, following the notation from Lai et al. (2017) (RACE).

**Interpretation**: Higher accuracy indicates better performance; the paper reports that an accuracy of 42.23% is well above the random baseline of 24.89% and other non-random baselines.

**Baseline Results**: Random baseline: 24.89% accuracy; Basic IR + BERT baseline: 29.62% accuracy; Best model (paragraph split + described query fields): 42.23% accuracy; Slavic pre-training result: 33.27% accuracy.

**Validation**: Validation via ablation study, per-category analysis, and comparison to random and non-random baselines; evaluation performed on a Bulgarian testset and on RACE dev for English pre-training experiments.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
