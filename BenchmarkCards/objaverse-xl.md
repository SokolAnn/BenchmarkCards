# Objaverse-XL

## 📊 Benchmark Details

**Name**: Objaverse-XL

**Overview**: Objaverse-XL is a large-scale, web-crawled dataset of 3D assets comprising over 10 million deduplicated 3D objects from diverse sources (manually designed objects, photogrammetry scans, professional scans, etc.). It is released to enable large-scale training and improved generalization for 3D vision tasks; the paper demonstrates improvements on novel view synthesis and other 3D tasks when models are pretrained on Objaverse-XL.

**Data Type**: 3D object files and rendered multi-view images (renders of each 3D object)

**Domains**:
- Computer Vision
- Computer Graphics
- Augmented Reality
- Generative AI

**Similar Benchmarks**:
- Objaverse 1.0
- ShapeNet
- ABO
- GSO
- OmniObject3D
- PhotoShape
- Thingi10K
- 3d-Future
- IKEA
- EGAD

**Resources**:
- [Resource](https://arxiv.org/abs/2307.05663)

## 🎯 Purpose and Intended Users

**Goal**: Provide a massive, diverse corpus of 3D objects (10.2M) to enable large-scale pretraining and advance research and applications in 3D vision, including improved zero-shot novel view synthesis and other 3D generative and discriminative tasks.

**Target Audience**:
- Machine Learning Researchers
- Computer Vision Researchers
- Model Developers
- Computer Graphics and Augmented Reality practitioners

**Tasks**:
- Novel View Synthesis
- 3D Reconstruction
- 3D Object Generation / Text-to-3D
- Representation Learning / Pretraining
- 3D Segmentation
- 3D Detection
- 2D Vision tasks (e.g., segmentation) using renders

**Limitations**: Objaverse-XL, while an order of magnitude larger than Objaverse 1.0, is still orders of magnitude smaller than billion-scale image-text datasets. Not all samples may be necessary to train high-performance models. The dataset is primarily released for generative tasks in this paper; benefits to discriminative tasks (e.g., 3D segmentation and detection) are left for future work.

## 💾 Data

**Source**: Web-crawled from multiple sources including GitHub, Thingiverse, Sketchfab (Objaverse 1.0 subset), Polycam (savable objects marked CC-BY 4.0), and the Smithsonian Institution (CC0 models).

**Size**: 10.2 million 3D objects (rendered successfully); original crawl indexed ~37M GitHub files, ~3.5M Thingiverse objects, 800K Sketchfab (Objaverse 1.0), 72K Polycam, 2.4K Smithsonian models; deduplication removed ~23M files.

**Format**: Various 3D file formats including .obj, .glb, .gltf, .usdz, .usd, .usda, .fbx, .stl, .dae, .ply, .abc, .blend; rendered multi-view images (12 renders per object) generated via Blender.

**Annotation**: No manual task labels. Provided metadata and automated annotations: source metadata (e.g., popularity, license, textual description), Blender-extracted metadata (sha256, file-size, polygon-count, vertex-count, edge-count, material-count, texture-count, object-count, animation-count, linked-files, scene-dimensions, missing-textures), CLIP ViT-L/14 image embeddings and derived predictions (aesthetic scores, NSFW predictions, face detection, hole detection), LAION-Aesthetics V2 tiers, and NSFW/face/bad-render automated labels (classifier-based).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (pretraining and fine-tuning models on Objaverse-XL)
- Zero-shot evaluation
- Controlled dataset-scaling experiments
- Automated classification (NSFW, face detection, bad-render classifier)

**Metrics**:
- Peak Signal-to-Noise Ratio (PSNR)
- Structural Similarity Index Measure (SSIM)
- Learned Perceptual Image Patch Similarity (LPIPS)
- Fréchet Inception Distance (FID)
- Cross-validation accuracy (for bad-render classifier)
- rvisual similarity score (as referenced for visual similarity)

**Calculation**: PSNR, SSIM, LPIPS, and FID are computed between predicted novel views and ground-truth views. In Figure 6 LPIPS values were multiplied by 10 for visualization. The bad-render classifier (2-layer MLP on CLIP ViT-L/14 features) reports cross-validation accuracy (>90%).

**Interpretation**: Higher PSNR and SSIM indicate better novel view synthesis quality; lower LPIPS and FID indicate better perceptual similarity and distributional match (the paper denotes PSNR (↑), SSIM (↑), LPIPS (↓), FID (↓) in tables).

**Baseline Results**: Zero123-XL (Table 2): Base PSNR 18.225, SSIM 0.877, LPIPS 0.088, FID 0.070; with alignment finetuning PSNR 19.876, SSIM 0.888, LPIPS 0.075, FID 0.056. PixelNeRF (Table 3): Base PSNR on DTU 15.32 and ShapeNet 22.71; w/ Objaverse-XL PSNR on DTU 17.53±0.37 and ShapeNet 24.22±0.55.

**Validation**: Evaluations include zero-shot evaluation on Google Scanned Objects, held-out subset evaluations of Objaverse-XL for PixelNeRF, and cross-validation (>90% accuracy) for the bad-render classifier trained on annotated Polycam renders.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Intellectual Property
- Data Laws
- Accuracy
- Robustness
- Misuse
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data, Reidentification
- **Intellectual Property**: Data usage rights restrictions, Confidential information in data
- **Data Laws**: Data usage restrictions, Data acquisition restrictions
- **Accuracy**: Data contamination
- **Robustness**: Data poisoning
- **Misuse**: Nonconsensual use
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Face detection analysis: estimated 266K objects include faces (≈2.5% of assets); faces often come from scans of dolls, historical sculptures, and anthropomorphic animations.

**Potential Harm**: ['Presence of NSFW content (identified and filtered using an automated classifier; 815 objects filtered out)', 'Potential reidentification of scanned individuals (possible visual identification if a scanned person is included or if names appear in metadata)', 'License and usage-related harms if downstream users do not follow the original object licenses']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: NSFW filtering applied on rendered images using a CLIP ViT-L/14-based NSFW classifier (render marked NSFW if ≥3 renders >0.9 score). Face detection applied (objects with ≥3 renders containing detected face counted). Authors note that faces are mostly from dolls, sculptures, and animations and that privacy concerns are limited but possible. Users may contact curators to request blacklisting of specific samples.

**Data Licensing**: The dataset as a whole will be distributed under the ODC-By 1.0 license. Individual objects retain their source licenses (examples: Thingiverse objects predominantly Creative Commons licenses, Polycam savable objects CC-BY 4.0, Smithsonian models CC0). Users must follow the licenses of individual objects and platform terms of service.

**Consent Procedures**: Individuals whose data may have been included were not notified about the collection and consent was not obtained (explicitly stated).

**Compliance With Regulations**: Not Applicable
