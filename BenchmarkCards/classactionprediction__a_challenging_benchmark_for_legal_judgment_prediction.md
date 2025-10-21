# ClassActionPrediction: A Challenging Benchmark for Legal Judgment Prediction

## 📊 Benchmark Details

**Name**: ClassActionPrediction: A Challenging Benchmark for Legal Judgment Prediction

**Overview**: We release, for the first time, a challenging Legal Judgment Prediction (LJP) dataset focused on class action cases in the United States. It is the first dataset in the common law system that focuses on the harder and more realistic task involving the complaints (plaintiff's pleas) as input instead of the often used facts summary written by the court. The dataset contains 10.8K class action complaints from 2012 to 2022 annotated with a binary outcome (win or lose for the plaintiff). A sample of 3,000 cases, human expert labels, and the code for the experiments are publicly released.

**Data Type**: text (plaintiff's complaints / complaint documents)

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- Swiss-Judgment-Prediction
- LexGLUE
- CaseHOLD
- ILDC

**Resources**:
- [Resource](https://huggingface.co/darrow-ai/USClassActions)
- [Resource](https://huggingface.co/datasets/darrow-ai/USClassActionOutcomes_ExpertsAnnotations)
- [GitHub Repository](https://github.com/darrow-labs/ClassActionPrediction)
- [Resource](https://arxiv.org/abs/2211.00582)

## 🎯 Purpose and Intended Users

**Goal**: Provide a challenging dataset for the Plea Judgment Prediction subtask of Legal Judgment Prediction that uses plaintiff's complaints (pleas) as input to predict binary outcomes (win/lose for the plaintiff) for US class action cases, and to study model calibration and interpretability in this setting.

**Target Audience**:
- Machine Learning Researchers
- Legal NLP Researchers
- Legal Experts
- Practitioners

**Tasks**:
- Legal Judgment Prediction
- Text Classification
- Binary Classification

**Limitations**: The best model achieves an accuracy of 66%; experiments were performed only on relatively short input spans (512 tokens for allegations and 2,048 tokens for full text); further optimization and longer input spans (e.g., 4,096 tokens or hierarchical models) are left for future work.

**Out of Scope Uses**:
- The authors state that comparable technology should only be used to support human specialists (legal scholars, or legal professionals).

## 💾 Data

**Source**: 10.8K class action complaints in the United States from 2012 to 2022; plaintiff's pleas (complaint texts) were extracted using a rule-based regex extraction system applied across diverse courts and states.

**Size**: 10,800 examples (10.8K class action complaints); a public sample of 3,000 cases is released

**Format**: N/A

**Annotation**: Binary outcome labels (win or lose for the plaintiff) derived from court rulings and mapped to win/lose according to the mapping in Table 1. Additionally, human expert annotations were collected for a randomly selected subset of 200 examples and expert labels are released for the sample.

## 🔬 Methodology

**Methods**:
- 5-fold cross-validation averaged across 5 random seeds
- Automated metrics (Accuracy, Precision, Recall, F1 Score)
- Model calibration using Temperature Scaling (TS)
- Interpretability analysis using Integrated Gradients (IG)
- Human expert evaluation on a 200-example subset

**Metrics**:
- Accuracy
- Expected Calibration Error (ECE)
- Precision
- Recall
- F1 Score

**Calculation**: Results are reported as mean ± std averaged across 5 random seeds using 5-fold cross-validation. For calibration, Temperature Scaling was applied and ECE reported before and after calibration. Texts were truncated to model maximum sequence length (2,048 for Longformer/BigBird, 512 for other models) unless otherwise specified.

**Interpretation**: Higher Accuracy indicates better predictive performance on the binary win/lose task. Lower ECE indicates better calibration (model confidence aligned with empirical likelihoods). Authors report human expert accuracy (53% overall, 60% on high-confidence subset) and model accuracies for comparison; models that are better calibrated provide more reliable confidence estimates for downstream use.

**Baseline Results**: Main reported results (accuracy, mean ± std): Full Text (truncated to 2048): Longformer 62.87 ± 2.06, BigBird 63.26 ± 3.40. Unified Allegations (truncated to 512): BERT 65.06 ± 1.67, LegalBERT 65.57 ± 0.26, CaseLawBERT 65.87 ± 0.60, LegalRoBERTa 65.95 ± 0.98. Separated Allegations (truncated to 512): CaseLawBERT 66.82 ± 0.78, LegalRoBERTa 65.97 ± 0.88. Authors state best model achieves 66.8% (reported for allegations). Human experts: 53.5% accuracy on 200 examples (60% on high-confidence subset).

**Validation**: Experiments used 5-fold cross-validation averaged over 5 random seeds. Hyperparameter tuning and preprocessing details (including a 70/15/15 split used for tuning) and early stopping on validation loss with patience=2 are provided in Appendix A.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Misuse

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Misuse**: Improper usage

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
