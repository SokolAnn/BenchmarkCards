# MultiBooked: A Corpus of Basque and Catalan Hotel Reviews Annotated for Aspect-level Sentiment Classification.

## 📊 Benchmark Details

**Name**: MultiBooked: A Corpus of Basque and Catalan Hotel Reviews Annotated for Aspect-level Sentiment Classification.

**Overview**: We introduce two datasets for supervised aspect-level sentiment analysis in Basque and Catalan, both of which are under-resourced languages. We provide high-quality annotations and benchmarks with the hope that they will be useful to the growing community of researchers working on these languages. The corpus is available at http://hdl.handle.net/10230/33928 or https://jbarnesspain.github.io/resources/ .

**Data Type**: text (hotel review documents with aspect-level opinion annotations: opinion holders, opinion targets, opinion expressions, and polarity labels)

**Domains**:
- Natural Language Processing

**Languages**:
- Catalan
- Basque

**Similar Benchmarks**:
- MPQA
- OpeNER
- SemEval-2014 Task 4
- SemEval-2015 Task 12
- SemEval-2016 Task 5
- USAGE review corpus

**Resources**:
- [Resource](http://hdl.handle.net/10230/33928)
- [Resource](https://jbarnesspain.github.io/resources/)

## 🎯 Purpose and Intended Users

**Goal**: The aim of this annotation project is to allow researchers to enable research on supervised aspect-level sentiment analysis in Basque and Catalan, as well as provide useful data for cross- and multi-lingual sentiment analysis.

**Target Audience**:
- Researchers working on Basque and Catalan languages
- Natural Language Processing researchers

**Tasks**:
- Aspect-level Sentiment Analysis
- Sequence Labeling
- Text Classification

**Limitations**: The drop in benchmark performance is attributed by the authors to the use of a relatively simple baseline system and to the richer morphological systems of Catalan and Basque which were not exploited.

## 💾 Data

**Source**: Crawled hotel reviews: Catalan reviews from www.booking.com; Basque reviews crawled from a number of websites (authors state a total of 35 different websites including www.airbnb.com, www.atrapalo.com, www.nekatur.net, www.rentalia.es, www.toprural.es, and www.tripadvisor.com). Reviews collected from November 2015 to January 2016. Language identification was used to remove Spanish or mixed reviews and reviews shorter than 7 tokens.

**Size**: 567 reviews (Catalan); 343 reviews (Basque). Number of targets: 2762 (Catalan), 1775 (Basque). Number of expressions: 2346 (Catalan), 2328 (Basque). Number of holders: 236 (Catalan), 296 (Basque). Average length in tokens: 45 (Catalan), 46.9 (Basque).

**Format**: KAF/NAF (stand-off XML) format

**Annotation**: Manual annotation following the OpeNER annotation scheme: annotators labeled opinion holders, opinion targets, opinion expressions, and polarity (STRONG NEGATIVE, NEGATIVE, POSITIVE, STRONG POSITIVE). Annotation performed using the KafAnnotator tool in a three-phase process with annotator comparison meetings and a third annotator adjudicating conflicts.

## 🔬 Methodology

**Methods**:
- Sequence labeling baseline using Conditional Random Field (CRF) on standard sequence-labeling features (word-, subword-, and part-of-speech features)
- Polarity classification using Bag-of-Words features with a linear Support Vector Machine (SVM)
- 10-fold cross-validation (with 80 percent of the data reserved for training during each fold)

**Metrics**:
- Weighted F1 score
- AvgAgr (average agr inter-annotator agreement)
- Mean Squared Error (MSE) for polarity agreement

**Calculation**: Inter-annotator agreement: agr(a||b) = |A_matching_B| / |A|; AvgAgr(a,b) = 1/2 * (agr(a||b) + agr(b||a)). Polarity MSE: assign integers to labels (Strong Negative: 0, Negative: 1, Positive: 2, Strong Positive: 3) and compute mean squared error per sentence, then average across corpus. Evaluation: weighted F1 score reported for extraction and classification using 10-fold cross-validation.

**Interpretation**: For AvgAgr, perfect agreement is 1.0 and no agreement is 0.0. Similar annotation projects report AvgAgr scores between 0.6 and 0.8. For polarity MSE, perfect agreement is 0.0; larger MSE indicates larger discrepancies in polarity assignment. Weighted F1 is used to evaluate extraction and classification performance (higher is better).

**Baseline Results**: Extraction (CRF) weighted F1: Targets 0.64 (Catalan), 0.57 (Basque); Expressions 0.52 (Catalan), 0.54 (Basque); Holders 0.56 (Catalan), 0.54 (Basque). Polarity classification (linear SVM) weighted F1: 0.80 (Catalan), 0.84 (Basque).

**Validation**: 10-fold cross-validation (80% training per fold). Inter-annotator agreement evaluated using AvgAgr for spans (targets, expressions, holders) and MSE for polarity.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
