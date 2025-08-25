

# 🎨 Neural Style Transfer with TensorFlow

This project is a Python implementation of Neural Style Transfer, a powerful technique that uses deep learning to compose images in the style of another image. It leverages a pre-trained model from TensorFlow Hub to separate and recombine the content and style of arbitrary images.

This script allows you to merge the "content" of one image with the "artistic style" of another, as described in the paper ["A Neural Algorithm of Artistic Style"](https://arxiv.org/abs/1508.06576) by Gatys et al.

## 🖼️ Examples

Here is an example of the output, where the content of the original photo is combined with the style of the reference artwork.

| Content Image | Style Image | Stylized Result |
| :---: | :---: | :---: |
|  |  |  |
| *(Your `orginal.jpg`)* | *(Your `style_refrence1.jpg`)* | *(The final generated image)* |

*(To add your own images to the README, simply place them in your project folder and change the placeholder text above to the file names, like `![My Original Photo](orginal.jpg)`)*

-----

## 🛠️ Technologies Used

  * **Python 3.x**
  * **TensorFlow:** For the core deep learning framework.
  * **TensorFlow Hub:** To load the pre-trained style transfer model.
  * **NumPy:** For numerical operations and tensor manipulation.
  * **Pillow (PIL):** For converting the final tensor back into an image file.
  * **Matplotlib:** To display the images.

-----

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3 installed on your system.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **(Recommended) Create a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    Create a file named `requirements.txt` and add the following lines to it:

    ```
    tensorflow
    tensorflow_hub
    numpy
    matplotlib
    Pillow
    ```

    Then, run the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

-----

## 🏃 How to Use

1.  Place your desired content image and style reference image into the project's root folder.
2.  Open the Python script (`your_script_name.py`).
3.  Update the `content_path` and `style_path` variables with the filenames of your images:
    ```python
    # 1. Define the file paths for your images
    content_path = "orginal.jpg"
    style_path = "style_refrence1.jpg"
    ```
4.  Run the script from your terminal:
    ```bash
    python your_script_name.py
    ```
5.  After a few moments, a Matplotlib window will pop up displaying your new, stylized image.

-----

## ✨ Acknowledgments

  * This project uses the **Magenta Arbitrary Image Stylization V1-256** model from [TensorFlow Hub](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2).
  * The methodology is based on the original research by Leon A. Gatys, Alexander S. Ecker, and Matthias Bethge.
