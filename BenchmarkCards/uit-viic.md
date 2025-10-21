# UIT-ViIC

## 📊 Benchmark Details

**Name**: UIT-ViIC

**Overview**: We first build a dataset which contains manually written captions for images from Microsoft COCO dataset relating to sports played with balls, we called this dataset UIT-ViIC. UIT-ViIC consists of 19,250 Vietnamese captions for 3,850 images.

**Data Type**: image-caption pairs

**Domains**:
- Computer Vision
- Natural Language Processing
- Machine Learning

**Languages**:
- Vietnamese

**Similar Benchmarks**:
- Microsoft COCO (MS-COCO)
- Flickr30k
- Flickr8k
- COCO-CN
- STAIR Captions
- Flickr30k-CN
- Flickr8k-CN
- Multi30k
- YJ Captions
- AIC-ICC
- IAPR TC-12
- Pascal sentences
- Bilingual caption
- COCO 4K

**Resources**:
- [Resource](https://sites.google.com/uit.edu.vn/uit-nlp/)
- [Resource](https://arxiv.org/abs/2002.00175)
- [GitHub Repository](https://github.com/oarriaga/neural_image_captioning)
- [GitHub Repository](https://github.com/trungtv/pyvi)
- [GitHub Repository](https://github.com/pytorch/pytorch)

## 🎯 Purpose and Intended Users

**Goal**: Introduce UIT-ViIC, the first Vietnamese image captioning dataset (extending MS-COCO) and evaluate state-of-the-art image captioning models on it.

**Target Audience**:
- Image Captioning research community
- Researchers in Computer Vision
- Researchers in Natural Language Processing
- Researchers in Machine Learning

**Tasks**:
- Image Captioning

**Limitations**: Dataset restricted to sportball category (3,850 images) and constructed by five annotators; category and dataset size are limited as stated by the authors.

## 💾 Data

**Source**: Images from Microsoft COCO (MS-COCO) (sportball category, 2017 edition); captions manually written by Vietnamese annotators.

**Size**: 3,850 images; 19,250 captions

**Format**: N/A

**Annotation**: Manual annotation by five native Vietnamese annotators (five captions per image) using a web-based annotation tool with content suggestions and annotation guidelines.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (training and evaluating neural image captioning models: NIC - Show and Tell; PyTorch-tutorial model)
- Automated metrics

**Metrics**:
- BLEU (BLEU-1 to BLEU-4)
- ROUGE-L
- CIDEr-D

**Calculation**: BLEU computed for n-grams 1 to 4; ROUGE-L and CIDEr-D computed as defined in the cited metric papers (BLEU [15], ROUGE [11], CIDEr [20]).

**Interpretation**: Higher metric scores indicate better match to reference captions; authors report that English-sportball outperforms Vietnamese sets on BLEU-1, whereas UIT-ViIC outperforms on BLEU-2 to BLEU-4 and CIDEr-D.

**Baseline Results**: Pytorch-tutorial model on UIT-ViIC: BLEU-1 0.710, BLEU-2 0.575, BLEU-3 0.476, BLEU-4 0.394, ROUGE-L 0.626, CIDEr-D 1.005. NIC - Show and Tell on UIT-ViIC: BLEU-1 0.682, BLEU-2 0.561, BLEU-3 0.411, BLEU-4 0.327, ROUGE-L 0.599, CIDEr-D 0.818. (Additional results for English-sportball and GT-sportball are reported in Tables 3 and 4 of the paper.)

**Validation**: Dataset split: 2,695 images for training, 924 images for validation, 231 images for test. Models validated using the 924-image validation set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
