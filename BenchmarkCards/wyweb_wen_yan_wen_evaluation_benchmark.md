# WYWEB (Wen Yan Wen Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: WYWEB (Wen Yan Wen Evaluation Benchmark)

**Overview**: We introduce the WYWEB evaluation benchmark, which consists of nine NLP tasks in classical Chinese, implementing sentence classification, sequence labeling, reading comprehension, and machine translation, to evaluate the performance of models on classical Chinese natural language understanding.

**Data Type**: text (sentence classification samples, sequence labeling sequences, reading comprehension multiple-choice QA pairs, token similarity pairs, and parallel sentence pairs for machine translation)

**Domains**:
- Natural Language Processing

**Languages**:
- Classical Chinese

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- CLUE
- CUGE
- CCLUE
- CLiMP
- QuoteR
- CBLUE
- SentEval
- RACE

**Resources**:
- [GitHub Repository](https://github.com/baudzhou/WYWEB)
- [Resource](https://cclue.top/)
- [GitHub Repository](https://github.com/garychowcmu/daizhigev20)
- [Resource](https://catalog.ldc.upenn.edu/docs/LDC2017T14/)
- [GitHub Repository](https://github.com/ethan-yt/guwenbert)
- [Resource](https://huggingface.co/TLC)

## 🎯 Purpose and Intended Users

**Goal**: To propose and establish a novel benchmark for classical Chinese natural language understanding by redesigning, creating and collecting nine classical Chinese NLP tasks to evaluate and analyze NLP models.

**Target Audience**:
- NLP researchers
- Model developers
- Classical Chinese researchers

**Tasks**:
- Sequence Labeling
- Named Entity Recognition
- Text Classification
- Token Similarity
- Reading Comprehension
- Machine Translation

**Limitations**: Lacking expertise knowledge and data; small dataset sizes for some tasks (e.g., XuCi); GJC category rule not certified by authoritative experts; lack of a diagnostic dataset; evaluated baseline models are primarily BERT/RoBERTa style and lack variety.

## 💾 Data

**Source**: Mix of sources as stated in the paper: Daizhige corpus, authoritative historical texts and Buddhist scriptures, examination papers, idiom dictionary, GLNER (GULIAN 2020) competition dataset, FSPC (THU-FSPC), and collected online modern-classical parallel translations.

**Size**: Per Table 1 (Train / Dev / Test examples): PUNC: 90,000 / 20,000 / 20,000 examples; TLC: 28,000 / 6,000 / 6,000 examples; GJC: 100,000 / 20,000 / 20,000 examples; XuCi: 800 / 200 / 200 examples; WYWRC: 3,000 / 500 / 500 examples; IRC: 3,000 / 1,000 / 1,000 examples; WYWMT: 20,000 / 3,000 / 3,000 examples; GLNER: 80,000 / 18,000 / 18,000 examples; FSPC: 3,000 / 1,000 / 1,000 examples.

**Format**: Mixture of formats as stated: JSON (WYWRC, GLNER, FSPC, IRC), TSV (PUNC sequence-pair TSV, TLC TSV, WYWMT TSV, Xuci TSV), text–category format for GJC (text–category), and other TSV/JSON as described per task.

**Annotation**: Annotators are volunteer students and scholars; processes include data collection, extracting, proofreading, double-checking between annotators, and final review by domain experts. For exam-paper-derived tasks annotators copy or OCR questions and proofread; quality checks applied (e.g., WYWMT filtering and sample length limit 5–200 characters). GLNER licensed from competition owner after contact.

## 🔬 Methodology

**Methods**:
- Automated metrics (task-specific)
- Fine-tuning of pre-trained language models
- Human evaluation (upper-bound testing by annotators)
- Leaderboard evaluation using provided toolkit (PyTorch and Transformers)

**Metrics**:
- F1 Score (sequence labeling: PUNC, GLNER)
- Accuracy (sentence classification tasks: GJC, TLC, FSPC; token similarity: XuCi; reading comprehension: WYWRC, IRC)
- BLEU Score (WYWMT)
- chrF2 (WYWMT)
- TER (Translation Edit Rate) (WYWMT)
- ROUGE-1
- ROUGE-2
- ROUGE-L

**Calculation**: Standard task-specific metrics are used: F1 for sequence labeling, Accuracy for classification and multiple-choice reading comprehension, BLEU/chrF2/TER/ROUGE for machine translation. For experiments, each model is fine-tuned with 3 runs and the model with the best development score is used for testing.

**Interpretation**: Higher metric values indicate better performance; human evaluation results are reported as upper bounds. The paper notes a significant gap between models and human performance and reports that larger models and more pretraining data/steps tend to perform better.

**Baseline Results**: Baseline results reported in the paper (examples): Table 2 - Human average 88.0; DeBERTa-base average 75.9; other model averages include GuwenBERT-base 72.9, GuwenBERT-large 75.6. Per-task metrics shown in Table 2. WYWMT (Table 3) BLEU scores: Human 45.6, guwenbert-base 40.1, DeBERTa-base 39.5, guwenbert-large 38.8.

**Validation**: Validation procedure: 3 training runs per model; select model with best development score for testing. Human performance measured by sampling (extract 30 samples in training phase, sample 100 items from the test set) and aggregating three annotators' results. Cross double-checking and expert final review were applied during annotation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Societal Impact
- Intellectual Property
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities, Impact on the environment
- **Intellectual Property**: Data usage rights restrictions
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Gender bias present in historical classical Chinese texts', 'Derogatory and insulting terms toward ethnic groups present in historical texts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sources are primarily public-domain classical texts and authoritative releases; the authors state there are generally not many ethical concerns regarding privacy or anonymity for the corpus used.

**Data Licensing**: For copyrighted texts the authors state they obtained permission/licensing (example: GLNER licensed after contacting owner). No specific license types (e.g., CC BY) are specified in the paper.

**Consent Procedures**: The authors contacted owners and obtained licenses where copyright issues were a concern; otherwise data are from public/open sources. No additional consent procedures are described.

**Compliance With Regulations**: Not Applicable
