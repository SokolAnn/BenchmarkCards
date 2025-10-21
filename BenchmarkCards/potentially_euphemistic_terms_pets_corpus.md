# Potentially Euphemistic Terms (PETs) corpus

## 📊 Benchmark Details

**Name**: Potentially Euphemistic Terms (PETs) corpus

**Overview**: We present a corpus of potentially euphemistic terms (PETs) along with example texts from the GloWbE corpus. Additionally, we present a subcorpus of texts where these PETs are not being used euphemistically. The resources are intended to support research on euphemism detection, identification, and generation in Natural Language Processing.

**Data Type**: text (sentences containing Potentially Euphemistic Terms: euphemistic and literal usages)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Corpus of Global Web-Based English (GloWbE)
- TweetEval

**Resources**:
- [GitHub Repository](https://github.com/marsgav/euphemism_project)
- [Resource](https://arxiv.org/abs/2205.02728)

## 🎯 Purpose and Intended Users

**Goal**: To create and analyze a corpus of Potentially Euphemistic Terms (PETs) with euphemistic and literal sentence usages to facilitate research on automatic euphemism detection, identification, and generation in NLP.

**Target Audience**:
- Natural Language Processing researchers
- Computational linguistics researchers

**Tasks**:
- Euphemism Detection
- Euphemism Identification
- Sentiment Analysis
- Offensive Language Detection

**Limitations**: Euphemisms are inherently ambiguous leading to inter-annotator disagreement; the PET list is not definitive and may change over time (the "euphemism treadmill"); the corpus is derived from only the US dialect portion of GloWbE.

## 💾 Data

**Source**: Sentences extracted from the US portion of the Corpus of Global Web-Based English (GloWbE). The PET list was compiled from euphemism dictionaries, English learner websites, online articles, prior studies (e.g., Kapron-King and Xu 2021; Rawson 1981; Holder 2008), and author linguistic knowledge.

**Size**: 1,965 total sentences (1,382 euphemistic sentences; 583 literal sentences); 129 PETs present in the corpus. Initial compiled PET list: 184 PETs; terminology list with morphological variations: 284 terms.

**Format**: N/A

**Annotation**: Manual annotation: each extracted row was annotated by the authors as '1' (euphemistic) or '0' (non-euphemistic). A sample of 500 sentences was annotated by graduate student language experts who provided labels, interpretations, and a confidence score (1-3).

## 🔬 Methodology

**Methods**:
- Sentence extraction using spaCy PhraseMatcher
- Manual annotation by authors and graduate student annotators
- Automated sentiment and offensiveness scoring using a roBERTa-based model fine-tuned on Tweets and evaluated with the TweetEval framework

**Metrics**:
- Relative percent change in sentiment probabilities (Neutral, Positive, Negative)
- Relative percent change in offensiveness probability (Not-Offensive, Offensive)
- Observed percent agreement
- Krippendorff's alpha

**Calculation**: Sentiment and offensiveness scores were computed for each sample using a roBERTa-based model, then recomputed after substituting each euphemism with its literal meaning. Scores (probabilities) before and after substitution were compared using relative percent change. Annotation reliability was measured using observed agreement and Krippendorff's alpha.

**Interpretation**: An increase in negative and offensive scores after substitution supports the assumption that euphemisms soften language. Inter-annotator reliability (Krippendorff's alpha = 0.415) was classified as 'fair', indicating annotation ambiguity for euphemisms.

**Baseline Results**: Model label average percent changes after substitution: Sentiment Neutral -2.6%, Positive -11.3%, Negative 54.6%. Offensiveness Not-Offensive -6.6%, Offensive 30.0%. Annotation reliability: Average observed percent agreement 71.74%, Krippendorff's alpha 0.415.

**Validation**: Model evaluation used the TweetEval framework for the roBERTa-based sentiment/offensiveness model. Annotation reliability was validated using observed agreement and Krippendorff's alpha.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
