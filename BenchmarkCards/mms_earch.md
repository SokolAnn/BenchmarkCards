# MMS EARCH

## 📊 Benchmark Details

**Name**: MMS EARCH

**Overview**: MMS EARCH is a comprehensive evaluation benchmark designed to assess the multimodal search performance of Large Multimodal Models (LMMs). It categorizes searching queries into two primary areas: News and Knowledge, encompassing 300 manually collected instances across 14 subfields, with no overlap with LMMs’ training data.

**Data Type**: text-image interleaved queries

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://mmsearch.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of LMMs in multimodal search capabilities through a structured pipeline that includes requerying, reranking, and summarization tasks.

**Target Audience**:
- Machine Learning Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Requery
- Rerank
- Summarization
- End-to-End Search

**Limitations**: N/A

## 💾 Data

**Source**: 300 manually collected instances covering 14 subfields, ensuring no overlap with LMMs’ training data.

**Size**: 300 queries, 2901 unique images

**Format**: N/A

**Annotation**: Manual collection and categorization by annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: The final score is derived from the weighted outcomes of the end-to-end task and individual tasks (requery, rerank, and summarization).

**Interpretation**: Higher scores indicate better multimodal search capabilities across utilized LMMs.

**Validation**: Evaluation covers closed-source and open-source LMMs through extensive experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
