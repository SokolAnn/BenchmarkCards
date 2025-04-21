HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="BenchmarkCards">
    <title>BenchmarkCards</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Dark mode theming */
        :root {
            /* Monochrome palette - Light Mode */
            --black: #000000;
            --dark-gray: #333333;
            --medium-gray: #666666;
            --light-gray: #e5e5e5;
            --off-white: #f8f8f8;
            --white: #ffffff;

            /* Spacing */
            --space-xs: 0.5rem; /* This is 8px */
            --space-sm: 1rem;   /* This is 16px */
            --space-md: 1.5rem; /* This is 24px */
            --space-lg: 2rem;   /* This is 32px */
            --space-xl: 3rem;   /* This is 48px */

            /* Transitions */
            --transition-fast: 0.15s ease;
            --transition-normal: 0.3s ease;

            /* Shadows */
            --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.05);
            --shadow-md: 0 8px 20px rgba(0, 0, 0, 0.08);
            --shadow-lg: 0 12px 28px rgba(0, 0, 0, 0.12);

            /* Typography */
            --font-serif: 'Georgia', 'Times New Roman', Times, serif;
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

            /* Element colors */
            --body-bg: var(--white);
            --body-text: var(--black);
            --header-bg: var(--white);
            --card-bg: var(--white);
            --card-border: var(--black);
            --pre-bg: var(--off-white);
        }

        /* Dark mode colors */
        [data-theme="dark"] {
            --body-bg: #121212;
            --body-text: #e0e0e0;
            --header-bg: #121212;
            --card-bg: #1e1e1e;
            --card-border: #ffffff;
            --pre-bg: #262626;

            /* Redefine colors for dark mode */
            --black: #ffffff;
            --dark-gray: #cccccc;
            --medium-gray: #999999;
            --light-gray: #333333;
            --off-white: #1e1e1e;
            --white: #121212;
        }

        /* Base styles */
        body {
            padding: 0;
            margin: 0;
            background-color: var(--body-bg);
            font-family: var(--font-sans);
            color: var(--body-text);
            min-height: 100vh;
            line-height: 1.6;
            transition: background-color var(--transition-normal), color var(--transition-normal);
        }

        /* Focus styles for better accessibility */
        *:focus-visible {
            outline: 2px solid var(--black);
            outline-offset: 3px;
        }

        /* Layout containers */
        .main-content {
            max-width: 1000px; /* Increased max-width for a wider layout */
            margin: 0 auto;
            padding: var(--space-md);
            display: flex;
            flex-direction: column;
            gap: var(--space-lg);
        }

        /* Navigation and header styles */
        .site-header {
            background-color: var(--header-bg);
            padding-top: var(--space-md);
            transition: background-color var(--transition-normal);
        }

        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: var(--space-sm);
        }

        .site-title {
            font-family: var(--font-serif);
            font-size: 2rem;
            font-weight: 700;
            color: var(--black);
            margin: 0;
            letter-spacing: -0.5px;
            transition: color var(--transition-normal);
        }

        .main-nav {
            display: flex;
            align-items: center;
             /* Removed flex-grow, justify-content */
        }

        .nav-links {
            display: flex;
            list-style: none;
            margin: 0;
            padding: 0;
            gap: var(--space-md);
            align-items: center;
        }

        .nav-links a {
            color: var(--medium-gray);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            letter-spacing: 0.3px;
            transition: color var(--transition-fast);
            padding: var(--space-xs) 0;
            position: relative;
        }

        .nav-links a:hover,
        .nav-links a:focus {
            color: var(--black);
        }

        .nav-links a.active {
            color: var(--black);
        }

        .paper-link {
            font-style: italic;
        }

        /* Theme toggle button */
        .theme-toggle {
            background: none;
            border: none;
            color: var(--medium-gray);
            cursor: pointer;
            font-size: 1rem;
            padding: var(--space-xs);
            transition: color var(--transition-fast);
             margin-left: var(--space-md); /* Increased space */
        }

        .theme-toggle:hover {
            color: var(--black);
        }

        /* Header border */
        .header-border {
            height: 1px;
            background-color: var(--black);
            margin: 0;
        }

        /* Card component */
        .card {
            border: none;
            border-radius: 0;
            box-shadow: none;
            border: 1px solid var(--card-border);
            transition: all var(--transition-normal);
            overflow: hidden;
            background-color: var(--card-bg);
        }

        .card:hover {
            box-shadow: var(--shadow-sm);
        }

        .card-header {
            background-color: var(--card-bg);
            border-bottom: 1px solid var(--card-border);
            padding: var(--space-md);
            font-family: var(--font-serif);
            font-weight: 600;
            font-size: 1.2rem;
            color: var(--black);
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: background-color var(--transition-normal), color var(--transition-normal);
             flex-wrap: wrap; /* Allow wrapping items */
             gap: var(--space-sm); /* Add space between items */
        }
        .card-header > span {
            flex-grow: 1; /* Allow title to take up space */
        }
         .card-header .btn-group {
            flex-shrink: 0; /* Prevent buttons from shrinking */
         }


        .card-body {
            padding: var(--space-lg);
            transition: background-color var(--transition-normal);
            background-color: var(--card-bg);
        }
         .card-body pre {
             /* Styles for both JSON and Markdown pre tags */
             white-space: pre-wrap; /* Wrap long lines in pre tags */
             word-break: break-word; /* Break words if necessary */
             padding: var(--space-md); /* Add padding inside pre */
             background-color: var(--pre-bg);
             font-family: 'Menlo', 'Consolas', monospace;
             font-size: 0.9rem;
             line-height: 1.6;
             border: 1px solid var(--card-border);
             transition: background-color var(--transition-normal), border-color var(--transition-normal);
             overflow-x: auto; /* Add horizontal scroll if needed */
         }


        /* Upload area component */
        .upload-area {
            border: 1px dashed var(--card-border);
            border-radius: 4px;
            padding: var(--space-xl) var(--space-lg);
            text-align: center;
            transition: all var(--transition-normal);
            background: var(--card-bg);
            margin-bottom: var(--space-lg);
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
        }

        .upload-area:focus {
            outline: none;
            border-color: var(--black);
            box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.1);
        }

        .upload-area.dragover {
            border-color: var(--black);
            background-color: var(--off-white);
        }

        .upload-icon {
            font-size: 2.5rem;
            color: var(--medium-gray);
            margin-bottom: var(--space-md);
            transition: color var(--transition-normal);
        }

        .upload-area:hover .upload-icon {
            color: var(--black);
        }

        .upload-text {
            font-family: var(--font-sans);
            font-size: 1.1rem;
            font-weight: 500;
            margin-bottom: var(--space-xs);
            color: var(--black);
        }

        .upload-hint {
            font-size: 0.9rem;
            color: var(--medium-gray);
            margin-bottom: var(--space-sm);
        }

        .upload-description {
            font-size: 0.85rem;
            color: var(--medium-gray);
            margin-top: var(--space-sm);
            opacity: 0.8;
        }

        #fileInput {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            border: 0;
        }

        /* Button styles */
        .btn {
            border-radius: 4px;
            font-weight: 600;
            padding: 0.7rem 1.5rem;
            transition: all var(--transition-normal);
            text-transform: uppercase;
            position: relative;
            letter-spacing: 0.5px;
            font-size: 0.85rem;
             text-decoration: none; /* Remove underline from link buttons */
             display: inline-flex; /* Make links behave like buttons */
             align-items: center;
             justify-content: center;
             cursor: pointer;
        }
         .btn-sm { /* Bootstrap small button style - not currently used */
             padding: 0.25rem 0.5rem;
             font-size: 0.875rem;
             border-radius: 0.2rem;
         }

        /* --- PRIMARY BUTTON STYLE (Solid Black/White) --- */
        .btn-primary {
            background-color: var(--black); /* Solid fill */
            border-color: var(--black); /* Border matches fill */
            color: var(--white); /* Text color */
        }

        .btn-primary:hover, .btn-primary:focus {
            background-color: var(--dark-gray); /* Darker on hover */
            border-color: var(--dark-gray);
            color: var(--white);
        }
         [data-theme="dark"] .btn-primary {
             background-color: var(--white); /* Solid fill in dark mode */
             border-color: var(--white); /* Border matches fill */
             color: var(--black); /* Text color in dark mode */
         }
         [data-theme="dark"] .btn-primary:hover, [data-theme="dark"] .btn-primary:focus {
             background-color: var(--light-gray); /* Lighter on hover in dark mode */
             border-color: var(--light-gray);
             color: var(--black);
         }


        /* --- OUTLINE PRIMARY BUTTON STYLE (Outline Black/White) --- */
        .btn-outline-primary { /* Style for outline buttons added */
            background-color: transparent; /* No fill */
            border-color: var(--black); /* Outline color */
            color: var(--black); /* Text color matches outline */
        }

        .btn-outline-primary:hover, .btn-outline-primary:focus {
             background-color: var(--off-white); /* Slight fill on hover */
             border-color: var(--black);
             color: var(--black);
        }
        [data-theme="dark"] .btn-outline-primary {
             background-color: transparent;
             border-color: var(--white); /* Outline color in dark mode */
             color: var(--white); /* Text color matches outline in dark mode */
         }
         [data-theme="dark"] .btn-outline-primary:hover, [data-theme="dark"] .btn-outline-primary:focus {
             background-color: var(--off-white); /* Slight fill on hover in dark mode */
             border-color: var(--white);
             color: var(--white);
         }


        .btn-success { /* Keeping success style as is */
            background-color: var(--white);
            border-color: var(--black);
            color: var(--black);
        }

        .btn-success:hover, .btn-success:focus {
            background-color: var(--off-white);
            border-color: var(--black);
            color: var(--black);
        }

        .btn-icon {
            /* Already has display: inline-flex and align-items: center, justify-content: center from .btn */
        }

        /* Download button */
        .download-btn {
             /* Download buttons now use btn styles, removing redundancy */
             /* Kept for structure, but main styling inherited from .btn */
        }

        /* Loader animation */
        .loader-container {
            display: none;
            text-align: center;
            padding: var(--space-lg);
        }

        .progress-container {
            width: 100%;
            max-width: 300px;
            margin: var(--space-lg) auto;
            position: relative;
        }

        .progress-bar {
            width: 100%;
            height: 1px;
            background-color: var(--light-gray);
            overflow: hidden;
            position: relative;
        }

        .progress-value {
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            background: var(--black);
            width: 10%;
            animation: indeterminateProgress 1.5s infinite ease-in-out;
        }

        @keyframes indeterminateProgress {
            0% {
                left: -35%;
                width: 30%;
            }
            60% {
                left: 100%;
                width: 30%;
            }
            100% {
                left: 100%;
                width: 0;
            }
        }

        .progress-text {
            font-size: 1rem;
            color: var(--medium-gray);
            margin-top: var(--space-sm);
            font-family: var(--font-serif);
            font-style: italic;
        }

        /* Result styles */
        #resultContainer {
            display: none;
        }

        /* Hide default result pre tag */
        #result {
             display: none;
        }

         /* Add margin between the view buttons within the group */
        .btn-group .btn:first-child { /* Add margin to the first button in the group */
             margin-right: var(--space-xs);
        }


        /* JSON syntax highlighting - REMOVED as requested */
        /*
        .json-key { color: var(--black); font-weight: 700; }
        .json-string { color: var(--dark-gray); }
        .json-number { color: var(--black); font-weight: 500; }
        .json-boolean { color: var(--black); font-style: italic; }
        .json-null { color: var(--medium-gray); font-style: italic; }
        */

        section#resultContainer .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Responsive adjustments */
        @media (max-width: 767px) {
            .site-header {
                padding: var(--space-lg) 0;
            }

            .site-header h1 {
                font-size: 2rem;
            }

            .card-body {
                padding: var(--space-md);
            }

            .upload-area {
                padding: var(--space-lg);
            }

            .btn {
                width: 100%;
                margin-bottom: var(--space-sm);
            }

             /* Adjust header layout on small screens */
             .top-bar {
                 flex-direction: column;
                 align-items: stretch;
             }
             .site-title {
                 text-align: center;
                 margin-bottom: var(--space-sm);
             }
             .main-nav {
                 flex-direction: column;
                 align-items: stretch;
                 margin-right: 0; /* Remove margin */
                 /* Removed margin-bottom here */
             }
             .nav-links {
                 flex-direction: column;
                 align-items: stretch;
                 gap: var(--space-sm);
             }
             .nav-links li {
                 width: 100%;
                 text-align: center;
             }
             .nav-links a {
                 padding: var(--space-xs) 0;
             }

             .contribute-button-container {
                 width: 100%;
                 text-align: center;
                 margin-bottom: var(--space-sm); /* Add space below the button */
             }
             .contribute-button-container .btn {
                 width: auto; /* Allow button to shrink */
                 /* Padding is already adjusted by .btn style */
             }

             .theme-toggle {
                 margin-left: 0; /* Remove margin */
                 align-self: center; /* Center toggle if alone below buttons */
             }

             .card-header {
                 flex-direction: column;
                 align-items: stretch;
             }
             .card-header > span {
                 text-align: center;
                 margin-bottom: var(--space-sm);
             }
             .card-header .btn-group,
             .card-header .download-btn {
                 width: 100%;
                 justify-content: center;
             }
             .card-header .btn-group button {
                 flex-grow: 1;
             }
             .card-header .btn-group .btn:first-child { /* Reset margin on first child in button group on small screens */
                 margin-right: 0;
             }
             .card-header .download-btn {
                 margin-left: 0 !important; /* Reset margin-left: auto from wider view */
             }
             /* Add space between the button group and download buttons on small screens */
             .card-header .btn-group {
                 margin-bottom: var(--space-sm);
             }
        }
    </style>
