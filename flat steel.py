import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ys_data = {
    "SP781": {
        "0.40 TO 0.60": {
            "POSCO": {"Bandwidth": 20, "Lowest": 145, "Highest": 165},
            "TATA": {"Bandwidth": 40, "Lowest": 135, "Highest": 175},
            "JCAPCPL": {"Bandwidth": None, "Lowest": None, "Highest": None},
            "RNAIPL Proposal": {"Bandwidth": 90, "Lowest": 135, "Highest": 165},
            "NES Spec": {"Bandwidth": 30, "Lowest": 135, "Highest": 225}
        },
        "0.60 TO 0.80": {
            "POSCO": {"Bandwidth": 20, "Lowest": 145, "Highest": 165},
            "TATA": {"Bandwidth": 40, "Lowest": 135, "Highest": 175},
            "JCAPCPL": {"Bandwidth": None, "Lowest": None, "Highest": None},
            "RNAIPL Proposal": {"Bandwidth": 90, "Lowest": 135, "Highest": 165},
            "NES Spec": {"Bandwidth": 30, "Lowest": 135, "Highest": 225}
        },
        "0.80 TO 1.00": {
            "POSCO": {"Bandwidth": 15, "Lowest": 150, "Highest": 165},
            "TATA": {"Bandwidth": 20, "Lowest": 145, "Highest": 165},
            "RNAIPL Proposal": {"Bandwidth": 25, "Lowest": 140, "Highest": 165},
            "NES Spec": {"Bandwidth": 90, "Lowest": 125, "Highest": 215},
            "NEW PROPOSAL": {"Bandwidth": 25, "Lowest": 150, "Highest": 175}
        },
        "1.00 TO 1.20": {
            "POSCO": {"Bandwidth": 20, "Lowest": 145, "Highest": 165},
            "TATA": {"Bandwidth": 20, "Lowest": 147, "Highest": 167},
            "RNAIPL Proposal": {"Bandwidth": 25, "Lowest": 145, "Highest": 170},
            "NES Spec": {"Bandwidth": 90, "Lowest": 115, "Highest": 205},
            "NEW PROPOSAL": {"Bandwidth": 25, "Lowest": 145, "Highest": 170}
        },
        "1.20 TO 1.60": {
            "POSCO": {"Bandwidth": 20, "Lowest": 145, "Highest": 165},
            "TATA": {"Bandwidth": 20, "Lowest": 150, "Highest": 170},
            "RNAIPL Proposal": {"Bandwidth": 25, "Lowest": 145, "Highest": 170},
            "NES Spec": {"Bandwidth": 90, "Lowest": 115, "Highest": 205},
            "NEW PROPOSAL": {"Bandwidth": 25, "Lowest": 150, "Highest": 175}
        },
        "1.60 TO 2.00": {
            "POSCO": {"Bandwidth": 20, "Lowest": 145, "Highest": 165},
            "TATA": {"Bandwidth": 20, "Lowest": 150, "Highest": 170},
            "RNAIPL Proposal": {"Bandwidth": 25, "Lowest": 145, "Highest": 170},
            "NES Spec": {"Bandwidth": 90, "Lowest": 115, "Highest": 205},
            "NEW PROPOSAL": {"Bandwidth": 25, "Lowest": 150, "Highest": 175}
        }
    },
    "SP782": {
        "0.40 TO 0.60": {
            "POSCO": {"Bandwidth": 10, "Lowest": 155, "Highest": 165},
            "TATA": {"Bandwidth": 25, "Lowest": 140, "Highest": 165},
            "RNAIPL Proposal": {"Bandwidth": 75, "Lowest": 140, "Highest": 165},
            "NEW PORPOSAL": {"Bandwidth": 25, "Lowest": 155, "Highest": 180}
        },
        "0.60 TO 0.80": {
            "TATA": {"Bandwidth": 18, "Lowest": 140, "Highest": 158},
            "RNAIPL PROPOSAL": {"Bandwidth": 25, "Lowest": 140, "Highest": 165},
            "NES SPEC": {"Bandwidth": 75, "Lowest": 130, "Highest": 205},
            "NEW PROPOSAL": {"Bandwidth": 25, "Lowest": 140, "Highest": 165}
        },
        "0.80 TO 1.00": {
            "NES SPEC": {"Bandwidth": 75, "Lowest": 120, "Highest": 195}
        },
        "1.00 TO 3.20": {
            "NES SPEC": {"Bandwidth": 75, "Lowest": 110, "Highest": 185}
        }
    },
    "SP783": {
        "0.40 TO 0.60": {
            "POSCO": {"Bandwidth": 15, "Lowest": 140, "Highest": 155},
            "TATA": {"Bandwidth": 20, "Lowest": 135, "Highest": 155},
            "RNAIPL Proposal": {"Bandwidth": 25, "Lowest": 135, "Highest": 160},
            "NES Spec": {"Bandwidth": 65, "Lowest": 120, "Highest": 185},
            "NEW PROPOSAL": {"Bandwidth": 25, "Lowest": 140, "Highest": 165}
        },
        "0.60 TO 0.80": {
            "POSCO": {"Bandwidth": 15, "Lowest": 140, "Highest": 155},
            "TATA": {"Bandwidth": 15, "Lowest": 135, "Highest": 150},
            "RNAIPL Proposal": {"Bandwidth": 25, "Lowest": 135, "Highest": 160},
            "NES Spec": {"Bandwidth": 65, "Lowest": 120, "Highest": 185},
            "NEW PROPOSAL": {"Bandwidth": 25, "Lowest": 140, "Highest": 165}
        },
        "0.80 TO 1.00": {
            "POSCO": {"Bandwidth": 16, "Lowest": 142, "Highest": 158},
            "RNAIPL Proposal": {"Bandwidth": 25, "Lowest": 125, "Highest": 150},
            "NES Spec": {"Bandwidth": 65, "Lowest": 110, "Highest": 175},
            "NEW PROPOSAL": {"Bandwidth": 25, "Lowest": 140, "Highest": 165}
        }
    },
    "SP781 - 440": {
        "0.60 TO 0.80": {
            "TATA": {"Bandwidth": 60, "Lowest": 300, "Highest": 360},
            "JCAPCPL": {"Bandwidth": 65, "Lowest": 295, "Highest": 360},
            "RNAIPL Proposal": {"Bandwidth": 105, "Lowest": 295, "Highest": 400},
            "NES Spec": {"Bandwidth": 60, "Lowest": 300, "Highest": 360}
        },
        "0.80 TO 1.00": {
            "POSCO": {"Bandwidth": 30, "Lowest": 350, "Highest": 380},
            "TATA": {"Bandwidth": 45, "Lowest": 295, "Highest": 340},
            "RNAIPL Proposal": {"Bandwidth": 65, "Lowest": 295, "Highest": 360},
            "NES SPEC": {"Bandwidth": 105, "Lowest": 285, "Highest": 390}
        },
        "1.00 TO 1.20": {
            "TATA": {"Bandwidth": 35, "Lowest": 295, "Highest": 330},
            "RNAIPL Proposal": {"Bandwidth": 85, "Lowest": 275, "Highest": 360},
            "NES Spec": {"Bandwidth": 105, "Lowest": 275, "Highest": 380},
            "NEW PROPOSAL": {"Bandwidth": 55, "Lowest": 295, "Highest": 350}
        },
        "1.20 TO 1.60": {
            "TATA": {"Bandwidth": 25, "Lowest": 295, "Highest": 320},
            "JCAPCPL": {"Bandwidth": 85, "Lowest": 275, "Highest": 360},
            "RNAIPL Proposal": {"Bandwidth": 105, "Lowest": 275, "Highest": 380},
            "NES Spec": {"Bandwidth": 55, "Lowest": 295, "Highest": 350}
        },
        "1.60 TO 2.00": {
            "TATA": {"Bandwidth": 40, "Lowest": 295, "Highest": 335},
            "RNAIPL Proposal": {"Bandwidth": 85, "Lowest": 275, "Highest": 360},
            "NES Spec": {"Bandwidth": 105, "Lowest": 275, "Highest": 380},
            "NEW PROPOSAL": {"Bandwidth": 55, "Lowest": 295, "Highest": 350}
        },
        "2.00 TO 3.20": {
            "POSCO": {"Bandwidth": 45, "Lowest": 300, "Highest": 345},
            "RNAIPL Proposal": {"Bandwidth": 85, "Lowest": 275, "Highest": 360},
            "NES Spec": {"Bandwidth": 105, "Lowest": 275, "Highest": 380},
            "NEW proposal": {"Bandwidth": 55, "Lowest": 300, "Highest": 355}
        }
    },
    "SP121": {
        "0.40 TO 0.60": {
            "POSCO": {"Bandwidth": 17, "Lowest": 135, "Highest": 152},
            "TATA": {"Bandwidth": 30, "Lowest": 150, "Highest": 180},
            "JCAPCPL": {"Bandwidth": 30, "Lowest": 135, "Highest": 165},
            "RNAIPL Proposal": {"Bandwidth": 35, "Lowest": 135, "Highest": 170},
            "NES Spec": {"Bandwidth": 90, "Lowest": 135, "Highest": 225},
            "NEW PROPOSAL": {"Bandwidth": 35, "Lowest": 150, "Highest": 185}
        },
        "0.60 TO 0.80": {
            "POSCO": {"Bandwidth": 17, "Lowest": 135, "Highest": 152},
            "JSW": {"Bandwidth": 30, "Lowest": 150, "Highest": 180},
            "TATA": {"Bandwidth": 30, "Lowest": 150, "Highest": 180},
            "JCAPCPL": {"Bandwidth": 30, "Lowest": 135, "Highest": 165},
            "RNAIPL Proposal": {"Bandwidth": 35, "Lowest": 135, "Highest": 170},
            "NES Spec": {"Bandwidth": 90, "Lowest": 135, "Highest": 225},
            "NEW PROPOSAL": {"Bandwidth": 35, "Lowest": 150, "Highest": 185}
        },
        "0.80 TO 1.00": {
            "POSCO": {"Bandwidth": 18, "Lowest": 132, "Highest": 150},
            "JSW": {"Bandwidth": 35, "Lowest": 140, "Highest": 175},
            "TATA": {"Bandwidth": 30, "Lowest": 155, "Highest": 185},
            "RNAIPL Proposal": {"Bandwidth": 30, "Lowest": 130, "Highest": 160},
            "NES Spec": {"Bandwidth": 90, "Lowest": 125, "Highest": 215},
            "NEW PROPOSAL": {"Bandwidth": 30, "Lowest": 155, "Highest": 185}
        },
        "1.0 TO 1.2": {
            "JSW": {"Bandwidth": 25, "Lowest": 140, "Highest": 165},
            "TATA": {"Bandwidth": 25, "Lowest": 150, "Highest": 175},
            "RNAIPL Proposal": {"Bandwidth": 35, "Lowest": 130, "Highest": 165},
            "NES Spec": {"Bandwidth": 90, "Lowest": 115, "Highest": 205},
            "NEW PROPOSAL": {"Bandwidth": 30, "Lowest": 150, "Highest": 180}
        },
        "1.2 TO 1.6": {
            "JSW": {"Bandwidth": 30, "Lowest": 140, "Highest": 170},
            "TATA": {"Bandwidth": 30, "Lowest": 155, "Highest": 185},
            "RNAIPL Proposal": {"Bandwidth": 35, "Lowest": 130, "Highest": 165},
            "NES Spec": {"Bandwidth": 90, "Lowest": 115, "Highest": 205},
            "NEW proposal": {"Bandwidth": 35, "Lowest": 150, "Highest": 185}
        },
        "1.6 TO 3.20": {
            "POSCO": {"Bandwidth": 23, "Lowest": 132, "Highest": 155},
            "RNAIPL Proposal": {"Bandwidth": 35, "Lowest": 130, "Highest": 165},
            "NES Spec": {"Bandwidth": 90, "Lowest": 115, "Highest": 205},
            "NEW PROPOSAL": {"Bandwidth": 35, "Lowest": 130, "Highest": 165}
        }
    },
    "SP122": {
        "0.40 TO 0.80": {
            "POSCO": {"Bandwidth": 8, "Lowest": 134, "Highest": 142},
            "RNAIPL Proposal": {"Bandwidth": 13, "Lowest": 157, "Highest": 170},
            "NES Spec": {"Bandwidth": 75, "Lowest": 130, "Highest": 205},
            "NEW PROPOSAL": {"Bandwidth": 30, "Lowest": 140, "Highest": 170}
        }
    },
    "SP123": {
        "0.40 TO 0.60": {
            "TATA": {"Bandwidth": 30, "Lowest": 135, "Highest": 165},
            "JCAPCPL": {"Bandwidth": 15, "Lowest": 135, "Highest": 150},
            "RNAIPL Proposal": {"Bandwidth": 30, "Lowest": 130, "Highest": 160},
            "NES Spec": {"Bandwidth": 65, "Lowest": 120, "Highest": 185},
            "NEW PROPOSAL": {"Bandwidth": 30, "Lowest": 135, "Highest": 165}
        },
        "0.60 TO 0.80": {
            "JSW": {"Bandwidth": 20, "Lowest": 130, "Highest": 150},
            "TATA": {"Bandwidth": 30, "Lowest": 130, "Highest": 160},
            "JCAPCPL": {"Bandwidth": 15, "Lowest": 135, "Highest": 150},
            "RNAIPL Proposal": {"Bandwidth": 30, "Lowest": 130, "Highest": 160},
            "NES Spec": {"Bandwidth": 65, "Lowest": 120, "Highest": 185},
            "NEW PROPOSAL ": {"Bandwidth": 30, "Lowest": 135, "Highest": 165}
        },
        "0.80 TO 1.00": {
            "TATA": {"Bandwidth": 25, "Lowest": 130, "Highest": 155},
            "RNAIPL Proposal": {"Bandwidth": 30, "Lowest": 125, "Highest": 155},
            "NES Spec": {"Bandwidth": 65, "Lowest": 110, "Highest": 175},
            "NEW PROPOSAL": {"Bandwidth": 30, "Lowest": 130, "Highest": 160}
        },
        "1.00 TO 1.20": {
            "TATA": {"Bandwidth": 25, "Lowest": 135, "Highest": 160},
            "RNAIPL Proposal": {"Bandwidth": 30, "Lowest": 120, "Highest": 150},
            "NES Spec": {"Bandwidth": 65, "Lowest": 100, "Highest": 165},
            "NEW PROPOSAL": {"Bandwidth": 30, "Lowest": 135, "Highest": 165}
        }
    },
    "SP152 - 440": {
        "0.80 TO 1.00": {
            "JSW": {"Bandwidth": 45, "Lowest": 280, "Highest": 325},
            "RNAIPL Proposal": {"Bandwidth": 85, "Lowest": 275, "Highest": 360},
            "NES Spec": {"Bandwidth": 105, "Lowest": 275, "Highest": 380},
            "NEW PROPOSAL": {"Bandwidth": 80, "Lowest": 280, "Highest": 360}
        },
        "1.0 TO 1.2": {
            "POSCO": {"Bandwidth": 40, "Lowest": 300, "Highest": 340},
            "JSW": {"Bandwidth": 65, "Lowest": 280, "Highest": 345},
            "RNAIPL Proposal": {"Bandwidth": 90, "Lowest": 265, "Highest": 355},
            "NES Spec": {"Bandwidth": 105, "Lowest": 265, "Highest": 370},
            "NEW PROPOSAL": {"Bandwidth": 40, "Lowest": 300, "Highest": 340}
        },
        "1.2 TO 1.6": {
            "POSCO": {"Bandwidth": 40, "Lowest": 300, "Highest": 340},
            "JSW": {"Bandwidth": 25, "Lowest": 340, "Highest": 365},
            "RNAIPL Proposal": {"Bandwidth": 90, "Lowest": 265, "Highest": 355},
            "NES Spec": {"Bandwidth": 105, "Lowest": 265, "Highest": 370},
            "NEW PROPOSAL": {"Bandwidth": 50, "Lowest": 340, "Highest": 390}
        },
        "1.6 TO 2.0": {
            "POSCO": {"Bandwidth": 40, "Lowest": 300, "Highest": 340},
            "JSW": {"Bandwidth": 90, "Lowest": 270, "Highest": 360},
            "RNAIPL Proposal": {"Bandwidth": 90, "Lowest": 265, "Highest": 355},
            "NES Spec": {"Bandwidth": 105, "Lowest": 265, "Highest": 370},
            "NEW PROPOSAL": {"Bandwidth": 60, "Lowest": 300, "Highest": 360}
        }
    },
    "SP153 - 590": {
        "1.0 TO 2.6": {
            "POSCO": {"Bandwidth": 30, "Lowest": 350, "Highest": 380}
        }
    }
}
 

