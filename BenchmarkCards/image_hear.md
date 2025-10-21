# IMAGE HEAR

## 📊 Benchmark Details

**Name**: IMAGE HEAR

**Overview**: An out-of-domain image dataset proposed to better evaluate image-to-audio models. The paper states: "we additionally collected 100 images from the web, containing 30 visual classes (≈2-8 images per class), denoted as IMAGE HEAR, and evaluate our method on it. ... This dataset is publicly available to support reproducibility and evaluation in future research."

**Data Type**: image

**Domains**:
- Computer Vision
- Audio

**Similar Benchmarks**:
- VGGSound

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide an out-of-domain benchmark (IMAGE HEAR) for evaluating image-to-audio models and to standardize comparison of image-to-audio generation models in future research.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image-to-Audio Generation
- Visually Guided Audio Generation
- Conditional Audio Generation

**Limitations**: IMAGE HEAR contains 100 images across 30 visual classes (≈2-8 images per class). The paper explicitly states that "we do not have the reference audio for the IMAGE HEAR dataset."

## 💾 Data

**Source**: Collected from the web: "we additionally collected 100 images from the web, containing 30 visual classes (≈2-8 images per class), denoted as IMAGE HEAR."

**Size**: 100 images

**Format**: N/A

**Annotation**: Labeled with 30 visual classes (≈2-8 images per class).

## 🔬 Methodology

**Methods**:
- Automated metrics (Fréchet Audio Distance, KL Divergence, Clip-Score, Classifier accuracy using PaSST)

**Metrics**:
- Fréchet Audio Distance (FAD)
- Kullback-Leibler Divergence (KL Divergence)
- Clip-Score (CS)
- Accuracy

**Calculation**: FAD: distance between multivariate normal distributions of features extracted by an audio classifier pre-trained on AudioSet. Clip-Score: adapted using Wav2Clip as audio encoder and the frozen CLIP image encoder; expectation of cosine similarity of resultant feature vectors multiplied by scaling factor γ=100; for videos each image CS is computed independently with the whole audio and averaged. KL Divergence: computed between class distributions of original samples and generated ones using PaSST audio classifier trained on AudioSet. For IMAGE HEAR there is no reference audio, so accuracy of the classifier on generated audio is reported.

**Interpretation**: FAD measures distance between generated and real distributions (lower FAD indicates higher fidelity). Higher Clip-Score and higher Accuracy indicate better relevance to the visual condition. KL Divergence measures divergence between class distributions (lower is closer).

**Baseline Results**: Selected results from Table 1 (as reported in the paper): Reference (real): CS 7.61, Accuracy 56.93%. SpecVQGAN [13] (1 Feats) on VGGSound: FAD 6.99, KL 3.19, CS 4.41, Accuracy 12.79%. SpecVQGAN (5 Feats) on VGGSound: FAD 6.81, KL 3.13, CS 4.54, Accuracy 14.44%. SpecVQGAN (212 Feats) on VGGSound: FAD 6.64, KL 3.10, CS 4.62, Accuracy 14.44%. Ours (IM2WAV) on VGGSound: FAD 6.41, KL 2.54, CS 7.19, Accuracy 35.77%. On IMAGE HEAR (single-image) Ours: CS 9.53, Accuracy 49.14% (other model numbers reported in Table 1 for baselines are also provided in the paper).

**Validation**: Followed original VGGSound train/test splits. For IMAGE HEAR evaluation, the authors generated 120 audios per image class with each image used for an equal number of samples to ensure statistical significance.

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
