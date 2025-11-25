# Visual Semantic Relatedness Dataset for Image Captioning

## 📊 Benchmark Details

**Name**: Visual Semantic Relatedness Dataset for Image Captioning

**Overview**: A textual visual context dataset for captioning, in which the publicly available dataset COCO Captions has been extended with information about the scene (such as objects in the image). The dataset provides textual visual contexts (objects and scenarios) associated with captions to learn semantic similarity/relatedness between text and image context for use in captioning systems (end-to-end or post-processing).

**Data Type**: image-caption pairs with textual visual context (object and scenario labels)

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- COCO Captions
- Visual Genome
- Conceptual Captions 12M
- Novel Object Captioning

**Resources**:
- [GitHub Repository](https://github.com/ahmedssabir/Textual-Visual-Semantic-Dataset)
- [Resource](https://arxiv.org/abs/2301.08784)

## 🎯 Purpose and Intended Users

**Goal**: Provide a combined visual context dataset (visual contexts, caption) to enable learning of textual semantic similarity and relatedness between text and its related visual context from the image, to improve image captioning systems.

**Target Audience**:
- Language and Vision research community

**Tasks**:
- Image Captioning
- Semantic Similarity (visual context to caption)
- Caption Re-ranking
- Image Retrieval

**Limitations**: Visual classifier struggles with complex backgrounds (wrong visual, object hallucination). Low/high cosine relatedness scores can lead to wrong annotations. Sensitive to out-of-vocabulary queries. Relies on quality of visual classiﬁers and caption generators.

## 💾 Data

**Source**: Based on the COCO Captions dataset; extended using out-of-the-box visual classifiers (ResNet-152, CLIP, Inception-Resnet Faster R-CNN) to extract textual visual context (top-3 object classes and scenarios) per image, filtered by confidence and semantic alignment using Sentence RoBERTa.

**Size**: COCO-visual: 413,915 captions for training and 87,721 captions for validation; COCO-overlapping: 71,540 overlap annotated captions; 45,000 captions generated for testing (VilBERT on Karpathy 5K test split).

**Format**: N/A

**Annotation**: Automatically generated via pre-trained visual classifiers extracting top-3 object classes per image, filtered by classifier confidence threshold (<0.2), semantic alignment (remove duplicated objects), and a semantic relatedness soft-label computed with Sentence RoBERTa cosine similarity with thresholding to produce final labels.

## 🔬 Methodology

**Methods**:
- Automated metrics (COCO offline evaluation suite)
- Human evaluation (small-scale user study)
- Similarity-based re-ranking using fine-tuned BERT and BERT-CNN
- k-Nearest Neighbor retrieval with FAISS

**Metrics**:
- BLEU (BLEU-4)
- METEOR
- ROUGE
- CIDEr
- SPICE
- BERTScore
- Div-1 (unique unigram ratio)
- Div-2 (unique bigram ratio)
- mBLEU (BLEU between candidate and human captions)
- Unique words per caption
- SBERT-sts (sentence-level SBERT similarity)

**Calculation**: Evaluation uses the official COCO offline evaluation suite to produce BLEU, METEOR, ROUGE, CIDEr and SPICE. BERTScore (B-S) is used for semantic-similarity based evaluation. Div-1 and Div-2 are computed as the ratio of unique unigram/bigram to number of words in the caption. mBLEU is BLEU between candidate caption and all human captions. SBERT-sts uses Sentence-BERT cosine similarity as a sentence-level score.

**Interpretation**: Lower mBLEU indicates more diverse captions. SBERT-sts correlates more with human judgments than BERTScore. The paper reports improvement across automatic metrics using BERT-based re-rankers except for BLEU and SPICE in some comparisons.

**Baseline Results**: Baseline VilBERT (Karpathy test split): BLEU-4 0.330, METEOR 0.272, ROUGE 0.554, CIDEr 1.104, SPICE 0.207, BERTScore 0.9352. Best reported re-ranker (BERT-CNN th>=0.3) example: BLEU-4 0.352, METEOR 0.275, ROUGE 0.560, CIDEr 1.131, SPICE 0.208, BERTScore 0.9366.

**Validation**: Validated on the Karpathy test split. Small-scale human evaluation: 19 test images with 12 human subjects asked to choose between baseline and similarity-based visual re-ranker captions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: Contains gender bias analysis: frequency count of object + gender in the training dataset, computation of men/women ratios, and experiments replacing gendered terms with gender-neutral terms to study effects on accuracy.

**Potential Harm**: ['Gender bias in image captioning (bias towards men in COCO and propagated in the dataset)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
