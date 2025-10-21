# WINOGRANDE

## 📊 Benchmark Details

**Name**: WINOGRANDE

**Overview**: WINOGRANDE is a large-scale dataset of 44k problems inspired by the original Winograd Schema Challenge (WSC) design, adjusted to improve both the scale and the hardness of the dataset. It was created via crowdsourcing and algorithmic bias reduction (AFLITE) to reduce dataset-specific spurious biases and to better evaluate commonsense reasoning.

**Data Type**: question-answering pairs (fill-in-the-blank pronoun resolution)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- WSC
- PDP
- SuperGLUE-WSC
- DPR
- KnowRef
- COPA
- Winogender

**Resources**:
- [Resource](http://winogrande.allenai.org)
- [Resource](https://www.wikihow.com/Special:Randomizer)
- [Resource](https://arxiv.org/abs/1907.10641)
- [GitHub Repository](https://github.com/pytorch/fairseq/tree/master/examples/roberta)

## 🎯 Purpose and Intended Users

**Goal**: To create a large-scale Winograd Schema Challenge-inspired dataset that is robust against spurious dataset-specific bias, to provide a harder benchmark for evaluating machine commonsense reasoning, and to serve as a resource for transfer learning.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Natural Language Processing Researchers

**Tasks**:
- Question Answering
- Coreference Resolution
- Commonsense Reasoning

**Limitations**: The authors note that (1) WINOGRANDE deviates from original WSC in formatting (uses blanks) and authorship (crowdworkers), (2) AFLITE may filter out only one of a twin pair so the debiased set is not always composed of twins (about 1/3 are not twins), and (3) while AFLITE reduces detectable dataset-specific biases, it cannot guarantee that future models will not learn other spurious correlations.

## 💾 Data

**Source**: Collected via crowdsourcing on Amazon Mechanical Turk (AMT) with anchor words sampled from WikiHow; followed by algorithmic bias reduction using AFLITE (RoBERTa embeddings + ensemble linear classifiers).

**Size**: WINOGRANDE all: 43,972 problems total (40,938 training, 1,267 development, 1,767 test). WINOGRANDE debiased: 12,282 instances (9,248 training, 1,267 development, 1,767 test). Additionally, 31k problems filtered out by AFLITE are released as additional resources.

**Format**: N/A

**Annotation**: Each collected question was validated by three distinct crowd workers. A question is considered valid if (1) the majority of the three workers chose the correct answer option, (2) they agree the two answer options are unambiguous, and (3) the question cannot be answered by simple word association. Worker qualifications and payment details were reported (AMT workers with >=99% approval rate and >=5,000 approvals; payment amounts provided).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation (majority vote of three crowd workers)
- Baseline model evaluation (BERT, RoBERTa, Ensemble LMs, WKH)
- Transfer learning evaluation

**Metrics**:
- Accuracy
- Kullback–Leibler divergence (KL divergence)

**Calculation**: Accuracy is computed as percentage correct on dev and test sets. Human performance is computed as the majority vote of three crowd workers per question. KL divergence is computed between distributions of principal component (d1) of RoBERTa pre-computed embeddings for the two answer options (used to quantify bias separation). AFLITE parameters when applied to WINOGRANDE: m=10,000, n=64, k=500, threshold = 0.75.

**Interpretation**: Higher Accuracy indicates closer alignment with human performance (human accuracy reported at ~94%). A dramatic reduction in KL divergence after AFLITE indicates reduced spurious correlation between instance representations and labels. Authors report that to reach human-level performance, current state-of-the-art models would need over 118,000 training instances (as estimated from the learning curve).

**Baseline Results**: Performance on WINOGRANDE debiased (test accuracy): WKH 49.6%, Ensemble LMs 50.9%, BERT 64.9%, RoBERTa 79.1%, BERT (local context) 51.9%, RoBERTa (local context) 50.0%, BERT-DPR (zero-shot) 51.0%, RoBERTa-DPR (zero-shot) 58.9%, Human performance 94.0%. Transfer learning results: RoBERTa fine-tuned on WINOGRANDE achieved new SOTA on several related datasets (e.g., WSC ~90.1%, DPR ~93.1%, COPA ~90.6%, KnowRef ~85.6%, Winogender ~97.1%).

**Validation**: Question-level validation by three crowd workers with majority vote and additional checks for ambiguity and word-association answers. Systematic bias reduction via AFLITE (ensemble of linear classifiers on RoBERTa embeddings) applied iteratively; AFLITE filtering parameters specified (m=10,000, n=64, k=500, threshold=0.75). Final debiased split and WINOGRANDE all splits reported.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The paper reports diagnostics for gender bias using the Winogender dataset, computing 'Gotcha' vs 'Non-Gotcha' gaps (ΔF and ΔM) and reporting accuracy differences to measure gender bias.

**Potential Harm**: ['Overestimation of machine commonsense capabilities due to dataset-specific spurious biases', 'Gender bias in coreference resolution (diagnosed via Winogender)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
