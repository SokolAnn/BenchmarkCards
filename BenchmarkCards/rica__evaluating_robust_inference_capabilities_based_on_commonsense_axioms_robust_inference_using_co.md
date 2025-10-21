# RICA: Evaluating Robust Inference Capabilities Based on Commonsense Axioms (Robust Inference using Commonsense Axioms)

## 📊 Benchmark Details

**Name**: RICA: Evaluating Robust Inference Capabilities Based on Commonsense Axioms (Robust Inference using Commonsense Axioms)

**Overview**: A new challenge, RICA: Robust Inference using Commonsense Axioms, that evaluates robust commonsense inference despite textual perturbations. RICA consists of natural language statements in a premise-conclusion format derived from first-order-logic commonsense axioms, uses novel entities to separate factual recall from reasoning, and introduces linguistic perturbations to test robustness.

**Data Type**: text (premise-conclusion statements; masked sentences and sentence pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SWAG
- CommonsenseQA
- PIQA
- Social IQA
- RiddleSense
- Winogrande
- COSMOS QA
- ReClor
- NumerSense

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate models' robust inference capabilities using commonsense axioms, specifically testing whether pre-trained language models can combine commonsense knowledge with natural language input and produce consistent inferences across linguistically-varied paraphrases.

**Target Audience**:
- ML Researchers
- Model Developers
- Commonsense Reasoning Researchers

**Tasks**:
- Masked Word Prediction
- Sentence Probability
- Textual Entailment

**Limitations**: Data and evaluation are in English only, which benefits English speakers more; data may include societal biases from source knowledge bases (ConceptNet, ATOMIC, Wikipedia); some statements are difficult for humans to verify (inter-annotator agreement reported).

## 💾 Data

**Source**: Automatically generated from commonsense knowledge bases (ConceptNet and ATOMIC) and web KB (Wikipedia); converted from first-order-logic axioms to text using a seq2seq model (BART); human verification via Amazon Mechanical Turk.

**Size**: Raw generated set: 257,000 statements covering ~43,000 axioms; Human-Verified set: 10,000 statements covering ~1,700 axioms; Human-Curated set: 1,600 statements covering 80 axioms; Joint Test Set: 2,600 statements; Human-Verified Test Set (sampled): 1,000 statements covering 170 axioms.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk: pairs presented with flipped comparators; two annotators per pair and a second round with three annotators for disagreements; majority voting used to validate statements; Fleiss-kappa reported (0.72 and 0.52).

## 🔬 Methodology

**Methods**:
- Automated model probing (Masked Word Prediction and Sentence Probability)
- Human evaluation (Amazon Mechanical Turk)
- Fine-tuning experiments across zero-shot, low-resource, high-resource, and large/noisy training settings
- Seq2seq conversion from FOL to natural language using BART for generation

**Metrics**:
- Accuracy
- Perplexity
- Fleiss-kappa
- Cohen's kappa

**Calculation**: Sentence Probability (SP) is computed as the product of each word's probability conditioned on previous words (left-to-right language modeling loss). Masked Word Prediction (MWP) accuracy is computed by comparing predicted comparator tokens (e.g., 'more' vs 'less'). Human accuracy computed via majority vote among annotators. Perplexity and validation loss reported for fine-tuning runs.

**Interpretation**: Models are considered successful only if they perform like humans on all probes. Human zero-shot accuracy is reported as 91.7%; model accuracy near 0.5 is equivalent to random guessing. Improvements via fine-tuning on generated/veriﬁed data are interpreted relative to human performance and robustness across human-curated perturbations.

**Baseline Results**: Zero-shot model performance ~0.5 (on par with random guessing). Humans obtained 91.7% accuracy (zero-shot). Fine-tuned models (e.g., RoBERTa and ERNIE) in high-resource settings reach near 90% on the human-verified set, but performance on the human-curated set remains around 50% (random).

**Validation**: Seq2seq conversion validated by sampling 5% of generated probes and native speaker inspection (0.8% fluency/grammar issues). Human verification via multi-round AMT (two annotators, then three annotators for disagreements) with majority voting; Fleiss-kappa reported. Fine-tuning uses validation splits and saves model with highest validation performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: Probes do not involve specific demographics; authors note the possibility that biases in source knowledge resources may be included in the data.

**Potential Harm**: ['Biases in knowledge resources may be included in the data', 'Benchmark and collected data benefit English speakers more']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Human evaluation conducted via Amazon Mechanical Turk; annotators paid approximately $11 per hour; annotators given sufficient time and engaged in discussions if they had concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
