# VIST-Character dataset

## 📊 Benchmark Details

**Name**: VIST-Character dataset

**Overview**: The VIST-Character dataset augments the test set of VIST (the Visual Storytelling dataset) with rich character-centric annotations, including visual and textual co-reference chains and importance ratings for characters. Based on this dataset the authors propose two new tasks: important character detection and character grounding in visual stories.

**Data Type**: multimodal (image sequences and associated story text; bounding boxes, textual and visual co-reference chains, and importance ratings)

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- VIST (Visual Storytelling)
- MPII-MD Co-ref+Gender
- M-VAD Names
- ActivityNet Captions
- Montreal Video Annotation Dataset

**Resources**:
- [Resource](https://labelstud.io/)
- [Resource](https://arxiv.org/abs/2303.17647)

## 🎯 Purpose and Intended Users

**Goal**: Provide character-centric annotations (textual and visual co-reference chains and importance ratings) for visual stories and define two tasks: important character detection and character grounding in visual stories, to enable character-centric story analysis and generation.

**Target Audience**:
- Researchers in Visual Storytelling
- Researchers in Natural Language Processing
- Researchers in Computer Vision
- Model developers working on character-centric story understanding and generation

**Tasks**:
- Important Character Detection
- Character Grounding (visual grounding of textual character mentions)
- Character Detection
- Co-reference Resolution
- Importance Ranking
- Bounding Box Annotation / Detection

**Limitations**: Dataset augments only the test set of VIST and contains 770 selected visual stories; stories with no characters in images were excluded. Fifty stories were quadruple-annotated and the rest single-annotated. The authors note that character grounding is sensitive to errors in earlier components (detection and co-reference) and that the image sequences contain redundant/background characters which reduce image-based precision.

## 💾 Data

**Source**: Selected from the VIST test set (Huang et al. 2016); augmented with character-centric annotations (textual mentions marked, bounding boxes on images, co-reference chains, and importance ratings).

**Size**: 770 visual stories; 3,119 characters; 768 plural and group characters; 4,979 bounding boxes; average 6.47 bounding boxes per story; average 4.05 characters per story.

**Format**: N/A

**Annotation**: Annotation involved: (1) marking words that refer to the same characters in story sentences, (2) drawing bounding boxes around the whole body of individual characters in images (special rules for plural/group characters), and (3) rating the importance of each character on a 1–5 star scale. An annotation interface based on LabelStudio was used. The authors quadruple-annotated fifty stories; the rest of the dataset was single-annotated. Four annotators with linguistic and NLP backgrounds were trained using the annotation instructions; one author's annotation was used as ground truth for some inter-annotator agreement calculations.

## 🔬 Methodology

**Methods**:
- Automated evaluation using Precision and Recall
- B-Cubed precision and recall for co-reference evaluation
- Exact match for co-reference chains
- Precision@k for importance ranking
- IoU-based bounding box evaluation (IoU > 60% considered correct)
- Baseline unsupervised models: distributional similarity-based alignment and CLIP-based alignment
- Use of pre-trained components: spaCy PoS tagger, WordNet hypernyms, NeuralCoref, SpanBERT, MTCNN, Inception ResNet pretrained on VGGFace2, CLIP, k-means clustering, and the Kuhn–Munkres (Hungarian) algorithm

**Metrics**:
- Precision
- Recall
- B-Cubed Precision
- B-Cubed Recall
- Exact Match Precision
- Exact Match Recall
- Precision@k (Precision@1, Precision@3, Precision@5)
- Intersection over Union (IoU)
- Pearson's Correlation

**Calculation**: Textual character detection: a predicted character phrase is correct when the head word of the noun phrase matches the gold-standard. Visual character detection: a predicted face region is correct when the face bounding box is entirely inside the annotated body bounding box. A bounding box is considered correct if IoU with gold bounding box is > 60%. B-Cubed measures the proportion of correctly predicted mentions in a co-reference chain. Exact match requires the predicted co-reference chain to be equivalent to the gold-standard chain. For CLIP-based chain similarity, the average CLIP similarity between each pair of textual mention and visual appearance in the two chains is used. For distributional similarity, C-dimensional binary vectors indicate presence per sentence/image and cosine or dot-product based similarity is used to populate the chain-to-chain similarity matrix; Hungarian algorithm applied to obtain matchings.

**Interpretation**: For grounding, recall is preferred to precision because visual character detection returns redundant/background characters that depress precision. Higher B-Cubed than exact match indicates mentions are detected but whole chains are difficult to recover exactly. Gold-standard inputs show substantially higher alignment performance, indicating sensitivity to upstream errors (detection and co-reference).

**Baseline Results**: Inter-annotator agreement (on 50 double annotations): Character Detection Precision 76.4%, Recall 71.5%; Co-reference (B-Cubed) Precision 82.0%, Recall 79.4%; Co-reference (Exact Match) Precision 63.2%, Recall 58.1%; Bounding Boxes Precision 67.8%, Recall 58.6%; Importance Ranking Recall 73.0%. Character detection results on VIST-Character: Textual Story Precision 74.4%, Recall 90.3%; Image Sequence Precision 40.5%, Recall 69.1%. Character co-reference: NeuralCoref (B-Cubed P 70.2% R 66.6%; Exact P 29.2% R 32.4%), SpanBERT (B-Cubed P 66.6% R 70.0%; Exact P 30.0% R 33.2%), ResNet visual (B-Cubed P 57.0% R 60.5%; Exact P 10.7% R 17.5%), CLIP visual (B-Cubed P 51.8% R 60.8%; Exact P 25.8% R 23.8%). Character grounding (alignment) on predictions: Distribution-based Recall 27.3% Precision 27.5%; CLIP-based Recall 21.7% Precision 28.5%. With gold-standard input: Distribution-based Recall 77.5%; CLIP-based Recall 58.5%. Importance ranking (Precision@k): Text-only P@1 53.6%, P@3 79.2%, P@5 87.4%; Image-only P@1 30.0%, P@3 30.8%, P@5 31.3%; Multi-modal P@1 29.4%, P@3 34.7%, P@5 34.3%. Pearson's correlation between occurrence count and importance rating: Textual Stories 0.61, Visual Stories 0.55, Multi-modal Stories 0.62.

**Validation**: Annotation validation: four annotators trained and inter-annotator agreement computed on fifty double-annotated stories; one author's annotation used as ground truth to compute precision and recall of other annotators. Experimental validation: comparison of model results on predicted inputs and on gold-standard inputs to estimate upper bounds and sensitivity to upstream errors.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state they augment the public VIST test set which 'does not contain sensitive information'. They obtained research ethical approval from their institute. Annotators were recruited, trained, asked to filter out samples that might cause ethical problems, and were paid during training and annotation.

**Data Licensing**: The authors state they will make the dataset and the codebase freely available online for academic use without copyright restrictions.

**Consent Procedures**: Research ethical approval was obtained; four annotators with linguistic and NLP backgrounds were recruited and trained and were paid. No additional consent procedures are specified in the paper.

**Compliance With Regulations**: Research ethical approval from the authors' institute is reported. No explicit mention of compliance with external regulations (e.g., GDPR, CCPA) is provided.
