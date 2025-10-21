# A Corpus for Detecting High-Context Medical Conditions in Intensive Care Patient Notes Focusing on Frequently Readmitted Patients

## 📊 Benchmark Details

**Name**: A Corpus for Detecting High-Context Medical Conditions in Intensive Care Patient Notes Focusing on Frequently Readmitted Patients

**Overview**: We introduce a dataset for patient phenotyping, defined as the identification of whether a patient has a given medical condition based on their patient note. Nursing Progress Notes and Discharge Summaries from the Intensive Care Unit of a large tertiary care hospital were manually annotated for the presence of several high-context phenotypes relevant to treatment and risk of re-hospitalization. This dataset contains 1102 Discharge Summaries and 1000 Nursing Progress Notes. Each Discharge Summary and Progress Note has been annotated by at least two expert human annotators (one clinical researcher and one resident physician). Annotated phenotypes include treatment non-adherence, chronic pain, advanced/metastatic cancer, as well as 10 other phenotypes. This dataset can be utilized for academic and industrial research in medicine and computer science, particularly within the field of medical natural language processing.

**Data Type**: text (Discharge Summaries and Nursing Progress Notes)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MIMIC-III

**Resources**:
- [Resource](https://mimic.physionet.org)
- [GitHub Repository](https://github.com/EdwardMoseley/ACTdb)
- [Resource](https://arxiv.org/abs/2003.03044)

## 🎯 Purpose and Intended Users

**Goal**: Provide a dataset of annotated discharge summaries and nursing progress notes for patient phenotyping (identifying whether a patient has given medical conditions from notes), focusing on high-context phenotypes relevant to treatment and risk of re-hospitalization in frequently readmitted ICU patients.

**Target Audience**:
- Academic researchers in medicine and computer science
- Industry researchers in medicine and computer science
- Medical Natural Language Processing researchers

**Tasks**:
- Text Classification
- Patient Phenotyping
- Multi-label Classification

**Limitations**: Data are unique to Beth Israel Deaconess Medical Center (BIDMC), and models resulting from these data may not generalize to notes generated at other hospitals. Admissions to hospitals not associated with BIDMC will not have been captured, and generalizability is limited due to the limited geographic distribution of patients which present to the hospital.

## 💾 Data

**Source**: Discharge Summaries and Nursing Progress Notes extracted from the MIMIC database (MIMIC-III) originating from Beth Israel Deaconess Medical Center, focusing on frequently readmitted ICU patients (defined as admitted to the ICU more than three times in a single year).

**Size**: 1102 Discharge Summaries and 1000 Nursing Progress Notes

**Format**: Tabular (fields: Subject Identifier (integer), Hospital Admission Identifier (integer), Category (string), Text (string), 15 Phenotypes (binary) including 'None' and 'Unsure', Batch Date (string), Operators (string))

**Annotation**: Manual annotation by expert annotators: each note annotated by at least two annotators (one clinical researcher and one resident physician). Operators were grouped and worked independently; annotation occurred over one year; 13 phenotypes annotated with an 'unsure' label option.

## 🔬 Methodology

**Methods**:
- Manual annotation by clinical researchers and resident physicians
- Inter-annotator agreement measurement using Cohen's Kappa
- Baseline model evaluation using Bag-of-Words + Logistic Regression and Convolutional Neural Network

**Metrics**:
- F1 Score
- Cohen's Kappa

**Calculation**: F1-score reported as percentage per phenotype for baseline models. Cohen's Kappa was calculated for each phenotype and pair of annotators for which precisely two note annotations were recorded.

**Interpretation**: Authors report inter-annotator Cohen's Kappa and baseline model F1-scores to demonstrate dataset quality and suitability for developing rule-based and statistical models for patient phenotyping.

**Baseline Results**: BoW and CNN F1-score (in %): Adv. / Metastatic Cancer: 56 (BoW), 74 (CNN); Adv. Heart Disease: 44, 75; Adv. Lung Disease: 24, 48; Alcohol Abuse: 67, 76; Chronic Neurologic Dystrophies: 46, 69; Chronic Pain: 41, 49; Depression: 58, 84; Obesity: 30, 95; Psychiatric disorders: 50, 83; Substance Abuse: 56, 75.

**Validation**: Inter-annotator agreement assessed via Cohen's Kappa per phenotype and annotator pair (Table 4). Statistical analyses and tabulations performed with R version 3.5.2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Laws
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Authors note limited geographic distribution of patients which limits generalizability; no detailed demographic breakdown is provided in the paper.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The corpus comprises original healthcare data which contains protected health information (PHI) per the Health Insurance Portability and Accountability Act of 1996 (HIPAA). Access to the data is restricted and subject to MIMIC-III access requirements.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data access and use are subject to HIPAA considerations; individuals must satisfy MIMIC-III access requirements (including taking a 'Data or Specimens Management' course and signing a user agreement) as outlined on the MIMIC-III database webpage.
