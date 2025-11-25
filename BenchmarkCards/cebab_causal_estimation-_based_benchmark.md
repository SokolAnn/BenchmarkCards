# CEBaB (Causal Estimation- Based Benchmark)

## 📊 Benchmark Details

**Name**: CEBaB (Causal Estimation- Based Benchmark)

**Overview**: We introduce CEBaB, a new benchmark dataset for assessing concept-based explanation methods in Natural Language Processing (NLP). CEBaB consists of short restaurant reviews with human-generated counterfactual reviews in which an aspect (food, noise, ambiance, service) of the dining experience was modified. Original and counterfactual reviews are annotated with multiply-validated sentiment ratings at the aspect-level and review-level.

**Data Type**: text (paired original and human-generated counterfactual restaurant reviews with aspect-level and review-level sentiment labels)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- ERASER
- GLUE
- SuperGLUE
- Dynabench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate concept-based explanation methods by estimating causal effects of real-world concepts (aspect-level sentiment: food, service, ambiance, noise) on NLP model outputs using human-created counterfactual texts and multiply-validated labels.

**Target Audience**:
- NLP Researchers
- Researchers developing model explanation methods

**Tasks**:
- Sentiment Analysis
- Aspect-based Sentiment Analysis
- Evaluation of Concept-based Explanation Methods (causal effect estimation)

**Limitations**: CEBaB is only grounded in one task, sentiment analysis.

## 💾 Data

**Source**: OpenTable reviews (2,299 original reviews related to 1,084 restaurants) expanded via crowdsourced human edits to create counterfactual reviews.

**Size**: 15,089 texts (grounded in 2,299 original reviews)

**Format**: JSON (released via the Hugging Face datasets library)

**Annotation**: Crowdsourced annotation with five crowdworkers per example. Aspect-level sentiment labels: Positive / Negative / Unknown (three-way). Review-level overall sentiment labels: 1 to 5 stars (five annotators per text, majority and full distributions provided).

## 🔬 Methodology

**Methods**:
- Automated metrics (ICaCE-Error using Cosine, L2, and NormDiff distances)
- Model-based evaluation (fine-tuned classifiers compared against empirical causal effects using paired original/counterfactual examples)
- Comparative evaluation of explanation methods and baselines (Approximate Counterfactual, CONEXP, S-Learner, TCAV, ConceptSHAP, INLP, CausaLM)

**Metrics**:
- ICaCE-Error (Empirical Individual Causal Concept Effect Error) using Cosine distance
- ICaCE-Error (Empirical Individual Causal Concept Effect Error) using L2 (Euclidean) distance
- ICaCE-Error (Empirical Individual Causal Concept Effect Error) using NormDiff distance
- Empirical Causal Concept Effect (\CaCE)
- Empirical Individual Treatment Effect (dITE) and Empirical Average Treatment Effect (dATE)
- Accuracy
- Macro-F1

**Calculation**: ICaCE-Error is the average distance between the empirical individual causal concept effect \ICaCE (computed as N(ϕ(x_{C=c0,u})) - N(ϕ(x_{C=c,u}))) and the explainer's predicted effect ENϕ(x_{C=c,u};c0), averaged over edit pairs. Distances used are Cosine, L2 (Euclidean), and NormDiff (absolute difference between Euclidean norms). \CaCE is aggregated average of \ICaCE over matching edit pairs. dITE and dATE use dataset labels to compute empirical treatment effects.

**Interpretation**: Lower ICaCE-Error indicates an explanation method better approximates the true individual causal concept effect. Cosine distance measures agreement in direction (ignores magnitude), L2 measures both direction and magnitude, and NormDiff measures magnitude only.

**Baseline Results**: A simple Approximate Counterfactual baseline (sampling an original review with matching aspect labels as an approximate counterfactual) outperforms most evaluated methods on ICaCE-Error. INLP and S-Learner achieve state-of-the-art on some metrics. For a bert-base-uncased five-way sentiment classifier, reported \CaCE (average change in classifier output) values include: food (Negative→Positive) = 1.90 (±0.03), service (Negative→Positive) = 1.42 (±0.04), ambiance (Negative→Positive) = 1.27 (±0.01), noise (Negative→Positive) = 0.75 (±0.02). Results are averaged over 5 seeds (see paper tables for full numeric results).

**Validation**: Dataset released with fixed train/dev/test splits enforcing grouped constraint (all edits related to an original review occur in the same split) and a rule that any group with a 'no majority' label is placed in the train set. Two train variants: inclusive (11,728 texts) and exclusive (1,755 examples). 99% of aspect-level edits have a majority label matching the editing goal; 88% of texts have a review-level majority label. Models' results on standard classification tasks (reported in Appendix) demonstrate dataset reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Trust

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset includes anonymized worker ids; crowdworker roles, compensation, and number of workers per task are provided in Appendix B.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
