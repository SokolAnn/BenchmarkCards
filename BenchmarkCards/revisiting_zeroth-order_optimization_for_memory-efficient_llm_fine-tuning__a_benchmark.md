# Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark

## 📊 Benchmark Details

**Name**: Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark

**Overview**: This work creates the first benchmark for zeroth-order (ZO) optimization in the context of LLM fine-tuning, performing a comprehensive study across multiple ZO methods, five LLM families (Roberta, OPT, LLaMA, Vicuna, Mistral), three task complexities, and five fine-tuning schemes to evaluate accuracy and efficiency and to investigate optimization principles and enhancements (block-wise descent, hybrid ZO-FO training, gradient sparsity).

**Data Type**: text (binary classification, question-answering, commonsense reasoning, multi-sentence reading comprehension)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- MeZO (Malladi et al., 2023)

**Resources**:
- [GitHub Repository](https://github.com/ZO-Bench/ZO-LLM)

## 🎯 Purpose and Intended Users

**Goal**: Establish the first benchmark for ZO optimization in LLM fine-tuning to evaluate and compare a broad range of ZO methods, reveal optimization principles (e.g., task alignment, forward gradient role), and propose enhancements to improve memory-efficient fine-tuning.

**Target Audience**:
- N/A

**Tasks**:
- Text Classification
- Question Answering
- Commonsense Reasoning
- Multi-sentence Reading Comprehension

**Limitations**: High variance of ZO methods and a scalability bottleneck when dealing with larger models and more complex tasks; crafting effective prompts for task alignment can be non-trivial.

## 💾 Data

**Source**: Stanford Sentiment Treebank v2 (SST2); Choice Of Plausible Alternatives (COPA); WinoGrande; MultiRC

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics (accuracy and efficiency)
- Comparative algorithm benchmarking across ZO and FO optimizers

**Metrics**:
- Accuracy (test accuracy)
- Peak Memory Usage (GB)
- GPU Resources (number of GPUs)
- Query Efficiency (number of function queries)
- Runtime Efficiency (per-iteration runtime in seconds)

**Calculation**: Accuracy measured as test accuracy on evaluation datasets; memory reported as peak memory usage in GB; GPU resources reported as number of GPUs used; query efficiency measured as number of function queries per gradient estimate (query budget q); runtime reported as per-iteration runtime (seconds), averaged (e.g., averaged over 100 iterations for the reported runtime costs). ZO optimizers typically used q=1 unless otherwise specified.

**Interpretation**: Higher test accuracy indicates better fine-tuning effectiveness; lower peak memory, fewer GPUs, lower query counts, and lower per-iteration runtime indicate better efficiency. Results are interpreted in light of trade-offs between algorithmic complexity, accuracy, query budget, and memory/runtime efficiency.

**Baseline Results**: Baselines include FO optimizers FO-SGD and FO-Adam. Example baseline: FO-SGD achieved 91.4% test accuracy on SST2 (Roberta-Large, FT) as reported in Table 2. Comparative results for multiple ZO and FO methods across settings are provided in the paper.

**Validation**: Hyperparameters selected via grid search for each method; ZO (BP-free) optimizers run for 20,000 iterations and FO optimizers run for 625 iterations unless otherwise stated; runtime averages computed (e.g., runtime averaged over 100 iterations for reported per-iteration runtimes).

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse
- Privacy
- Intellectual Property
- Societal Impact

**Atlas Risks**:
- **Misuse**: Spreading disinformation, Dangerous use
- **Privacy**: Exposing personal information
- **Intellectual Property**: Copyright infringement
- **Societal Impact**: Impact on the environment

**Potential Harm**: ['Generating misinformation', 'Phishing attacks', 'Releasing copyrighted information', 'Releasing private information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
