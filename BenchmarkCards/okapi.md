# Okapi

## 📊 Benchmark Details

**Name**: Okapi

**Overview**: Okapi is the first system with instruction-tuned LLMs based on reinforcement learning from human feedback (RLHF) for multiple languages. Okapi introduces instruction and response-ranked data in 26 diverse languages and presents benchmark datasets (translated ARC, HellaSwag, and MMLU) to enable evaluation of generative LLMs in multiple languages.

**Data Type**: instruction-input-output triples (text); question-answering pairs (multiple-choice); ranked response outputs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Russian
- German
- Chinese
- French
- Spanish
- Italian
- Dutch
- Vietnamese
- Indonesian
- Arabic
- Hungarian
- Romanian
- Danish
- Slovak
- Ukrainian
- Catalan
- Serbian
- Croatian
- Hindi
- Bengali
- Tamil
- Nepali
- Malayalam
- Marathi
- Telugu
- Kannada

**Similar Benchmarks**:
- ARC
- HellaSwag
- MMLU
- TruthfulQA

**Resources**:
- [GitHub Repository](https://github.com/nlp-uoregon/Okapi)

## 🎯 Purpose and Intended Users

**Goal**: Develop an open-source RLHF-based instruction-tuned LLM framework for multiple languages, create instruction and response-ranked data in 26 languages, and provide translated benchmark datasets to evaluate generative LLMs across multiple languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Instruction Following
- Text Generation
- Question Answering

**Limitations**: Coverage limited to 26 languages (not exhaustive); experiments use BLOOM and LLaMA 7B base models only; instruction and evaluation data are automatically generated and translated via ChatGPT which may introduce noise and may not reflect human-provided data; evaluations do not explicitly measure hallucination, toxicity, or biases.

## 💾 Data

**Source**: Instruction data generated from Alpaca (52K) plus 106K additional English instructions produced via a Self-Instruct procedure; instructions, inputs, and outputs translated into target languages using ChatGPT; ranked response outputs produced by prompting ChatGPT to rank model-generated responses; evaluation datasets created by translating ARC, HellaSwag, and MMLU into target languages using ChatGPT.

**Size**: 158,000 instruction examples (52,000 from Alpaca + 106,000 generated); 42,000 ranked instruction examples; translated evaluation datasets: ARC: 1,170 examples; HellaSwag: 9,162 examples; MMLU: 13,062 examples.

**Format**: JSON (instruction examples and translations organized as JSON objects; ranking outputs provided as integer ranks)

**Annotation**: Translations and response rankings produced via ChatGPT prompts. Ranking annotations use integer overall ranks (1 to 4) per response; instruction generation used Self-Instruct with ROUGE-based filtering.

## 🔬 Methodology

**Methods**:
- Supervised Fine-tuning (SFT)
- Reward model training (contrastive ranking loss)
- Reinforcement Learning from Human Feedback (RLHF) using Proximal Policy Optimization (PPO)
- Machine translation and ranking via ChatGPT
- Self-Instruct generation for English instructions

**Metrics**:
- Accuracy
- ROUGE

**Calculation**: Model performance computed using the Eleuther AI Language Model Evaluation Harness as adopted by the HuggingFace Open LLM Leaderboard; accuracy is computed on the multiple-choice datasets (ARC, HellaSwag, MMLU). ROUGE is used during instruction generation filtering.

**Interpretation**: Higher Accuracy indicates better performance on the translated multiple-choice evaluation datasets. The paper reports that RLHF generally outperforms SFT across base models and datasets; performance is higher for high-resource languages than medium- or low-resource languages.

**Baseline Results**: Reported averages for BLOOM (base), BLOOMZ, SFT, and RLHF on translated datasets: ARC averages (BLOOM / BLOOMZ / SFT / RLHF): 28.2 / 27.4 / 28.4 / 30.0. HellaSwag averages: 36.8 / 34.7 / 37.7 / 39.5. MMLU averages: 27.1 / 26.0 / 26.6 / 26.9. LLaMA reported averages (base / SFT / RLHF): ARC 33.3 / 35.2 / 37.3; HellaSwag 46.4 / 47.1 / 49.6; MMLU 29.8 / 30.1 / 30.8.

**Validation**: Evaluation on translated ARC, HellaSwag, and MMLU using the Eleuther AI evaluation harness; comparisons include base models (BLOOM, LLaMA), BLOOMZ, SFT-tuned models, and RLHF-tuned models; performance reported overall and by high-/medium-/low-resource language groups.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Value Alignment
- Accuracy

**Atlas Risks**:
- **Robustness**: Hallucination
- **Fairness**: Data bias
- **Value Alignment**: Toxic output
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Performance is reported broken down by language-resource groups (High-Resource, Medium-Resource, Low-Resource); the paper observes that high-resource languages achieve higher performance and that RLHF gains are smaller for low-resource languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
