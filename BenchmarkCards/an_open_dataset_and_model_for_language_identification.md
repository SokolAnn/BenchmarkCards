# An Open Dataset and Model for Language Identification

## 📊 Benchmark Details

**Name**: An Open Dataset and Model for Language Identification

**Overview**: The paper presents a curated, open dataset of monolingual text covering 201 languages, manually auditing a sample from each source and language to ensure label reliability; it also presents a fastText-based LID model trained on this dataset (60.5 million parameters) and makes both the dataset and model publicly available. The dataset and model are analysed and compared to existing open LID systems.

**Data Type**: text (monolingual lines; sentence-level)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- FLORES-200 Evaluation Benchmark
- NLLB
- WiLI benchmark dataset
- CLD3

**Resources**:
- [GitHub Repository](https://github.com/laurieburchell/open-lid-dataset)
- [GitHub Repository](https://github.com/facebookresearch/fairseq/tree/nllb)
- [GitHub Repository](https://github.com/facebookresearch/flores/blob/main/)
- [Resource](https://tinyurl.com/nllblid218e)
- [Resource](https://pypi.org/project/pycld3)
- [Resource](https://www.csd3.cam.ac.uk)
- [Resource](https://www.dirac.ac.uk)
- [Resource](https://omniglot.com/writing/minangkabau.htm)

## 🎯 Purpose and Intended Users

**Goal**: Provide a curated, open dataset covering 201 languages with manual auditing of samples to ensure reliable language labels; train and release a high-coverage LID model on this dataset; analyse model performance and highlight open problems in LID research.

**Target Audience**:
- Research community

**Tasks**:
- Language Identification

**Limitations**: The dataset and model cover 201 languages (those testable with the FLORES-200 Evaluation Benchmark). The test set consists of sentences from a single domain (Wikipedia articles), so performance on this test set may not reflect performance in other domains. Most of the data was not audited by native speakers; future versions should verify more languages with native speakers.

## 💾 Data

**Source**: Sources were chosen to maximise trustworthy language labels and avoid web-crawled datasets. The majority of source datasets were derived from news sites, Wikipedia, or religious text, with some from transcribed conversations, literature, or social media. Specific sources are listed in Appendix A (examples: Leipzig Corpora Collection, Global Voices, Tatoeba, NLLB Seed, MADAR, LTI LangID Corpus, SETIMES, Tatoeba, MIZAN, etc.).

**Size**: 121 million lines of data in 201 language classes; mean lines per language before sampling 602,812; smallest class 532 lines (South Azerbaijani); largest class 7.5 million lines (English).

**Format**: Raw text lines (one line per sentence/text); line-based files after minimal preprocessing.

**Annotation**: Manual audit and standardisation of language labels: two authors audited random samples from each source and language (one native Bulgarian speaker and one native English speaker); language codes were standardised to match Costa-jussà et al. (2022) conventions with conservative reassignment for macrolanguages.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation on FLORES-200 dev-test (FLORES-200*)
- Model comparison to existing open LID systems (NLLB, CLD3)
- Manual audit of dataset samples

**Metrics**:
- F1 Score (macro-average)
- False Positive Rate (FPR) (macro-average)
- Pearson correlation between training data size and per-language F1 (reported value: 0.0242)

**Calculation**: Macro-averages of F1 scores and FPR are reported across languages to avoid downweighting low-resource languages. FPR is reported following Caswell et al. (2020) to indicate real-world performance under class skew.

**Interpretation**: Higher macro-average F1 indicates better per-language classification performance; lower macro-average FPR indicates fewer false positives in imbalanced scenarios. Macro-averaging is used to give equal weight to low-resource languages.

**Baseline Results**: On FLORES-200* (201 languages): Our model F1 = 0.927, FPR = 0.033. On FLORES-200* ∩ NLLB (193 languages): Our model F1 = 0.959, FPR = 0.020; NLLB F1 = 0.950, FPR = 0.023. On FLORES-200* ∩ CLD3 (95 languages): Our model F1 = 0.989, FPR = 0.011; NLLB F1 = 0.985, FPR = 0.019; CLD3 F1 = 0.968, FPR = 0.030. Model training: fastText model, 60.5 million parameters, ~1 hour 45 minutes training on a 76-CPU 256 GiB RAM node; inference over 206,448 test lines took 22.4 seconds (~9,216.4 lines/sec).

**Validation**: Evaluation on the FLORES-200 dev-test (human-verified target side) after removing three languages (resulting in FLORES-200* with 201 languages). Manual audit of random samples from each source and language to ensure label reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on cultural diversity, Impact on affected communities
- **Governance**: Lack of data transparency

**Demographic Analysis**: The paper analyses performance by language resource class using the taxonomy of Joshi et al. (2020), reporting mean F1 and mean FPR per class and providing per-language breakdowns in Appendix C.

**Potential Harm**: ['Representation washing (false impression of progress for low-resource languages due to noisy labels)', 'Exclusion of minority dialects, scripts, or microlanguages through choices of coverage', 'Worse downstream performance for particular language groups due to unequal LID performance']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Authors checked that each dataset was either under an open license for research purposes or described as free to use; further license information is available in the code repository.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
