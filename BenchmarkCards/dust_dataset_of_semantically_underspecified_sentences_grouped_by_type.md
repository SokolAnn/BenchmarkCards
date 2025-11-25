# DUST (Dataset of semantically Underspecified Sentences grouped by Type)

## 📊 Benchmark Details

**Name**: DUST (Dataset of semantically Underspecified Sentences grouped by Type)

**Overview**: We introduce DUST, a Dataset of semantically Underspecified Sentences (and more specified counterparts) grouped by the Type of underspecification they belong to, and propose a suite of experiments to answer the questions above using DUST.

**Data Type**: sentence pairs (underspecified sentence and more specified counterpart)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LA V A (Language and Vision Ambiguities)
- CLAIRE (CLArifying Insertions from REvision Edits)
- Winograd Schema Challenge

**Resources**:
- [GitHub Repository](https://github.com/frank-wildenburg/DUST)
- [Resource](https://web.mit.edu/lavacorpus/)
- [GitHub Repository](https://github.com/acidAnn/claire)
- [Resource](https://huggingface.co/datasets/winograd_wsc)

## 🎯 Purpose and Intended Users

**Goal**: To study whether pre-trained language models (LMs) correctly identify and interpret underspecified sentences.

**Tasks**:
- Text Classification
- Language Modeling

**Limitations**: DUST is arguably a small dataset, and would benefit from expansion. Type 4 (word-level homonymy) is excluded from the benchmark. The work does not explore the inner mechanisms underlying models' abilities.

**Out of Scope Uses**:
- Commercial use (DUST is a non-commercial dataset intended for research purposes)

## 💾 Data

**Source**: DUST is composed of data from LA V A (Berzak et al., 2015), CLAIRE (Roth et al., 2022), and the Winograd Schema Challenge (Levesque et al., 2012); for each underspecified sentence we provide a more specified counterpart, based on Egg's (2010) categorization.

**Size**: 2,123 underspecified sentences and 2,123 specified counterparts (2,123 sentence pairs)

**Format**: N/A

**Annotation**: Created from existing datasets (LA V A, CLAIRE, WSC) and manually crafted more specified counterparts; grammaticality of pre-edit CLAIRE sentences scored with GRUEN and low-scoring sentences excluded.

## 🔬 Methodology

**Methods**:
- Perplexity-based evaluation
- Prompted perplexity comparison (specification-matched vs specification-mismatched inputs)
- Naturalistic continuation evaluation (continuation perplexity comparison)
- Generative multiple-choice probing (MCQ) (preliminary)
- Qualitative analysis

**Metrics**:
- Perplexity
- Accuracy (proportion of inputs where specification-matched prompt received lower perplexity)
- Absolute difference in perplexities between continuations
- Statistical significance (p-values reported)

**Calculation**: For Experiment 1 we compute, for a given prompt, the product of the model perplexities assigned to each token in it and compare specification-matched vs specification-mismatched inputs. For Experiment 2 we record the absolute value of the difference in the perplexities assigned to each continuation given a sentence.

**Interpretation**: If models recognize underspecification, inputs where labels are correct should receive higher probability / lower perplexity than mismatched labels. For continuations, underspecified sentences should yield smaller absolute differences between continuation perplexities (weaker preferences), while specified sentences should yield larger differences (stronger preference for the compatible continuation).

**Baseline Results**: Experiment 1 overall accuracies (proportion where specification-matched input received lower perplexity): Mistral 7B: 0.74; Llama 2: 0.65; OPT-13B: 0.55; GPT-2 XL: 0.53; Flan-T5 XXL: below chance in some settings. Sentiment sanity-check (SST-5) yielded at least 65% and average 75% accuracy across models.

**Validation**: Sanity check with sentiment (SST-5) showing models assign lower perplexity to sentiment-matched inputs (>=65%, avg 75%). Statistical significance tests reported (e.g., p < .05, p < .001) for comparisons against chance and between models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Data Laws
- Robustness
- Accuracy
- Value Alignment

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy
- **Value Alignment**: Harmful output

**Potential Harm**: Choosing an arbitrary interpretation of an underspecified sentence can lead to undesired or even harmful consequences for communication (e.g., misinterpretation by an assistant or incorrect machine translation); models could perpetuate harmful biases present in their training data and generate false or misleading output.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: DUST does not include images from LA V A; the names used in LA V A sentences refer to its authors. CLAIRE (WikiHow) articles and revisions were not filtered for personally identifiable or offensive content. Winograd sentences do not contain personally identifiable or offensive content.

**Data Licensing**: DUST is released under a CC BY-NC-SA license. CLAIRE is CC BY-NC-SA 3.0. Winograd Schema Challenge dataset is CC BY 4.0. LA V A was released with an unclear (potentially open-source) license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
