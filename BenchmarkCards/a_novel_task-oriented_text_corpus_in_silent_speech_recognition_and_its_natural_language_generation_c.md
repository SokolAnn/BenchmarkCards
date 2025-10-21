# A Novel Task-Oriented Text Corpus in Silent Speech Recognition and its Natural Language Generation Construction Method

## 📊 Benchmark Details

**Name**: A Novel Task-Oriented Text Corpus in Silent Speech Recognition and its Natural Language Generation Construction Method

**Overview**: We construct a novel task-oriented text corpus, which is utilized in the field of silent speech recognition (SSR). In the process of construction, we propose a task-oriented hybrid construction method based on natural language generation algorithm. The algorithm focuses on the strategy of data-to-text generation, and has two advantages including linguistic quality and high diversity (template-based method and deep neural networks respectively). In an SSR experiment with the generated text corpus, analysis results show that the performance of our hybrid construction method outperforms the pure method such as template-based natural language generation or neural natural language generation models.

**Data Type**: text (task-oriented session texts for Silent Speech Recognition)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- N/A

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To construct a novel task-oriented text corpus for use in silent speech recognition (SSR) and to propose a task-oriented hybrid construction method based on natural language generation (data-to-text generation) combining template-based and neural methods.

**Target Audience**:
- N/A

**Tasks**:
- Natural Language Generation
- Data-to-Text Generation
- Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Constructed via a task-oriented hybrid construction method: seed text corpus created from cycle templates and a seed lexicon (template-based generation), followed by expansion using deep neural network natural language generation models (BERT-based encoding and bi-directional LSTM/seq2seq generation). Seed corpus results are manually judged and iteratively refined.

**Size**: N/A

**Format**: N/A

**Annotation**: Manual quality judgment/review of seed text corpus (seed corpus judged manually as described in Step 4).

## 🔬 Methodology

**Methods**:
- Template-based natural language generation for seed corpus construction
- Deep neural network natural language generation (BERT encoder, bi-directional LSTM, sequence-to-sequence with attention)
- Hybrid combination of template-based seed corpus and neural NLG for corpus expansion
- Manual review/judgment of seed corpus quality

**Calculation**: N/A

**Interpretation**: The hybrid model is interpreted to provide two advantages: improved linguistic quality (from template-based seeds) and higher diversity (from neural NLG). The paper reports that the hybrid model outperforms pure template-based or pure neural NLG methods in SSR experiments (no quantitative metric values provided).

**Baseline Results**: The paper states that the hybrid construction method outperforms pure methods such as template-based natural language generation or neural natural language generation models in SSR experiments; no specific numerical baseline results are provided.

**Validation**: Validation is described as an SSR experiment using the generated text corpus and analysis comparing the hybrid method to template-only and neural-only NLG methods; detailed experimental setup and quantitative validation procedures are not provided.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