</head>
<body>
    <header class="site-header">
        <div class="container main-content"> <!-- Use main-content container for header alignment -->
            <div class="top-bar">
                <h1 class="site-title">BenchmarkCards</h1>
                <nav class="main-nav">
                    <ul class="nav-links">
                        <li><a href="/" class="active">Home</a></li> <!-- Use / for home -->
                        <li><a href="https://github.com/SokolAnn/BenchmarkCards" target="_blank">GitHub</a></li>
                        <li><a href="https://arxiv.org/abs/2410.12974" target="_blank" class="paper-link">Our Paper</a></li>
                    </ul>
                </nav>
                 <!-- New Contribute Button -->
                <div class="contribute-button-container">
                    <a href="https://github.com/SokolAnn/BenchmarkCards" target="_blank" class="btn btn-primary" role="button" aria-label="Contribute to BenchmarkCards on GitHub">
                        <i class="fab fa-github me-2" aria-hidden="true"></i>
                        CONTRIBUTE
                    </a>
                </div>
                <button id="themeToggle" class="theme-toggle" aria-label="Toggle dark mode">
                    <i class="fas fa-moon" aria-hidden="true"></i>
                </button>
            </div>
        </div>
        <div class="header-border"></div>
    </header>

    <main class="container main-content">
        <section class="card upload-card">
            <div class="card-body">
                <form id="uploadForm">
                    <div
                        id="dropArea"
                        class="upload-area"
                        tabindex="0"
                        role="button"
                        aria-label="Upload PDF file. Drag and drop or click to browse files">
                        <i class="fas fa-file-upload upload-icon" aria-hidden="true"></i>
                        <p class="upload-text">Drag & drop your PDF here</p>
                        <p class="upload-hint">or click to browse files</p>
                        <p class="upload-description">Upload a research paper describing an LLM benchmark</p>
                        <input type="file" id="fileInput" name="file" accept=".pdf" aria-label="PDF file upload" />
                    </div>

                    <div class="text-center">
                        <button type="submit" id="submitBtn" class="btn btn-primary btn-icon" disabled> <!-- Added disabled initially -->
                            <i class="fas fa-wand-magic-sparkles me-2" aria-hidden="true"></i>
                            <span>GENERATE BENCHMARK CARD</span>
                        </button>
                    </div>
                </form>

                <div id="loaderContainer" class="loader-container" aria-live="polite">
                    <div class="progress-container" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">
                        <div class="progress-bar">
                            <div class="progress-value"></div>
                        </div>
                    </div>
                    <p class="progress-text">Analyzing your benchmark paper...</p>
                </div>
                 <!-- Add error message container -->
                <div id="errorContainer" class="alert alert-danger mt-3" role="alert" style="display: none;">
                    <!-- Error message will be inserted here by JavaScript -->
                </div>
            </div>
        </section>

        <section id="resultContainer" class="card result-card" aria-live="polite">
            <header class="card-header">
                <span>Benchmark Card</span>
                <!-- Add button group for toggling views -->
                <div class="btn-group" role="group" aria-label="View format">
                    <button id="btnJSON" type="button" class="btn btn-primary">View JSON</button>
                    <button id="btnMD"   type="button" class="btn btn-outline-primary">View Markdown</button>
                </div>
                 <!-- Download buttons -->
                <a id="downloadJSONButton" href="#" class="btn btn-primary download-btn" aria-label="Download JSON">
                    <i class="fas fa-download me-2" aria-hidden="true"></i> JSON
                </a>
                 <!-- Markdown download button, initially hidden -->
                <a id="downloadMDButton" href="#" class="btn btn-primary download-btn" aria-label="Download Markdown" style="display: none;">
                    <i class="fas fa-download me-2" aria-hidden="true"></i> Markdown
                </a>
            </header>
            <div class="card-body">
                <!-- Separate pre tags for JSON and Markdown -->
                <pre id="jsonResult" tabindex="0" style="display: block;"></pre>
                <pre id="mdResult"   tabindex="0" style="display: none;"></pre>
                <!-- Keep the original result pre tag but hide it -->
                <pre id="result" tabindex="0" style="display: none;"></pre>
            </div>
        </section>
    </main>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // --- Element References ---
            const themeToggle = document.getElementById('themeToggle');
            const themeIcon = themeToggle.querySelector('i');
            const dropArea = document.getElementById('dropArea');
            const fileInput = document.getElementById('fileInput');
            const uploadForm = document.getElementById('uploadForm');
            const submitBtn = document.getElementById('submitBtn');
            const loaderContainer = document.getElementById('loaderContainer');
            const resultContainer = document.getElementById('resultContainer');
            const errorContainer = document.getElementById('errorContainer'); // Reference to the error div
            const jsonResultPre = document.getElementById('jsonResult'); // New reference for JSON pre
            const mdResultPre = document.getElementById('mdResult');     // New reference for Markdown pre
            // const resultElement = document.getElementById('result'); // Old reference, now hidden
            const btnJSON = document.getElementById('btnJSON'); // Reference to JSON toggle button
            const btnMD = document.getElementById('btnMD');     // Reference to Markdown toggle button
            const downloadJSONButton = document.getElementById('downloadJSONButton'); // Reference to JSON download button
            const downloadMDButton = document.getElementById('downloadMDButton'); // Reference to MD download button

            // --- Theme Toggle Functionality ---
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.setAttribute('data-theme', 'dark');
                themeIcon.classList.remove('fa-moon');
                themeIcon.classList.add('fa-sun');
            }

            themeToggle.addEventListener('click', function() {
                const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
                const newTheme = currentTheme === 'light' ? 'dark' : 'light';

                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);

                if (newTheme === 'dark') {
                    themeIcon.classList.remove('fa-moon');
                    themeIcon.classList.add('fa-sun');
                } else {
                    themeIcon.classList.remove('fa-sun');
                    themeIcon.classList.add('fa-moon');
                }
            });

            // --- File Upload (Drag & Drop & Click) ---
            // Make upload area accessible via keyboard
            dropArea.addEventListener('keydown', function(e) {
                if (e.keyCode === 13 || e.keyCode === 32) {
                    e.preventDefault();
                    fileInput.click();
                }
            });

            // File input click handler
            dropArea.addEventListener('click', function() {
                fileInput.click();
            });

            // File selected via input
            fileInput.addEventListener('change', function() {
                handleFileSelection(fileInput.files);
            });

            // Drag and drop functionality
            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                dropArea.addEventListener(eventName, preventDefaults, false);
            });

            function preventDefaults(e) {
                e.preventDefault();
                e.stopPropagation();
            }

            ['dragenter', 'dragover'].forEach(eventName => {
                dropArea.addEventListener(eventName, function() {
                    dropArea.classList.add('dragover');
                }, false);
            });

            ['dragleave', 'drop'].forEach(eventName => {
                dropArea.addEventListener(eventName, function() {
                    dropArea.classList.remove('dragover');
                }, false);
            });

            dropArea.addEventListener('drop', function(e) {
                const dt = e.dataTransfer;
                const files = dt.files;
                handleFileSelection(files);
            });

            function handleFileSelection(files) {
                 hideError(); // Hide any previous errors
                 if (files.length && files[0].type === 'application/pdf') {
                    const fileName = files[0].name;
                    dropArea.querySelector('.upload-text').textContent = fileName;
                    dropArea.querySelector('.upload-hint').textContent = 'PDF file selected';
                    dropArea.style.borderColor = '#000000'; // Optional: Visual feedback

                    // Set ARIA attributes for accessibility
                    dropArea.setAttribute('aria-label', `Selected file: ${fileName}. Click to change.`);
                     submitBtn.disabled = false; // Enable the submit button
                } else if (files.length) {
                    // Show error for non-PDF files
                    showError('Please upload a PDF file');
                    resetUploadArea();
                     submitBtn.disabled = true; // Disable the submit button
                } else {
                    // No file selected (e.g., user cancelled)
                     resetUploadArea();
                     submitBtn.disabled = true; // Disable the submit button
                }
            }

            function resetUploadArea() {
                dropArea.querySelector('.upload-text').textContent = 'Drag & drop your PDF here';
                dropArea.querySelector('.upload-hint').textContent = 'or click to browse files';
                dropArea.querySelector('.upload-description').textContent = 'Upload a research paper describing an LLM benchmark';
                dropArea.style.borderColor = '';
                dropArea.setAttribute('aria-label', 'Upload PDF file. Drag and drop or click to browse files');
                 fileInput.value = ''; // Clear the file input
            }

            function showError(message) {
                 errorContainer.textContent = message;
                 errorContainer.style.display = 'block';
                 // Announce error for screen readers
                 errorContainer.setAttribute('aria-live', 'assertive'); // Ensure screen readers read this immediately
                 // Optional: Remove after a delay
                 // setTimeout(() => { hideError(); }, 5000);
            }

             function hideError() {
                 errorContainer.style.display = 'none';
                 errorContainer.textContent = '';
                 errorContainer.removeAttribute('aria-live'); // Remove assertive region once hidden
             }

            // --- Form submission ---
            uploadForm.addEventListener('submit', async function(e) {
                e.preventDefault();

                if (!fileInput.files[0]) {
                    showError('Please select a PDF file');
                    return;
                }

                const formData = new FormData();
                formData.append('file', fileInput.files[0]);
                // Get the model value from the select element if you add one later
                // For now, hardcode as seen in your previous app.py code
                 //formData.append('model', document.getElementById('modelSelect').value);
                 formData.append('model', 'gpt-4o'); // Using 'gpt-4o' as seen in your previous app.py code

                // Reset state and show loading indicator
                hideError();
                resultContainer.style.display = 'none';
                uploadForm.style.display = 'none';
                loaderContainer.style.display = 'block';
                submitBtn.disabled = true; // Disable during processing

                // Simulate API progress updates
                startProgressSimulation();

                try {
                    const response = await fetch('/extract/', {
                        method: 'POST',
                        body: formData
                    });

                    stopProgressSimulation();
                    loaderContainer.style.display = 'none';
                    uploadForm.style.display = 'block';
                    submitBtn.disabled = false; // Re-enable submit after response


                    if (!response.ok) {
                        const errorData = await response.json();
                        throw new Error(errorData.detail || 'Failed to extract data');
                    }

                    const data = await response.json(); // Data is { json_result, md_result }

                    // Display results
                    // Use textContent to avoid unwanted HTML parsing for both JSON and Markdown
                    jsonResultPre.textContent = JSON.stringify(data.json_result, null, 2);
                    mdResultPre.textContent = data.md_result;

                    // Show result container and default to JSON view
                    resultContainer.style.display = 'block';
                    showView('json'); // Call helper to show JSON view by default

                    // Set up download links (create Object URLs)
                    const jsonBlob = new Blob([JSON.stringify(data.json_result, null, 2)], { type: 'application/json' });
                    const mdBlob = new Blob([data.md_result], { type: 'text/markdown' });

                    downloadJSONButton.href = URL.createObjectURL(jsonBlob);
                    downloadMDButton.href = URL.createObjectURL(mdBlob);

                    // Suggest filenames
                    let baseFilename = fileInput.files[0].name.replace(/\.pdf$/i, '');
                    // Optional: try to get benchmark name from JSON for a better filename
                    try {
                         const benchmarkName = data.json_result?.benchmark_details?.name;
                         if (benchmarkName) {
                              // Sanitize the name for a filename
                              baseFilename = benchmarkName.toLowerCase().replace(/[^a-z0-9_\s-]/g, '').replace(/\s+/g, '_').replace(/-+/g, '-').replace(/^-+|-+$/g, '') || baseFilename;
                         }
                    } catch (e) {
                        console.error("Error sanitizing filename from JSON:", e);
                    }
                    downloadJSONButton.download = baseFilename + '.json';
                    downloadMDButton.download = baseFilename + '.md';


                    // Announce completion for screen readers
                    resultContainer.setAttribute('aria-label', 'Benchmark card generated successfully');

                    // Allow submitting another file (reset form state)
                    resetForm();

                } catch (error) {
                    console.error('Extraction error:', error);
                    stopProgressSimulation();
                    loaderContainer.style.display = 'none';
                    uploadForm.style.display = 'block';
                    submitBtn.disabled = false; // Re-enable submit on error
                    showError('Extraction failed: ' + error.message);
                    // Keep result container hidden on hard error
                    resultContainer.style.display = 'none';
                }
            });

            // --- Progress simulation ---
            let progressInterval;
            let progressTextElement; // Added reference

            function startProgressSimulation() {
                progressTextElement = document.querySelector('.progress-text'); // Get reference
                const messages = [
                    "Analyzing your benchmark paper...",
                    "Extracting methodology details...",
                    "Identifying benchmark metrics...",
                    "Structuring benchmark data...",
                    "Creating your benchmark card..."
                ];
                let messageIndex = 0;

                progressTextElement.textContent = messages[messageIndex]; // Set initial text
                progressTextElement.setAttribute('aria-label', messages[messageIndex]);

                progressInterval = setInterval(() => {
                    messageIndex = (messageIndex + 1) % messages.length;
                    progressTextElement.textContent = messages[messageIndex];
                    progressTextElement.setAttribute('aria-label', messages[messageIndex]);
                }, 3000);
            }

            function stopProgressSimulation() {
                clearInterval(progressInterval);
                if (progressTextElement) { // Check if element exists before accessing
                     progressTextElement.textContent = ''; // Clear text
                     progressTextElement.removeAttribute('aria-label');
                }
            }

            function resetForm() {
                uploadForm.reset();
                resetUploadArea();
                 hideError(); // Also hide error message on form reset
                 // Keep resultContainer visible if data was successful, hide if error occurred
                 // The fetch block handles hiding on error and showing on success
            }

            // --- View Toggle Logic ---
            function showView(format) {
                 // First, remove active/outline classes from both buttons
                 btnJSON.classList.remove('btn-primary', 'btn-outline-primary');
                 btnMD.classList.remove('btn-primary', 'btn-outline-primary');

                 if (format === 'json') {
                    btnJSON.classList.add('btn-primary');
                    btnMD.classList.add('btn-outline-primary'); // Correct class for inactive
                    jsonResultPre.style.display = 'block';
                    mdResultPre.style.display = 'none';
                    downloadJSONButton.style.display = 'inline-flex'; // Show JSON download
                    downloadMDButton.style.display = 'none'; // Hide MD download
                 } else if (format === 'md') {
                    btnMD.classList.add('btn-primary');
                    btnJSON.classList.add('btn-outline-primary'); // Correct class for inactive
                    jsonResultPre.style.display = 'none';
                    mdResultPre.style.display = 'block';
                    downloadJSONButton.style.display = 'none'; // Hide JSON download
                    downloadMDButton.style.display = 'inline-flex'; // Show MD download
                 }
                 // Ensure the correct download button href is already set by the fetch handler
            }

            btnJSON.addEventListener('click', () => showView('json'));
            btnMD.addEventListener('click', () => showView('md'));

            // --- JSON Formatting (Removed as requested) ---
            // function formatJSON(json) { ... }


            // Note: The standalone downloadJSON function defined in the original HTML was removed
            // as the download is now handled directly by the <a> tags with object URLs.

            // Initial state: Disable submit button until file is selected
            submitBtn.disabled = true;
        });
    </script>
</body>
</html>
"""