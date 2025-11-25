# Benchmark for Evaluating Binary Code Understanding Using Large Language Models

## 📊 Benchmark Details

**Name**: Benchmark for Evaluating Binary Code Understanding Using Large Language Models

**Overview**: This benchmark evaluates the effectiveness of Large Language Models (LLMs) in real-world reverse engineering scenarios, focusing on two key binary code understanding tasks: function name recovery and binary code summarization.

**Data Type**: decompiled pseudo code, function names, natural language summaries

**Domains**:
- Software Security

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/FFmpeg/FFmpeg)
- [GitHub Repository](https://github.com/redis/redis)
- [GitHub Repository](https://github.com/curl/curl)
- [GitHub Repository](https://github.com/robertdavidgraham/masscan)
- [GitHub Repository](https://github.com/karpathy/llama2.c)
- [GitHub Repository](https://github.com/ggerganov/whisper.cpp)
- [GitHub Repository](https://github.com/openssl/openssl)
- [GitHub Repository](https://github.com/facebook/zstd)
- [GitHub Repository](https://github.com/ImageMagick/ImageMagick)
- [GitHub Repository](https://github.com/libvips/libvips)
- [GitHub Repository](https://github.com/libexpat/libexpat)
- [GitHub Repository](https://github.com/ultrajson/ultrajson)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of Large Language Models in understanding binary code through function name recovery and binary code summarization tasks.

**Target Audience**:
- ML Researchers
- Software Security Practitioners
- Reverse Engineers

**Tasks**:
- Function Name Recovery
- Binary Code Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Real-world software projects implemented in C language available on GitHub

**Size**: 81,185 functions, 2,000 instances

**Format**: JSONL

**Annotation**: Automated annotation using ChatGPT for generating summaries

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model-based evaluation

**Metrics**:
- Precision
- Recall
- F1 Score
- BLEU-4
- METEOR
- Rouge-L

**Calculation**: Metrics are computed based on token-level comparisons for function names and summary generation evaluations.

**Interpretation**: Higher precision and recall indicate better performance in accurately recovering function names and summarizing binary code.

**Baseline Results**: ChatGPT and various LLMs were used as baselines for evaluation against deep learning-based expert models such as SymLM and BinT5.

**Validation**: The benchmark dataset was constructed ensuring no data leakage, with systematic correctness checks by domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
