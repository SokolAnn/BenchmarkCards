# A Dataset of Peer Reviews (PeerRead) (PeerRead v1)

## 📊 Benchmark Details

**Name**: A Dataset of Peer Reviews (PeerRead) (PeerRead v1)

**Overview**: We present the first public dataset of scientific peer reviews available for research purposes (PeerRead v1), providing an opportunity to study this important artifact. The dataset consists of 14.7K paper drafts and the corresponding accept/reject decisions in top-tier venues including ACL, NIPS and ICLR, and includes 10.7K textual peer reviews for a subset of the papers. We describe the data collection process, report observed phenomena in peer reviews, and propose two NLP tasks based on this dataset: predicting paper acceptance and predicting numerical review aspect scores.

**Data Type**: text (paper drafts and textual peer reviews, accept/reject labels, and aspect scores)

**Domains**:
- Natural Language Processing
- Machine Learning
- Artificial Intelligence

**Similar Benchmarks**:
- Publons
- Crossref

**Resources**:
- [GitHub Repository](https://github.com/allenai/PeerRead)
- [Resource](https://arxiv.org/abs/1804.09635)

## 🎯 Purpose and Intended Users

**Goal**: Lower the barrier to studying peer reviews for the scientific community by introducing the first public dataset of peer reviews for research purposes (PeerRead).

**Target Audience**:
- The scientific community
- Inexperienced authors and first-time reviewers
- Reviewers
- Area chairs
- Program chairs
- Other researchers (e.g., NLP/ML researchers)

**Tasks**:
- Text Classification (Paper acceptance prediction)
- Regression (Review aspect score prediction)

**Limitations**: Data collection varies across sections, so different sections may have different license agreements. The CoNLL 2016 section is small (22 papers, 39 reviews) and too small for training. Aspect annotations were inferred from review text and annotators could infer about half of the aspect scores; re-annotation consistency was 77% (2% inconsistent). Some arXiv labels (probably-rejected vs accepted) can be noisy; a sanity check found a small number of labeling errors.

## 💾 Data

**Source**: Collected from multiple sources: opt-in submissions coordinated with conference systems (CoNLL 2016, ACL 2017), public peer reviews from NIPS 2013–2017, OpenReview reviews for ICLR 2017, and arXiv submissions from 2007–2017 (matched to target venues to label accepted/probably-rejected).

**Size**: 14,784 paper drafts and 10,770 textual reviews (total dataset size reported as 14.7K papers and 10.7K reviews).

**Format**: JSON (json-encoded text files with paper objects), PDF for each paper, and extracted text obtained via Science Parse.

**Annotation**: 1.3K reviews were annotated with seven aspect scores (appropriateness, clarity, originality, soundness/correctness, meaningful comparison, substance, impact) by two of the authors using ACL 2016 instructions; aspect scores are integers on a 1–5 scale, with a special 'not discussed' value when an aspect is not addressed in the review. Opted-in sections include reviewer-provided aspect scores where available.

## 🔬 Methodology

**Methods**:
- Automated evaluation using classification and regression models
- Human annotation (aspect score annotation by authors)
- 5-fold cross-validation for hyperparameter tuning
- Train/dev/test splits with 0.90:0.05:0.05

**Metrics**:
- Accuracy
- Root Mean Squared Error (RMSE)
- Mean Squared Error (MSE)
- Error reduction relative to majority baseline

**Calculation**: Acceptance prediction: report test set Accuracy (%) using standard train/dev/test splits and hyperparameter tuning via 5-fold cross-validation. Aspect prediction: loss is Mean Squared Error between predicted and gold scores; reported evaluation metric is Root Mean Squared Error (RMSE) on test set.

**Interpretation**: For acceptance prediction, higher Accuracy is better; reported error reduction is relative to a majority baseline. For aspect prediction, lower RMSE is better. The paper reports up to 6–21% error reduction in acceptance prediction compared to the majority baseline and that some models slightly improve over the mean baseline for aspect prediction.

**Baseline Results**: Acceptance prediction (test accuracies): Majority baselines and best model reported — ICLR: Majority 57.6% vs Best 65.3% (+7.7); arXiv cs.cl: Majority 68.9% vs Best 75.7% (+6.8); arXiv cs.lg: Majority 67.9% vs Best 70.7% (+2.8); arXiv cs.ai: Majority 92.1% vs Best 92.6% (+0.5). Aspect prediction: Paper;Review and Review models slightly outperform the Mean baseline on several aspects (reported via RMSE plots); specific RMSE values are provided in the paper figures.

**Validation**: Standard train/dev/test splits (0.9/0.05/0.05); hyperparameters tuned via 5-fold cross-validation; annotation quality assessed via re-annotation consistency (77% consistent, 2% inconsistent) and a sanity check for arXiv labeling which identified a small number of mislabelings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Data Laws

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Data Laws**: Data usage restrictions

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential to detect author demographic biases in accept/reject decisions (e.g., nationality) as explicitly suggested by the authors.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Collection includes opt-in submissions; reviews collected include anonymous reviews (paper explicitly states reviews are anonymous in sources).

**Data Licensing**: Different sections may have different license agreements (paper notes that data collection varies across sections and license agreements may differ).

**Consent Procedures**: Opt-in procedure for authors and reviewers in coordinated conference sections (authors and reviewers opted-in their drafts and anonymous reviews for inclusion).

**Compliance With Regulations**: Not Applicable
