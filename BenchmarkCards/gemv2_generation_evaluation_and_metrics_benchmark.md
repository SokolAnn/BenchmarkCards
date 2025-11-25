# GEMv2 (Generation, Evaluation, and Metrics benchmark)

## 📊 Benchmark Details

**Name**: GEMv2 (Generation, Evaluation, and Metrics benchmark)

**Overview**: The new version of the Generation, Evaluation, and Metrics Benchmark introduces a modular infrastructure for dataset, model, and metric developers to benefit from each others work. GEMv2 supports 40 documented datasets in 51 languages, provides interactive data card creation and rendering tools, and an online evaluation process that collects model outputs and computes metrics for all datasets.

**Data Type**: text (text-to-text pairs for Natural Language Generation tasks)

**Domains**:
- Natural Language Processing

**Languages**:
- Amharic
- Azerbaijani
- Bengali
- Burmese
- Dutch
- Gujarati
- Hausa
- Igbo
- Javanese
- Kirundi
- Kyrgyz
- Marathi
- Nepali
- Oromo
- Pashto
- Persian
- Pidgin
- Punjabi
- Scottish Gaelic
- Serbian
- Sinhala
- Somali
- Sundanese
- Swahili
- Swedish
- Tamil
- Telugu
- Tigrinya
- Ukrainian
- Urdu
- Uzbek
- Welsh
- Yoruba
- Czech
- Italian
- Thai
- Turkish
- Vietnamese
- Arabic
- Finnish
- Hindi
- Japanese
- Korean
- Portuguese
- Indonesian
- Chinese
- German
- Russian
- Spanish
- French
- English
- West African Pidgin English

**Similar Benchmarks**:
- GEM (Generation, Evaluation, and Metrics benchmark)
- SuperGLUE

**Resources**:
- [Resource](https://huggingface.co/spaces/GEM/DatasetCardForm)
- [Resource](https://huggingface.co/GEM)
- [Resource](https://huggingface.co/spaces/GEM/submission-form)
- [Resource](https://huggingface.co/autotrain)
- [GitHub Repository](https://github.com/huggingface/hf_benchmarks)
- [Resource](https://gem-benchmark.com)
- [Resource](https://huggingface.co/spaces/GEM/results)

## 🎯 Purpose and Intended Users

**Goal**: Unify infrastructure for generation research by providing a modular, living benchmark that standardizes dataset documentation, loading, metric computation, and online evaluation for Natural Language Generation.

**Target Audience**:
- Dataset developers
- Model developers
- Metric developers
- Evaluation researchers
- Natural Language Generation researchers

**Tasks**:
- Data-to-Text
- Summarization
- Response Generation
- Simplification
- Paraphrasing
- Question Generation
- Reasoning
- Slide Generation

**Limitations**: GEMv2 avoids explicit curation decisions beyond licensing and consent, which has implications for dataset deprecation and may decrease curation; combining every dataset with every metric may lead to flawed evaluations for languages and metrics that have not been tested; the overview paper omits detailed human evaluation procedures (to be released separately).

## 💾 Data

**Source**: A collection of 40 documented datasets (27 new tasks plus 13 ported from GEMv1) drawn from prior dataset releases and community submissions (examples include WikiLingua, XLSum, WikiCatSum, CommonGen, ToTTo, XSum, and many others).

**Size**: 40 datasets (sizes vary per dataset; see Table 3 for per-dataset training sizes, e.g., 70,000 examples for CommonGen, 120,000 examples for ToTTo, 480,000 examples for WikiAuto+ASSET/TURK/Split&Rephrase, etc.)

**Format**: Datasets provided via Hugging Face dataset repositories and loadable with the Datasets library; standardized fields include linearized_input (string), target (string), references (list of strings), and gem_id; data card output is a structured JSON converted to markdown and web viewer rendering.

**Annotation**: Varies by dataset: some datasets are automatically created, some are crowdworker-created, and some are expert-created. The paper reports an almost even split between automatically-, crowdworker-, and expert-created datasets (with crowdworker-created slightly more common).

## 🔬 Methodology

**Methods**:
- Automated metrics computation using the GEM-metrics library
- Online evaluation (submission of model outputs to the Hugging Face Hub and AutoTrain evaluation jobs)
- Local evaluation using the gem-metrics library
- Human evaluation (not detailed in this overview paper; human evaluation working group exists and instructions to be released separately)

**Metrics**:
- BLEU Score
- ROUGE (e.g., ROUGE-L)
- BLEURT
- Various model-based NLG metrics (via Docker integration)

**Calculation**: Metrics are computed using the GEM-metrics library where each metric implements a compute() function; for online submissions AutoTrain downloads the submission and the reference splits from the Hub and runs GEM-metrics to compute metrics (Docker integration is supported to avoid dependency conflicts).

**Interpretation**: N/A

**Validation**: Dataset selection followed a SuperGLUE-like process with three requirements: dataset authors must consent, data must be openly available under a permissive license, and the task must be castable as text-to-text. Data card completeness and quality are supported via an interactive collection tool with progress indicators; many datasets include challenge splits and re-splitting for validation and robustness testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Intellectual Property
- Transparency
- Governance
- Fairness
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Intellectual Property**: Data usage rights restrictions
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Governance**: Lack of data transparency
- **Fairness**: Data bias
- **Robustness**: Hallucination
- **Data Laws**: Data usage restrictions

**Demographic Analysis**: The paper analyzes language coverage and resource taxonomy (Table 1 and Table 2) showing counts of supported languages and their resource classes; no human-demographic breakdowns are provided.

**Potential Harm**: ['Exposure of personal information (PII) in datasets', 'Flawed or misleading evaluations due to combining datasets and metrics across languages without tested metrics or appropriate tokenization', 'Challenges in dataset deprecation and potential for dataset erasure or misuse of outdated datasets']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data cards report PII likelihood: 20 data cards report PII is unlikely or definitely not included, while 10 report PII is likely or definitely included. The paper discusses different justifications for absent PII (restricted domain, public domain sources, simulated data, rater instructions).

**Data Licensing**: The majority of datasets use Creative Commons variants (22); 4 datasets use the MIT license and 3 use Apache 2.0. Most datasets allow unrestricted use, with 8 limiting use to non-commercial cases.

**Consent Procedures**: A requirement for inclusion is that dataset authors must consent to inclusion in GEMv2.

**Compliance With Regulations**: Not Applicable
