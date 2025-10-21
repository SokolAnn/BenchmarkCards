# The Gutenberg Dialogue Dataset

## 📊 Benchmark Details

**Name**: The Gutenberg Dialogue Dataset

**Overview**: A dataset ensemble of dialogues extracted from public-domain books in Project Gutenberg. The paper builds a high-quality English dataset of 14.8M utterances and smaller datasets in German, Dutch, Spanish, Portuguese, Italian, and Hungarian, describes the extraction pipeline and heuristics, analyzes extraction errors, and demonstrates that pretraining on this data yields better response quality than pretraining on the noisier Opensubtitles dataset in several settings.

**Data Type**: Multi-turn dialogue utterances (text)

**Domains**:
- Natural Language Processing
- Conversational AI

**Languages**:
- English
- German
- Dutch
- Spanish
- Portuguese
- Italian
- Hungarian

**Similar Benchmarks**:
- Opensubtitles
- DailyDialog
- Persona-Chat
- Cornell Movie Corpus

**Resources**:
- [Resource](https://www.gutenberg.org/)
- [GitHub Repository](https://github.com/ricsinaruto/gutenberg-dialog)
- [GitHub Repository](https://github.com/ricsinaruto/dialog-eval)
- [Resource](https://ricsinaruto.github.io/chatbot.html)
- [Resource](https://arxiv.org/abs/2004.12752)

## 🎯 Purpose and Intended Users

**Goal**: Create a dataset which offers a better size-quality trade-off than other dialogue corpora.

**Target Audience**:
- Researchers

**Tasks**:
- Dialogue Modeling
- Multi-turn Response Generation
- Single-turn Response Generation
- Language Model Pretraining

**Limitations**: Not intended as a gold-standard dataset. Dataset is based on written (book) dialogues which may differ from modern spoken chit-chat; heuristics and parameters tuned primarily for English so other-language datasets are smaller and delimiters/parameters for other languages were not analyzed as thoroughly, leaving room for improvement. Extraction introduces noise and segmentation errors (detailed error analysis provided).

## 💾 Data

**Source**: Extracted from public-domain books available from Project Gutenberg using an open-source, heuristic-based extraction pipeline.

**Size**: English: 14,773,741 utterances (2,526,877 dialogues); German: 226,015 utterances (43,440 dialogues); Dutch: 129,471 utterances (23,541 dialogues); Spanish: 58,174 utterances (6,912 dialogues); Italian: 41,388 utterances (6,664 dialogues); Hungarian: 18,816 utterances (2,826 dialogues); Portuguese: 16,228 utterances (2,233 dialogues).

**Format**: N/A

**Annotation**: Automatically extracted using rule-based heuristics for delimiter detection, dialogue splitting, and turn segmentation; manual error analysis performed on sampled utterances and dialogues.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (17 metrics implemented in the DIALOG-EVAL repository)
- Pretraining and finetuning experiments with GPT-2 and Transformer architectures
- Manual error analysis of sampled utterances and dialogues
- Zero-shot and finetuning evaluation scenarios

**Metrics**:
- Response Length
- Per-word Unigram Entropy
- Per-utterance Unigram Entropy
- Per-word Bigram Entropy
- Per-utterance Bigram Entropy
- Unigram KL Divergence
- Bigram KL Divergence
- Embedding Average (AVG)
- Embedding Extrema (EXT)
- Embedding Greedy (GRE)
- Coherence (cosine similarity between input and response)
- Distinct-1
- Distinct-2
- BLEU-1
- BLEU-2
- BLEU-3
- BLEU-4

**Calculation**: Metrics are computed as implemented in the DIALOG-EVAL repository (Csáky et al., 2019). BLEU measures n-gram overlap (n=1..4). Entropy and KL divergence are computed at unigram and bigram levels, per-word and per-utterance. Embedding metrics (AVG, EXT, GRE) and coherence use embedding similarity measures; distinct-n is the ratio of unique n-grams. Detailed definitions follow Csáky et al. (2019) and referenced metric papers (Papineni et al., 2002; Li et al., 2016; Liu et al., 2016).

**Interpretation**: The authors note that automatic metrics correlate poorly with human judgment and should be assessed jointly; individual metrics can be misleading. They interpret improvements across many metrics as evidence that Gutenberg pretraining yields better downstream response quality than Opensubtitles in several settings.

**Baseline Results**: Gutenberg pre-training performs better than Opensubtitles on DailyDialog across nearly all metrics in both zero-shot and finetuned settings (reported in the paper). Gutenberg pre-training also outperforms Opensubtitles on most metrics across the seven languages evaluated, except Hungarian where Opensubtitles was better on some metrics.

**Validation**: Dialogues are split into train (90%), validation (5%), and test (5%) with dialogues from the same book placed in the same split. Validation of extraction quality includes manual error analyses: 100 utterance pairs and 50 dialogues sampled for English. Model validation uses validation-loss minimum for stopping during training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data source: Project Gutenberg public-domain books (copyrighted works removed). The extraction pipeline is released under the MIT license (paper states 'MIT licensed pipeline').

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
