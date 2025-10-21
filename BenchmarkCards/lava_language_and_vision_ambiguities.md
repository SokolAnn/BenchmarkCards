# LAVA (Language and Vision Ambiguities)

## 📊 Benchmark Details

**Name**: LAVA (Language and Vision Ambiguities)

**Overview**: A multimodal corpus containing ambiguous sentences paired with short videos that visualize the different interpretations of each sentence, introduced to support the task of disambiguating a sentence given a visual scene which depicts one of the possible interpretations of that sentence.

**Data Type**: sentence-video pairs (text and video)

**Domains**:
- Natural Language Processing
- Computer Vision

**Similar Benchmarks**:
- UCF Sports
- YouTube (action recognition datasets)
- HMDB
- MSCOCO
- TACOS
- Dataset of Siddharth et al. (2014)

**Resources**:
- [Resource](https://arxiv.org/abs/1603.08079)

## 🎯 Purpose and Intended Users

**Goal**: Introduce a task for grounded language understanding in which an ambiguous sentence must be disambiguated using a visual depiction (video), and release a multimodal corpus (LAVA) that enables systematic study of linguistic ambiguities in visual contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Computer Vision and Natural Language Processing researchers

**Tasks**:
- Visual Grounding
- Ambiguity Resolution
- Sentence-Video Matching

**Limitations**: N/A

## 💾 Data

**Source**: Newly compiled LAVA corpus: sentences generated from POS tag sequence templates instantiated with a lexicon; videos filmed in an indoor environment depicting specific interpretations (variations include different actors, directions and two camera viewpoints).

**Size**: 237 sentences; 1,679 videos; average 7.1 videos per sentence; average 3.37 videos per sentence interpretation; average video length 3.02 seconds (90.78 frames); total ~1.4 hours of footage (152,434 frames).

**Format**: N/A

**Annotation**: Each sentence is accompanied by candidate interpretations encoded in first order logic; syntactic ambiguities additionally have Context Free Grammar (CFG) parses; discourse ambiguities include provided antecedents/logical forms or unambiguous sentence forms for ellipsis. Videos depict a single candidate interpretation each.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (1-out-of-2 or 1-out-of-3 classification per sentence-video pair)
- Automated metrics (accuracy over classification task)

**Metrics**:
- Accuracy

**Calculation**: For each sentence-video pair perform a 1-out-of-2 or 1-out-of-3 classification to select the interpretation that best fits the video; report classification Accuracy averaged over the entire corpus. Chance performance reported as 49.04%.

**Interpretation**: Overall accuracy indicates model capability to resolve visually grounded linguistic ambiguities; per-category accuracies indicate relative difficulty across ambiguity types (syntactic, semantic, discourse) and dependence on visual detector performance.

**Baseline Results**: The presented model achieved an overall Accuracy of 75.36% on the LAVA corpus. Per-category accuracies: syntactic ambiguities 84.26%, semantic ambiguities 72.28%, discourse ambiguities 64.44%. Chance performance is 49.04%.

**Validation**: Object detectors (CNN and DPM) were trained on held-out sections of the corpus and a scoring function was trained on held-out portions; evaluation performed on the corpus using the described 1-out-of-N classification setup.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
