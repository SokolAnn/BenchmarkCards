# text2fabric

## 📊 Benchmark Details

**Name**: text2fabric

**Overview**: We introduce text2fabric, a novel dataset that links free-text descriptions to various fabric materials. The dataset comprises 15,461 natural language descriptions associated to 3,000 corresponding images (45,000 rendered images in total when including variations) of fabric materials, and is used to analyze how people describe fabric appearance and to fine-tune vision-language models for tasks such as fine-grained retrieval and captioning.

**Data Type**: image-caption pairs (rendered fabric images and free-text descriptions)

**Domains**:
- Computer Vision
- Computer Graphics
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Describable Textures Dataset (DTD)
- Describable Textures in Detail Dataset (DTD2)
- LAION

**Resources**:
- [Resource](https://valentin.deschaintre.fr/text2fabric)
- [GitHub Repository](https://github.com/commonsense/conceptnet-numberbatch)
- [Resource](https://substance3d.adobe.com/assets/allassets?assetType=substanceMaterial&category=Fabric)
- [Resource](https://stock.adobe.com/)

## 🎯 Purpose and Intended Users

**Goal**: Relate high-quality renderings of fabric materials to natural language descriptions to analyze the visual language used for fabric appearance and to improve vision-language models for fabric-specific tasks such as fine-grained retrieval, image-based search, and caption generation.

**Target Audience**:
- ML Researchers
- Computer Vision Researchers
- Computer Graphics Researchers
- Model Developers

**Tasks**:
- Fine-Grained Text-based Retrieval
- Image-based Retrieval
- Image Captioning
- Keyword Extraction

**Limitations**: Dataset stimuli are specific to the selected rendered fabrics and may not generalize to all real-world fabrics; some attributes (e.g., military and weathering) are correlated in the dataset; describers were selected as non-expert but familiar with fashion/design which may introduce bias or inaccuracies; dataset uses rendered images rather than photographs which may limit some applications; models struggle with negative queries and extremely intricate patterns.

**Out of Scope Uses**:
- Material generation (stated as out of scope for this study)

## 💾 Data

**Source**: Rendered images generated with Substance Stager from 3,000 fabric materials obtained from Substance 3D Assets (procedural materials and high-quality scans); natural language descriptions collected via crowdsourcing from qualified describers.

**Size**: 45,000 images; 15,461 valid descriptions; 3,000 distinct fabric materials (dataset also reports 3,706 invalid descriptions rejected, 19.3% rejection rate).

**Format**: Rendered images at 4K resolution; natural language descriptions as plain text. Exact file download format not specified in the paper.

**Annotation**: Manual crowdsourced free-text descriptions collected from qualified participants (native English speakers with normal color vision and familiarity with fashion/design). Participants underwent training and a qualification test; each image has at least five valid descriptions. Descriptions were manually audited (accepted/rejected with reasons) and rated on a 5-point quality scale; post-processing included spell checking, non-alphabetic character removal, stop-word filtering, tokenization and lemmatization.

## 🔬 Methodology

**Methods**:
- Crowdsourced human annotation
- Fine-tuning of pre-trained vision-language models (CLIP ViT-B/16, BLIP ViT-B)
- Automated evaluation (retrieval over material database, embedding similarity)
- Statistical analysis (Kruskal-Wallis test, ANOSIM, Wilcoxon signed-rank test)

**Metrics**:
- Top-K Recall (Top-1, Top-5, Top-10, Top-20, Top-100)
- Cosine Similarity (between normalized embeddings)
- Precision
- Average similarity (mean ± standard deviation)
- ANOSIM test statistic and p-value
- Kruskal-Wallis test statistic and p-value
- Wilcoxon signed-rank test and p-value
- 5-point human quality rating

**Calculation**: Cosine similarity is computed between normalized image/text embeddings. Top-K recall is computed as the fraction of test queries for which the correct material appears in the top K retrieved items across the full database of 3,000 materials. Intra-image and inter-image similarities are averaged pairwise cosine similarities over description embeddings. Statistical significance is assessed with ANOSIM for similarity comparisons, Kruskal-Wallis for attribute rank differences, and Wilcoxon signed-rank for paired representation comparisons.

**Interpretation**: Higher Top-K recall indicates better retrieval performance. Higher intra-image similarity relative to inter-image similarity indicates that the same fabric elicits more similar descriptions. Higher cosine similarity between images of the same material across geometries/illuminations indicates greater invariance of the learned representation. p-values from statistical tests indicate significance (paper uses p<0.05 as significance threshold).

**Baseline Results**: Text-based retrieval (baseline geometry): Native CLIP Top-1 2.94%, Top-5 8.31%, Top-10 12.59%, Top-20 18.37%, Top-100 41.29%. Native BLIP Top-1 3.42%, Top-5 9.94%, Top-10 14.60%, Top-20 20.17%, Top-100 34.26%. BLIP (no pretrain) Top-1 1.60%, Top-5 5.98%, Top-10 10.64%, Top-20 17.00%, Top-100 34.36%. Fine-tuned CLIP (Ours) Top-1 13.81%, Top-5 33.91%, Top-10 46.76%, Top-20 59.76%, Top-100 87.63%. Unseen geometry (plane_draped) Top-1: Native CLIP 1.34%, Native BLIP 2.27%, Ours (1 geometry) 5.98%, Ours (4 geometries) 7.38%. Representation invariance (average cosine similarities): Ours (varying geometry) 0.951±0.012 vs Native CLIP 0.835±0.042; Ours (varying lighting) 0.973±0.007 vs Native CLIP 0.945±0.011.

**Validation**: Data validation: manual auditing of descriptions (accept/reject and 5-point rating), qualification test for annotators, ensured at least five valid descriptions per image, rejected describers with high rejection rates (>35%). Model validation: dataset split into training and test (12,334 training and 3,129 test descriptions for retrieval experiments), ensured that procedural variations of a given material in training are not used for testing; test-time retrieval performed on materials unseen during training; statistical tests used to confirm significance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: 122 describers (ages 18 through 65); 45% identified as female, 12.3% as male, none as other gender identities, 42.7% preferred not to reply. All describers were required to be native English speakers, have normal color vision, and be familiar with fashion or design.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
