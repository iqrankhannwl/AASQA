## Clone Repository
git clone https://github.com/iqrankhannwl/AASQA.git

## Create Virtual Environment:
```bash
python -m venv venv
```
## Activate Virtual Environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS and Linux
```bash
source venv/bin/activate

```

## Install Dependencies:

```bash
pip install -r req.txt

```

## Run the Application:

```bash
streamlit run app.py
```

```bash
air-quality-dashboard/
│
├── app.py                    # Main application script
├── data/                     # Directory for sample data files
│   └── sample.csv            # Sample CSV data file
├── scripts/                  # Directory for custom graph scripts
│   └── graphs.py             # Custom graph functions
├── src/                      # Directory for additional source files
│   └── Home.py               # Home page functionality
├── README.md                 # Project README file
├── requirements.txt          # List of project dependencies
└── LICENSE                   # License file (e.g., MIT License)
```