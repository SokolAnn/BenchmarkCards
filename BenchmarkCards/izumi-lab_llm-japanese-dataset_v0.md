# izumi-lab/llm-japanese-dataset v0

## 📊 Benchmark Details

**Name**: izumi-lab/llm-japanese-dataset v0

**Overview**: This study constructed a Japanese chat dataset for tuning large language models (LLMs), which consist of about 8.4 million records. The dataset we constructed consisted of various tasks, such as translation and knowledge tasks, and is intended to support Japanese in those LLMs and make a dataset for training or tuning LLMs in Japanese.

**Data Type**: text (instruction-input-response chat records; translation pairs; question-answering pairs; dialogue)

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese
- English

**Similar Benchmarks**:
- Alpaca
- JGLUE
- Language Model Evaluation Harness

**Resources**:
- [Resource](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset)
- [GitHub Repository](https://github.com/masanorihirano/llm-japanese-dataset)
- [Resource](https://huggingface.co/izumi-lab/llama-13b-japanese-lora-v0-1ep)

## 🎯 Purpose and Intended Users

**Goal**: The purpose of this dataset was to improve the performance of Japanese language processing capability and connect English language processing capabilities with Japanese input and output.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Machine Translation
- Question Answering
- Dialogue Generation
- Text Simplification
- Answer Extraction
- Title Generation
- Abstract Generation
- News Headline Generation

**Limitations**: Qualitative comparison only; evaluation in the paper is qualitative rather than quantitative. The provided tuned model was trained with only one epoch of LoRA tuning; authors note that increasing epochs and constructing specialized evaluation tasks for Japanese (e.g., a Japanese version of the Language Model Evaluation Harness) are future work.

## 💾 Data

**Source**: Combined from multiple public datasets explicitly listed in the paper, including: Coursera Parallel Corpus Mining (Coursera Parallel Corpus), ParaNatCom (Parallel English-Japanese abstract corpus from Nature Communications), tab-delimited bilingual sentence pairs (manythings.org), Asian Language Treebank (ALT), Tanaka Corpus, Japanese-English Subtitle Corpus (JESC), Japanese WordNet, Easy Japanese Corpus (SNOW T15, SNOW T23), Wikipedia (jawiki 20230401), AIO (AI King) Official Distribution Dataset Version 2.0, Japanese Movie Recommendation Dialogue (JMRD), JCommonsenseQA (part of JGLUE), Aozora Paperback works, JSQuAD (part of JGLUE), Japanese-Alpaca-LoRA (translation of Alpaca), databricks-dolly-15k-ja (Japanese-translated Dolly), and Wikinews (ja.wikinews.org).

**Size**: 8,393,726 data points

**Format**: Instruction/Input/Response chat record format (Instruction, Input, Response) as shown in paper examples

**Annotation**: Programmatic conversion and assembly of existing public corpora into instruction-input-response chat format; no manual annotation procedure for the combined dataset is described.

## 🔬 Methodology

**Methods**:
- Model fine-tuning using LoRA (Low-Rank Adaptation) on LLaMA 13B
- Qualitative manual comparison of model outputs

**Calculation**: N/A

**Interpretation**: Authors report slight qualitative improvements in Japanese responses after LoRA tuning using the constructed dataset; improvements were observed in example comparisons but were not measured with quantitative metrics.

**Baseline Results**: Qualitative example comparisons between LLaMA (base) and LLaMA+LoRA (tuned with the dataset) are provided in the paper; no quantitative baseline metrics are reported.

**Validation**: No formal quantitative validation procedure reported. Authors set temperature to 0.0 for prompt generation to increase reproducibility and list hyperparameters used (e.g., learning rate 3e-4, input length 256, batch size 130, epochs 1); authors state that constructing evaluation tasks and a Japanese evaluation harness is future work.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Component datasets use various licenses; examples listed in the paper include Apache License 2.0; CC BY 4.0; CC BY; CC BY-SA 4.0; BSD-like license (Japanese WordNet); CC BY-SA 3.0; CC BY 2.5.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
