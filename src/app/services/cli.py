import argparse

def create_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="File copier utility", 
        add_help=True,
        color=True
    )
    
    parser.add_argument(
        "--input",
        "-i",
        help="Specify several source folders for copying.",
    )
    
    parser.add_argument(
        "--output"
        "-o",
        help="Specify target folder for copying."
    )
    
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging."
    )
    
    return parser