ts_data = {
    "SP781": {
        "0.40 TO 0.60": {
            "POSCO": {"Bandwidth": 20, "Lowest": 295, "Highest": 315},
            "TATA": {"Bandwidth": 15, "Lowest": 300, "Highest": 315},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.60 TO 0.80": {
            "POSCO": {"Bandwidth": 20, "Lowest": 295, "Highest": 315},
            "TATA": {"Bandwidth": 15, "Lowest": 295, "Highest": 310},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.80 TO 1.00": {
            "POSCO": {"Bandwidth": 18, "Lowest": 297, "Highest": 315},
            "TATA": {"Bandwidth": 18, "Lowest": 287, "Highest": 305},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.00 TO 1.20": {
            "POSCO": {"Bandwidth": 15, "Lowest": 290, "Highest": 305},
            "TATA": {"Bandwidth": 15, "Lowest": 285, "Highest": 300},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.20 TO 1.60": {
            "POSCO": {"Bandwidth": 15, "Lowest": 290, "Highest": 305},
            "TATA": {"Bandwidth": 15, "Lowest": 290, "Highest": 305},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.60 TO 2.00": {
            "POSCO": {"Bandwidth": 15, "Lowest": 290, "Highest": 305},
            "TATA": {"Bandwidth": 10, "Lowest": 290, "Highest": 300},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        }
    },
    "SP782": {
        "0.40 TO 0.60": {
            "POSCO": {"Bandwidth": 10, "Lowest": 295, "Highest": 305},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.60 TO 0.80": {
            "TATA": {"Bandwidth": 20, "Lowest": 295, "Highest": 315},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.80 TO 1.00": {
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.00 TO 3.20": {
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        }
    },
    "SP783": {
        "0.40 TO 0.60": {
            "POSCO": {"Bandwidth": 15, "Lowest": 290, "Highest": 305},
            "TATA": {"Bandwidth": 20, "Lowest": 290, "Highest": 310},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.60 TO 0.80": {
            "POSCO": {"Bandwidth": 15, "Lowest": 290, "Highest": 305},
            "TATA": {"Bandwidth": 15, "Lowest": 295, "Highest": 310},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.80 TO 1.00": {
            "POSCO": {"Bandwidth": 16, "Lowest": 286, "Highest": 302},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.00 TO 3.20": {
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        }
    },
    "SP781 - 440": {
        "0.60 TO 0.80": {
            "TATA": {"Bandwidth": 35, "Lowest": 445, "Highest": 480},
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        },
        "0.80 TO 1.00": {
            "POSCO": {"Bandwidth": 15, "Lowest": 475, "Highest": 490},
            "TATA": {"Bandwidth": 25, "Lowest": 450, "Highest": 475},
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        },
        "1.00 TO 1.20": {
            "TATA": {"Bandwidth": 25, "Lowest": 455, "Highest": 480},
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        },
        "1.20 TO 1.60": {
            "TATA": {"Bandwidth": 20, "Lowest": 450, "Highest": 470},
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        },
        "1.60 TO 2.00": {
            "TATA": {"Bandwidth": 20, "Lowest": 450, "Highest": 470},
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        },
        "2.00 TO 3.20": {
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        }
    },
    "SP121": {
        "0.40 TO 0.60": {
            "POSCO": {"Bandwidth": 15, "Lowest": 290, "Highest": 305},
            "TATA": {"Bandwidth": 20, "Lowest": 295, "Highest": 315},
            "JCAPCPL": {"Bandwidth": 30, "Lowest": 285, "Highest": 315},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.60 TO 0.80": {
            "POSCO": {"Bandwidth": 15, "Lowest": 290, "Highest": 305},
            "JSW": {"Bandwidth": 30, "Lowest": 295, "Highest": 325},
            "TATA": {"Bandwidth": 20, "Lowest": 290, "Highest": 310},
            "JCAPCPL ": {"Bandwidth": 30, "Lowest": 285, "Highest": 315},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.80 TO 1.00": {
            "POSCO": {"Bandwidth": 12, "Lowest": 288, "Highest": 300},
            "JSW": {"Bandwidth": 30, "Lowest": 290, "Highest": 320},
            "TATA": {"Bandwidth": 18, "Lowest": 292, "Highest": 310},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.0 TO 1.2": {
            "JSW": {"Bandwidth": 25, "Lowest": 290, "Highest": 315},
            "TATA": {"Bandwidth": 20, "Lowest": 290, "Highest": 310},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.2 TO 1.6": {
            "JSW": {"Bandwidth": 25, "Lowest": 290, "Highest": 315},
            "TATA": {"Bandwidth": 20, "Lowest": 290, "Highest": 310},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.6 TO 3.20": {
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        }
    },
    "SP122": {
        "0.40 TO 0.80": {
            "POSCO": {"Bandwidth": 8, "Lowest": 292, "Highest": 300},
            "JCAPCPL": {"Bandwidth": 12, "Lowest": 298, "Highest": 310},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.80 TO 1.00": {
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.00 TO 3.20": {
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        }
    },
    "SP123": {
        "0.40 TO 0.60": {
            "TATA": {"Bandwidth": 25, "Lowest": 287, "Highest": 312},
            "JCAPCPL": {"Bandwidth": 25, "Lowest": 290, "Highest": 315},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.60 TO 0.80": {
            "JSW": {"Bandwidth": 17, "Lowest": 295, "Highest": 312},
            "TATA": {"Bandwidth": 20, "Lowest": 295, "Highest": 315},
            "JCAPCPL": {"Bandwidth": 25, "Lowest": 290, "Highest": 315},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "0.80 TO 1.00": {
            "TATA": {"Bandwidth": 15, "Lowest": 295, "Highest": 310},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.00 TO 1.20": {
            "TATA": {"Bandwidth": 10, "Lowest": 295, "Highest": 305},
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        },
        "1.20 TO 3.20": {
            "NES Spec": {"Bandwidth": None, "Lowest": 270, "Highest": None, "Note": "min"}
        }
    },
    "SP152 - 440": {
        "0.80 TO 1.0": {
            "POSCO": {"Bandwidth": 30, "Lowest": 450, "Highest": 465},
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        },
        "1.0 TO 1.2": {
            "POSCO": {"Bandwidth": 15, "Lowest": 450, "Highest": 480},
            "TATA": {"Bandwidth": 25, "Lowest": 445, "Highest": 460},
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        },
        "1.2 TO 1.6": {
            "TATA": {"Bandwidth": 20, "Lowest": 450, "Highest": 470},
            "POSCO": {"Bandwidth": 15, "Lowest": 450, "Highest": 480},
            "NES Spec": {"Bandwidth": None, "Lowest": 440, "Highest": None, "Note": "min"}
        }
    },
    "SP153 - 590": {
         "NES Spec": {"Bandwidth": None, "Lowest": None, "Highest": None, "Note": "min"}
    }
}


el_data = {
    "data_structured": {
        "SP781": {
            "0.40 TO 0.60": {
                "POSCO": {"Lowest": 44, "Highest": 47},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 42, "Highest": 46},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 44, "Highest": 48},
                "RNTBCI": {"Lowest": 44, "Highest": 48},
                "NES Spec": {"Lowest": 40, "Highest": 49}
            },
            "0.60 TO 0.80": {
                "POSCO": {"Lowest": 44, "Highest": 47},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 43, "Highest": 48},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 44, "Highest": 48},
                "RNTBCI": {"Lowest": 44, "Highest": 48},
                "NES Spec": {"Lowest": 41, "Highest": 50}
            },
            "0.80 TO 1.00": {
                "POSCO": {"Lowest": 45, "Highest": 48},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 43, "Highest": 49},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 45, "Highest": 51},
                "RNTBCI": {"Lowest": 45, "Highest": 51},
                "NES Spec": {"Lowest": 42, "Highest": 51}
            },
            "1.00 TO 1.20": {
                "POSCO": {"Lowest": 48, "Highest": 52},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 46, "Highest": 50},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 47, "Highest": 53},
                "RNTBCI": {"Lowest": 47, "Highest": 53},
                "NES Spec": {"Lowest": 43, "Highest": 52}
            },
            "1.20 TO 1.60": {
                "POSCO": {"Lowest": 48, "Highest": 52},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 46, "Highest": 50},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 47, "Highest": 53},
                "RNTBCI": {"Lowest": 47, "Highest": 53},
                "NES Spec": {"Lowest": 44, "Highest": 53}
            },
            "1.60 TO 2.00": {
                "POSCO": {"Lowest": 48, "Highest": 52},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 50, "Highest": 53},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 47, "Highest": 53},
                "RNTBCI": {"Lowest": 47, "Highest": 53},
                "NES Spec": {"Lowest": 45, "Highest": 55}
            }
        },
        "SP782": {
            "0.40 TO 0.60": {
                "POSCO": {"Lowest": 45, "Highest": 47},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 45, "Highest": 50},
                "RNTBCI": {"Lowest": 45, "Highest": 50},
                "NES Spec": {"Lowest": 42, "Highest": 50}
            },
            "0.60 TO 0.80": {
                "POSCO": {"Lowest": None, "Highest": 47},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 43, "Highest": 47},
                "JCAPCPL": {"Lowest": 45, "Highest": 50},
                "RNAIPL": {"Lowest": 45, "Highest": 50},
                "RNTBCI": {"Lowest": 45, "Highest": 50},
                "NES Spec": {"Lowest": 43, "Highest": 51}
            },
            "0.80 TO 1.00": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": None, "Highest": None},
                "RNTBCI": {"Lowest": None, "Highest": None},
                "NES Spec": {"Lowest": None, "Highest": None}
            },
            "1.00 TO 3.20": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": None, "Highest": None},
                "RNTBCI": {"Lowest": None, "Highest": None},
                "NES Spec": {"Lowest": None, "Highest": None}
            }
        },
        "SP783": {
            "0.40 TO 0.60": {
                "POSCO": {"Lowest": 46, "Highest": 49},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 45, "Highest": 48},
                "JCAPCPL": {"Lowest": 46, "Highest": 50},
                "RNAIPL": {"Lowest": 46, "Highest": 50},
                "RNTBCI": {"Lowest": 46, "Highest": 50},
                "NES Spec": {"Lowest": 44, "Highest": 52}
            },
            "0.60 TO 0.80": {
                "POSCO": {"Lowest": 46, "Highest": 49},
                "TATA": {"Lowest": 45, "Highest": 48},
                "RNAIPL": {"Lowest": 46, "Highest": 50},
                "RNTBCI": {"Lowest": 46, "Highest": 50},
                "NES Spec": {"Lowest": 45, "Highest": 53}
            },
            "0.80 TO 1.00": {
                "POSCO": {"Lowest": 47, "Highest": 50},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 48, "Highest": 54},
                "RNTBCI": {"Lowest": 48, "Highest": 54},
                "NES Spec": {"Lowest": 46, "Highest": 54}
            },
            "1.00 TO 3.20": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": None, "Highest": None},
                "RNTBCI": {"Lowest": None, "Highest": None},
                "NES Spec": {"Lowest": None, "Highest": None}
            }
        },
        "SP781 - 440": {
            "0.60 TO 0.80": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 30, "Highest": 33},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 30, "Highest": 38},
                "RNTBCI": {"Lowest": 30, "Highest": 38},
                "NES Spec": {"Lowest": 26, "Highest": 38}
            },
            "0.80 TO 1.00": {
                "POSCO": {"Lowest": 31, "Highest": 33},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 32, "Highest": 36},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 30, "Highest": 38},
                "RNTBCI": {"Lowest": 30, "Highest": 38},
                "NES Spec": {"Lowest": 27, "Highest": 39}
            },
            "1.00 TO 1.20": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 32, "Highest": 37},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 30, "Highest": 38},
                "RNTBCI": {"Lowest": 30, "Highest": 38},
                "NES Spec": {"Lowest": 28, "Highest": 40}
            },
            "1.20 TO 1.60": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": None, "Highest": None},
                "RNTBCI": {"Lowest": None, "Highest": None},
                "NES Spec": {"Lowest": None, "Highest": None}
            },
            "1.60 TO 2.00": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 34, "Highest": 38},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest":30, "Highest": 38},
                "RNTBCI": {"Lowest": 30, "Highest": 38},
                "NES Spec": {"Lowest": 30, "Highest": 38}
            },
            "2.00 TO 3.20": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 30, "Highest": 38},
                "RNTBCI": {"Lowest": 30, "Highest": 38},
                "NES Spec": {"Lowest": 30, "Highest": 38}
            }
        },
        "SP121": {
            "0.40 TO 0.60": {
                "POSCO": {"Lowest": 47, "Highest": 50},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 42, "Highest": 47},
                "JCAPCPL": {"Lowest": 47, "Highest": 49},
                "RNAIPL": {"Lowest": 46, "Highest": 50},
                "RNTBCI": {"Lowest": 46, "Highest": 50},
                "NES Spec": {"Lowest": 40, "Highest": 49}
            },
            "0.60 TO 0.80": {
                "POSCO": {"Lowest": 47, "Highest": 50},
                "JSW": {"Lowest": 46, "Highest": 50},
                "TATA": {"Lowest": 42, "Highest": 47},
                "JCAPCPL": {"Lowest": 46, "Highest": 50},
                "RNAIPL": {"Lowest": 46, "Highest": 50},
                "RNTBCI": {"Lowest": 46, "Highest": 50},
                "NES Spec": {"Lowest": 41, "Highest": 50}
            },
            "0.80 TO 1.00": {
                "POSCO": {"Lowest": 48, "Highest": 50},
                "JSW": {"Lowest": 46, "Highest": 51},
                "TATA": {"Lowest": 43, "Highest": 47},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 47, "Highest": 51},
                "RNTBCI": {"Lowest": 47, "Highest": 51},
                "NES Spec": {"Lowest": 42, "Highest": 51}
            },
            "1.00 TO 1.20": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": 47, "Highest": 52},
                "TATA": {"Lowest": 44, "Highest": 48},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 48, "Highest": 53},
                "RNTBCI": {"Lowest": 47, "Highest": 52},
                "NES Spec": {"Lowest": 43, "Highest": 52}
            },
            "1.20 TO 1.60": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": 48, "Highest": 53},
                "TATA": {"Lowest": 45, "Highest": 49},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 48, "Highest": 53},
                "RNTBCI": {"Lowest": 47, "Highest": 52},
                "NES Spec": {"Lowest": 44, "Highest": 53}
            },
            "1.60 TO 3.20": {
                "POSCO": {"Lowest": 49, "Highest": 52},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 48, "Highest": 53},
                "RNTBCI": {"Lowest": 48, "Highest": 53},
                "NES Spec": {"Lowest": 45, "Highest": 55}
            }
        },
        "SP122": {
            "0.40 TO 0.80": {
                "POSCO": {"Lowest": 48, "Highest": 50},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": 46, "Highest": 48},
                "RNAIPL": {"Lowest": 47, "Highest": 52},
                "RNTBCI": {"Lowest": 47, "Highest": 52},
                "NES Spec": {"Lowest": 42, "Highest": 52}
            }
        },
        "SP123": {
            "0.40 TO 0.60": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 44, "Highest": 48},
                "JCAPCPL": {"Lowest": 46, "Highest": 49},
                "RNAIPL": {"Lowest": 47, "Highest": 53},
                "RNTBCI": {"Lowest": 46, "Highest": 52},
                "NES Spec": {"Lowest": 44, "Highest": 52}
            },
            "0.60 TO 0.80": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": 49, "Highest": 52},
                "TATA": {"Lowest": 45, "Highest": 48},
                "JCAPCPL": {"Lowest": 46, "Highest": 49},
                "RNAIPL": {"Lowest": 47, "Highest": 53},
                "RNTBCI": {"Lowest": 46, "Highest": 52},
                "NES Spec": {"Lowest": 45, "Highest": 53}
            },
            "0.80 TO 1.00": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 46, "Highest": 50},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 48, "Highest": 54},
                "RNTBCI": {"Lowest": 47, "Highest": 53},
                "NES Spec": {"Lowest": 46, "Highest": 54}
            },
            "1.00 TO 1.20": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 48, "Highest": 50},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 49, "Highest": 55},
                "RNTBCI": {"Lowest": 48, "Highest": 54},
                "NES Spec": {"Lowest": 47, "Highest": 55}
            }
        },
        "SP152-440": {
            "0.80 TO 1.00": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 31, "Highest": 33},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 31, "Highest": 40},
                "RNTBCI": {"Lowest": 31, "Highest": 40},
                "NES Spec": {"Lowest": 28, "Highest": 40}
            },
            "1.0 TO 1.2": {
                "POSCO": {"Lowest": 32, "Highest": 35},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 31, "Highest": 34},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 32, "Highest": 41},
                "RNTBCI": {"Lowest": 32, "Highest": 41},
                "NES Spec": {"Lowest": 29, "Highest": 41}
            },
            "1.2 TO 1.6": {
                "POSCO": {"Lowest": 34, "Highest": 37},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 31, "Highest": 36},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 34, "Highest": 32},
                "RNTBCI": {"Lowest": 33, "Highest": 41},
                "NES Spec": {"Lowest": 30, "Highest": 32}
            },
            "1.6 TO 2.00": {
                "POSCO": {"Lowest": 36, "Highest": 38},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": 32, "Highest": 35},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": 35, "Highest": 40},
                "RNTBCI": {"Lowest": 35, "Highest": 33},
                "NES Spec": {"Lowest": 31, "Highest": 44}
            }
        },
        "SP153-590": {
            "0.40 TO 0.60": {
                "POSCO": {"Lowest": None, "Highest": None},
                "JSW": {"Lowest": None, "Highest": None},
                "TATA": {"Lowest": None, "Highest": None},
                "JCAPCPL": {"Lowest": None, "Highest": None},
                "RNAIPL": {"Lowest": None, "Highest": None},
                "RNTBCI": {"Lowest": None, "Highest": None},
                "NES Spec": {"Lowest": None, "Highest": None}
            }
        }
    }
}
def dict_to_df(data_dict):
    records = []
    for grade, thicknesses in data_dict.items():
        for thickness, manufacturers in thicknesses.items():
            for manufacturer, values in manufacturers.items():
                record = {'Grade': grade, 'Thickness': thickness, 'Manufacturer': manufacturer}
                
                if isinstance(values, dict):
                    record['Lowest'] = values.get('Lowest', None)
                    record['Highest'] = values.get('Highest', None)
                    record.update(values)
                else:
                    record['Lowest'] = None
                    record['Highest'] = None
                
                records.append(record)
    
    return pd.DataFrame(records)

