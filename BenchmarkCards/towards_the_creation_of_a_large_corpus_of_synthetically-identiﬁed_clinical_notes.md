# Towards the Creation of a Large Corpus of Synthetically-Identiﬁed Clinical Notes

## 📊 Benchmark Details

**Name**: Towards the Creation of a Large Corpus of Synthetically-Identiﬁed Clinical Notes

**Overview**: This work presents a first step toward creating a large synthetically-identiﬁed corpus of clinical notes and corresponding PHI annotations in order to facilitate the development de-identiﬁcation tools. Further, one such tool is evaluated against this corpus in order to understand the advantages and shortcomings of this approach.

**Data Type**: text (clinical notes with PHI annotations / synthetically-identified notes)

**Domains**:
- Natural Language Processing
- Healthcare

**Similar Benchmarks**:
- Informatics for Integrating Biology and the Bedside (i2b2) 2006 corpus
- 2014 i2b2/UTHealth corpus

**Resources**:
- [Resource](http://names.mongabay.com/)

## 🎯 Purpose and Intended Users

**Goal**: 1. Provide first steps toward a corpus of clinical notes that have been synthetically-identified, meaning they have been de-identiﬁed and PHI has been replaced with reasonable surrogates. 2. Evaluate a baseline de-identiﬁcation system against this data in order to understand advantages and shortcomings of this approach.

**Target Audience**:
- Researchers developing de-identification tools
- Clinical Natural Language Processing researchers
- The research community (clinical NLP)

**Tasks**:
- De-identification
- Named Entity Recognition

**Limitations**: The system created by Neamatullah et al. favors recall over precision as it introduces virtually no false negatives, while there are numerous false positives accounting for up to 15% of the PHI instances detected. Creation of the synthetically-identified dataset directly from the identified data is necessary so as not to unnecessarily introduce meaningless surrogate data. Using surrogate data may constrain the natural variety of names, places, and other entities that appear in notes (e.g., through misspellings); thus, making the task slightly easier. Patient identity coreference was not performed for this initial work.

## 💾 Data

**Source**: MIMIC-III (publicly available dataset developed by the MIT Lab for Computational Physiology)

**Size**: 2,083,180 notes; 1,685,352 notes contain PHI (80.90%); 492,393,558 tokens; 12,596,126 PHI instances; data for 61,532 ICU stays for 46,520 patients

**Format**: N/A

**Annotation**: Synthetically-identified notes were created by substituting surrogate values for annotated PHI. Names were chosen proportional to their frequency from the 2005 U.S. Census and hospitals were chosen uniformly from a list of U.S. hospitals. Initial efforts focused on patient names and hospitals.

## 🔬 Methodology

**Methods**:
- Conditional Random Field (CRF) statistical modeling for de-identification
- Automated token-level evaluation (precision, recall, F1)

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Evaluation performed at the token-level so that multi-token PHI instances are treated separately. Token-level precision, recall, and F1 are reported.

**Interpretation**: Token-level precision/recall/F1 indicate the percentage of PHI tokens detected. The authors report that 'the more data, the better': precision is already good with small training data, while recall continues to improve substantially with more training data.

**Baseline Results**: PATIENT_NAME (# training files -> precision, recall, f1): 100 -> 0.89, 0.78, 0.83; 200 -> 0.90, 0.87, 0.88; 500 -> 0.91, 0.93, 0.92; 1000 -> 0.92, 0.96, 0.94. HOSPITAL (# training files -> precision, recall, f1): 100 -> 0.92, 0.72, 0.81; 200 -> 0.93, 0.79, 0.86; 500 -> 0.94, 0.87, 0.91; 1000 -> 0.95, 0.89, 0.92.

**Validation**: Evaluation performed on the synthetically-identified corpus using token-level precision, recall, and F1. No additional validation procedures beyond the token-level evaluation on this corpus are described.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Potential Harm**: ['Exposure of protected health information (PHI) / violation of patient privacy']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Notes are synthetically-identified by substituting surrogate values for annotated PHI. The original MIMIC-III notes were made publicly available after de-identification using a rule-based system (Neamatullah et al.).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
