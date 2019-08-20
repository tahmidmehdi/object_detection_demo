import numpy as np
import pandas as pd
import argparse


def main():
    # Initiate argument parser
    parser = argparse.ArgumentParser(
        description="Sample CSV-to-pbtxt converter"
    )
    parser.add_argument(
        "-i",
        "--inputFile",
        help="Path to the folder where the input .xml files are stored",
        type=str,
    )
    parser.add_argument(
        "-o", "--outputFile", help="Name of output .pbtxt file (including path)", type=str
    )

    args = parser.parse_args()

    objectsDf = pd.read_csv(args.inputFile, header=0)
    classes = np.unique(objectsDf['class'])

    # Create the `label_map.pbtxt` file
    pbtxt_content = ""
    for i in range(len(classes)):
        pbtxt_content = (
            pbtxt_content
            + "item {{\n    id: {0}\n    name: '{1}'\n}}\n\n".format(
                i + 1, classes[i]
            )
        )
    pbtxt_content = pbtxt_content.strip()
    with open(args.outputFile, "w") as f:
        f.write(pbtxt_content)


if __name__ == "__main__":
    main()
