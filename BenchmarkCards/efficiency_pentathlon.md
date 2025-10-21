# Efficiency Pentathlon

## 📊 Benchmark Details

**Name**: Efficiency Pentathlon

**Overview**: A benchmark for holistic and realistic evaluation of model efficiency that focuses on inference, provides a strictly-controlled hardware platform, and incorporates a suite of metrics (latency, throughput, memory overhead, number of parameters, and energy consumption). It includes a software library for seamless integration and is initially focused on Natural Language Processing models while allowing extension to other fields.

**Data Type**: text (machine translation and text classification instances)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German

**Similar Benchmarks**:
- Dynabench
- Dynaboard
- HELM
- HULK
- Long-Range Arena
- MLPerf

**Resources**:
- [GitHub Repository](https://github.com/allenai/efficiency-pentathlon)
- [GitHub Repository](https://github.com/allenai/catwalk)
- [Resource](https://shop.openenergymonitor.com/single-phase-6-channel-energy-monitoring-emontx-v4/)
- [Resource](https://openreview.net/forum?id=bgWHz41FMB7)
- [Resource](https://onnx.ai/)

## 🎯 Purpose and Intended Users

**Goal**: Establish a standardized platform for evaluating the inference efficiency of AI models via a strictly-controlled hardware environment, realistic deployment scenarios, and a diverse set of efficiency metrics to enable fair and reproducible comparisons.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Machine Translation
- Text Classification
- Text Generation

**Limitations**: Hosted server currently has two NVIDIA RTX 8000 GPUs (previous-generation Turing architecture) and 1TB DDR4 memory; current hardware limits evaluation to models that can run on this hardware. Requiring code and checkpoint submission prohibits evaluation of models that are not publicly available or that cannot be run on the provided hardware. Pentathlon focuses on inference efficiency and does not evaluate training efficiency.

**Out of Scope Uses**:
- Evaluation of models that are not publicly available or that cannot be executed on the provided hardware

## 💾 Data

**Source**: Uses existing public datasets for evaluation. Examples in the paper: WMT14 DE-EN (WMT test set and training data subsets) and RAFT (few-shot text classification datasets, e.g., ADE Corpus V2).

**Size**: WMT14 DE-EN: Fixed batching uses full test set of 3,002 instances; Poisson batching draws 4,000 instances (with replacement); Single stream uses 1,000 randomly selected test instances; Offline scenario randomly selects 8,000 instances from the training data. RAFT: collection of 11 datasets (sizes not specified in paper).

**Format**: N/A

**Annotation**: N/A (benchmark uses existing labeled datasets such as parallel corpora for WMT14 DE-EN and labels provided by RAFT; no new annotation procedure described)

## 🔬 Methodology

**Methods**:
- Automated benchmarking on a strictly-controlled hosted server
- Evaluation under four standardized scenarios: Fixed batching, Poisson batching, Single stream, Offline
- Energy measurement using a physical energy-monitoring device connected to the host machine
- Submission via code and checkpoints with stdin/stdout interface; scheduler ensures only one inference workload runs at a time

**Metrics**:
- Throughput (instances/s; words/s for generation tasks)
- Latency (milliseconds)
- Memory overhead (GiB; maximum CPU and GPU memory consumption)
- Energy consumption (W·h) and carbon footprint (CO2 emissions using carbon intensity data)
- Number of parameters (model size)

**Calculation**: Throughput measured in instances/s (and words/s for text generation). Latency measured in milliseconds. Memory overhead measured as maximum CPU and GPU memory consumption in GiB. Energy consumption measured with a physical power monitoring device connected to the host machine; model energy = meter reading during run minus host machine idling power. Carbon emissions computed using carbon intensity data based on geographical location and time of day (Schmidt et al., 2022).

**Interpretation**: Provides a holistic view of model efficiency where higher throughput, lower latency, lower memory overhead, lower energy consumption, and smaller model size indicate better efficiency for different application contexts. No single metric suffices; metric importance depends on deployment scenario (e.g., mobile prioritizes energy, offline prioritizes throughput).

**Baseline Results**: Pentathlon evaluation on WMT14 DE-EN and RAFT shows: OPUS outperforms larger MBART and M2M100 models in both accuracy and efficiency; WMT21-Meta achieves highest BLEU but with substantial efficiency costs; ONNX yields over 20% improvements in latency and throughput in the single-stream scenario; FP16 quantization improves efficiency, especially for larger models.

**Validation**: Controlled hardware environment (dedicated in-house server with two NVIDIA RTX 8000 GPUs, two Intel Xeon CPUs, 1TB DDR4) and a scheduler to ensure single inference workload at a time. All models evaluated on identical hardware; evaluation instances and seeds controlled so models are evaluated on the same instances and order. Preliminary experiments indicate consistency across runs, and therefore multiple rounds were not performed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Environmental impact
- Fairness
- Misuse

**Atlas Risks**:
- **Societal Impact**: Impact on the environment
- **Misuse**: Improper usage
- **Governance**: Unrepresentative risk testing

**Potential Harm**: ['Increased overall emissions due to increased ease of use/access (Jevons paradox)', 'Increased access to ML models by bad actors who would have otherwise been limited by computational resources']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The paper states that the license of the WMT14 DE-EN dataset is not listed on the dataset website; dataset licensing is not specified in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
