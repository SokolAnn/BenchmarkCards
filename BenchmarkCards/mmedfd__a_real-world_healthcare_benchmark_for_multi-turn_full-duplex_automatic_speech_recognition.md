# MMedFD: A REAL-WORLD HEALTHCARE BENCHMARK FOR MULTI-TURN FULL-DUPLEX AUTOMATIC SPEECH RECOGNITION

## 📊 Benchmark Details

**Name**: MMedFD: A REAL-WORLD HEALTHCARE BENCHMARK FOR MULTI-TURN FULL-DUPLEX AUTOMATIC SPEECH RECOGNITION

**Overview**: MMedFD is a benchmark for multi-turn, full-duplex Chinese healthcare dialogue constructed from live user–agent interactions under full-duplex conditions.

**Data Type**: speech-text pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Kinetics-JOJO/MMedFD)
- [Resource](https://huggingface.co/datasets/HanselZz/MMedFD)

## 🎯 Purpose and Intended Users

**Goal**: Establish a reproducible framework for benchmarking streaming ASR and end-to-end duplex agents in healthcare deployment.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- ASR Developers

**Tasks**:
- Automatic Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Collected from a deployed AI assistant during internal testing

**Size**: 5,805 dialogues, 39.04 hours of audio

**Format**: PCM

**Annotation**: Annotated with role labels and medical entities for supervised training and evaluation

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)
- Healthcare Word Error Rate (HC-WER)

**Calculation**: WER is calculated based on the Levenshtein distance considering substitutions, deletions, and insertions.

**Interpretation**: Lower values of WER, CER, and HC-WER indicate better performance in transcribing spoken dialogue.

**Validation**: Validation was conducted using separate held-out test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data, Data privacy rights alignment

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures and anonymization procedures included removing personally identifiable information (PII) during data curation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent was obtained for the collection and use of data.

**Compliance With Regulations**: Data collection complied with governance policies and institutional ethics guidelines.
