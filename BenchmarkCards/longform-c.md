# LongForm-C

## 📊 Benchmark Details

**Name**: LongForm-C

**Overview**: The LongForm-C dataset, which is created by reverse instructions. We generate instructions via LLMs for human-written corpus examples using reverse instructions. This approach provides a cheaper and cleaner instruction-tuning dataset with natural output and one suitable for long text generation.

**Data Type**: text (instruction-output pairs; long-form text)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FLAN
- Dolly
- Self-Instruct
- Unnatural Instructions
- Super-NaturalInstructions
- BigBench
- MURI
- CRAFT

**Resources**:
- [GitHub Repository](https://github.com/akoksal/LongForm)
- [Resource](https://arxiv.org/abs/2304.08460)

## 🎯 Purpose and Intended Users

**Goal**: To create LongForm-C, an instruction-following long text generation dataset using reverse instructions to improve instruction tuning for long-form text generation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Long-form Text Generation
- Story Generation
- Poem Generation
- Email Generation
- Recipe Generation
- Grammar Error Correction
- Text Summarization
- Table-to-Text Generation
- Long-form Question Answering
- Multilingual News Generation
- Natural Language Understanding (MMLU evaluation)

**Limitations**: Focuses on long text generation and may have limitations regarding structured prediction tasks in NLP with some LLMs. Models may present hallucination problems similar to those found in LLMs. T5 variants may lack newline tokens affecting readability of long outputs. Some corpus examples contain irrelevant metadata or are overly detailed, which can lead to overly long or unsuitable responses.

## 💾 Data

**Source**: Human-written passages and existing instruction-output pairs from C4, English Wikipedia, Stack Exchange (subcorpus of the Pile), WikiHow, NIv2 (Super-NaturalInstructions), BigBench, BEA-2019 (BEA-GEC), and Enron. The dataset includes examples generated via reverse instructions (LLM-generated instructions for corpus examples), structured corpora examples (Stack Exchange, WikiHow), and reformulated NLP tasks.

**Size**: 27,739 examples (15,000 generated via reverse instructions; additional 12,739 examples from structured corpora and NLP datasets). Split: 23,652 training / 2,042 validation / 2,045 test.

**Format**: N/A

**Annotation**: Instruction generation for reverse instructions uses OpenAI text-davinci-003 (zero-shot) with three templates (formal, informal chatbot, search-query) and optional length-control templates. Structured corpora use existing (instruction, output) pairs (Stack Exchange, WikiHow) without LLMs. NLP tasks are reformulated using templates. Human validation: Mechanical Turk annotation on 100 randomly selected corpus examples showed 97 out of 100 instructions were relevant.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Model comparison / benchmarking (finetuning PLMs and comparing to baselines)

**Metrics**:
- METEOR
- BLEU
- ROUGE-L
- self-BLEU
- MMLU (accuracy)

**Calculation**: METEOR is used as the main metric for long text generation; BLEU, ROUGE-L and self-BLEU are also reported. Generation is performed with nucleus sampling (top-p) p=0.9 for all LMs. MMLU is evaluated in a 5-shot setting.

**Interpretation**: Higher METEOR indicates better long-form generation quality. The authors report that LongForm models achieve large relative METEOR improvements over prior models (e.g., >63% in-domain and >35% out-of-domain relative METEOR improvement as reported in the paper).

**Baseline Results**: Average in-domain METEOR (reported): Flan-T5 12.5, Alpaca-LLaMA-7B 15.2, OPT-30B 12.3, LongForm-T5-XL 24.3, LongForm-OPT-6.7B 24.2, LongForm-LLaMA-7B 24.8. LongForm-OPT-2.7B outperforms OPT-30B despite being ten times smaller (as stated).

**Validation**: Human evaluation of 100 randomly selected reverse-instruction examples on Mechanical Turk (97% judged relevant). Ablation studies on LongForm-C subsets (RI, SC, NLP) and out-of-domain evaluation on recipe generation (RGen), ELI5, and WritingPrompts (WP) datasets were conducted to validate effectiveness and generalization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Robustness
- Accuracy

**Atlas Risks**:
- **Misuse**: Improper usage, Spreading disinformation
- **Robustness**: Hallucination

**Potential Harm**: ['Malicious use', 'Misinformation due to hallucination']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
