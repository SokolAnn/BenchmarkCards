# CG-Bench (Clue-grounded Question Answering Benchmark for Long Video Understanding)

## 📊 Benchmark Details

**Name**: CG-Bench (Clue-grounded Question Answering Benchmark for Long Video Understanding)

**Overview**: CG-Bench is designed for clue-grounded question answering in long videos, featuring 1,219 manually curated videos and 12,129 question-answering pairs in three main question types: perception, reasoning, and hallucination.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- NExT-GQA
- Video-MME
- MLVU
- LongVideoBench

**Resources**:
- [Resource](https://cg-bench.github.io/leaderboard/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the ability of multimodal large language models in understanding long videos through clue-grounded question answering.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually collected videos from the internet, categorizing into a systematic tagging framework.

**Size**: 1,219 videos and 12,129 QAC triplets

**Format**: N/A

**Annotation**: Manually annotated QAC triplets by watching entire videos and selecting relevant clues.

## 🔬 Methodology

**Methods**:
- Clue-grounded white box evaluation
- Clue-grounded black box evaluation
- Multiple-choice question evaluation
- Open-ended question answering evaluation

**Metrics**:
- Accuracy
- mIoU (Mean Intersection over Union)
- rec.@IoU (Recall at IoU thresholds)
- Acc.@IoU (Accuracy at IoU thresholds)

**Calculation**: Metrics are calculated based on predictions and ground truths through specified intervals for clue retrieval and answer correctness.

**Interpretation**: Higher scores in metrics indicate better model understanding and clue retrieval capabilities.

**Baseline Results**: GPT-4o achieved a long-acc. score of 45.2% on this benchmark.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
