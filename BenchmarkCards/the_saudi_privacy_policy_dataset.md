# The Saudi Privacy Policy Dataset

## 📊 Benchmark Details

**Name**: The Saudi Privacy Policy Dataset

**Overview**: This paper introduces the Saudi Privacy Policy Dataset, a diverse compilation of Arabic privacy policies from various sectors in Saudi Arabia, annotated according to the 10 principles of the Personal Data Protection Law (PDPL). The annotated dataset is intended for assessing privacy policy compliance, benchmarking privacy practices across industries, and developing automated tools for monitoring adherence to data protection regulations.

**Data Type**: text (privacy policy lines / sentences)

**Domains**:
- Data Science
- Natural Language Processing
- Legal

**Languages**:
- Arabic

**Resources**:
- [GitHub Repository](https://github.com/iwan-rg/Saudi_Privacy_policy)
- [Resource](https://www.sama.gov.sa/en-us/licenseentities/pages/licensedbanks.aspx)
- [Resource](https://www.my.gov.sa/wps/portal/snp/agencies/!ut/p/z0/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zivQIsTAwdDQz9_d29TAwCnQ1DjUy9wgwMgk31g1Pz9AuyHRUBX96rjw!!/)
- [Resource](https://chi.gov.sa/en/insurancecompanies/Pages/default.aspx)
- [Resource](https://laws.boe.gov.sa/boelaws/laws/lawdetails/b7cfae89-828e-4994-b167-adaa00e37188/1)
- [Resource](https://gdpr-info.eu/)

## 🎯 Purpose and Intended Users

**Goal**: To address the lack of comprehensive and annotated privacy policy datasets tailored to the Saudi Arabian context by gathering privacy policies from various sectors and annotating them according to the PDPL's 10 principles, facilitating research, compliance assessment, benchmarking, and development of NLP and machine learning tools for privacy policy analysis.

**Target Audience**:
- Researchers
- Policymakers
- Industry Professionals

**Tasks**:
- Text Classification
- Text Analysis
- Privacy Policy Compliance Assessment

**Limitations**: Only the first webpage of privacy policies was collected; PDF files, additional links, and websites with disabled copy-text functionality were discarded. Some websites were excluded due to downtime or incorrectly stated privacy policies.

## 💾 Data

**Source**: Data were acquired from multiple sources including the Saudi Central Bank, the Saudi Arabia National United Platform, the Council of Health Insurance, and general websites found using Google and Wikipedia (classification-based searching on Wikipedia).

**Size**: 1,000 websites; 4,638 lines of text; 775,370 tokens; corpus size 8,353 KB

**Format**: CSV

**Annotation**: Manual annotation by the authors according to the 10 principles of the Personal Data Protection Law (PDPL). Annotations were performed using Microsoft Excel; three annotators (each annotated 333 policies) with native Arabic background performed the labeling. Intersection files (302) were used to compute Inter-Annotator Agreement.

## 🔬 Methodology

**Methods**:
- Manual data scraping and extraction
- Data cleaning and preprocessing (normalization, tokenization)
- Manual annotation by human annotators using Microsoft Excel
- Inter-Annotator Agreement measurement

**Metrics**:
- Cohen's kappa
- Inter-Annotator Agreement (percentage)

**Calculation**: Cohen's kappa was computed between each pair of annotators on the intersection files (302 files) to measure agreement. The paper reports category-level Cohen's kappa values (e.g., Finance 0.96, E-commerce 0.94, Government 0.92, News 0.98, Healthcare 0.98, Educational 0.94, Other 0.97) and average agreement percentages of 95%, 96%, and 95% between annotator pairs.

**Interpretation**: Results show almost perfect agreement between annotators.

**Validation**: Validation of annotations via Inter-Annotator Agreement using Cohen's kappa computed on 302 intersection files between annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Legal Compliance

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data were collected from publicly accessible websites; the authors state the data used do not pose any ethical concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Dataset annotations aligned with the Personal Data Protection Law (PDPL); the PDPL is stated to be established to be compatible with the General Data Protection Regulation (GDPR).
