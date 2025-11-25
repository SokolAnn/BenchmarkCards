# MUTANT: A Multi-sentential Code-mixed Hinglish Dataset

## 📊 Benchmark Details

**Name**: MUTANT: A Multi-sentential Code-mixed Hinglish Dataset

**Overview**: We propose a novel task of identifying multi-sentential code-mixed text (MCT) from multilingual articles and build a first-of-its-kind multi-sentential code-mixed Hinglish dataset (MUTANT). The MUTANT dataset comprises 67k articles with 85k identified Hinglish MCTs. We propose a token-level language-aware pipeline, extend the code-mixing index to a multi-sentential framework, and make the dataset publicly available to facilitate future research.

**Data Type**: multi-sentential code-mixed text spans (Hinglish)

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi
- English

**Similar Benchmarks**:
- Phinc
- Gupshup
- Hinge

**Resources**:
- [Resource](https://arxiv.org/abs/2302.11766)
- [Resource](https://aamaadmiparty.org/media/press-releases)
- [Resource](https://www.inc.in/media/speeches)
- [Resource](https://www.pmindia.gov.in/hi/mann-ki-baat/)
- [Resource](https://www.pib.gov.in)
- [Resource](https://www.pmindia.gov.in/hi/news-updates/)
- [Resource](https://www.bhaskar.com)
- [Resource](https://www.jagran.com)
- [GitHub Repository](https://github.com/ritwikmishra/devanagari-to-roman-script-transliteration)

## 🎯 Purpose and Intended Users

**Goal**: Identify multi-sentential code-mixed text (MCT) from multilingual documents and provide a multi-sentential Hinglish dataset (MUTANT) to facilitate future research in code-mixed and low-resource languages.

**Target Audience**:
- ML Researchers
- Natural Language Processing researchers
- Model Developers

**Tasks**:
- Question Answering
- Text Summarization
- Machine Translation
- Language Model Pre-training

**Limitations**: •Contrary to the previous works, all the data sources comprises the non social media sites. This could potentially limit the diversity in the code-mixed text as observed on social media platforms.
•In the current form, the dataset is limited to only one code-mixed language. We believe the proposed technique to extract MCT could be expanded to other code-mixed languages in the future.
•The data sources could potentially have their own biases (topical, style of writing, etc). We expect future works to be cautious while generalizing the results obtained on this dataset.

## 💾 Data

**Source**: Political speeches and press releases scraped from Aam Aadmi Party press releases, Indian National Congress speeches, Man-ki-baat transcripts, Press Information Bureau articles, PM speeches; Hindi news articles scraped from Dainik Bhaskar and Dainik Jagran.

**Size**: 67,007 articles; 84,937 identified MCTs (MUTANT); average 159 tokens per MCT; average 10.23 sentences per MCT

**Format**: N/A

**Annotation**: Semi-automated: automated identification via a token-level language-aware pipeline using L3Cube-HingLID (for Roman script) with Devanagari-to-Roman transliteration for Devanagari tokens, combined with Dual MEC (CMI-based) thresholding. A small manually annotated dataset (SAnD) of 120 articles and 568 MSTs (121 MSTs labeled as code-mixed) was created by an expert annotator and used for threshold selection and tuning.

## 🔬 Methodology

**Methods**:
- Token-level language annotation using L3Cube-HingLID
- Devanagari-to-Roman transliteration (GitHub tool)
- Code-Mixing Index (CMI)
- Dual Multilinguality Estimation Criteria (Dual MEC) combining sentence-level CMI and Multilinguality Ratio (MR)
- Grid search for optimal (CMI threshold, MR threshold)
- Threshold generalization techniques: Local Average (LA), Global Average (GA), Average of LA and GA (ALG), Single data source generalization (SDG), Multi data source generalization (MDG)
- Qualitative human evaluation with two human evaluators

**Metrics**:
- Accuracy
- False MCT Rate (FMR)
- Diversity@10 (D@10)
- Code-Mixing Index (CMI)
- Cohen’s kappa

**Calculation**: Accuracy: (number of correct MCT and non-MCT predictions / total number of MST) * 100. FMR (False MCT Rate): ratio of incorrectly identified MCT to total number of actual monolingual MST, reported as percent. D@10 (Diversity@10): percentage of articles in a data source having more than 10% correctly identified MCT. CMI: as defined in Equation (1) in the paper measuring degree of code-mixing per text (ranges 0-100). Sentence-level CMI and Multilinguality Ratio (MR) are combined; thresholds for CMI (β) and MR (φ) selected by grid search on SAnD.

**Interpretation**: High Accuracy (%) is preferred. Low FMR (%) is preferred. High D@10 (%) is preferred. Low CMI indicates prevalence of a single language; high CMI indicates high degree of code-mixing. Sentence-level CMI > β labels a sentence as code-mixed; MR > φ labels an MST as code-mixed.

**Baseline Results**: The Multi data source generalization (MDG) threshold generalization technique yields consistently better trade-offs with higher accuracy and lower FMR across datasets compared to mean-based generalization techniques (LA, GA, ALG), as reported in Tables 6-8; the paper states MDG 'satisfies both conditions with low FMR and high accuracy on all the datasets'.

**Validation**: Thresholds (β and φ) were selected via grid search on the small annotated dataset SAnD (120 articles, 568 MSTs). Performance of the MCT identification pipeline and generalization techniques was evaluated on subsets of SAnD (Dspeech, Dnews, Dspeech + Dnews). Qualitative validation was performed by two independent human evaluators on a random sample (5 articles from each source) reporting complete agreement and Cohen's kappa scores.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Governance**: Lack of testing diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
