# C REOLE VAL

## 📊 Benchmark Details

**Name**: C REOLE VAL

**Overview**: C REOLE VAL is a collection of benchmark datasets spanning 8 different NLP tasks, covering up to 28 Creole languages. It includes novel development datasets for reading comprehension, relation classification, and machine translation for Creoles, alongside existing benchmarks.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education
- Religion

**Languages**:
- Haitian Creole
- Mauritian Creole
- Chavacano
- Jamaican Creole
- Bislama
- Tok Pisin
- Sranan Tongo
- Nigerian Pidgin
- English
- Spanish
- French
- Portuguese

**Resources**:
- [GitHub Repository](https://github.com/hclent/CreoleVal)

## 🎯 Purpose and Intended Users

**Goal**: To empower research on Creoles in NLP and computational linguistics and to facilitate the inclusion of Creoles in multilingual evaluations.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Linguists

**Tasks**:
- Machine Translation
- Relation Classification
- Reading Comprehension
- Named Entity Recognition
- Sentiment Analysis

**Limitations**: Limited domain diversity and difficulties in gathering high-quality data for all Creole languages.

## 💾 Data

**Source**: Novel datasets constructed for various NLP tasks across Creole languages, alongside existing datasets.

**Size**: 3,410,975 sentences

**Format**: JSON

**Annotation**: Manual annotation by experts.

## 🔬 Methodology

**Methods**:
- Baseline experiments in zero-shot settings
- Manual validation and correction by native speakers

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- chrF

**Calculation**: Evaluation of models based on performance metrics such as BLEU and Accuracy.

**Interpretation**: Higher scores indicate better performance in cross-lingual transfer learning tasks.

**Baseline Results**: Results from zero-shot transfer learning experiments across multiple datasets.

**Validation**: Conducted by native speakers and linguistic experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Demographics of Creole speakers were considered in the design and validation of datasets.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons licenses are applied to the datasets where specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
