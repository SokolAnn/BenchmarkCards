# Prediction bias

## 📊 Benchmark Details

**Name**: Prediction bias

**Overview**: A framework to measure models' reliance on identified spurious features in Question Answering by (i) implementing heuristics that compute an attribute Ah for each sample, (ii) splitting evaluation data into two groups by a threshold Th on Ah, and (iii) computing the difference in model performance between these groups using bootstrapped evaluation (the measured quantity is called Prediction bias). The framework is used to assess robustness of pre-trained QA models and the efficiency of debiasing methods.

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- HANS
- PAWS
- AdversarialQA

**Resources**:
- [Resource](https://arxiv.org/abs/2305.06841v2)
- [GitHub Repository](https://github.com/MIR-MU/isbiasedTh)

## 🎯 Purpose and Intended Users

**Goal**: To measure the scale of models' reliance on any identified spurious feature (Prediction bias) and to assess robustness towards a large set of known and newly identified prediction biases for various pre-trained models and debiasing methods in Question Answering.

**Tasks**:
- Question Answering

**Limitations**: Non-trivial interpretation of measured results: Prediction bias provides lower bounds and can be confounded by the natural polarization of sample difficulty. The measure should not be used standalone and should be contextualized with human-level prediction bias (the authors use SQuAD validation annotations by three annotators for this).

**Out of Scope Uses**:
- Using the Prediction bias measure as a standalone evaluation (the paper states it should be used as a complement to in-distribution evaluation)

## 💾 Data

**Source**: SQuAD (Rajpurkar et al., 2016) as primary evaluation dataset; out-of-distribution datasets used include AdversarialQA (Bartolo et al., 2020), NaturalQuestions (Kwiatkowski et al., 2019), and TriviaQA (Joshi et al., 2017).

**Size**: SQuAD validation set: 10,570 examples (as stated in Appendix C).

**Format**: N/A

**Annotation**: SQuAD validation set contains annotations by three annotators (used to quantify a level of Prediction bias explainable by natural question difficulty).

## 🔬 Methodology

**Methods**:
- Heuristic-based dataset segmentation (compute attribute Ah = h(X) per sample and split by threshold Th)
- Bootstrapped evaluation (samples = 800, trials = 100 as used in experiments)
- Exact Match for in-distribution split evaluation
- Out-of-distribution evaluation on external QA datasets
- Hyperparameter search for heuristic threshold Th
- Comparison to human annotator-level Prediction bias

**Metrics**:
- Exact Match
- F1 Score
- Bootstrapped confidence intervals (quantiles q61=0.975 and q62=0.025 used in measurement)

**Calculation**: Prediction bias is computed by splitting dataset X into X1 and X2 by a heuristic h and threshold Th, bootstrapping evaluations on sampled subsets (samples=800, trials=100) to obtain performance estimates E1 and E2, computing upper and lower quantiles (q61=0.975, q62=0.025) and returning dist = max(0; E62_1 - E61_2; E62_2 - E61_1) as the scale of learned prediction bias (see Algorithm 1 in the paper).

**Interpretation**: Due to bootstrapping with q61=0.975 and q62=0.025, the authors state the model's true performance polarization is 95.06%-likely to be equal or higher than the measured Prediction bias. The measure provides a lower bound and must be contextualized with in-distribution performance and human-level Prediction bias; reductions in Prediction bias are meaningful only down to the level of natural sample difficulty.

**Baseline Results**: Original model out-of-distribution F1-scores reported in Table 1 (AdversarialQA / NaturalQuestions / TriviaQA): 29.8 / 67.8 / 46.1.

**Validation**: Bootstrapped evaluation (samples=800, trials=100) on dataset splits; hyperparameter search for optimal heuristic threshold Th maximizing measured distance; SQuAD validation used for threshold selection and human-annotator comparisons; bias models selected by maximizing F1-score difference between biased and non-biased segments on SQuAD validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Potential Harm**: ['Socially problematic biases (applicability to quantifying stereotypes and gender bias is discussed)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
