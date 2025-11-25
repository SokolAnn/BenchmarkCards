# Evidence Inference 2.0

## 📊 Benchmark Details

**Name**: Evidence Inference 2.0

**Overview**: An expanded release of the Evidence Inference dataset: we collect an additional 2,503 ICO prompts (a 25% expansion of the original dataset), release an abstract-only subset for rapid prototyping, provide updated corpus, documentation, and code, and evaluate transformer-based models for inferring comparative performance of interventions (Intervention vs Comparator w.r.t. Outcome) from clinical trial articles and extracting supporting evidence spans.

**Data Type**: text (full-text clinical trial articles and abstract-only subsets; ICO prompts and evidence spans)

**Domains**:
- Natural Language Processing
- Healthcare

**Similar Benchmarks**:
- Evidence Inference (Lehman et al., 2019)
- EBM-NLP (Nye et al., 2018)

**Resources**:
- [Resource](http://evidence-inference.ebm-nlp.com/)
- [Resource](https://arxiv.org/abs/2005.04177)

## 🎯 Purpose and Intended Users

**Goal**: To expand the Evidence Inference dataset (add 2,503 prompts for a total of 12,616 prompts across 3,346 articles), provide an abstract-only subset, and evaluate stronger transformer-based baseline models for the task of inferring reported comparative findings and extracting supporting evidence from RCT reports to support NLP for Evidence Based Medicine.

**Target Audience**:
- Natural Language Processing Researchers
- Machine Learning Researchers
- Evidence-Based Medicine researchers and practitioners
- Model Developers

**Tasks**:
- Question Answering
- Text Classification
- Information Extraction (evidence span extraction / evidence identification)

**Limitations**: The authors report that adding the newly collected training data did not improve pipeline model performance (suggesting a performance plateau for the current pipeline architecture) and that stronger performance may require models with better inductive biases for the domain or improved evidence identification strategies.

## 💾 Data

**Source**: Randomized Controlled Trial reports from PubMed; expanded Evidence Inference dataset via additional annotations (prompt generation, prompt annotation, verification) performed by Medical Doctors. Combined total reported: 12,616 unique prompts from 3,346 unique articles (combining new data with Lehman et al., 2019).

**Size**: 12,616 prompts; 3,346 articles; abstract-only subset: 6,375 prompts (9,680 annotations, ~40% of annotations).

**Format**: N/A

**Annotation**: Manual annotation by Medical Doctors (hired via Upwork). Annotation pipeline comprised prompt generation, prompt annotation, and verification. Annotators recorded ICO (Intervention, Comparator, Outcome) prompts, labeled relationship as 'increase', 'decrease', 'no difference', or 'invalid prompt', and marked evidence spans (rationales). Eleven doctors were hired for new annotations (1 prompt generator, 6 prompt annotators, 4 verifiers).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (BERT-based pipeline: evidence identification then evidence classification)
- Automated metrics (macro-averaged Precision, Recall, F1 Score)
- Ablation studies and diagnostics (oracle evidence experiments, negative sampling ablations)
- Human annotation verification

**Metrics**:
- Precision
- Recall
- F1 Score (macro-averaged)
- Area Under ROC Curve (AUROC)
- Top-1 Accuracy

**Calculation**: Classification metrics (Precision, Recall, F1) are reported as macro-averaged across classes. AUROC and Top-1 Accuracy are reported for evidence identification. Models were selected based on best macro-averaged F1 on a nested held-out set.

**Interpretation**: Macro-averaged F1 is used as the primary performance indicator for the inference task. Oracle evidence experiments (using ground-truth spans or sentences) provide upper bounds on end-to-end performance. The authors report 20+ absolute point improvements in F1 over the prior baseline, and note that lack of further improvement from added data suggests architectural limitations.

**Baseline Results**: Baseline (Lehman et al., 2019): Precision 0.526, Recall 0.516, F1 0.514 (macro-averaged). Biomed RoBERTa Pipeline (this work): Precision 0.784, Recall 0.777, F1 0.780 (macro-averaged).

**Validation**: Human verification by a third doctor for each prompt: prompt generation answers 94.0% accurate, prompt generation rationales 96.1% accurate; prompt annotation answers 90.0% accurate, prompt annotation rationales 88.8% accurate. Inter-annotator Krippendorff's alpha reported as 0.854 overall (0.784 between prompt generator and annotator). Models were validated/selected on nested held-out sets (best macro F1).

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
