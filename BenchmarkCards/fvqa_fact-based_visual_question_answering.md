# FVQA (Fact-based Visual Question Answering)

## 📊 Benchmark Details

**Name**: FVQA (Fact-based Visual Question Answering)

**Overview**: Here we introduce FVQA (Fact-based VQA), a VQA dataset which requires, and supports, much deeper reasoning. FVQA primarily contains questions that require external information to answer. We extend a conventional visual question answering dataset (image-question-answer triplets) through additional image-question-answer-supporting-fact tuples. Each supporting-fact is represented as a structural triplet, such as <Cat,CapableOf,ClimbingTrees>.

**Data Type**: multimodal: images and question-answer pairs with supporting-fact triplets (RDF)

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- DAQUAR
- COCO-QA
- VQA-real
- Visual Genome
- Visual7W
- Visual Madlibs
- VQA-abstract
- VQA-balanced
- KB-VQA
- Facebook bAbI

**Resources**:
- [Resource](https://arxiv.org/abs/1606.05433)
- [Resource](http://www.w3.org/2004/02/skos/)
- [Resource](http://web.media.mit.edu/˜push/Kurzweil.html)

## 🎯 Purpose and Intended Users

**Goal**: To build a new Visual Question Answering dataset (FVQA) that provides supporting-facts (structured knowledge triples) for each image-question-answer tuple, requiring and enabling deeper reasoning that uses external commonsense knowledge.

**Target Audience**:
- Computer Vision Researchers
- Natural Language Processing Researchers
- Machine Learning Researchers

**Tasks**:
- Visual Question Answering
- Question Answering
- Knowledge-based Question Answering
- Supporting-fact retrieval

**Limitations**: Answers are restricted to concepts from the image and the incorporated knowledge bases; ‘Yes’/‘No’ questions are excluded by construction. Some scene/action answers can be expressed in multiple ways, which can reduce measured accuracy.

**Out of Scope Uses**:
- Yes/No question evaluation

## 💾 Data

**Source**: 2190 images sampled from the Microsoft COCO validation set and ImageNet test set; supporting facts and relations extracted from DBpedia, ConceptNet and WebChild; question-answer-supporting-fact tuples collected via an online question collection system by human annotators.

**Size**: 2,190 images; 5,826 questions; 4,216 unique supporting facts; 5 random splits (per split: ~1,100 training images and ~1,090 test images; per split ~2,927 training questions and ~2,899 test questions).

**Format**: Supporting facts stored as RDF triples accessible via SPARQL; images as original Microsoft COCO / ImageNet image files; question-answer-supporting-fact tuples collected as text (via online collection system).

**Annotation**: Collected by 38 human volunteers using a bespoke online question collection system. Annotators chose a visual concept and an associated supporting-fact and then authored a question whose answer depends on both the image and the selected supporting-fact. Answers are limited to the two concepts in the supporting-fact.

## 🔬 Methodology

**Methods**:
- Automated metrics (string-matching accuracy, WUPS)
- Model-based evaluation (baselines: SVM, LSTM, hierarchical co-attention models; proposed KB-query based model)
- Human evaluation (5 subjects for test-suite human performance; 3 subjects for common-sense/fact verification)

**Metrics**:
- Top-1 Accuracy
- Top-3 Accuracy
- Top-10 Accuracy
- Wu-Palmer Similarity (WUPS) at thresholds 0.9 and 0.0
- Supporting-fact prediction accuracy

**Calculation**: Accuracy: proportion of correctly answered test questions. A predicted answer is correct iff its string matches the ground-truth answer after normalization (all answers normalized by the python INFLECT package). WUPS measures lexical/semantic similarity; WUPS@0.9 is stricter, WUPS@0.0 is loose. Top-N: predicted answer is considered correct if the ground-truth appears in the top N candidates.

**Interpretation**: Higher Top-N accuracy and higher WUPS indicate better model performance. WUPS@0.9 is a stricter similarity measure; WUPS@0.0 is a loose measure. Human Top-1 provides an upper-bound reference on this task.

**Baseline Results**: Selected reported results (averaged over 5 splits, ±std):
- Ours, top-3-QQmaping: Top-1 Accuracy 56.91% ± 0.99 (Table V).
- Ours, top-1-QQmaping: Top-1 Accuracy 52.56% ± 1.03 (Table V).
- Ours, gt-QQmaping (uses ground-truth question-query mapping): Top-1 Accuracy 63.63% ± 0.73 (Table V).
- Hie-Question+Image+Pre-VQA: Top-1 Accuracy 43.14% ± 0.61 (Table V).
- LSTM-Question+Image+Pre-VQA: Top-1 Accuracy 24.98% ± 0.60 (Table V).
- Human (5 subjects): Top-1 Accuracy 77.99% ± 0.75 (Table V).
Supporting-fact prediction (Table XIII): Ours, top-3-QQmaping Top-1 supporting-fact accuracy 41.12% ± 0.74.

**Validation**: Dataset split validation: 5 random train/test splits; reported results are averaged across the 5 test splits with standard deviation. Human studies: 3 independent subjects to verify whether questions require commonsense and whether supporting-facts are helpful (97.6% and >99% agreement statistics reported); 5 independent subjects used to measure human performance on test splits.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
