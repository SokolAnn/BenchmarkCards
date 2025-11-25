# Two Word Test (TWT)

## 📊 Benchmark Details

**Name**: Two Word Test (TWT)

**Overview**: An open-source benchmark that assesses semantic abilities of large language models using two-word noun-noun phrases. The test requires meaningfulness judgments of 1,768 noun-noun combinations that were rated by 150 human participants and is provided in both a 0-4 Likert-scale version and a binary 'makes sense'/'nonsense' version.

**Data Type**: text (two-word noun-noun phrases with human meaningfulness ratings)

**Domains**:
- Natural Language Processing
- Psycholinguistics

**Languages**:
- English

**Similar Benchmarks**:
- General Language Understanding Evaluation (GLUE)
- SuperGLUE

**Resources**:
- [GitHub Repository](https://github.com/NickRiccardi/two-word-test)

## 🎯 Purpose and Intended Users

**Goal**: To measure LLM comprehension of combinatorial semantics by having models judge the meaningfulness of two-word noun-noun phrases.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Cognitive Scientists

**Tasks**:
- Text Classification
- Ordinal Rating (Meaningfulness Judgment)

**Limitations**: Ambiguous phrases (392 with mean ratings between 1.5 and 2.5) were removed from the set; the test does not rely on inference or complex multi-step reasoning; performance may reflect limits of text corpora coverage and underlying semantic knowledge rather than executive control.

**Out of Scope Uses**:
- Logical reasoning
- Planning
- Inferring implied content
- Disambiguating ambiguous words
- Solving puzzles or other multi-step problems

## 💾 Data

**Source**: Derived from Graves et al. (2013): 500 common nouns combined to form all noun-noun combinations, filtered by corpus occurrence and manual removal; final set used here consists of noun-noun phrases from that procedure.

**Size**: 1,768 phrases (977 nonsense and 761 meaningful)

**Format**: N/A

**Annotation**: Human meaningfulness ratings on a 0-4 Likert scale collected from 150 participants (from Graves et al. 2013); binary labels provided for a binary version (bTWT).

## 🔬 Methodology

**Methods**:
- Automated model evaluation (LLM prompting with provided instructions and examples)
- Statistical hypothesis testing (Crawford & Howell single-case t-test)
- Signal Detection Theory analysis (d', β, hit/false alarm rates)
- Receiver Operating Characteristic (ROC) and Area Under Curve (AUC) analysis
- Chi-squared (χ2) tests
- Permutation / chance distribution comparisons
- Simulated human response distributions (10,000 samples per phrase)

**Metrics**:
- d' (d-prime)
- β (beta; log10 reported)
- Area Under the Curve (AUC)
- Chi-squared (χ2)
- Crawford & Howell t-test (single-case vs. control group)
- TWT failure rate (% of phrases with p < .05 relative to human distribution)

**Calculation**: For numerical TWT: human phrase-wise means and standard deviations were used to generate a Gaussian distribution of 10,000 simulated human responses per phrase (bounded to 0-4 and rounded to integers). Each LLM rating for a phrase was compared to the simulated human distribution using the Crawford & Howell t-test; a 'TWT failure' is defined as p < .05. For binary bTWT: hits, misses, false alarms, and correct rejections were computed to derive d' and β; ROC curves and AUC were computed. χ2 tests compared LLM response frequencies to human frequencies. Permutation (chance) distributions were generated for comparison.

**Interpretation**: Higher d' and AUC indicate better discrimination (d' = 0 is chance; >4 is near-perfect). β < 0 (log10) indicates a liberal bias, β > 0 indicates a conservative bias. A TWT failure (p < .05 in Crawford & Howell test) indicates the LLM rating is significantly different from human responses for that phrase. Lower % failures indicates closer alignment to human judgments.

**Baseline Results**: TWT failure rates (all 1,768 phrases / most-agreed 868 phrases): Bard 42.7% / 57.9%; GPT-3.5 49.3% / 62.4%; GPT-4 23.4% / 23.2%. bTWT (all 1,768 phrases): Bard d' = 0.55, β = -0.11, AUC = 0.60; GPT-3.5 d' = 0.78, β = -0.36, AUC = 0.59; GPT-4 d' = 1.79, β = 0.17, AUC = 0.81. For the 868 most-agreed phrases: Bard d' = 0.74, β = -0.13, AUC = 0.63; GPT-3.5 d' = 1.23, β = -0.54, AUC = 0.65; GPT-4 d' = 2.58, β = 0.20, AUC = 0.90. χ2 comparisons were significant for all models (examples: GPT-3.5 χ2 = 538.1, p < .001; GPT-4 χ2 = 10.6, p = .001 for all phrases).

**Validation**: Benchmark comparisons are validated against human ratings from Graves et al. (2013). Simulated human distributions (10,000 samples) and permuted-chance distributions were generated to contextualize model performance. Statistical tests (Crawford & Howell t-test, χ2, SDT metrics, ROC/AUC) and permutation comparisons were used to assess reliability and significance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
