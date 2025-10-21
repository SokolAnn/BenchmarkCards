# TCQL (text-to-CQL dataset)

## 📊 Benchmark Details

**Name**: TCQL (text-to-CQL dataset)

**Overview**: This paper presents the first text-to-CQL task to automate the translation of natural language into Corpus Query Language (CQL). It provides a comprehensive framework including a specifically curated large-scale dataset, methodologies leveraging large language models for text-to-CQL, and evaluation metrics assessing syntactic validity and semantic correctness of generated CQL queries.

**Data Type**: text (natural language to CQL query pairs)

**Domains**:
- Natural Language Processing
- Linguistics (Corpus Linguistics)

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- Spider
- WikiSQL
- BIRD
- OverpassNL

**Resources**:
- [GitHub Repository](https://github.com/INL/BlackLab)
- [Resource](https://cwb.sourceforge.io/cqpweb.php)
- [Resource](https://www.sketchengine.eu/)
- [Resource](https://dumps.wikimedia.org/)
- [GitHub Repository](https://github.com/attardi/wikiextractor)

## 🎯 Purpose and Intended Users

**Goal**: To introduce the text-to-CQL task and provide a dataset and evaluation framework to convert natural language descriptions into Corpus Query Language (CQL), facilitating access to and analysis of annotated text corpora.

**Target Audience**:
- Researchers
- Practitioners

**Tasks**:
- Semantic Parsing
- Query Generation (natural language to Corpus Query Language)

**Limitations**: The TCQL dataset is constructed from automatically generated and manually labeled data due to lack of large amounts of raw human-generated CQL queries; generated queries may not always be meaningful. Scalability to longer text queries and dependency on computational resources may limit applicability.

## 💾 Data

**Source**: Corpus sources: TCFL Textbook (Chinese teaching materials) and EnWiki (Wikipedia). TCQL pairs are created from these corpora; corpora annotated using Stanford CoreNLP.

**Size**: TCQL labeled dataset: 13,367 examples (9,362 train, 1,328 dev, 2,677 test). Corpus sizes: TCFL Textbook: 578.4 k sentences, 7.7 M tokens; EnWiki: 138.6 M sentences, 3.1 B tokens.

**Format**: N/A

**Annotation**: Manual annotation with a 4-round process: initial CQL→NL generation via OpenAI GPT-4 API, two rounds of re-labeling by human annotators (8 retained annotators out of 14 recruited), and final review by two CQL-expert reviewers.

## 🔬 Methodology

**Methods**:
- In-Context Learning (Documentation Prompt, Few-shot ICL: 1-shot and 3-shot)
- Prompt engineering for LLMs
- Fine-tuning pretrained language models (prefix-tuning and full model fine-tuning; BART-Chinese and BART-English used)
- Automated evaluation using Exact Match, Valid Accuracy, Execution Accuracy, and CQLBLEU

**Metrics**:
- Exact Match (EM)
- Valid Accuracy (VA)
- Execution Accuracy (EX)
- CQLBLEU (combination of BLEU and AST tree similarity; α=0.5, β=0.5)

**Calculation**: Exact Match (EM): checks whether generated CQL exactly matches reference query. Valid Accuracy (VA): checks syntactic correctness of generated CQL with respect to CQL grammar. Execution Accuracy (EX): whether generated CQL executes on the corpus engine and returns the desired result (BlackLab used as execution engine). CQLBLEU: CQLBLEU(Qc,Qr) = α·BLEU(Qc,Qr) + β·TS(Qc,Qr), where TS is AST tree similarity computed by parsing CQL into ASTs (Tc=Parse(Qc), Tr=Parse(Qr)) and comparing non-leaf node signatures; authors set α=0.5 and β=0.5.

**Interpretation**: EM is a strict string-level match; VA indicates syntactic validity; EX assesses practical correctness by execution on the corpus engine (may capture semantic equivalence even if EM fails); CQLBLEU balances syntactic (BLEU) and semantic/structural (AST similarity) similarity.

**Baseline Results**: Reported results (from Table 5):
- BART-Chinese (TCFL Textbook): Valid Accuracy 46.52, Execution Accuracy 80.46, CQLBLEU 50.95 (EM not provided).
- BART-English (EnWiki): Exact Match 37.58, Valid Accuracy 81.74, Execution Accuracy 44.30, CQLBLEU 82.13.
- GPT-4 DP (Documentation Prompt): TCFL EM 35.17, VA 77.52, EX 51.79, CQLBLEU 74.95; EnWiki EM 14.93, VA 75.37, EX 24.49, CQLBLEU 67.63.
- GPT-4 1SL: TCFL EM 47.81, VA 81.84, EX 62.71, CQLBLEU 82.22; EnWiki EM 43.31, VA 82.24, EX 51.87, CQLBLEU 82.93.
- GPT-4 3SL: TCFL EM 67.49, VA 90.28, EX 77.85, CQLBLEU 91.83; EnWiki EM 58.24, VA 89.74, EX 65.53, CQLBLEU 89.93.

**Validation**: Dataset annotation validated via 4 rounds: GPT-4 generated initial NL from CQL, two rounds of human annotator re-labeling, and final review by two CQL-expert reviewers. Execution validation performed using the BlackLab corpus engine to verify execution-based metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
