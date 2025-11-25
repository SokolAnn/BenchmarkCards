# UNIDETOX (Universal Detoxification of Large Language Models via Dataset Distillation)

## 📊 Benchmark Details

**Name**: UNIDETOX (Universal Detoxification of Large Language Models via Dataset Distillation)

**Overview**: UNIDETOX is a universally applicable method for mitigating toxicity across various large language models (LLMs) using a novel and efficient dataset distillation technique. It generates detoxifying text that can be used to universally fine-tune any LLM without model-specific hyperparameter tuning.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/EminLU/UniDetox)
- [Resource](https://huggingface.co/openai-community/gpt2-xl)
- [Resource](https://huggingface.co/facebook/opt-6.7b)
- [Resource](https://huggingface.co/tiiuae/falcon-7b)
- [Resource](https://huggingface.co/meta-llama/Llama-2-7b-hf)
- [Resource](https://huggingface.co/unitary/toxic-bert)
- [Resource](https://huggingface.co/datasets/LennardZuendorf/Dynamically-Generated-Hate-Speech-Dataset)
- [Resource](https://huggingface.co/datasets/toxigen/toxigen-data)
- [Resource](https://huggingface.co/datasets/cais/mmlu)

## 🎯 Purpose and Intended Users

**Goal**: To provide a universal method for detoxifying large language models using distilled detoxifying text, improving toxicity mitigation while maintaining fluency and performance.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Dynamically Generated Hate Speech (DGHS) dataset and ToxiGen dataset for evaluation.

**Size**: 25,150 examples for training, 896 validation examples, and 940 test examples.

**Format**: N/A

**Annotation**: Detoxifying text is distilled from existing toxic data using contrastive decoding.

## 🔬 Methodology

**Methods**:
- Dataset Distillation
- Fine-tuning

**Metrics**:
- Toxicity Probability (TP)
- Expected Maximum Toxicity (EMT)
- Perplexity (PPL)
- Accuracy

**Calculation**: Metrics are calculated using generated text continuations evaluated for toxicity and fluency.

**Interpretation**: Lower TP and EMT scores indicate better detoxification performance.

**Baseline Results**: UNIDETOX outperforms previous detoxification methods.

**Validation**: Technique validated through experiments across multiple LLMs including GPT-2, OPT, Falcon, and LLaMA2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
