# A Large-scale Dataset of (Open Source) License Text Variants

## 📊 Benchmark Details

**Name**: A Large-scale Dataset of (Open Source) License Text Variants

**Overview**: We introduce a large-scale dataset of the complete texts of free/open source software (FOSS) license variants. The dataset consists of 6.5 million unique license files collected from the Software Heritage archive and includes derived metadata such as file length measures, detected MIME type, detected SPDX license (using ScanCode), example origin, and oldest public commit in which the license appeared.

**Data Type**: text (license text files)

**Domains**:
- Software Engineering
- Legal
- Natural Language Processing

**Similar Benchmarks**:
- Software Heritage (SWH) graph dataset
- World of Code
- GHTorrent
- ScanCode LicenseDB
- SPDX

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.6379164)
- [Resource](https://archive.softwareheritage.org)
- [Resource](https://annex.softwareheritage.org/public/dataset/license-blobs/)
- [Resource](https://docs.softwareheritage.org/devel/swh-graph/api.html#get--graph-randomwalk--src--dst)
- [Resource](https://www.aboutcode.org/projects/scancode.html)
- [Resource](https://scancode-licensedb.aboutcode.org/)
- [Resource](https://spdx.org/license-list)
- [GitHub Repository](https://github.com/OpenSourceOrg/licenses/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale dataset of open source license text variants and associated metadata to support empirical studies on open source licensing, training of automated license classifiers, natural language processing (NLP) analyses of legal texts, and historical/phylogenetic studies on FOSS licensing.

**Target Audience**:
- Empirical Software Engineering researchers
- Natural Language Processing researchers
- Machine Learning practitioners interested in license classification
- Researchers studying software licensing and software provenance

**Tasks**:
- Text Classification
- Text Mining
- Natural Language Processing
- Historical / phylogenetic analysis of texts

**Limitations**: The dataset contains noisy and non-license files by design; origin and earliest metadata are missing for approximately 11–12% of blobs; there is no guarantee that all blobs contain license texts considered open/free by OSI/FSF; license notices embedded only within source files are underrepresented; the dataset is an incomplete snapshot and not fully representative of all existing license variants.

**Out of Scope Uses**:
- Providing the full list of all projects known to ship a given license blob (the dataset provides only a single example origin per blob and obtaining the full list is out of scope).
- Thoroughly extracting license notices that only appear within source files (left as future work).

## 💾 Data

**Source**: Collected from the Software Heritage archive (SWH) using the Software Heritage graph dataset and including origins such as public Git repositories (GitHub, GitLab), FOSS distributions (e.g., Debian), and package manager repositories (e.g., PyPI, NPM).

**Size**: 6,482,295 deduplicated license files (license blobs); primary archive blobs.tar.zst is 14 GiB; additional sample archive blobs-sample20k.tar.zst containing 20,000 license files.

**Format**: License blobs shipped as a sharded tar archive file (blobs.tar.zst) compressed with Zstandard; metadata provided as portable CSV files compressed with Zstandard (CSV files for blobs, fileinfo, scancode, origins, earliest, etc.).

**Annotation**: Automatically mined metadata: MIME type and encoding detected with libmagic (python-magic); line and word counts for text files computed with custom Python code; license detection via ScanCode producing SPDX identifiers and confidence scores (score in [0,100]); origin and earliest-commit metadata obtained via traversal of the Software Heritage graph (randomwalk API and custom graph traversal).

## 🔬 Methodology

**Methods**:
- Automated data retrieval from Software Heritage archive
- Filename-based selection using an SQL regular expression on the SWH graph dataset
- MIME type detection using libmagic
- Line and word counting via custom Python code
- License detection using the ScanCode toolkit (Python API)
- Origin and earliest-commit metadata extraction via Software Heritage graph traversal
- Provision of a replication package to recreate dataset

**Metrics**:
- Counts (number of unique license blobs)
- File size in bytes
- Line count
- Word count
- MIME type distribution (percentages)
- ScanCode license detection score (confidence, range [0,100])
- Occurrences (number of commits containing a blob)
- Earliest commit timestamp (Unix time)

**Calculation**: MIME types and encodings detected via libmagic; for files with text/ and UTF-8 encoding, line and word counts computed using custom Python code; ScanCode run with no minimum score threshold and a 2-minute timeout per blob returning SPDX identifiers and a confidence score in [0,100]; origins via the Software Heritage randomwalk API to select a random origin per blob; earliest commit obtained by traversing the transposed archive graph and selecting the commit with the oldest timestamp; occurrences count equals number of commits referencing the blob in the archive.

**Interpretation**: Higher ScanCode score (closer to 100) indicates higher tool confidence in a license detection; counts and occurrences provide measures of corpus size and relative prevalence but are not direct measures of real-world license popularity (paper explicitly notes that counting variants is not a measure of license popularity); missing origin/earliest metadata (~11–12%) and potential forged timestamps (e.g., UNIX epoch) affect interpretation of provenance and historical metrics.

**Validation**: A replication package is provided to recreate the dataset from Software Heritage; dataset quality and coverage validated via metadata statistics (e.g., MIME type distribution) and manual verification of some noisy classes; paper reports metadata coverage gaps (≈11–12% missing origin/earliest metadata) and discusses limitations and potential mitigations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Transparency**: Uncertain data provenance

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
