# CNN and Daily Mail corpora

## 📊 Benchmark Details

**Name**: CNN and Daily Mail corpora

**Overview**: Large scale supervised reading comprehension data created from news articles and their summaries to evaluate models' ability to answer questions posed on the contents of documents.

**Data Type**: text (document–query–answer triples / Cloze-style questions)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- MCTest

**Resources**:
- [GitHub Repository](http://www.github.com/deepmind/rc-data/)

## 🎯 Purpose and Intended Users

**Goal**: Provide large scale supervised reading comprehension data to evaluate a model's ability to read a single document and answer queries about its contents.

**Target Audience**:
- Natural Language Processing Researchers

**Tasks**:
- Reading Comprehension
- Question Answering

**Limitations**: Focuses on single-document reading comprehension and excludes external world knowledge; articles of over 2000 tokens and queries whose answer entity did not appear in the context were filtered out.

**Out of Scope Uses**:
- Using external world knowledge or co-occurrence statistics to answer queries

## 💾 Data

**Source**: Articles and associated summary bullet points from the CNN and Daily Mail websites; summary points converted into Cloze-style queries via entity detection and anonymisation.

**Size**: Approximately 93,000 CNN articles and 220,000 Daily Mail articles; combined corpus of roughly 1,000,000 document–query–answer triples.

**Format**: N/A

**Annotation**: Automatically generated Cloze-style questions from summary bullet points; entities replaced with abstract entity markers using a coreference system and randomly permuted during training and testing.

## 🔬 Methodology

**Methods**:
- Automated metrics (Accuracy)
- Benchmarking against baselines and heuristic models
- Model-based evaluation (neural networks and symbolic models)

**Metrics**:
- Accuracy
- Precision@Recall
- Precision

**Calculation**: Accuracy reported as the percentage of correctly answered queries; precision/recall curves used for attention models as shown in Precision@Recall plots.

**Interpretation**: Higher Accuracy indicates better reading comprehension performance; results show attention-based neural models (Attentive and Impatient Readers) outperform baselines and non-attention models.

**Baseline Results**: Table 5 reports accuracies. Example test set results: CNN test - Maximum frequency 33.2, Exclusive frequency 39.3, Frame-semantic model 40.2, Word distance model 50.9, Deep LSTM Reader 57.0, Uniform Reader 39.4, Attentive Reader 63.0, Impatient Reader 63.8. Daily Mail test - Maximum frequency 25.5, Exclusive frequency 32.8, Frame-semantic model 35.5, Word distance model 55.5, Deep LSTM Reader 62.2, Uniform Reader 34.4, Attentive Reader 69.0, Impatient Reader 68.0.

**Validation**: Model hyperparameters were tuned on the respective validation sets; validation data is from March 2015 and test data from April 2015. Hyperparameter search ranges and training details are described in the appendix.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Entities in documents and queries are anonymised: a coreference system establishes coreferents, entities are replaced with abstract entity markers according to coreference, and these markers are randomly permuted whenever a data point is loaded.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
