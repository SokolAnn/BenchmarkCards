# NUSAAKSARA

## 📊 Benchmark Details

**Name**: NUSAAKSARA

**Overview**: NUSAAKSARA is a novel public benchmark for Indonesian languages that focuses on preserving indigenous scripts. It covers diverse tasks such as image segmentation, OCR, transliteration, translation, and language identification, constructed through expert annotation from various historical manuscripts and documents.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- Indonesian

**Resources**:
- [Resource](https://huggingface.co/datasets/NusaAksara/NusaAksara)

## 🎯 Purpose and Intended Users

**Goal**: To safeguard and revitalize Indonesia's traditional scripts by providing a comprehensive benchmark dataset for research and development in NLP technologies.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Linguists
- Cultural Preservationists

**Tasks**:
- Image Segmentation
- Optical Character Recognition (OCR)
- Transliteration
- Machine Translation
- Language Identification

**Limitations**: This study observed only eight of the recognized local scripts, and the lack of Unicode support for Lampung scripts presents a significant challenge for transcription-related tasks.

## 💾 Data

**Source**: The dataset contains scanned documents written in 8 different scripts created from historical manuscripts, literary works, and educational literature.

**Size**: 10,000 examples

**Format**: Image and text files

**Annotation**: Annotated by native speakers, linguists, and educators through expert validation processes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Character Error Rate (CER)
- Word Error Rate (WER)
- BLEU Score
- chrF++

**Calculation**: Metric calculations are done based on the output of systems against gold standard annotations for transliteration and translation tasks.

**Interpretation**: Lower CER and WER indicate better OCR and transliteration performances, while higher BLEU and chrF++ scores reflect better translation quality.

**Baseline Results**: Models struggle with OCR tasks, often yielding high error rates; specifically, proprietary models like GPT-4o perform better on Lontara scripts compared to open-source solutions.

**Validation**: Results from validation indicated high agreement rates among annotators, particularly for transcription and translation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The benchmark includes a variety of languages and scripts, focusing primarily on underrepresented and low-resource languages.

**Potential Harm**: ['Cultural loss due to neglect of indigenous scripts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: N/A - Data is released under a non-commercial license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
