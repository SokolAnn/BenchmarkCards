# COUNTER FACT+

## 📊 Benchmark Details

**Name**: COUNTER FACT+

**Overview**: COUNTER FACT+ is a dynamic specificity benchmark that adapts to the model edit under test by modifying neighborhood prompts (prepending the model edit) to better surface unwanted side effects of model edits. It extends the existing COUNTER FACT benchmark and is more sensitive to unintended associations introduced by model editing.

**Data Type**: text (neighborhood prompts / prompt-completion pairs)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- COUNTER FACT
- ParaRel
- zsRE

**Resources**:
- [GitHub Repository](https://github.com/apartresearch/specificityplus)
- [Resource](https://specificityplus.apartresearch.com/)
- [GitHub Repository](https://github.com/kmeng01/memit)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more challenging, dynamic specificity benchmark (COUNTER FACT+) and an additional metric (Neighborhood KL divergence, NKL) to detect and quantify unwanted side effects of model editing techniques that are not detected by the original COUNTER FACT benchmark.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Model Editing Evaluation
- Specificity Evaluation
- Question Answering

**Limitations**: The approach is based on manual inspection of test cases (not scalable). More research is needed to assess effectiveness in complex scenarios such as dialogue and multi-turn conversations. The benchmark has not been evaluated for multiple simultaneous edits, parameter pruning, or transfer learning. N/A

## 💾 Data

**Source**: Derived from the COUNTER FACT dataset (Meng et al., 2022a). COUNTER FACT is a collection of 21,919 non-factual statements of the form (subject, relation, object). COUNTER FACT+ is obtained by modifying the COUNTER FACT neighborhood prompts by prepending the model edit to each neighborhood prompt.

**Size**: 21,919 non-factual statements

**Format**: JSON (dataset samples shown in appendix in JSON format)

**Annotation**: Automatically constructed: neighborhood prompts and paraphrases are sampled as in COUNTER FACT (paraphrase prompts and neighborhood prompts sampled automatically); COUNTER FACT+ modifies neighborhood prompts by prepending the model edit.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Neighborhood Score (NS)
- Neighborhood Magnitude (NM)
- Neighborhood KL Divergence (NKL) (Kullback–Leibler divergence of next-token distributions)

**Calculation**: NS is the fraction of neighborhood prompts for which the post-edit probability of the correct token P*(oc) > P*(o*). NM is P*(oc) - P*(o*). NKL is the KL divergence between the next-token probability distribution of the unedited model P(w) and the edited model P*(w): NKL = sum_{w in W} P(w) log(P(w) / P*(w)).

**Interpretation**: High NS and high NM indicate higher specificity (fewer unwanted side effects). A lower NKL indicates higher specificity (the edited model's next-token distribution is more similar to the unedited model).

**Baseline Results**: Example results (means from paper, 99% CI in tables): On GPT-J (6B) unedited model NS = 0.83 (COUNTER FACT) and 0.63 (COUNTER FACT+). For ROME on GPT-J: NS 0.79 (COUNTER FACT) -> 0.33 (COUNTER FACT+). For MEMIT on GPT-J: NS 0.82 -> 0.40. For FT-L on GPT-J: NS 0.79 -> 0.54. NKL and NM results are reported in Tables 2 and 3 of the paper.

**Validation**: Confidence intervals obtained via bootstrap resampling (N=1,000) to compute 99% confidence intervals for reported metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Potential Harm**: Detecting and preventing unwanted side effects of model edits (unintended associations introduced by edits).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
