# V-STaR (Video Spatio-Temporal Reasoning)

## 📊 Benchmark Details

**Name**: V-STaR (Video Spatio-Temporal Reasoning)

**Overview**: V-STaR is introduced to evaluate Video Large Language Models (Video-LLMs) on their spatio-temporal reasoning capabilities for answering video-based questions that involve understanding 'when', 'where', and 'what'. The benchmark includes a dataset constructed with semi-automated GPT-4-powered pipeline, featuring coarse-to-fine Chain-of-Thought (CoT) questions.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- TVQA
- QAEgo4D
- Next-GQA
- E.T. Bench

**Resources**:
- [Resource](https://V-STaR-Bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive assessment of the spatio-temporal reasoning ability of Video-LLMs in understanding video content through structured reasoning chains.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Video Question Answering
- Spatio-Temporal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Videos collected from existing datasets (VidSTG, TVQA+, GOT-10k) and YouTube.

**Size**: 2,094 videos with a total of 64.12 hours of footage

**Format**: Various video formats

**Annotation**: Coarse-to-fine Chain-of-Thought (CoT) questions and spatial-temporal labels generated via a semi-automated process.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation through CoT reasoning

**Metrics**:
- Accuracy
- Mean Temporal IoU (mtIoU)
- Mean Visual IoU (mvIoU)
- Logarithmic Geometric Mean (LGM)
- Arithmetic Mean (AM)

**Calculation**: Accuracy is calculated based on the correctness of answers; mtIoU and mvIoU are used for evaluating temporal and spatial grounding metrics respectively. The LGM aggregates the performance across the reasoning chain.

**Interpretation**: A higher LGM indicates better overall performance in spatio-temporal reasoning.

**Baseline Results**: Experiments conducted on 14 contemporary Video-LLMs reveal significant gaps between models and expected performance on the V-STaR benchmark.

**Validation**: The benchmark's validation involves assessing the reasoning capabilities across multiple models under structured question chains.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
