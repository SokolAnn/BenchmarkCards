# C3 (free-form multiple-choice Chinese machine reading Comprehension dataset)

## 📊 Benchmark Details

**Name**: C3 (free-form multiple-choice Chinese machine reading Comprehension dataset)

**Overview**: The first free-form multiple-choice Chinese machine reading comprehension dataset (C3), containing 13,369 documents and 19,577 multiple-choice free-form questions collected from Chinese-as-a-second-language examinations. C3 includes two subsets: C3-D (dialogue) and C3-M (mixed-genre). The dataset is designed to require prior knowledge (linguistic, domain-specific, and general world knowledge) for many questions and to serve as a platform to study leveraging prior knowledge for text comprehension.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Chinese

**Similar Benchmarks**:
- RACE
- DREAM
- DuReader
- CMRC 2018
- ChID

**Resources**:
- [Resource](https://dataset.org/c3/)
- [Resource](https://arxiv.org/abs/1904.09679)
- [GitHub Repository](https://github.com/hankcs/HanLP)

## 🎯 Purpose and Intended Users

**Goal**: To introduce C3, a challenging free-form multiple-choice Chinese MRC dataset that requires linguistic, domain-specific, and general world prior knowledge; to present an analysis of required prior knowledge and to provide a platform for studying how to leverage various kinds of prior knowledge for text comprehension and for crosslingual/multilingual MRC research.

**Target Audience**:
- Researchers
- Model Developers

**Tasks**:
- Machine Reading Comprehension
- Question Answering

**Limitations**: C3 may not be suitable for evaluating the comprehension ability of machine readers on lengthy texts as the average document length in C3 is relatively short compared to datasets such as DuReader and RACE.

## 💾 Data

**Source**: Collected from Hanyu Shuiping Kaoshi (HSK) and Minzu Hanyu Kaoshi (MHK) Chinese-as-a-second-language examinations (real and practice exams) that are freely accessible online; problems are expert-designed in the original exams.

**Size**: 13,369 documents and 19,577 questions in total. Training: 8,023 documents / 11,869 questions; Development: 2,674 documents / 3,816 questions; Test: 2,672 documents / 3,892 questions.

**Format**: N/A

**Annotation**: Original questions and correct options come from exam materials designed by experts. Additionally, two authors annotated the types of required prior knowledge over a subset of 600 instances (inter-annotator agreement Cohen's kappa = 0.62).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Cohen's kappa

**Calculation**: Accuracy is reported as the percentage of questions for which the selected option matches the gold (correct) option. Cohen's kappa is reported for inter-annotator agreement on the prior-knowledge annotation (0.62).

**Interpretation**: Higher Accuracy indicates better model performance; the paper highlights a substantial gap between model performance and human performance (human readers 96.0%), particularly on questions requiring prior knowledge, indicating C3's difficulty.

**Baseline Results**: Random baseline ~27.8% accuracy. Distance-Based Sliding Window ~45.8-47.9% accuracy. Co-Matching ~48-55% accuracy (varies by subset). Pre-trained model baselines: BERT variants ~64-67% accuracy; BERT-wwm-ext (best-performing model reported) ~68.5% accuracy. Human performance: 96.0% accuracy.

**Validation**: Duplicate problems were removed and data were randomly split at the problem level into 60% training, 20% development, and 20% test. A subset of 600 instances was annotated for required prior-knowledge types by two annotators (authors) with Cohen's kappa = 0.62. Experiments were run with multiple random seeds and development-set selection.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
