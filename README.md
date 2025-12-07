# Simple Academic Personal Page

A lightweight, maintenance-free website template for academics, researchers, and students. 

**No complex frameworks. No Hugo/Jekyll. Just one JSON file.**

![Python](https://img.shields.io/badge/Built%20with-Python-3776AB?style=flat&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Style-Bootstrap%205-7952B3?style=flat&logo=bootstrap&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-222222?style=flat&logo=github&logoColor=white)

## How it Works

1.  **You edit `data.json`** (add your bio, papers, news).
2.  **GitHub Actions** detects the change.
3.  A Python script runs automatically, merging your data with the design template.
4.  Your website is **published** to GitHub Pages.


##  Quick Start Guide

### 1. Create your Repository
Click the **"Use this template"** button at the top right of this page to create your own copy of this repository.

### 2. Configure GitHub Pages
1.  Go to your repository **Settings**.
2.  Click **Pages** on the left sidebar.
3.  Under **Build and deployment** > **Source**, select **Deploy from a branch**.
4.  Under **Branch**, select `gh-pages` and `/ (root)`.
    * *Note: If you don't see `gh-pages` yet, make a small edit to a file and commit it. The automated workflow will create the branch for you.*
5.  Click **Save**.

### 3. Update Your Content
1.  Open `data.json` in your repository.
2.  Edit the values to match your profile.
    * **Tip:** You can use Markdown (bold `**text**`, links `[text](url)`) inside the text fields!
3.  Commit your changes.
4.  Wait ~1 minute, and your site will be live!


##  Project Structure

* `data.json`: **The Source of Truth.** This is the only file you need to edit regularly.
* `template.html`: The HTML design. Edit this if you want to change the layout or colors.
* `build.py`: The Python script that generates the website.
* `.github/workflows/deploy.yml`: The automation configuration.
* `assets/images/`: Place your profile picture and project images here.

---

## Editing `data.json`

The data file is structured into simple sections. If you don't want a section (e.g., you don't have "News" yet), simply delete that block from the JSON, and it will disappear from the website.

```json
{
  "basics": {
    "name": "Your Name",
    "image": "images/profile.jpg",
    "bio": "I am a **Researcher**..." // Markdown is supported here!
  },
  "projects": [ ... ],
  "publications": [ ... ]
}
````

### Adding Images

1.  Upload your image to the `images/` folder on GitHub.
2.  In `data.json`, reference it like this: `"image": "images/my-photo.jpg"`


## Local Development (Optional)

If you prefer to preview changes on your own computer before pushing to GitHub:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/your-repo.git](https://github.com/yourusername/your-repo.git)
    ```
2.  **Install Python requirements:**
    ```bash
    pip install jinja2 markdown
    ```
3.  **Build the site:**
    ```bash
    python build.py
    ```
4.  **Open `index.html`** in your browser to see the result.


## Customization

  * **Colors & Fonts:** Open `template.html` and look for the `<style>` block at the top. You can change `--primary-color` and `--accent-color`.
  * **Layout:** The template uses **Bootstrap 5**. You can use standard Bootstrap classes to modify the grid or spacing.

## License

This project is open source and available under the [MIT License](https://www.google.com/search?q=LICENSE). Feel free to use it for your personal academic website!
