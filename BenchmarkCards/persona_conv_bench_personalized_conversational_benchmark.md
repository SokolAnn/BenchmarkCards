# PERSONA CONV BENCH (Personalized Conversational Benchmark)

## 📊 Benchmark Details

**Name**: PERSONA CONV BENCH (Personalized Conversational Benchmark)

**Overview**: PERSONA CONV BENCH is a large-scale benchmark for evaluating personalized reasoning and generation in multi-turn conversations with large language models (LLMs). It provides three core tasks: sentence classification, impact regression, and user-centric text generation across 10 diverse Reddit-based domains.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LaMP
- LongLaMP
- PGraphRAG

**Resources**:
- [Resource](https://huggingface.co/datasets/PERSONABench/PERSONA-Bench)
- [GitHub Repository](https://github.com/PERSONA-bench/PERSONA/tree/Latest)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on LLMs that can adapt to individuals' conversational styles, track long-term context, and generate more contextually rich and engaging responses.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Sentiment Classification
- Impact Forecasting
- Next-Text Generation

**Limitations**: Our benchmark draws from a specific set of online discussion domains, and some tasks may not generalize to highly specialized or low-resource settings.

## 💾 Data

**Source**: Crawled from Reddit using a multithreaded scraper focused on high-engagement discussion domains.

**Size**: 19,215 posts with over 111,239 conversations

**Format**: JSON

**Annotation**: Automatically collected based on user interactions and engagement metrics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Matthews Correlation Coefficient (MCC)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- ROUGE-1
- ROUGE-L
- BLEU
- METEOR
- SBERT

**Calculation**: Metrics are calculated based on model predictions against ground-truth targets, focusing on how well the model predicts sentiment, scores, or text generation.

**Interpretation**: Higher scores indicate better performance in estimating sentiment, predicting scores, and generating contextually relevant responses.

**Baseline Results**: Various LLMs were benchmarked, showing significant performance gains when incorporating personalized conversational context.

**Validation**: Performance evaluated under a zero-shot setting without task-specific fine-tuning.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark includes demographic considerations in the dataset, focusing on user preferences and historical context.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was collected in compliance with platform terms and is intended strictly for non-commercial research use.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
