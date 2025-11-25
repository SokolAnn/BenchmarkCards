# UGIF-DataSet

## 📊 Benchmark Details

**Name**: UGIF-DataSet

**Overview**: A multi-lingual, multi-modal UI grounded dataset for step-by-step task completion on the smartphone. UGIF-DataSet contains 4,184 tasks across 8 languages and pairs how-to queries (text and speech) with English instruction steps and sequences of Android UI screenshots, view hierarchies, and actions recorded from human annotators to evaluate retrieval, parsing, and UI grounding for creating on-device step-by-step tutorials.

**Data Type**: multimodal: how-to queries (text and speech), instruction-step to macro pairs, UI screenshots (images), view hierarchies (XML), and action sequences

**Domains**:
- Natural Language Processing
- Human-Computer Interaction
- Computer Vision

**Languages**:
- English
- Hindi
- Kannada
- Marathi
- Gujarati
- Bengali
- Swahili
- Spanish

**Similar Benchmarks**:
- PixelHelp

**Resources**:
- [Resource](https://arxiv.org/abs/2211.07615)

## 🎯 Purpose and Intended Users

**Goal**: Build a UI navigation agent and evaluate how well step-by-step tutorials can be created on the Android UI by grounding help documents to UI screens; provide a multilingual, multimodal dataset to evaluate retrieval, parsing, and UI grounding.

**Target Audience**:
- Natural Language Processing researchers

**Tasks**:
- Retrieval
- Parsing
- Instruction Following
- UI Grounding

**Limitations**: The UGIF-DataSet contains only one speech sample per query; all instructions scraped from the Google support site (does not cover forums or other sites); all UI captures start at the home screen.

## 💾 Data

**Source**: Crawled Android support site (Pixel Help) how-to pages; human annotators operating virtual Android devices recorded UI screenshots, view hierarchy XML, and action sequences while executing how-to instructions. Annotators translated and spoke queries and created oracle macro parses.

**Size**: 4,184 tasks across 8 languages (523 how-to queries per language). Dataset split per language: 152 train / 106 dev / 265 test samples.

**Format**: Screenshots (image files), view hierarchy in XML, instruction text, speech recordings, and action sequence logs (macros and step timestamps).

**Annotation**: Manual annotation by human annotators operating virtual Android devices: annotators translated/spoke queries, parsed how-to steps to macro sequences (oracle parses), and recorded screen-action sequences. Annotation process used an internal tool with approval by ethics, privacy, and legal committees.

## 🔬 Methodology

**Methods**:
- Automated metrics (parsing exact-match accuracy)
- End-to-end task completion evaluation (sequence exact-match)
- Retrieval using multilingual sentence embeddings (LaBSE)
- Parsing using large language models (PaLM, GPT-3, T5, UL2) with few-shot and fine-tuning/soft-prompt tuning
- Grounding using similarity metrics (Jaccard, UiBERT, LaBSE) and heuristics

**Metrics**:
- Parsing accuracy (exact match)
- End-to-end task completion success rate (sequence exact match)
- Precision at 1 (P@1) for retrieval

**Calculation**: Parsing accuracy: exact match between generated macro sequence and oracle parse. End-to-end success rate: considered successful only if the entire sequence of actions predicted by the model exactly matches the annotator's recorded sequence. Retrieval P@1 measured by cosine similarity of embeddings to retrieve the closest how-to.

**Interpretation**: High parsing accuracy indicates correctly generated macro sequences; end-to-end success requires exact reproduction of the recorded action sequence (following the how-to exactly). Lower scores indicate parsing, retrieval, or grounding failures, with notable degradation in non-English UI languages.

**Baseline Results**: Parsing accuracy (UGIF-DataSet test): PaLM 540B full finetune 70.1%; PaLM 62B full finetune 67.5%; PaLM 540B soft prompt tune 66.8%; UL2 20B full finetune 66.8%; T5 11B full finetune 66.8%. End-to-end task completion success rate (UGIF-DataSet test): Oracle parse + LaBSE ground (en) 52.8%; PaLM 540B parse + LaBSE ground (en) 48.6%; PaLM 540B parse + LaBSE ground (sw) 32.1%. Comparison to PixelHelp: Li et al. (2020a) PixelHelp (en) 70.5%; Ours on PixelHelp (en) 71.1%.

**Validation**: Development set used to determine grounding scrolling threshold T and for hyperparameter search. Fine-tuning and soft prompt-tuning performed with hyperparameter search over dropout values on TPU training; performance reported on dev/test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Robustness
- Societal Impact
- Misuse
- Accuracy

**Atlas Risks**:
- **Misuse**: Improper usage
- **Societal Impact**: Impact on affected communities
- **Robustness**: Data poisoning, Hallucination
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy, Unrepresentative data

**Potential Harm**: Automated agents operating over the UI could be misused and 'pollute the global digital commons' making app developers require identification, which 'could hurt marginalized communities and users who struggle with such entry barriers.'

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: On-device grounding preferred for privacy reasons; annotation pipeline and internal tool were used with approval by ethics, privacy, and legal committees.

**Data Licensing**: Not Applicable

**Consent Procedures**: Internal annotation process approved by ethics, privacy, and legal committees (no further consent procedure details provided).

**Compliance With Regulations**: Not Applicable
