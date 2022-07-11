# passGen
A python-made random password generator. I made this to experiment with [`PySimpleGui`](https://pysimplegui.readthedocs.io/en/latest/) and [`pyinstaller`](https://pyinstaller.org/en/stable/index.html).

## Functionality
- Create randomly generated passwords!
- Up to 32 characters in length!
- Choose to include numbers, special characters, upper- and lowercase characters!

## Installation
I've compiled the scripts to a single windows executable (.exe) file, which can be directly run on a windows machine. See the releases for the file.

### Running with python
To run this with python, I recommend using a conda environment. For most users, the following code should be enough:
```bash
# Optional: create a new conda environment
conda create --name passGen python=3.8 -y
conda activate passGen

# Install the dependencies
conda install numpy -y
conda install pysimplegui -c conda-forge

# Run the app
python ui.py
```

Alternatively, the conda environment can be installed using the `requirements.yaml` file.
```bash
# Create a new conda environment
conda env create -f requirements.yaml
conda activate passGen

# Run the app
python ui.py
```
