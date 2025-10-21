# MidiCaps (A Large-Scale MIDI Dataset with Text Captions)

## 📊 Benchmark Details

**Name**: MidiCaps (A Large-Scale MIDI Dataset with Text Captions)

**Overview**: MidiCaps is the first openly available large-scale MIDI dataset with text captions, consisting of over 168,000 MIDI files paired with textual descriptions detailing musical content, thus facilitating multi-modal exploration and analysis.

**Data Type**: MIDI files with text captions

**Domains**:
- Music Information Retrieval
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/amaai-lab/MidiCaps)
- [GitHub Repository](https://github.com/AMAAI-Lab/MidiCaps)

## 🎯 Purpose and Intended Users

**Goal**: To enable research that combines LLMs with symbolic music by providing a large-scale curated MIDI dataset with captions.

**Target Audience**:
- ML Researchers
- Music Researchers
- Domain Experts

**Tasks**:
- Music Information Retrieval
- Music Understanding
- Cross-Modal Translation

**Limitations**: Due to the symbolic nature of music, labeling files of various lengths is inherently difficult. Additionally, extracting features from synthesized audio files may impact accuracy.

## 💾 Data

**Source**: Lakh MIDI Dataset

**Size**: 168,407 MIDI files with matching text captions

**Format**: MIDI

**Annotation**: Generated using in-context learning with a Large Language Model (Claude 3), based on features extracted from MIDI files.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Overall matching
- Genre matching
- Mood matching
- Key matching
- Chord matching
- Tempo matching

**Calculation**: Captions were rated based on various matching criteria by participants in a listening study.

**Interpretation**: Higher ratings indicate better matching of the captions to the MIDI audio and overall quality of the captions.

**Validation**: Tested through subjective evaluation via a listening study.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY 4.0 License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
