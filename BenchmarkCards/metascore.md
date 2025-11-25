# MetaScore

## 📊 Benchmark Details

**Name**: MetaScore

**Overview**: MetaScore is a new dataset consisting of 963K musical scores paired with rich metadata, including user-annotated tags, collected from an online music forum. It enables text-to-music generation and supports controllable attributes such as instruments, genre, composer, and complexity.

**Data Type**: musical scores with metadata

**Domains**:
- Music Information Retrieval

**Languages**:
- English

**Similar Benchmarks**:
- MidiCaps

**Resources**:
- [Resource](https://wx83.github.io/MetaScore_Official/)

## 🎯 Purpose and Intended Users

**Goal**: To build a natural language-based symbolic music generation system with a new public dataset that enables controllable music generation.

**Target Audience**:
- Music Researchers
- AI Practitioners
- Music Composers

**Tasks**:
- Text-to-Music Generation
- Symbolic Music Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from the MuseScore forum.

**Size**: 963,000 musical scores

**Format**: XML

**Annotation**: User-annotated tags and metadata.

## 🔬 Methodology

**Methods**:
- Subjective listening tests
- Automated metrics

**Metrics**:
- Coherence
- Arrangement
- Adherence
- Overall Quality

**Calculation**: Metrics calculated based on listening tests and automated comparisons with baseline models.

**Interpretation**: Higher values in metrics indicate better quality of generated music.

**Baseline Results**: Compared against the BART-based model and Text2MIDI models.

**Validation**: Results validated through subjective evaluations with music experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Copyright
- Data Quality

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons licenses for publicly released content.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Acknowledges potential copyright issues and advises careful use.
