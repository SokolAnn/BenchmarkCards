# fMoW-mm (multimodal dataset)

## 📊 Benchmark Details

**Name**: fMoW-mm (multimodal dataset)

**Overview**: We introduce fMoW-mm, a multimodal dataset incorporating satellite imagery, maps, metadata, and text annotations, aimed at enhancing vision-language datasets for remote sensing.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- fMoW (Functional Map of the World)

**Resources**:
- [Resource](https://bit.ly/fMoW-mm)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the generation of detailed and context-rich captions for remote sensing images using external data sources.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Remote Sensing Experts

**Tasks**:
- Text Generation
- Automatic Target Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Combination of satellite images from fMoW-rgb, maps from OpenStreetMap, and associated metadata.

**Size**: 83,412 samples

**Format**: N/A

**Annotation**: Generated captions using GPT-4o integrated with metadata and maps.

## 🔬 Methodology

**Methods**:
- Data augmentation using external maps
- Caption generation with LLM (GPT-4o)

**Metrics**:
- FDR (False Discovery Rate) to evaluate hallucinations
- BLEU for caption quality

**Calculation**: FDR calculated using precision over proper nouns based on reference lists of correct landmarks.

**Interpretation**: Lower FDR indicates fewer hallucinations in the generated captions.

**Baseline Results**: Comparison with vision-language models like CLIP and RemoteCLIP demonstrated higher performance with the fMoW-mm dataset.

**Validation**: Performance evaluated through ablation studies on map resolutions and types, and the effectiveness in few-shot object detection.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
