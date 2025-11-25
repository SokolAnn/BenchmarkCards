# MACRONYM: A Large-Scale Dataset for Multilingual and Multi-Domain Acronym Extraction

## 📊 Benchmark Details

**Name**: MACRONYM: A Large-Scale Dataset for Multilingual and Multi-Domain Acronym Extraction

**Overview**: We propose a new dataset for multilingual multi-domain Acronym Extraction (AE). Specifically, 27,200 sentences in 6 typologically different languages and 2 domains, i.e., Legal and Scientific, is manually annotated for AE.

**Data Type**: text (sentence-level annotated sentences with acronym and long-form spans)

**Domains**:
- Legal
- Scientific

**Languages**:
- English
- Danish
- Spanish
- French
- Persian
- Vietnamese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Introduce the first multilingual and multi-domain manually labeled dataset for Acronym Extraction to support research and advanced model development.

**Target Audience**:
- ML Researchers
- Model Developers
- NLP Researchers

**Tasks**:
- Acronym Extraction

**Limitations**: Dataset currently covers 6 languages and 2 domains only; Persian and Vietnamese portions are relatively small; sentence filtering for candidate selection was applied only to English, French, Spanish, and Danish.

## 💾 Data

**Source**: United Nations Parallel Corpus (UNPC); Europarl corpus; ACL anthology papers (English scientific papers); public computer science M.S./Ph.D. theses in Persian and Vietnamese.

**Size**: 27,200 annotated sentences total; Legal-English: 4,000 sentences; Legal-Spanish: 6,400 sentences; Legal-French: 8,000 sentences; Legal-Danish: 3,000 sentences; Scientific-English: 4,000 sentences; Scientific-Persian: 1,000 sentences; Scientific-Vietnamese: 800 sentences.

**Format**: N/A

**Annotation**: Manual annotation by native speakers recruited via Upwork; two annotators per language independently annotated sampled sentences then resolved disagreements to produce the final annotations. Annotators were trained with guidelines and examples; acronyms are required to be single words and long forms annotated must be in the same language as the sentence.

## 🔬 Methodology

**Methods**:
- Automated evaluation using a rule-based AE system (Veyseh et al., 2021)
- Sequence labeling with BIO tagging using fine-tuned transformer-based models (mBERT, XLM-R)
- Evaluation in four learning settings: Mono-Lingual Mono-Domain, Mono-Lingual Cross-Domain, Cross-Lingual Mono-Domain, Cross-Lingual Cross-Domain

**Metrics**:
- F1 Score (model performance)
- Krippendorff's alpha (inter-annotator agreement) with MASI distance

**Calculation**: Inter-annotator agreement computed using Krippendorff's alpha with MASI distance for initial independent annotations. Model performance measured and reported using F1 Score (as shown in Table 2).

**Interpretation**: Lower F1 scores indicate poorer model performance; the paper interprets substantially lower performance in cross-lingual and cross-domain settings compared to mono-lingual mono-domain as evidence of challenges due to language differences and domain shift. High Krippendorff's alpha indicates annotation quality.

**Baseline Results**: Table 2 (F1 scores). Mono-Lingual Mono-Domain (Rule-Based / mBERT / XLMR): Legal-English: 16.55 / 61.66 / 62.07; Legal-Spanish: 10.82 / 51.43 / 55.41; Legal-French: 10.05 / 58.77 / 61.14; Legal-Danish: 8.78 / 50.05 / 48.38; Scientific-English: 20.72 / 60.51 / 59.00; Scientific-Persian: 60.59 / 62.41 / 63.10; Scientific-Vietnamese: 53.44 / 58.71 / 59.13. (Full table includes additional cross-domain and cross-lingual settings as reported in the paper.)

**Validation**: For each language-domain pair, annotated sentences were randomly split into training/development/test with ratios 80/10/10. Hyper-parameters were tuned on development data. Inter-annotator agreement (Krippendorff's alpha with MASI) was computed to assess annotation quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
