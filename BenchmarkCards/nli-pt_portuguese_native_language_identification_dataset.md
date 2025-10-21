# NLI-PT (Portuguese Native Language Identification Dataset)

## 📊 Benchmark Details

**Name**: NLI-PT (Portuguese Native Language Identification Dataset)

**Overview**: NLI-PT, the first Portuguese dataset compiled for Native Language Identification (NLI), includes 1,868 student essays written by learners of European Portuguese (L2) whose native languages (L1s) include Chinese, English, Spanish, German, Russian, French, Japanese, Italian, Dutch, Tetum, Arabic, Polish, Korean, Romanian, and Swedish. NLI-PT includes the original student text and four different types of annotation: POS, fine-grained POS, constituency parses, and dependency parses. The dataset was created by unifying data from existing Portuguese learner corpora and uniformly annotating them for research in NLI, Second Language Acquisition, and educational Natural Language Processing.

**Data Type**: text (learner essays with linguistic annotations: POS, fine-grained POS, constituency parses, dependency parses)

**Domains**:
- Natural Language Processing
- Education
- Second Language Acquisition

**Languages**:
- Portuguese
- Chinese
- English
- Spanish
- German
- Russian
- French
- Japanese
- Italian
- Dutch
- Tetum
- Arabic
- Polish
- Korean
- Romanian
- Swedish

**Similar Benchmarks**:
- COPLE2
- Leiria corpus
- PEAPL2
- CAL2
- International Corpus of Learner English

**Resources**:
- [Resource](http://www.clul.ulisboa.pt/en/resources-en/11-resources/894-nli-pt-a-portuguese-native-language-identification-dataset)
- [Resource](http://alfclul.clul.ul.pt/teitok/learnercorpus)
- [Resource](http://teitok.iltec.pt/peapl2/)
- [Resource](http://www.clul.ulisboa.pt/pt/24-recursos/350-recolha-de-dados-de-ple)
- [Resource](http://cal2.clunl.edu.pt/)
- [Resource](https://arxiv.org/abs/1804.11346)

## 🎯 Purpose and Intended Users

**Goal**: To provide the first Portuguese dataset specifically compiled and uniformly annotated for Native Language Identification (NLI), enabling research on NLI, Second Language Acquisition, and educational Natural Language Processing.

**Target Audience**:
- Researchers in Native Language Identification
- Researchers in Second Language Acquisition
- Researchers in Educational Natural Language Processing

**Tasks**:
- Native Language Identification
- Grammatical Error Detection and Correction
- Computer-aided Language Learning
- Spellchecking
- L1 interference analysis

**Limitations**: The dataset combines data from different source corpora with varying L1 distributions and topic distributions; the dataset is not balanced by topic which can lead to topic bias in NLI experiments. Only some source corpora were linguistically annotated originally and annotations had to be unified. Text length and topic representation are highly variable.

## 💾 Data

**Source**: Compiled from three existing Portuguese learner corpora: COPLE2, Leiria corpus, and PEAPL2.

**Size**: 1,868 texts; 380,417 tokens; 20,685 types

**Format**: Unified text format (cleaned text files with accompanying linguistic annotation layers); source formats included XML and TXT and were converted to a unified format.

**Annotation**: Annotated with simple POS, fine-grained POS (using Freeling Portuguese morphological module), constituency parses (LX Parser), and dependency parses (DepPattern).

## 🔬 Methodology

**Methods**:
- Automated evaluation using machine learning (linear Support Vector Machine)
- Stratified 10-fold cross-validation

**Metrics**:
- Accuracy

**Calculation**: A linear SVM (LIBLINEAR) using a bag-of-words model was trained and evaluated with stratified 10-fold cross-validation on a subset of five L1s.

**Interpretation**: Reported accuracy (70%) represents baseline lexical performance on the selected subset; authors note this result may be affected by topic bias because the dataset is not balanced by topic.

**Baseline Results**: 70% Accuracy using a linear SVM (bag-of-words) on a subset of five L1s: Chinese (355 texts), English (236 texts), German (214 texts), Italian (216 texts), Spanish (271 texts).

**Validation**: Stratified 10-fold cross-validation was used to evaluate the baseline classifier.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of data transparency

**Demographic Analysis**: Distribution by L1 and by CEFR proficiency levels is provided in Tables 2 and 4; counts per L1 and per proficiency level are reported.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
