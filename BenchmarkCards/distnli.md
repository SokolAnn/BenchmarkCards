# DistNLI

## 📊 Benchmark Details

**Name**: DistNLI

**Overview**: We introduce DistNLI, a new diagnostic dataset for natural language inference that targets the semantic difference arising from distributivity, and employ the causal mediation analysis framework to quantify the model behavior and explore the underlying mechanism in this semantically-related task.

**Data Type**: text (premise-hypothesis pairs)

**Domains**:
- Natural Language Processing
- Linguistics

**Languages**:
- English

**Similar Benchmarks**:
- SNLI
- XNLI
- MNLI
- ConjNLI
- HANS

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: A diagnostic NLI dataset to examine to what extent pre-trained language models can discern the phenomenon of distributivity (predicative distributivity), and to apply causal mediation analysis to quantify model behavior and investigate underlying mechanisms.

**Target Audience**:
- Natural Language Processing Researchers
- Computational Linguists

**Tasks**:
- Natural Language Inference

**Limitations**: Due to the specificity of the linguistic phenomenon involved and its size, this DistNLI dataset should only be used as a diagnostic dataset in the investigation of distributivity of verb predication. Subjects are limited to two coordinated determiner phrases; occasionally some minimal pairs may contradict world knowledge despite filtering.

## 💾 Data

**Source**: Synthetic generation via templates of premise-hypothesis pairs ([DP1] and [DP2] [Pred] as premise; [DP1]/[DP2] [Pred] as hypothesis). Predicates were scraped from existing categorized predicates in past publications on distributivity and augmented with additional predicates of similar patterns.

**Size**: 328 premise-hypothesis pairs

**Format**: N/A

**Annotation**: Two-stage human annotation: initial annotation by three graduate students (native speakers of American English with linguistics and NLP background) with example/explanation provided; highly controversial items (three distinct labels) discarded; dataset further confirmed/validated by an expert in Semantics and NLP. Final split: control group (164 distributive pairs) and intervention group (164 ambiguous pairs).

## 🔬 Methodology

**Methods**:
- Causal Mediation Analysis (TE, NIE, NDE)
- Synthetic dataset generation via templates
- Human annotation (two-stage with expert validation)
- Statistical testing (one-sample t-test on TE, significance level 0.05)
- Neuron interventions / mediator interventions (setting neuron values to null/matched values) and layer-wise neuron analysis (top 1% NIE neurons)

**Metrics**:
- Total Effect (TE)
- Natural Indirect Effect (NIE)
- Natural Direct Effect (NDE)
- Accuracy
- Log odds ratio

**Calculation**: TE is computed as the log odds ratio: TE = log( Odds(non-entailment | swapped predicate) / Odds(non-entailment | null) ). NIE and NDE are defined analogously using log odds ratios with mediator m set to its null/observed values. The authors adopt a log odds ratio formulation that guarantees TE = NIE + NDE decomposition (citing VanderWeele and Vansteelandt (2010)).

**Interpretation**: TE>0: presence of an ambiguous predicate causes higher odds of non-entailment. TE=0: no causal relationship between predicate type and model prediction. TE<0: ambiguous predicate causes lower odds of non-entailment. NIE is interpreted similarly as the mediated contribution to TE. TE is decomposed as TE = NIE + NDE.

**Baseline Results**: Pre-examination and TE results reported. Pre-examination (accuracy on DistNLI control/intervention): examples from Table 2 include DeBERTa-base Distributive Acc 100.00 / Ambiguous Acc 0.00; DeBERTa-large Distributive Acc 100.00 / Ambiguous Acc 0.00; RoBERTa-large Distributive Acc 100.00 / Ambiguous Acc 0.61. One-sample t-test of TE over DistNLI (Table 3): DeBERTa-base mean TE 0.040 (p=0.320, not significant); DeBERTa-large mean TE 0.314 (p < 7e-06); DeBERTa-xlarge mean TE 0.351 (p < 7e-16); DeBERTa-v2-xlarge mean TE 0.856 (p < 2e-29); DeBERTa-v2-xxlarge mean TE 0.828 (p < 3e-18); RoBERTa-large mean TE 0.779 (p < 4e-13).

**Validation**: Annotation validation by an expert in Semantics and NLP; statistical validation of TE via one-sample t-test with significance level 0.05; neuron-level validation via selection of top 1% neurons by individual NIE and layer-wise NIE aggregation. Note: DeBERTa-v2-xxlarge excluded from some experiments due to limited computational resources as stated.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
