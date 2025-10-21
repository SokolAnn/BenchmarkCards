# Hamtajoo (A Persian Plagiarism Checker for Academic Manuscripts)

## 📊 Benchmark Details

**Name**: Hamtajoo (A Persian Plagiarism Checker for Academic Manuscripts)

**Overview**: Hamtajoo is a Persian plagiarism detection system for academic manuscripts designed to investigate patterns of text re-use in Persian academic papers, addressing the challenges of plagiarism in less-resourced languages.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Persian

**Resources**:
- [Resource](http://www.sid.ir/)

## 🎯 Purpose and Intended Users

**Goal**: To develop an efficient plagiarism detection system tailored to the complexities of the Persian language and academic writing.

**Target Audience**:
- Academics
- Researchers
- Educational Institutions

**Tasks**:
- Plagiarism Detection

**Limitations**: N/A

## 💾 Data

**Source**: A reference collection of Persian academic papers indexed by SID (Scientific Information Database).

**Size**: 480,000 documents

**Format**: Various file formats including .doc, .docx, .txt

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Candidate retrieval
- Text alignment

**Metrics**:
- Recall
- Precision
- F-Measure

**Calculation**: Performance metrics are computed based on comparisons of detected plagiarism to known instances in the corpus.

**Interpretation**: Higher recall indicates better detection of plagiarized content, while higher precision means fewer false positives.

**Baseline Results**: Hamtajoo achieved the second rank in recall measure and the best results in runtime during evaluations against other plagiarism detection systems.

**Validation**: Performance evaluated using standard datasets from PAN Plagiarism Detection competitions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
