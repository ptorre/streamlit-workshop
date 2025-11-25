# Workshop Setup 🚀

Completing this setup before the workshop ensures we can dive straight into coding without install delays.

## Prerequisites

Start by making sure you have the following software installed:

- **Git:** https://git-scm.com/downloads  
- **uv (package manager):** https://docs.astral.sh/uv/getting-started/installation/  
  Used to manage project dependencies and ensure consistent Python versions. After installing `uv`, restart the terminal.
- **A code editor/IDE:** I recommend VS Code: https://code.visualstudio.com/download  
- **A way to work with Jupyter Notebooks:** I recommend the Jupyter extension for VS Code: https://code.visualstudio.com/docs/datascience/jupyter-notebooks

## Step 1: Clone the course repo

Run: 
```sh 
git clone https://github.com/arilamstein/streamlit-workshop.git
cd streamlit-workshop
```

## Step 2: Create the course virtual environment

Run:
```sh
uv sync
```

This creates `.venv` and installs all dependencies pinned for the workshop.

## Step 3: Activate the virtual environment

Use the command for your OS/shell:

- Mac/Linux:  `source .venv/bin/activate`

- Windows (Command Prompt):  `.venv\Scripts\activate`

- Windows (PowerShell): `.venv\Scripts\Activate.ps1`

Verify:
- Run `python --version` → should report a version starting with **Python 3.13**
- Run `which python` (Mac/Linux) or `where python` (Windows) → should show a path inside `.venv`

## Step 4: Verify the Streamlit demo app

Run:  
```sh
cd 1-intro
streamlit run streamlit_app.py
```

**Expected result**: A browser opens showing a table of data. If it does, you’re good to go.  

Stop the app (Ctrl+C in the terminal) before continuing.

## Step 5: Verify Jupyter notebooks

Open `1-intro/review.ipynb`.

- **Recommended:** If you’re using VS Code, install the [Jupyter extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).  
  Then select the **kernel** for this project’s virtual environment (usually labeled `.venv`), run the first cell, and confirm it executes without errors.

- **Alternative (if not using VS Code):**  
  Make sure you're in the `1-intro` directory, then run:
  ```sh
  uv run jupyter notebook review.ipynb
  ```

## Final check

If you:  
- cloned the repo,  
- created and activated the environment,  
- launched the Streamlit demo,  
- and ran the `review.ipynb` notebook,  

🎉 You’re ready for the workshop. If you hit issues, reach out on the support channel before the event with screenshots and your OS/shell details.
