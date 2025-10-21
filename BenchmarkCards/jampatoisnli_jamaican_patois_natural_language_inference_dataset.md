# JamPatoisNLI (Jamaican Patois Natural Language Inference Dataset)

## 📊 Benchmark Details

**Name**: JamPatoisNLI (Jamaican Patois Natural Language Inference Dataset)

**Overview**: JamPatoisNLI provides the first dataset for natural language inference in a creole language, Jamaican Patois. JamPatoisNLI, which consists of naturally-occurring premises and expert-written hypotheses, is a step towards steering research into a traditionally underserved language and a useful benchmark for understanding cross-lingual NLP.

**Data Type**: premise-hypothesis sentence pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- Jamaican Patois

**Similar Benchmarks**:
- Stanford NLI (SNLI)
- Multi-NLI (MNLI)
- Adversarial NLI (ANLI)
- XNLI
- AmericasNLI
- OCNLI

**Resources**:
- [Resource](https://arxiv.org/abs/2212.03419)

## 🎯 Purpose and Intended Users

**Goal**: Provide the first natural language inference dataset in Jamaican Patois to serve as a benchmark for studying cross-lingual transfer to creole and low-resource languages and to encourage research on NLP for Jamaican Patois and creole languages.

**Target Audience**:
- Natural Language Processing Researchers

**Tasks**:
- Natural Language Inference

**Limitations**: The dataset is small: 650 examples in total with relatively small validation and test splits compared to high-resource language datasets; limited availability of native speakers constrained dataset size (explicitly stated in the paper).

## 💾 Data

**Source**: Premises drawn from naturally occurring written Jamaican Patois: Twitter (634 examples), Anthology: Shelley Sykes-Coley (6 examples), Poetry: Rt. Hon. Dr. Louise Bennett-Coverley (4 examples), Online blog (6 examples). The paper also states remaining examples drawn from a cultural website (jamaicans.com).

**Size**: 650 examples (250 training, 200 development, 200 test)

**Format**: N/A

**Annotation**: Hypotheses were manually written by the first author (a fluent/native speaker). Labels (entailment, neutral, contradiction) were assigned following MNLI/ANLI-style criteria. A random sample of 100 sentence pairs (evenly distributed across classes) was double-annotated by volunteer fluent speakers for validation (Fleiss Kappa 88.99%).

## 🔬 Methodology

**Methods**:
- Automated evaluation (Accuracy)
- Zero-shot evaluation
- Few-shot fine-tuning evaluation
- Hyperparameter search
- Qualitative analysis (hand-crafted transition examples)

**Metrics**:
- Accuracy
- Fleiss Kappa

**Calculation**: Accuracy reported as percentage of correct label predictions; experiment results averaged over three runs with different random seeds (and standard deviation reported for best model across ten experiments). Fleiss Kappa computed on 100 double-annotated examples (88.99%).

**Interpretation**: Higher Accuracy indicates more effective cross-lingual transfer. The authors interpret higher few-shot and zero-shot accuracies on JamPatoisNLI (relative to AmericasNLI) as evidence that relatedness to English boosts transfer effectiveness. RoBERTa-based models outperform BERT-based models in these experiments.

**Baseline Results**: Majority baseline: 33.50%. Best BERT-based results on full few-shot JamPatoisNLI: bert-uncased-unfrozen 66.17%; mbert-uncased-unfrozen 65.33%. Best RoBERTa-based results on full few-shot JamPatoisNLI: roberta-unfrozen 76.50%; xlm-unfrozen 75.17%. Zero-shot roberta-unfrozen: 67.50%. For AmericasNLI best zero-shot: 42.00%.

**Validation**: 100 examples were double-annotated by volunteer fluent speakers; Fleiss Kappa = 88.99% and percentage accuracy = 89.00% on that sample. Experimental results averaged across three seeds; standard deviation reported for best model across ten runs (1.43% on test set for xlm-unfrozen).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
