# WikiResNLI and NatResNLI

## 📊 Benchmark Details

**Name**: WikiResNLI and NatResNLI

**Overview**: The paper proposes two English NLI datasets to probe language models' reasoning with respective readings: WikiResNLI (a controlled synthetic dataset based on analogies/Wikidata) and NatResNLI (a naturally occurring dataset). The benchmarks are designed to encompass various explicit and implicit realizations of "respectively" and to evaluate zero-shot and few-shot generalization of LMs.

**Data Type**: premise-hypothesis pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SNLI
- MNLI
- ANLI
- FEVER-NLI
- LingNLI
- WANLI
- GLUE

**Resources**:
- [GitHub Repository](https://github.com/ruixiangcui/WikiResNLI_NatResNLI)
- [Resource](https://sentence.yourdictionary.com/respectively)
- [Resource](https://www.dictionary.com/browse/respectively)
- [Resource](https://crosstalk.cell.com/blog/how-to-use-respectively-respectfully)

## 🎯 Purpose and Intended Users

**Goal**: To investigate whether NLI models can reason with respective readings (explicit and implicit realizations of "respectively") in zero-shot and few-shot settings, and to analyze what cues models leverage and how they generalize from synthetic to natural examples.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Natural Language Inference

**Limitations**: Both WikiResNLI and NatResNLI have only one sentence in the premise and do not exhaust all possible and complicated realizations of respective readings. Experiments are English-specific and limited to LMs that can be run with an academic budget.

## 💾 Data

**Source**: WikiResNLI: synthetic data generated from an analogy dataset (WiQueen) extracted from Wikidata (Garneau et al., 2021). NatResNLI: naturally occurring sentences collected from online resources (sentence.yourdictionary.com, dictionary.com) and a writing-advice blog; premises curated and filtered by the authors.

**Size**: WikiResNLI EXPLICIT: 2,317 premises (18,536 premise-hypothesis pairs total); development set: 1,312 premise-hypothesis pairs; training set: 1,577 premises (12,616 premise-hypothesis pairs). WikiResNLI IMPLICIT (test set derived by removing "respectively"): 451 premises (3,608 premise-hypothesis pairs). NatResNLI: 76 premises and 608 premise-hypothesis pairs. Additional statistics: WikiResNLI EXPLICIT contains 139 different predicates; NatResNLI average premise length 20.1 tokens, hypothesis length 10.1 tokens, average 2.32 conjuncts per sentence (max 4).

**Format**: N/A

**Annotation**: WikiResNLI: hypotheses are automatically generated following rule-based templates; for WikiResNLI IMPLICIT, two authors manually annotated 139 predicates for whether they allow a single subject predicating conjunction of two objects to exclude ambiguous predicates. NatResNLI: two authors wrote hypotheses; annotations collected via Amazon Mechanical Turk with five workers per premise-hypothesis pair; majority vote adopted as final labels; inter-annotator agreement (Fleiss' kappa) = 0.65.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Few-shot fine-tuning
- Fine-tuning pretrained encoder models (RoBERTa, ALBERT, DeBERTa) on NLI corpora
- In-context learning (LLaMA, FLAN-T5, GPT-JT)
- Human annotation (Amazon Mechanical Turk) for NatResNLI

**Metrics**:
- Accuracy
- Fleiss' kappa
- Label distribution percentages

**Calculation**: Accuracy reported as percentage of correct predictions. Inter-annotator agreement for NatResNLI measured by Fleiss' kappa (0.65). For NatResNLI, majority vote of five annotators per pair is adopted as final label.

**Interpretation**: Higher accuracy indicates better model reasoning with respective readings. The paper notes random-guessing baselines depend on label setup (three-way baseline 33.3%; for tasks restricted to entailment/contradiction baseline becomes 50%). Fleiss' kappa of 0.65 indicates moderate agreement among annotators for NatResNLI.

**Baseline Results**: Zero-shot on WikiResNLI EXPLICIT: best model (DeBERTa) achieves 35% accuracy when fine-tuned with MNLI and can reach 68.5% when fine-tuned with nearly all NLI training datasets. Zero-shot on WikiResNLI IMPLICIT: DeBERTa achieves 43.7% when fine-tuned with all NLI corpora (about 10% above chance). NatResNLI performance is generally lower due to domain drift; models can surpass 95% after 32-shot training in some settings while pre-assigned labels match humans at ~90% (see paper for detailed per-condition numbers).

**Validation**: NatResNLI labels were validated via human annotation on Amazon Mechanical Turk (five annotators per pair); majority vote used as final label; Fleiss' kappa reported as 0.65. For WikiResNLI IMPLICIT, two authors manually annotated predicates to exclude ambiguous cases when constructing the test set.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
