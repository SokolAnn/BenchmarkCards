# The BabyLM Challenge: Sample-efficient pretraining on a developmentally plausible corpus

## 📊 Benchmark Details

**Name**: The BabyLM Challenge: Sample-efficient pretraining on a developmentally plausible corpus

**Overview**: This shared task is intended for participants with an interest in small scale language modeling, human language acquisition, low-resource NLP, and cognitive modeling. In partnership with CoNLL and CMCL, we provide a platform for approaches to pretraining with a limited-size corpus sourced from data inspired by the input to children. The task has three tracks, two of which restrict the training data to pre-released datasets of 10M and 100M words and are dedicated to explorations of approaches such as architectural variations, self-supervised objectives, or curriculum learning. The final track only restricts the amount of text used, allowing innovation in the choice of the data, its domain, and even its modality.

**Data Type**: text (mixed-domain pretraining corpus, mostly transcribed speech)

**Domains**:
- Natural Language Processing
- Cognitive Modeling
- Language Acquisition

**Languages**:
- English

**Similar Benchmarks**:
- CHILDES
- British National Corpus (BNC)
- Children’s Book Test
- Children’s Stories Text Corpus
- Standardized Project Gutenberg Corpus
- OpenSubtitles
- QCRI Educational Domain Corpus (QED)
- Wikipedia
- Simple Wikipedia
- Switchboard Dialog Act Corpus

**Resources**:
- [Resource](https://babylm.github.io/)
- [GitHub Repository](https://github.com/babylm/babylm.github.io/raw/main/babylm_data.zip)
- [Resource](https://arxiv.org/abs/2301.11796)
- [Resource](http://www.natcorp.ox.ac.uk)
- [Resource](https://www.kaggle.com/datasets/edenbd/children-stories-text-corpus)
- [Resource](https://dumps.wikimedia.org/enwiki/20221220/)
- [Resource](https://dumps.wikimedia.org/simplewiki/20221201/)

## 🎯 Purpose and Intended Users

**Goal**: Incentivize research on optimizing pretraining given data limitations inspired by human development, democratize research on pretraining by focusing on small-scale, developmentally plausible corpora, and provide a shared evaluation pipeline to compare approaches.

**Target Audience**:
- participants with an interest in small scale language modeling
- researchers in human language acquisition
- low-resource Natural Language Processing researchers
- cognitive modeling researchers

**Tasks**:
- Language Modeling (sequence scoring / assigning log-likelihood or pseudo log-likelihood)
- Classification (fine-tuning for classiﬁcation tasks)
- Syntactic Evaluation (targeted syntactic evaluations)
- Natural Language Understanding

**Limitations**: N/A

**Out of Scope Uses**:
- Pretrained models may not be used for any purpose such as reranking or data augmentation.

## 💾 Data

**Source**: Mixed-domain corpus composed of CHILDES; British National Corpus (dialogue portion); Children’s Book Test; Children’s Stories Text Corpus; Standardized Project Gutenberg Corpus; OpenSubtitles; QCRI Educational Domain Corpus (QED); Wikipedia (English); Simple Wikipedia; Switchboard Dialog Act Corpus.

**Size**: STRICT: 98.04M words; STRICT-SMALL: 9.96M words; dataset download size: 240MB zipped, 700MB unzipped; LOOSE track allows up to 100M words.

**Format**: Raw text files (distributed as a zip; 240MB zipped, 700MB unzipped)

**Annotation**: Raw text; no annotations

## 🔬 Methodology

**Methods**:
- Automated evaluation via a shared evaluation pipeline (Google Colab)
- Model sequence scoring using log-likelihood or pseudo log-likelihood
- Fine-tuning models to perform classification tasks for certain evaluations
- Baseline model training using hyperparameters from OPT, RoBERTa, and T5 to provide naïve baselines

**Calculation**: Models must be able to score a sequence (e.g., assign a log-likelihood or pseudo log-likelihood). Evaluation pipeline expects model outputs in a specified format and assumes compatibility with HuggingFace's transformers library (or equivalent scoring produced by participant's own pipeline).

**Interpretation**: Winners for the STRICT tracks are determined based on performance on the shared evaluation set. For the LOOSE track, winners are selected holistically based on evaluation performance, relevance to the shared task goals, potential impact, and novelty; computational/ training efficiency may also be considered for the LOOSE track.

**Validation**: More details about the evaluation pipeline and the set of tasks will be released subsequently; the pipeline is distributed so users can evaluate submissions in Google Colab or via the public evaluation code.

## ⚠️ Targeted Risks

**Risk Categories**:
- Societal Impact

**Atlas Risks**:
- **Societal Impact**: Impact on the environment

**Potential Harm**: ['Pretraining is expensive from a computational, energy, and financial perspective.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