ys_df = dict_to_df(ys_data)
ts_df = dict_to_df(ts_data)
el_df = dict_to_df(el_data['data_structured'])

grades = ys_df["Grade"].unique()
selected_grade = st.selectbox("Select Steel Grade", grades, key="grade_select")

thicknesses = ys_df["Thickness"].unique()
selected_thickness = st.selectbox("Select Thickness", thicknesses, key="thickness_select")

ys_filtered = ys_df[(ys_df["Grade"] == selected_grade) & (ys_df["Thickness"] == selected_thickness)]
ts_filtered = ts_df[(ts_df["Grade"] == selected_grade) & (ts_df["Thickness"] == selected_thickness)]
el_filtered = el_df[(el_df["Grade"] == selected_grade) & (el_df["Thickness"] == selected_thickness)]

if ys_filtered.empty or ts_filtered.empty or el_filtered.empty:
    st.warning("No data available for the selected grade and thickness.")
    st.stop()

combined_df = pd.merge(ys_filtered, ts_filtered, on=['Manufacturer', 'Grade', 'Thickness'], suffixes=('_YS', '_TS'))
combined_df = pd.merge(combined_df, el_filtered[['Manufacturer', 'Grade', 'Thickness', 'Lowest', 'Highest']], on=['Manufacturer', 'Grade', 'Thickness'])

