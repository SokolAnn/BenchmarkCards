# SDW -ASL: A Dynamic System to Generate Large Scale Dataset for Continuous American Sign Language

## 📊 Benchmark Details

**Name**: SDW -ASL: A Dynamic System to Generate Large Scale Dataset for Continuous American Sign Language

**Overview**: We proposed a system that can generate large scale ASL datasets for continuous ASL. ... We are releasing the first version of our ASL dataset, which contains 30k sentences, 416k words, a vocabulary of 18k words, in a total of 104 hours. This is the largest continuous sign language dataset published to date in terms of video duration.

**Data Type**: Condensed body pose sequences (3D pose, hand and face landmarks) paired with time-stamped English sentence text (sentence-video pairs)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- American Sign Language
- English

**Similar Benchmarks**:
- PHOENIX14T
- MS-ASL
- How2Sign

**Resources**:
- [Resource](https://adeddb94ac1d.ngrok.io)

## 🎯 Purpose and Intended Users

**Goal**: Create a publicly available ASL dataset serving as a standard for the ASL research community and design a system that allows the dataset to be evolved, expanded, and improved, particularly to support ASL production research.

**Target Audience**:
- ASL research community
- Researchers in Natural Language Processing
- Researchers in Computer Vision

**Tasks**:
- Sign Language Production
- Sign Language Comprehension

**Limitations**: Dataset focuses on uniformity for ASL production and excludes diverse dialects; created from a small number of consistent news-anchor sources which limits signer diversity.

**Out of Scope Uses**:
- Interviews
- Event reports
- Holiday celebrations
- Video content without WebVTT or embedded closed captions

## 💾 Data

**Source**: Collected from two ASL News channels (news anchor videos with WebVTT or embedded closed captions); video clips segmented using closed captions and OCR.

**Size**: 30,000 sentences; 416,000 words; vocabulary of 18,000 words; 104 hours of video.

**Format**: Condensed body pose data sequences (MediaPipe landmarks: first 24 BlazePose landmarks, 21 hand landmarks, 468 face mesh landmarks) paired with time-stamped English sentence text (WebVTT).

**Annotation**: Automatically generated from closed captions and OCR (Python-tesseract) with post-processing to combine fragments; human review and minor corrections supported via a web-based interface.

## 🔬 Methodology

**Methods**:
- Automated segmentation using WebVTT timestamps and OCR (Python-tesseract)
- Pose extraction using MediaPipe (BlazePose, hand and face landmarks) with bounding box and outlier filtering
- Post-processing to combine caption fragments and timestamps
- Human review and manual correction via a web-based interface

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: Human review and manual correction via a web-based interface; outlier filtering and bounding-box filtering applied to improve pose detection robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
- **Privacy**: Exposing personal information

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: By only releasing the pose data sequence (post data sequence), the privacy of the signers is protected.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
