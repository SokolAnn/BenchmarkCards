# Polish-ASTE: Aspect-Sentiment Triplet Extraction Datasets for Polish

## 📊 Benchmark Details

**Name**: Polish-ASTE: Aspect-Sentiment Triplet Extraction Datasets for Polish

**Overview**: This paper introduces two new datasets for Aspect-Sentiment Triplet Extraction (ASTE) that contain customer opinions about hotels and purchased products expressed in Polish.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Polish

**Similar Benchmarks**:
- SemEval

**Resources**:
- [Resource](https://creativecommons.org/licenses/by-sa/4.0/)
- [Resource](https://anonymous.4open.science/r/Polish-ASTE-Datasets-anonymous/corpora)

## 🎯 Purpose and Intended Users

**Goal**: To provide datasets for the challenging task of Aspect-Sentiment Triplet Extraction (ASTE) in the Polish language.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Aspect-Sentiment Triplet Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Customer reviews taken from the Wroclaw Corpus of Consumer Reviews Sentiment (WCCRS), specifically from the domains of hotels and products.

**Size**: 1,197 examples for hotels, 851 examples for products

**Format**: JSON

**Annotation**: Annotated by Polish native speakers using the Doccano annotation platform.

## 🔬 Methodology

**Methods**:
- GTS (Grid Tagging Scheme)
- EPISA (Exploiting Phrase Interrelations Span-level Approach)

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated using exact match criteria for triplet accuracy.

**Interpretation**: Higher F1 scores indicate better performance by models in extracting aspect-sentiment triplets.

**Baseline Results**: TrelBERT achieved the highest F1-score values for the Polish datasets.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0 Deed

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