st.subheader("Selected Data")
st.dataframe(combined_df)

color_dict = {
    'jsw': 'darkblue',
    'posco': 'sandybrown',
    'tata': 'lightblue',
    'jcap': 'brown',
    'nes spec': 'red'
}

def plot_box_comparisons(ys_df, ts_df, el_df):
    sns.set(style="whitegrid")

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    def create_box_plot(data, ax, title, ylabel):
        # Separate "nes spec" data for setting limits
        nes_spec_data = data[data['Manufacturer'].str.lower() == 'nes spec']
        other_data = data[data['Manufacturer'].str.lower() != 'nes spec']
        
        box_data = pd.DataFrame({
            'Manufacturer': other_data['Manufacturer'],
            'Lowest': other_data['Lowest'],
            'Highest': other_data['Highest']
        })
        melted_data = pd.melt(box_data, id_vars=['Manufacturer'], value_vars=['Lowest', 'Highest'], var_name='Type', value_name='Value')
        palette = [color_dict.get(manufacturer.lower(), 'gray') for manufacturer in other_data['Manufacturer']]
        
        sns.boxplot(x='Manufacturer', y='Value', data=melted_data, ax=ax, palette=palette)
    
        for i, manufacturer in enumerate(other_data['Manufacturer'].unique()):
            low = other_data[other_data['Manufacturer'] == manufacturer]['Lowest'].values[0]
            high = other_data[other_data['Manufacturer'] == manufacturer]['Highest'].values[0]
            ax.text(i, low, f"{low}", color="black", ha="center", va="top", fontweight="bold")
            ax.text(i, high, f"{high}", color="black", ha="center", va="bottom", fontweight="bold")
        
        if not nes_spec_data.empty:
            nes_spec_low = nes_spec_data['Lowest'].values[0]
            nes_spec_high = nes_spec_data['Highest'].values[0]
            
            ax.axhline(y=nes_spec_low, color=color_dict.get('nes spec', 'red'), linestyle='-', )
            ax.axhline(y=nes_spec_high, color=color_dict.get('nes spec', 'red'), linestyle='-', )
            
            ax.text(len(other_data['Manufacturer']), nes_spec_low, f"NES Spec Lower: {nes_spec_low}", color="black", ha="left", va="top", fontweight="bold")
            ax.text(len(other_data['Manufacturer']), nes_spec_high, f"NES Spec Upper: {nes_spec_high}", color="black", ha="left", va="bottom", fontweight="bold")

        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.set_xlabel('Manufacturer')
        ax.set_xticks(range(len(other_data['Manufacturer'])))
        ax.set_xticklabels(other_data['Manufacturer'], rotation=45)
        ax.legend()
    create_box_plot(ys_df, axes[0], 'Yield Strength Comparison', 'Strength Value')
    create_box_plot(ts_df, axes[1], 'Tensile Strength Comparison', 'Strength Value')
    create_box_plot(el_df, axes[2], 'Elongation Comparison', 'Elongation Value')

    plt.tight_layout()
    st.pyplot(fig)

plot_box_comparisons(ys_filtered, ts_filtered, el_filtered)
