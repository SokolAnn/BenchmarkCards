# JAMP: Controlled Japanese Temporal Inference Dataset for Evaluating Generalization Capacity of Language Models

## 📊 Benchmark Details

**Name**: JAMP: Controlled Japanese Temporal Inference Dataset for Evaluating Generalization Capacity of Language Models

**Overview**: We present JAMP, a Japanese NLI benchmark focused on temporal inference. The dataset includes a range of temporal inference patterns (46 tense fragments) created from templates based on formal semantics, automatically generated using a Japanese case frame dictionary and well-designed templates while controlling the distribution of inference patterns and gold labels. We evaluate generalization capacities of monolingual/multilingual LMs by splitting the dataset based on tense fragments (temporal inference patterns).

**Data Type**: text (premise–hypothesis sentence pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Similar Benchmarks**:
- JSeM
- Temporal NLI
- PLMUTE
- PLMUTE_ja
- SNLI
- SICK
- JSNLI
- JSICK

**Resources**:
- [GitHub Repository](https://github.com/tomo-ut/temporalNLI_dataset)
- [Resource](https://arxiv.org/abs/2306.10727)
- [Resource](https://huggingface.co/transformers/)

## 🎯 Purpose and Intended Users

**Goal**: To construct a temporal inference dataset that precisely assesses the generalization capacities of language models for temporal NLI and to enable fine-grained analysis across diverse temporal inference patterns.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Natural Language Inference
- Temporal Reasoning

**Limitations**: Aspect and temporal commonsense are outside the scope of the dataset. The proposed method is currently applicable only to Japanese because it relies on a Japanese case frame dictionary.

**Out of Scope Uses**:
- Aspect and temporal commonsense are outside the scope of the dataset.
- Method currently applicable only to Japanese (requires Japanese case frame dictionary).

## 💾 Data

**Source**: Templates created from temporal inference problems in JSeM; vocabulary and case-frame selections from the Japanese case frame dictionary (Kawahara and Kurohashi, 2006); temporal expressions generated programmatically according to defined formats; templates based on formal-semantics-derived tense fragments.

**Size**: 10,094 examples total (9,750 training examples; 344 test examples). Training distribution: 3,050/3,340/3,360 (Entailment/Contradiction/Neutral). Test distribution: 114/112/118 (Entailment/Contradiction/Neutral).

**Format**: N/A

**Annotation**: Gold labels automatically determined by template conditions (Entailment / Contradiction / Neutral) during generation; manual filtering of unusable or harmful sentences from the test set; manual verification of a random sample of test cases.

## 🔬 Methodology

**Methods**:
- Automated metrics (accuracy)
- Model evaluation: zero-shot (monolingual)
- Model evaluation: zero-shot (cross-lingual)
- Model evaluation: fine-tuning (including splits by tense fragment, time format, time span)

**Metrics**:
- Accuracy

**Calculation**: Accuracy computed as the proportion of correctly predicted labels. Reported as averages and standard deviations over five runs.

**Interpretation**: Higher accuracy indicates better ability to solve temporal NLI and generalize across the specified splits. Models achieve high accuracy on IID (seen) data but show large drops on unseen tense-fragment splits, indicating poor generalization for certain temporal phenomena (e.g., habituality).

**Baseline Results**: Zero-shot accuracies (monolingual and cross-lingual) are approximately 40% on average. RoBERTa-large (fine-tuned) achieves up to 0.984 ± 0.01 accuracy on the IID fine-tuning setting. Large monolingual models generally outperform base models; models show substantial accuracy drops on unseen tense fragment splits.

**Validation**: Manual inspection of all test examples by three graduate students (approximately 40% of generated test sentences were filtered out). Random sample of 100 test cases was manually checked for correctness; gold labels confirmed to be annotated as intended (with some debatable cases noted). Statistical analysis for dataset artifacts performed following Gardner et al. (2021) protocol to detect token-level spurious correlations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Data Quality

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Offensive content in generated sentences (manually filtered ~30 offensive verbs/nouns).', 'Semantically or grammatically unnatural or harmful sentences filtered from the test set.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Japanese case frame dictionary distributed by Gengo-Shigen-Kyokai; JSeM is licensed under BSD-3-Clause. The paper states that their use of these datasets is consistent with the terms of the license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
