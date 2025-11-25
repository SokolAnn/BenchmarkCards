# VerSe

## 📊 Benchmark Details

**Name**: VerSe

**Overview**: We introduce VerSe, a new dataset that augments existing multimodal datasets (COCO and TUHOI) with sense labels. VerSe contains 3518 images, each annotated with one of 90 verbs, and the OntoNotes sense realized in the image. VerSe serves two main purposes: (1) to show the feasibility of annotating images with verb senses (rather than verbs or actions); (2) to function as test bed for evaluating automatic visual sense disambiguation methods.

**Data Type**: multimodal (images with associated textual annotations: object labels and image descriptions; sense label annotations)

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- COCO
- TUHOI
- HICO
- ImageNet

**Resources**:
- [GitHub Repository](https://github.com/spandanagella/verse)
- [GitHub Repository](https://github.com/karpathy/neuraltalk)

## 🎯 Purpose and Intended Users

**Goal**: To show the feasibility of annotating images with verb senses and to function as a test bed for evaluating automatic visual sense disambiguation methods.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Computer Vision Researchers
- Natural Language Processing Researchers

**Tasks**:
- Visual Sense Disambiguation
- Word Sense Disambiguation
- Action Recognition

**Limitations**: The source datasets exhibit a Zipfian distribution of verbs (many verbs are represented by only a few images), so only verbs with five or more images were selected (resulting in 90 verbs). TUHOI contains many singleton action categories (1576 out of 2974 occur only once), limiting usefulness for VSD. Some automatically generated image descriptions are often irrelevant for the action depicted, resulting in inferior performance when using predicted descriptions.

## 💾 Data

**Source**: VerSe is built on top of the COCO and TUHOI datasets and uses OntoNotes for sense inventories; sense-specific images for visual sense representations were collected via Bing image search using queries formulated from OntoNotes definitions and examples.

**Size**: 3510 images

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk: depictability annotation used 3 AMT workers per synset (majority label used); sense annotation used 5 AMT workers per image (majority label used). Inter-annotator agreement reported as Fleiss' Kappa: 0.645 for depictability, 0.659 for sense annotation.

## 🔬 Methodology

**Methods**:
- Unsupervised Lesk-based algorithm (variant using vector representations)
- Textual embeddings (word2vec over object labels and image descriptions)
- Visual embeddings (VGG-16 fc7 CNN features)
- Multimodal embeddings (concatenation, Canonical Correlation Analysis (CCA), Deep CCA (DCCA))
- Supervised logistic regression (for comparison)

**Metrics**:
- Accuracy

**Calculation**: Accuracy: proportion (percentage) of images for which the predicted sense equals the gold-standard annotated sense (reported as accuracy scores).

**Interpretation**: Higher accuracy indicates better disambiguation. Performance is compared to baselines: First Sense (FS) heuristic and Most Frequent Sense (MFS) heuristic; MFS is treated as an upper limit for unsupervised approaches.

**Baseline Results**: First Sense heuristic accuracy: 70.8 (motion verbs), 80.6 (non-motion verbs). Most Frequent Sense heuristic accuracy: 86.2 (motion verbs), 90.7 (non-motion verbs).

**Validation**: For CCA/DCCA training, text representations from COCO and Flickr30k and VGG-16 features were split into train/dev/test using an 80/10/10 split. Evaluation of disambiguation methods was performed on the VerSe test data; inter-annotator agreement measured with Fleiss' Kappa for annotation quality.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
