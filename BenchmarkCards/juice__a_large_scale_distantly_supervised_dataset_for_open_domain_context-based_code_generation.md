# JuICe: A Large Scale Distantly Supervised Dataset for Open Domain Context-based Code Generation

## 📊 Benchmark Details

**Name**: JuICe: A Large Scale Distantly Supervised Dataset for Open Domain Context-based Code Generation

**Overview**: We present JuICe, a corpus of 1.5 million examples with a curated test set of 3.7K instances based on online programming assignments. JuICe is a large-scale open-domain dataset of target code cells paired with a sequence of natural language (NL) and code context from Jupyter notebooks, collected to study code generation conditioned on a long context history. Using JuICe, we define and evaluate two tasks: (1) generation of the API call sequence in a code cell, and (2) full code cell generation, both conditioned on the NL-code history up to a particular code cell.

**Data Type**: code cells paired with sequences of natural language markdown and code (target cell + NL/code context)

**Domains**:
- Software Engineering
- Data Science
- Education

**Languages**:
- English

**Similar Benchmarks**:
- CONCODE (Iyer et al., 2018)
- CoNaLa (Yin et al., 2018)
- ATIS (Zettlemoyer and Collins, 2009)
- SequentialQA (Iyyer et al., 2017)
- SCONE (Long et al., 2016)

**Resources**:
- [GitHub Repository](https://github.com/rajasagashe/juicecells)
- [Resource](https://arxiv.org/abs/1910.02216)

## 🎯 Purpose and Intended Users

**Goal**: To introduce the task of code generation under the paradigm of interactive computing (conditioned on interleaved NL markdown and code cells) and to collect and release a large-scale dataset (JuICe) with a human-curated dev/test set to train and evaluate models for context-based code generation.

**Tasks**:
- Full code generation
- API sequence generation

**Limitations**: The training set contains noise (e.g., target NL referring to another code cell), and training data is distantly supervised and noisier than the human-curated dev/test. Models struggle to effectively incorporate more than 3 context cells as input sequence length becomes large. N/A

## 💾 Data

**Source**: Publicly available Jupyter notebooks collected from github.com (notebooks created before May 2019) for the training set; high-quality nbgrader notebooks and in-class exercise solution notebooks mined from GitHub for the human-curated dev/test sets.

**Size**: Train: 1,518,049 examples; Dev: 1,744 examples; Test: 1,981 examples; Human-curated dev+test total: 3,725 examples; Overall corpus described as 1.5 million examples (over 1.5M source code cells paired with context).

**Format**: N/A

**Annotation**: Training data: distantly supervised automatic extraction from public notebooks. Dev/Test: human-curated using nbgrader assignment notebooks and in-class exercise/solution notebook pairs; correct instructor/student solutions verified via nbgrader metadata and execution on test cases; for in-class exercises, instructor solutions verified by existence in at least 2 other GitHub repositories.

## 🔬 Methodology

**Methods**:
- Retrieval baseline (Ret-Train, Ret-Context)
- LSTM encoder-decoder with attention (Seq2Seq LSTM)
- Transformer
- Retrieval and non-neural baselines
- Human performance estimation (using student notebook solutions)

**Metrics**:
- Exact Match (EM)
- BLEU score
- Precision
- Recall

**Calculation**: For full code generation: Exact Match (EM) measures strict exact matching of generated code to the target; corpus-level BLEU score provides partial credit for partially correct snippets. For the API sequence task: predicted API calls treated as a set and evaluated using Precision and Recall against the gold set of API calls.

**Interpretation**: EM is a strict metric measuring ability to generate fully functioning code; BLEU serves as a measure of partial credit for partially correct snippets. For API sequences, higher Precision/Recall indicate better retrieval of API calls relevant to the target cell.

**Baseline Results**: Full code generation (Dev/Test) - LSTM K=3 N=1,518,049: Dev BLEU=21.66, Dev EM=5.57; Test BLEU=20.92, Test EM=5.71. Retrieval baselines and Transformers reported lower BLEU/EM (see paper Table 6). API sequence task (Dev/Test) - LSTM K=3 N=1,518,049: Dev Precision=51.34, Dev Recall=44.83; Test Precision=52.60, Test Recall=46.46 (see paper Table 7). Human performance estimate on a subset: code generation 60% BLEU and 23% EM; API sequence 84% Precision and 85% Recall.

**Validation**: Dev/Test are human-curated from nbgrader and in-class exercise notebooks. For nbgrader assignments, solutions are extracted using nbgrader metadata (instructor solutions verified by successful execution on test cases). For in-class exercises, solution/exercise notebook pairs were matched (over 50% cell similarity) and instructor solutions verified by presence in at least 2 other GitHub repositories. Duplicate target/context pairs were removed from training by downsampling to ensure uniqueness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper notes that students are expected to confidentially send their completed assignment to instructors, but "the solutions are often later posted on Github."

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
