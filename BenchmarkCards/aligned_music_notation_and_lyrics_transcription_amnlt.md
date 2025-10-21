# Aligned Music Notation and Lyrics Transcription (AMNLT)

## 📊 Benchmark Details

**Name**: Aligned Music Notation and Lyrics Transcription (AMNLT)

**Overview**: This paper introduces and formalizes the Aligned Music Notation and Lyrics Transcription (AMNLT) challenge, which addresses the complete transcription of vocal scores by jointly considering music symbols, lyrics, and their synchronization.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/efm18/AMNLT.git)

## 🎯 Purpose and Intended Users

**Goal**: To create a comprehensive framework for the transcription of vocal music scores that integrates the alignment between music notation and lyrics.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Transcription

**Limitations**: N/A

## 💾 Data

**Source**: Four datasets: GregoSynth, Solesmes, Einsiedeln, and Salzinnes

**Size**: 20,000 pages for GregoSynth, 854 systems for Solesmes, 1,816 excerpts for Einsiedeln, and 2,965 excerpts for Salzinnes

**Format**: gabc, s-gabc, MEI

**Annotation**: Annotations follow specific encoding formats and were conducted with expert supervision.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Music Error Rate (MER)
- Character Error Rate (CER)
- Syllable Error Rate (SylER)
- Alignment Error Rate (AlER)

**Calculation**: Metrics are calculated based on the edit distance for each transcription related to musical elements and lyrics.

**Interpretation**: Lower scores in MER, CER, SylER, and AlER indicate better transcription and alignment quality.

**Baseline Results**: N/A

**Validation**: Performance evaluated through experiments on four distinct datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
